# forEachIndexed

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

在每个字符上执行给定的 `action` , 提供顺序索引, 并带有字符。 @param `action` 函数, 以字符和字符本身的索引来计算字符的索引, 并按字符执行动作 。

??? note "查看英文原文"

    Performs the given `action` on each character, providing sequential index with the character.
    @param `action` function that takes the index of a character and the character itself
    and performs the action on the character.

## 声明与重载

### 1. Common

```kotlin
public inline fun CharSequence.forEachIndexed(action: (index: Int, Char) -> Unit): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L1205)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
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

```text title="输出"
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

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
