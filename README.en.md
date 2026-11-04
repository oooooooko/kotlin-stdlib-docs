# Kotlin Standard Library Usage

[简体中文](README.md) | **English**

Bilingual usage documentation for **kotlin-stdlib 2.4.21**, built with **MkDocs + Material**. The layout follows the [BRV documentation](https://liangjingkanji.github.io/BRV/): white header, compact typography, three-column documentation layout, and a collapsible version menu.

- [Chinese website](https://oooooooko.github.io/kotlin-stdlib-docs/)
- [English website](https://oooooooko.github.io/kotlin-stdlib-docs/en/)
- [Coverage report](https://oooooooko.github.io/kotlin-stdlib-docs/coverage/)

## Content and coverage

Only **Common APIs** are included. JVM-, JS-, Native-, and Wasm-specific APIs, platform interop annotations, and declarations introduced after 2.4.21 are excluded. Examples run on the JVM using the pinned toolchain.

The source inventory is pinned to [Kotlin v2.4.21](https://github.com/JetBrains/kotlin/tree/v2.4.21). API pages preserve Common declarations, overloads, KDoc, and source links. A language switcher opens the matching page in the other language.

The inventory covers **23 packages, 2,590 Common API groups, and 6,611 declarations**, with 2,617 content pages per language. Every group has a compiled and executed representative example with captured output. [data/coverage.json](data/coverage.json) records **zero missing groups**. Overloads share pages; a representative example does not establish coverage of every overload or target platform.

English KDoc preserves upstream prose. Chinese KDoc is a machine-translated draft, not individually human-reviewed; the English original remains available. Identifier substitutions that cannot be safely restored fall back to English. The `map` tutorial and `Preconditions.kt` guide have separately written Chinese and English explanations.

Local verification passed **2,413 unique programs**, including **2,187 exact output comparisons**.

Examples contain complete programs and captured output. Random, time-dependent, temporary-path, and platform-dependent output can vary. Some upstream edge-case samples use `kotlin-test`; reflection examples may additionally need `kotlin-reflect`, both at 2.4.21. Each page identifies relevant dependencies.

## Local preview

Requires Python 3.12+; example verification also requires JDK 17.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/mkdocs serve -a 127.0.0.1:8765
```

Open [the Chinese homepage](http://127.0.0.1:8765/) or [the English homepage](http://127.0.0.1:8765/en/). The version menu currently contains only **2.4.21**.

## Build and verify

```sh
.venv/bin/python scripts/bootstrap_kotlin.py
.venv/bin/python scripts/verify_examples.py --fixtures
.venv/bin/python scripts/build_docs.py
.venv/bin/python scripts/check_docs.py --require-complete
.venv/bin/mkdocs build --strict
```

The bootstrap script downloads the pinned compiler and verification dependencies to ignored `.tools/` storage. Model weights and the upstream source checkout are not required for normal builds. The generated website is written to `site/`.

`scripts/check_docs.py --require-complete` additionally fails if any API entry still lacks a verified example. This stricter completion check is distinct from a successful website build.

## Regenerate the inventory

```sh
git clone --depth 1 --filter=blob:none --sparse --branch v2.4.21 https://github.com/JetBrains/kotlin.git .tools/kotlin-source
git -C .tools/kotlin-source sparse-checkout set libraries/stdlib license
.venv/bin/python scripts/collect_api.py
.venv/bin/python scripts/prepare_examples.py
.venv/bin/python scripts/generate_examples.py
.venv/bin/python scripts/index_example_calls.py
.venv/bin/python scripts/curate_common_examples.py
.venv/bin/python scripts/build_docs.py
```

The inventory uses Kotlin's own parser, respects the stdlib build's legacy-source exclusions, and retains public and protected declarations. Example indexing uses resolved Kotlin IR symbols rather than matching method names alone. Test-derived programs are extracted and initially executed in a restricted macOS sandbox; their validated fixtures are stored in the repository.

To regenerate Chinese drafts, install the optional dependencies in `requirements-translation.txt`, then run `scripts/translate_kdoc.py`. Normal site builds use the checked-in translation cache and perform no model download.

## Deployment

On pushes to `main`, GitHub Actions validates examples, checks bilingual parity, and performs a strict MkDocs build. Publishing to GitHub Pages is gated on zero missing examples. The repository now passes the example coverage check. Pull requests run checks without publishing.

## Attribution

See [LICENSE](LICENSE) and [NOTICE](NOTICE) for Kotlin source, samples, translation model, and font attribution. This is an unofficial project and is not affiliated with JetBrains or the Kotlin Foundation.
