# foldIndexed

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Accumulates value starting with `initial` value and applying `operation` from left to right
to current accumulator value and each character with its index in the original char sequence.

Returns the specified `initial` value if the char sequence is empty.

@param `operation` function that takes the index of a character, current accumulator value
and the character itself, and calculates the next accumulator value.

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <R> CharSequence.foldIndexed(initial: R, operation: (index: Int, acc: R, Char) -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L1146)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() {
    val text = "abc"
    println(text.findAnyOf(listOf("b", "c")))
    println(text.findLastAnyOf(listOf("b", "c")))
    println(text.flatMapTo(mutableListOf<Char>()) { listOf(it, it) })
    println(text.flatMapIndexedTo(mutableListOf<String>()) { index, char -> listOf("$index:$char") })
    println(text.foldIndexed("") { index, acc, char -> "$acc$index$char" })
    println(text.foldRight("") { char, acc -> "$acc$char" })
    println(text.foldRightIndexed("") { index, char, acc -> "$acc$index$char" })
    text.forEachIndexed { index, char -> println("$index:$char") }
    println(text.mapTo(mutableListOf<String>()) { it.uppercase() })
    println(text.mapIndexedTo(mutableListOf<String>()) { index, char -> "$index:$char" })
    println(text.mapNotNullTo(mutableListOf<Char>()) { it.takeIf { c -> c != 'b' } })
    println(text.mapIndexedNotNullTo(mutableListOf<Char>()) { index, char -> char.takeIf { index > 0 } })
    println(text.onEach { print(it.uppercase()) })
    println(text.onEachIndexed { index, char -> print("$index$char ") })
    println(text.single { it == 'b' })
    println(text.sumByDouble { it.code.toDouble() })
    println(text.toCollection(linkedSetOf<Char>()))
}
```

```text title="Output"
(1, b)
(2, c)
[a, a, b, b, c, c]
[0:a, 1:b, 2:c]
0a1b2c
cba
2c1b0a
0:a
1:b
2:c
[A, B, C]
[0:a, 1:b, 2:c]
[a, c]
[b, c]
ABCabc
0a 1b 2c abc
b
294.0
[a, b, c]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
