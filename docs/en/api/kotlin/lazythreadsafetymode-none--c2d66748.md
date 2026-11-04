# LazyThreadSafetyMode.NONE

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

No locks are used to synchronize access and initialization of a `Lazy` instance value.
If the instance is accessed from multiple threads, its behavior is unspecified.

This mode should not be used unless the `Lazy` instance is guaranteed never to be initialized from more than one thread.

## Declarations and overloads

### 1. Common

```kotlin
NONE,
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Lazy.kt#L80)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

fun main() {
    val value = kotlin.LazyThreadSafetyMode.NONE
    println(value)
}
```

```text title="Output"
NONE
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
