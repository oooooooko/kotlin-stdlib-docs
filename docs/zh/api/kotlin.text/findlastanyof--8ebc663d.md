# findLastAnyOf

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

在此字符序列中查找所指定的 `strings` 中的任何一次最后一次发生, 从指定的 `startIndex` 开始, 并且不考虑此案例 。

为了避免在`strings` 字符串中字符共的模糊结果, 这种方法从此字符串的结尾开始, 在每个位置上都发现 `strings` 中的第一个元素与该字符串相同 。

@param 开头 Index 字符索引 。 搜索向着字符串开头向后进行 。 @param 忽略 Case `true` 以忽略字符在匹配字符串时的字符 。 默认为 `false` 。 @return 以默认方式, 默认为 @return 。 匹配字符串最后发生的索引是 `strings` 和 字符串匹配的, 如果找不到 `strings` 则 或 `null` 。

??? note "查看英文原文"

    Finds the last occurrence of any of the specified `strings` in this char sequence,
    starting from the specified `startIndex` and optionally ignoring the case.
    
    To avoid ambiguous results when strings in `strings` have characters in common, this method proceeds from
    the end toward the beginning of this string, and finds at each position the first element in `strings`
    that matches this string at that position.
    
    @param startIndex The index of character to start searching at. The search proceeds backward toward the beginning of the string.
    @param ignoreCase `true` to ignore character case when matching a string. By default `false`.
    @return A pair of an index of the last occurrence of matched string from `strings` and the string matched or `null` if none of `strings` are found.

## 声明与重载

### 1. Common

```kotlin
public fun CharSequence.findLastAnyOf(strings: Collection<String>, startIndex: Int = lastIndex, ignoreCase: Boolean = false): Pair<Int, String>?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1077)

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
