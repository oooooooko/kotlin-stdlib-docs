# contentEquals

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if the contents of this char sequence are equal to the contents of the specified `other`,
i.e. both char sequences contain the same number of the same characters in the same order.

@sample samples.text.Strings.contentEquals

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.5")
public expect infix fun CharSequence?.contentEquals(other: CharSequence?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1568)

### 2. Common

```kotlin
@SinceKotlin("1.5")
public expect fun CharSequence?.contentEquals(other: CharSequence?, ignoreCase: Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1577)

Returns `true` if the contents of this char sequence are equal to the contents of the specified `other`, optionally ignoring case difference.

@param ignoreCase `true` to ignore character case when comparing contents.

@sample samples.text.Strings.contentEquals

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val stringBuilder = StringBuilder()
    stringBuilder.append("Kot").append("lin")
    println(stringBuilder)
    println(stringBuilder contentEquals "Kotlin")

    stringBuilder.setCharAt(0, 'k')
    println(stringBuilder)
    println("Kotlin".contentEquals(stringBuilder))
    println("Kotlin".contentEquals(stringBuilder, ignoreCase = true))
}
```

```text title="Output"
Kotlin
true
kotlin
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L621)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
