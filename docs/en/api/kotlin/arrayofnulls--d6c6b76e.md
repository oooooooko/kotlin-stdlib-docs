# arrayOfNulls

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns an array of objects of the given type with the given `size`, initialized with null values.

@throws RuntimeException if the specified `size` is negative.

## Declarations and overloads

### 1. Common

```kotlin
@Suppress("REIFIED_TYPE_PARAMETER_NO_INLINE")
public expect fun <reified T> arrayOfNulls(size: Int): Array<T?>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Library.kt#L21)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


enum class State { READY, DONE }
fun main() {
    println(arrayOfNulls<String>(3).contentToString())
    println(enumValues<State>().contentToString())
}
```

```text title="Output"
[null, null, null]
[READY, DONE]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
