# toList

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Converts this pair into a list.
@sample samples.misc.Tuples.pairToList

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Pair<T, T>.toList(): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Tuples.kt#L46)

### 2. Common

```kotlin
public fun <T> Triple<T, T, T>.toList(): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Tuples.kt#L80)

Converts this triple into a list.
@sample samples.misc.Tuples.tripleToList

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val mixedList: List<Any> = Pair(1, "a").toList()
    println(mixedList)
    println(mixedList[0] is Int)
    println(mixedList[1] is String)

    val intList: List<Int> = Pair(0, 1).toList()
    println(intList)
}
```

```text title="Output"
[1, a]
true
true
[0, 1]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/tuples.kt#L23)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val mixedList: List<Any> = Triple(1, "a", 0.5).toList()
    println(mixedList)
    println(mixedList[0] is Int)
    println(mixedList[1] is String)
    println(mixedList[2] is Double)

    val intList: List<Int> = Triple(0, 1, 2).toList()
    println(intList)
}
```

```text title="Output"
[1, a, 0.5]
true
true
true
[0, 1, 2]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/tuples.kt#L34)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
