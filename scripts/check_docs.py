"""Check API inventory, bilingual parity, example metadata, and recorded coverage."""

import argparse
import json
from pathlib import Path
from collect_api import common_groups

ROOT=Path(__file__).resolve().parents[1]


def main(require_complete=False):
    api=json.loads((ROOT/"data/api.json").read_text())
    coverage=json.loads((ROOT/"data/coverage.json").read_text())
    assert api["version"]==coverage["version"]=="2.4.21"
    assert api["scope"]==coverage["scope"]=="Common"
    assert common_groups(api["groups"])==api["groups"],"Platform-specific declarations in Common inventory"
    assert not api["parse_errors"],"Unresolved source parser errors"
    assert coverage["api_entries"]==len(api["groups"])
    assert coverage["entries_missing_examples"]==len(coverage["missing_examples"])
    assert coverage["entries_with_verified_examples"]+coverage["entries_missing_examples"]==len(api["groups"])
    for group in api["groups"]:
        for language in ("zh","en"):
            assert (ROOT/"docs"/language/group["path"]).is_file(),(language,group["key"])
    for language in ("zh","en"):
        assert (ROOT/"docs"/language/"guides/preconditions.md").is_file()
    zh={p.relative_to(ROOT/"docs/zh") for p in (ROOT/"docs/zh").rglob("*.md")}
    en={p.relative_to(ROOT/"docs/en") for p in (ROOT/"docs/en").rglob("*.md")}
    assert zh==en,(zh-en,en-zh)
    expected_api={Path(g["path"]) for g in api["groups"]}|{Path("api")/g["package"]/"index.md" for g in api["groups"]}
    assert {p for p in zh if p.parts[0]=="api"}==expected_api,"Stale or missing API pages"
    examples=0
    for filename in ("manual-examples.json","examples.json","generated-examples.json","test-examples.json"):
        path=ROOT/"data"/filename
        if not path.exists():
            continue
        for key,entry in json.loads(path.read_text()).items():
            assert entry["verified_version"]=="2.4.21",key
            assert "fun main()" in entry["code"],key
            assert isinstance(entry["output"],str),key
            examples+=1
    if require_complete:
        assert not coverage["missing_examples"],f"{len(coverage['missing_examples'])} API entries still lack examples"
    print(f"PASS {len(api['groups'])} API entries, {len(zh)} matching pages per language, {examples} recorded programs")
    print(f"Example coverage: {coverage['entries_with_verified_examples']}/{coverage['api_entries']}")


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-complete",action="store_true")
    main(parser.parse_args().require_complete)
