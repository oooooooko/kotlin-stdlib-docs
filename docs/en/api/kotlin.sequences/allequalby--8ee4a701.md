# allEqualBy

`kotlin.sequences` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if all elements in the sequence yield the same value
produced by the given `selector` function.

Returns `true` for an empty sequence.

The `selector` values are compared sequentially using structural equality (`==`),
and all elements are considered equal by the `selector` value if the `selector`
value of the first element equals the `selector` value of every subsequent element.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

The operation is _terminal_.

@sample samples.generated.allequal.AllEqualSequencesSamples.allEqualBy

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <T, K> Sequence<T>.allEqualBy(selector: (T) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1517)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(sequenceOf<String>().allEqualBy { it.length })
    println(sequenceOf("apple").allEqualBy { it.length })

    println(sequenceOf("apple", "mango", "peach").allEqualBy { it.length })
    println(sequenceOf("apple", "mango", "peach").allEqualBy { it })
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualSequencesSamples.kt#L28)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
