# Preconditions.kt

Argument checks, state checks, and failure paths. This guide covers all **5 function families and 9 overloads** in this file in **kotlin-stdlib 2.4.21**.

| API | Purpose | Failure exception | Return value |
| --- | --- | --- | --- |
| [`require`](../api/kotlin/require--c4d0cf24.md) | Validate an argument condition | `IllegalArgumentException` | `Unit` |
| [`requireNotNull`](../api/kotlin/requirenotnull--506b0c8f.md) | Require a non-null argument | `IllegalArgumentException` | `T` |
| [`check`](../api/kotlin/check--20f65c28.md) | Validate program state | `IllegalStateException` | `Unit` |
| [`checkNotNull`](../api/kotlin/checknotnull--25a38b02.md) | Require non-null state | `IllegalStateException` | `T` |
| [`error`](../api/kotlin/error--ca00fccf.md) | Fail immediately | `IllegalStateException` | `Nothing` |

## Default messages

| API | Message |
| --- | --- |
| `require` | `Failed requirement.` |
| `check` | `Check failed.` |
| `requireNotNull` / `checkNotNull` | `Required value was null.` |

## Usage notes

- Use `require` / `requireNotNull` for invalid arguments; use `check` / `checkNotNull` for invalid state.
- A `lazyMessage` is evaluated only on failure, avoiding message construction on successful paths.
- Non-null checking contracts enable smart casts for eligible variables.
- `error` returns `Nothing`, making it useful in failure branches of `when` or Elvis expressions.
- Each linked API page includes a standalone program without a test-library dependency, with successful results and exception messages verified on 2.4.21.

[Preconditions.kt · v2.4.21](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt)
