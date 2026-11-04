# checkNotNull

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Require a non-null value representing program state. Return the non-null value on success, with smart casts for eligible variables. A null value throws `IllegalStateException`, unlike the `IllegalArgumentException` thrown by `requireNotNull`. This is suitable for state errors such as an uninitialized object.

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun <T : Any> checkNotNull(value: T?): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt#L106)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun <T : Any> checkNotNull(value: T?, lazyMessage: () -> Any): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt#L121)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
fun stateLength(state: String?): Int {
    checkNotNull(state)
    return state.length
}

fun main() {
    println(stateLength("ready"))
    println(checkNotNull("initialized") { "state is not initialized" })

    try {
        stateLength(null)
    } catch (e: IllegalStateException) {
        println("${e::class.simpleName}: ${e.message}")
    }

    try {
        checkNotNull(null as String?) { "state is not initialized" }
    } catch (e: IllegalStateException) {
        println("${e::class.simpleName}: ${e.message}")
    }
}
```

```text title="Output"
5
initialized
IllegalStateException: Required value was null.
IllegalStateException: state is not initialized
```

## Version and sources

This page's explanation and examples have been separately prepared. Declarations are pinned to `v2.4.21`; examples were verified on the JVM with Kotlin / stdlib 2.4.21.
