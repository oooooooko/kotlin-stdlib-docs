# error

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Immediately throw an `IllegalStateException` with the supplied message. This function never returns normally. Its `Nothing` return type allows use in a `when` branch or Elvis expression where another result type is expected. It terminates the current path rather than returning an error string.

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun error(message: Any): Nothing
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt#L143)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
fun statusText(code: Int): String = when (code) {
    200 -> "OK"
    else -> error("Unexpected status: $code")
}

fun main() {
    println(statusText(200))

    try {
        println(statusText(500))
    } catch (e: IllegalStateException) {
        println("${e::class.simpleName}: ${e.message}")
    }
}
```

```text title="Output"
OK
IllegalStateException: Unexpected status: 500
```

## Version and sources

This page's explanation and examples have been separately prepared. Declarations are pinned to `v2.4.21`; examples were verified on the JVM with Kotlin / stdlib 2.4.21.
