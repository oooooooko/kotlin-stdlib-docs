# requireNotNull

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Require a non-null argument and return its non-null value. A null argument throws `IllegalArgumentException`. Its contract enables smart casts for eligible variables after a successful check. The custom message is evaluated only for null input.

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun <T : Any> requireNotNull(value: T?): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt#L42)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun <T : Any> requireNotNull(value: T?, lazyMessage: () -> Any): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt#L54)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
fun textLength(text: String?): Int {
    requireNotNull(text)
    return text.length
}

fun main() {
    println(textLength("Kotlin"))
    println(requireNotNull("stdlib") { "text is required" })

    try {
        textLength(null)
    } catch (e: IllegalArgumentException) {
        println("${e::class.simpleName}: ${e.message}")
    }

    try {
        requireNotNull(null as String?) { "text is required" }
    } catch (e: IllegalArgumentException) {
        println("${e::class.simpleName}: ${e.message}")
    }
}
```

```text title="Output"
6
stdlib
IllegalArgumentException: Required value was null.
IllegalArgumentException: text is required
```

## Version and sources

This page's explanation and examples have been separately prepared. Declarations are pinned to `v2.4.21`; examples were verified on the JVM with Kotlin / stdlib 2.4.21.
