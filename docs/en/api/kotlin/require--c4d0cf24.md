# require

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Validate a condition on a caller-supplied argument. A false condition throws `IllegalArgumentException`. The `lazyMessage` overload computes its custom error message only when the check fails. Successful checks continue normally.

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun require(value: Boolean): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt#L13)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun require(value: Boolean, lazyMessage: () -> Any): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt#L26)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
fun main() {
    require(3 > 0)
    println("argument valid")

    try {
        require(-1 > 0)
    } catch (e: IllegalArgumentException) {
        println("${e::class.simpleName}: ${e.message}")
    }

    try {
        require(-1 > 0) { "count must be positive" }
    } catch (e: IllegalArgumentException) {
        println("${e::class.simpleName}: ${e.message}")
    }
}
```

```text title="Output"
argument valid
IllegalArgumentException: Failed requirement.
IllegalArgumentException: count must be positive
```

## Version and sources

This page's explanation and examples have been separately prepared. Declarations are pinned to `v2.4.21`; examples were verified on the JVM with Kotlin / stdlib 2.4.21.
