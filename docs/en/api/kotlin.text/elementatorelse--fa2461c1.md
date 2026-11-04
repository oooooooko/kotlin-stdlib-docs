# elementAtOrElse

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a character at the given `index` or the result of calling the `defaultValue` function if the `index` is out of bounds of this char sequence.

@sample samples.text.Strings.elementAtOrElse

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharSequence.elementAtOrElse(index: Int, defaultValue: (Int) -> Char): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L27)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val phone = "+263783"

    // in-bounds indices return the character at that position
    println(phone.elementAtOrElse(0) { 'X' })
    println(phone.elementAtOrElse(phone.lastIndex) { 'X' })

    // an out-of-bounds index evaluates the fallback lambda
    println(phone.elementAtOrElse(-1) { if (it < 0) '<' else '>' })
    println(phone.elementAtOrElse(8) { if (it < 0) '<' else '>' })

    // empty string always evaluates the fallback lambda
    println("".elementAtOrElse(0) { 'X' })
}
```

```text title="Output"
+
3
<
>
X
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L115)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
