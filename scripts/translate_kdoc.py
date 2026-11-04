"""Translate cached public KDoc prose locally; preserve Kotlin identifiers and code blocks."""

import argparse
import json
import re
import time

from collect_api import ROOT

MODEL = "Helsinki-NLP/opus-mt-en-zh"


def markdown_doc(doc):
    # KDoc symbol references are inline code, not broken relative Markdown links.
    doc = re.sub(r"\[([^\]\n]+)\](?!\()", lambda m:"`"+m[1]+"`", doc)
    doc = re.sub(r"\[([^\]]+)\]\(#[^)]+\)",r"\1",doc)
    doc = re.sub(r"\]\((/docs/[^)]+)\)",lambda m:"](https://kotlinlang.org"+m[1]+")",doc)
    return doc


def blocks(doc):
    return re.split(r"(```[\s\S]*?```|\n\s*\n)", markdown_doc(doc))


def chunks(block, limit=900):
    if block.isspace() or not block or block.startswith("```"):
        return []
    words = re.split(r"(\s+)", block)
    result, current = [], ""
    for word in words:
        if len(current)+len(word)>limit and current.strip():
            result.append(current.strip())
            current = ""
        current += word
    if current.strip():
        result.append(current.strip())
    return result


def protected(value):
    symbols = []
    def replace(match):
        symbols.append(match[0])
        return str(800000000+len(symbols))
    return re.sub(r"`[^`\n]+`|https?://\S+|@\w+", replace, value), symbols


def restore(value, symbols):
    for index, symbol in enumerate(symbols, 1):
        token = str(800000000+index)
        value = re.sub(r"\s*"+token+r"\s*", lambda _:" "+symbol+" ", value)
    return value.strip()


def translate(batch_size, repair=False):
    import torch
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
    api = json.loads((ROOT/"data/api.json").read_text())
    prose = sorted({chunk for group in api["groups"] for declaration in group["declarations"] for block in blocks(declaration["kdoc"]) for chunk in chunks(block)})
    destination = ROOT/"data/translations.json"
    translated = json.loads(destination.read_text()) if destination.exists() else {}
    if repair:
        from build_docs import repair_translation
        pending=[p for p in prose if p not in translated or repair_translation(p,translated[p]) is None]
    else:
        pending = [p for p in prose if p not in translated]
    print(f"KDoc prose chunks: {len(prose)}, pending: {len(pending)}", flush=True)
    if not pending:
        return
    torch.set_num_threads(4)
    tokenizer = AutoTokenizer.from_pretrained(MODEL, cache_dir=str(ROOT/".tools/models"))
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL, cache_dir=str(ROOT/".tools/models"))
    model.to("mps" if torch.backends.mps.is_available() else "cpu").eval()
    if repair:
        # Short lines prevent the model from dropping later Markdown list items.
        pattern=r'\[[^\]\n]+\]\(https?://[^\s]+\)|`[^`\n]+`|https?://\S+|@\w+'
        pieces={p:re.split(r'(\n|(?<=[.!?]) +(?=[A-Z]))',p) for p in pending}
        lines=list(dict.fromkeys(line for parts in pieces.values() for line in parts if line.strip()))
        fixed={}
        for offset in range(0,len(lines),batch_size):
            batch=lines[offset:offset+batch_size]
            inputs=[]; maps=[]
            for line in batch:
                symbols=[]
                def protect(match):
                    symbols.append(match[0]); return 'ZX'+str(len(symbols))+'XZ'
                inputs.append(re.sub(pattern,protect,line)); maps.append(symbols)
            encoded=tokenizer(inputs,return_tensors="pt",padding=True).to(model.device)
            with torch.inference_mode():
                generated=model.generate(**encoded,max_new_tokens=384,num_beams=1)
            for line,value,symbols in zip(batch,tokenizer.batch_decode(generated,skip_special_tokens=True),maps):
                residue=re.sub(r'ZX\d+XZ','',value)
                if any(value.count('ZX'+str(i)+'XZ')!=1 for i in range(1,len(symbols)+1)) or re.search(r'[XZ]{3,}|ZX\d',residue):
                    # Translate only prose spans when a line loses a placeholder.
                    spans=re.split('('+pattern+')',line)
                    text=[span for index,span in enumerate(spans) if index%2==0 and re.search(r'[A-Za-z]{2}',span)]
                    if text:
                        encoded=tokenizer(text,return_tensors="pt",padding=True).to(model.device)
                        with torch.inference_mode(): result=model.generate(**encoded,max_new_tokens=384,num_beams=1)
                        replacements=iter(tokenizer.batch_decode(result,skip_special_tokens=True))
                        spans=[next(replacements) if index%2==0 and re.search(r'[A-Za-z]{2}',span) else span for index,span in enumerate(spans)]
                    value=''.join(spans)
                else:
                    for i,symbol in enumerate(symbols,1):value=value.replace('ZX'+str(i)+'XZ',symbol)
                fixed[line]=value
            for original,parts in pieces.items():
                if all(not part.strip() or part in fixed for part in parts):
                    translated[original]=''.join(fixed.get(part,part) for part in parts)
            destination.write_text(json.dumps(translated,ensure_ascii=False,indent=2)+"\n")
            print(f"Repaired {min(offset+batch_size,len(lines))}/{len(lines)} prose lines",flush=True)
        return
    start = time.monotonic()
    for offset in range(0,len(pending),batch_size):
        batch = pending[offset:offset+batch_size]
        inputs, protected_symbols = zip(*(protected(p) for p in batch))
        encoded = tokenizer(list(inputs), return_tensors="pt", padding=True, truncation=False).to(model.device)
        with torch.inference_mode():
            generated = model.generate(**encoded, max_new_tokens=384, num_beams=1)
        for original, output, symbols in zip(batch, tokenizer.batch_decode(generated,skip_special_tokens=True),protected_symbols):
            result = restore(output,symbols)
            if any(str(800000000+i) in result for i in range(1,len(symbols)+1)):
                raise RuntimeError("Unrestored identifier in translation")
            translated[original] = result
        destination.write_text(json.dumps(translated,ensure_ascii=False,indent=2)+"\n")
        print(f"Translated {min(offset+batch_size,len(pending))}/{len(pending)} ({time.monotonic()-start:.0f}s)",flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-size",type=int,default=32)
    parser.add_argument("--repair",action="store_true",help="Repair drafts that lost identifiers or links.")
    args=parser.parse_args()
    translate(args.batch_size,args.repair)
