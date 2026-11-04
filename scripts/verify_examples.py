"""Compile and run unique documentation fixtures using Kotlin / stdlib 2.4.21."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
VARIABLE_OUTPUT = re.compile(r'\bRandom\.(?:Default|next\w+)|\.`?(?:random|randomOrNull|shuffle|shuffled)`?\s*\(\s*\)|Clock\.System|TimeSource\.Monotonic|System\.(?:nanoTime|currentTimeMillis)|\bmeasure(?:TimeMillis|NanoTime|Time|TimedValue)`?\s*\(|\bDate\(\s*\)')


def output_can_vary(code, output):
    identity_hash = re.search(r'`?hashCode`?\s*\(',code) and any(marker in code for marker in ('Any()', 'Demo', '::'))
    return bool(identity_hash or VARIABLE_OUTPUT.search(code) or re.search(r'@[0-9a-fA-F]{5,}|/(?:private/)?(?:var/folders|tmp)/',output))


def normalize_output(output):
    output = re.sub(r'\b(?:generated|verified|indexed|platformsamples)\.[a-z][0-9a-f]{8,}\.', '', output)
    output = re.sub(r'\b(?:[SGTP][0-9a-f]{8,}|Example[0-9a-f]{8,})Kt\b', 'ExampleKt', output)
    return re.sub(r'\b(?:[sgtp][0-9a-f]{8,}|Example[0-9a-f]{8,})\.kt\b', 'Example.kt', output)


def package_source(code, namespace):
    prefix = re.match(r'\A(?:@file:[^\n]*\n|\s*\n)*', code)[0]
    return prefix + 'package ' + namespace + '\n' + code[len(prefix):]


def guide_examples(path):
    fences=list(re.finditer(r'^```(\w+)[^\n]*\n(.*?)^```\s*$',path.read_text(),re.MULTILINE|re.DOTALL))
    return [(fence[2],fences[index+1][2]) for index,fence in enumerate(fences) if fence[1]=='kotlin' and 'fun main()' in fence[2] and index+1<len(fences) and fences[index+1][1]=='text']


def fixture_programs(manual_only=False):
    paths = ['manual-examples.json'] if manual_only else [
        'manual-examples.json', 'examples.json', 'generated-examples.json', 'test-examples.json'
    ]
    programs = {}
    for filename in paths:
        path = ROOT / 'data' / filename
        if not path.exists():
            continue
        for key, value in json.loads(path.read_text()).items():
            value = dict(value)
            value['key'] = key
            value['test_derived'] = filename == 'test-examples.json'
            value['compare_output'] = value.get('deterministic', True) and not value['test_derived'] and not output_can_vary(value['code'],value['output'])
            digest = hashlib.sha256(value['code'].encode()).hexdigest()[:16]
            if digest not in programs:
                programs[digest] = value
    if not manual_only:
        guide = ROOT / 'docs/zh/collections/map.md'
        blocks = guide_examples(guide)
        for index, (code, output) in enumerate(blocks):
            code = code.rstrip() + '\n'
            digest = hashlib.sha256(code.encode()).hexdigest()[:16]
            programs[digest] = {'key': f'map tutorial #{index+1}', 'code': code, 'output': output, 'compare_output': True, 'test_derived': False}
    return programs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fixtures', action='store_true', help='Verify the canonical fixture registry (default).')
    parser.add_argument('--manual-only', action='store_true')
    parser.add_argument('--kotlinc', default=str(ROOT / '.tools/maven-kotlinc/bin/kotlinc'))
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--force', action='store_true', help='Ignore prior successful local verification.')
    args = parser.parse_args()
    compiler = shutil.which(args.kotlinc)
    if not compiler:
        parser.error('Run python scripts/bootstrap_kotlin.py first, or specify --kotlinc.')
    version = subprocess.run([compiler, '-version'], capture_output=True, text=True, check=True)
    if not re.search(r'kotlinc-jvm 2\.4\.21(?:\s|$)', version.stdout + version.stderr):
        parser.error('Kotlin 2.4.21 is required.')
    lib = Path(compiler).resolve().parents[1] / 'lib'
    stdlib = lib / 'kotlin-stdlib.jar'
    test_jar = lib / 'kotlin-test.jar'
    reflect_jar = ROOT / '.tools/kotlin-reflect-2.4.21.jar'
    compiler_classpath = os.pathsep.join(map(str, [stdlib, test_jar, reflect_jar]))
    programs = fixture_programs(args.manual_only)
    (ROOT / '.tools').mkdir(exist_ok=True)
    cache_path = ROOT / '.tools/verified-examples.json'
    context = hashlib.sha256((sys.platform + version.stdout + version.stderr).encode() + stdlib.read_bytes() + test_jar.read_bytes() + reflect_jar.read_bytes()).hexdigest()
    prior = json.loads(cache_path.read_text()) if cache_path.exists() and not args.force else {}
    cache = prior.get('programs', {}) if prior.get('context') == context else {}
    def cache_key(entry):
        fields={k:entry.get(k) for k in ('code','output','compare_output','test_derived','dependencies')}
        fields.update({k:entry[k] for k in ('stdin','compiler_options','files') if k in entry})
        return hashlib.sha256(json.dumps(fields,sort_keys=True).encode()).hexdigest()
    entries = [(digest,entry) for digest,entry in programs.items() if cache_key(entry) not in cache]
    passed = len(programs) - len(entries)
    compared = sum(int(entry['compare_output']) for entry in programs.values() if cache_key(entry) in cache)
    if passed:
        print(f'Reusing {passed} successful checks for the same compiler, libraries, JDK, and program contents.',flush=True)
    docker_container = None
    with tempfile.TemporaryDirectory(prefix='verify-', dir=ROOT / '.tools') as staging, tempfile.TemporaryDirectory(prefix='stdlib-runs-') as run_directory:
        work = Path(staging)
        run_root = Path(run_directory).resolve()
        if sys.platform != 'darwin' and any(entry['test_derived'] for entry in programs.values()):
            if not shutil.which('docker'):
                parser.error('Test-derived programs require Docker on Linux, or sandbox-exec on macOS.')
            image = 'eclipse-temurin:17-jre'
            subprocess.run(['docker', 'pull', image], check=True, stdout=subprocess.DEVNULL)
            docker_container = subprocess.check_output([
                'docker', 'run', '--detach', '--rm', '--network', 'none', '--read-only',
                '--tmpfs', '/tmp:rw,nosuid,nodev,size=256m',
                '--volume', f'{ROOT / ".tools"}:{ROOT / ".tools"}:ro',
                '--volume', f'{run_root}:{run_root}:rw', image, 'sleep', 'infinity'
            ], text=True).strip()
        try:
            ordinary=[item for item in entries if not item[1].get('compiler_options') and not item[1].get('files')]
            batches=[ordinary[offset:offset+100] for offset in range(0,len(ordinary),100)]
            batches.extend([[item] for item in entries if item[1].get('compiler_options') or item[1].get('files')])
            for offset,batch in enumerate(batches):
                sources = []
                compiler_options=[]
                classes = work / f'classes-{offset}'
                for digest, entry in batch:
                    source = work / ('Example' + digest + '.kt')
                    source.write_text(package_source(entry['code'],'verified.p'+digest),encoding='utf-8')
                    sources.append(str(source))
                    paths={'main':str(source)}
                    for filename,code in entry.get('files',{}).items():
                        extra=work/digest/filename
                        extra.parent.mkdir(parents=True,exist_ok=True)
                        extra.write_text(package_source(code,'verified.p'+digest),encoding='utf-8')
                        sources.append(str(extra)); paths[filename]=str(extra)
                    options=entry.get('compiler_options',[])[:]
                    for name,path in paths.items():
                        options=[option.replace('{'+name+'}',path) for option in options]
                    compiler_options.extend(options)
                compiled = subprocess.run([
                    compiler, '-nowarn', '-no-stdlib', '-no-reflect', '-classpath', compiler_classpath,
                    '-d', str(classes), *compiler_options, *sources
                ], capture_output=True, text=True, timeout=180)
                if compiled.returncode:
                    raise RuntimeError((compiled.stdout + compiled.stderr)[-15000:])

                def run(item):
                    digest, entry = item
                    cwd = run_root / digest
                    cwd.mkdir()
                    runtime = [classes, stdlib]
                    if 'import kotlin.test' in entry['code'] or entry['test_derived']:
                        runtime.append(test_jar)
                    if entry.get('dependencies') or entry['key'].startswith('samples.'):
                        runtime.append(reflect_jar)
                    command = ['java', '-Xmx512m', '-Dfile.encoding=UTF-8', '-cp', os.pathsep.join(map(str, runtime)), 'verified.p' + digest + '.Example' + digest + 'Kt']
                    if entry['test_derived']:
                        if sys.platform == 'darwin':
                            profile = f'(version 1) (allow default) (deny network*) (deny file-write*) (allow file-write* (subpath "{cwd}") (subpath "/private/tmp") (subpath "/tmp")) (deny file-read* (subpath "{Path.home()}")) (allow file-read-metadata) (allow file-read* (subpath "{ROOT / ".tools"}"))'
                            command = ['sandbox-exec', '-p', profile, *command]
                        else:
                            command = ['docker', 'exec', '--workdir', str(cwd), '--env', 'TZ=UTC', docker_container, *command]
                    env = {key: os.environ[key] for key in ('PATH', 'JAVA_HOME', 'LANG') if key in os.environ}
                    env.update({'TMPDIR': str(cwd), 'TZ': 'UTC'})
                    result = subprocess.run(command, cwd=cwd, env=env, input=entry.get('stdin',''), capture_output=True, text=True, timeout=12)
                    if result.returncode:
                        raise AssertionError(entry['key'] + '\n' + result.stderr[-4000:])
                    if entry['compare_output'] and normalize_output(result.stdout) != normalize_output(entry['output']):
                        raise AssertionError(f"{entry['key']}\nExpected: {entry['output']!r}\nActual: {result.stdout!r}")
                    return int(entry['compare_output'])

                with ThreadPoolExecutor(max_workers=args.workers) as pool:
                    for (_,entry),matches in zip(batch,pool.map(run, batch)):
                        passed += 1
                        compared += matches
                        cache[cache_key(entry)] = bool(matches)
                cache_path.write_text(json.dumps({'context':context,'programs':cache},indent=2)+'\n')
                print(f'PASS {passed}/{len(programs)} programs ({compared} exact output checks)', flush=True)
        finally:
            cache_path.write_text(json.dumps({'context':context,'programs':cache},indent=2)+'\n')
            if docker_container:
                subprocess.run(['docker', 'rm', '--force', docker_container], stdout=subprocess.DEVNULL, check=False)
    if not passed:
        raise AssertionError('No examples found.')
    print(f'Kotlin / stdlib 2.4.21: {passed} unique programs passed; {compared} output snapshots matched.')


if __name__ == '__main__':
    main()
