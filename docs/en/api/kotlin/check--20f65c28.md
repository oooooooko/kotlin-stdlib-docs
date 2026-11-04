# check

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Validate the current state of an object or program. A false condition throws `IllegalStateException`. Use `require` for invalid arguments and `check` for invalid state. A custom message is evaluated only when the check fails.

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun check(value: Boolean): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt#L75)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun check(value: Boolean, lazyMessage: () -> Any): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt#L90)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
fun main() {
    check(true)
    println("state valid")

    try {
        check(false)
    } catch (e: IllegalStateException) {
        println("${e::class.simpleName}: ${e.message}")
    }

    try {
        check(false) { "service is not initialized" }
    } catch (e: IllegalStateException) {
        println("${e::class.simpleName}: ${e.message}")
    }
}
```

```text title="Output"
state valid
IllegalStateException: Check failed.
IllegalStateException: service is not initialized
```

## Version and sources

This page's explanation and examples have been separately prepared. Declarations are pinned to `v2.4.21`; examples were verified on the JVM with Kotlin / stdlib 2.4.21.
