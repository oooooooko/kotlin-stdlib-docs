# replaceRange

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回含有此字符序列内容的字符序列序列, 其给定范围内的部分由 `replacement` 字符序列替换。 @param startIndex 将替换的第一个字符索引。 @param endIndex 将替换后的第一个字符索引替换为字符串。

@sample 样本.text.Strings.replerange

??? note "查看英文原文"

    Returns a char sequence with content of this char sequence where its part at the given range
    is replaced with the `replacement` char sequence.
    @param startIndex the index of the first character to be replaced.
    @param endIndex the index of the first character after the replacement to keep in the string.
    
    @sample samples.text.Strings.replaceRange

## 声明与重载

### 1. Common

```kotlin
public fun CharSequence.replaceRange(startIndex: Int, endIndex: Int, replacement: CharSequence): CharSequence
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L508)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun String.replaceRange(startIndex: Int, endIndex: Int, replacement: CharSequence): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L526)

将给定范围的字符串部分替换为 `replacement` 字符字符序列。 @param 开头 Index 将替换第一个字符的索引。 @param 结尾Index 将替换后第一个字符的索引替换为字符串中保存的第一个字符。

@sample 样本.text.Strings.replerange

### 3. Common

```kotlin
public fun CharSequence.replaceRange(range: IntRange, replacement: CharSequence): CharSequence
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L537)

返回含有此字符序列内容的字符序列,其给定 `range` 的字符序列被`replacement` 字符序列所取代。

`range`的末期指数包括在要替换的部分。

@sample 样本.text.Strings.replerange

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun String.replaceRange(range: IntRange, replacement: CharSequence): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L548)

将给定 `range` 的字符串部分替换为 `replacement` 字符串 。

`range`的末期指数包括在要替换的部分。

@sample 样本.text.Strings.replerange

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val text = "Hello, world!"

    // Replacing the range that corresponds to the "world" substring with "Kotlin"
    println(text.replaceRange(startIndex = 7, endIndex = 12, replacement = "Kotlin"))

    // Also possible to replace using a Range
    println(text.replaceRange(7..11, replacement = "Kotlin"))

    // Empty replacement effectively removes the range
    println(text.replaceRange(7..11, ""))

    // Replacing at the end of the string: endIndex is exclusive
    println(text.replaceRange(0, 5, "Hey"))

    // But for the overload accepting the range, range's end is inclusive (thus the comma is also replaced)
    println(text.replaceRange(0..5, "Hey"))

    // Throws if startIndex is greater than endIndex
    assertFails { text.replaceRange(startIndex = 7, endIndex = 4, replacement = "Kotlin") }
    // Throws if startIndex or endIndex is out of the string indices range
    assertFails { text.replaceRange(startIndex = 7, endIndex = 20, replacement = "Kotlin") }
    // For ranges, the end is inclusive, so it has to be lower than the length of a char sequence
    assertFails { text.replaceRange(7..text.length, replacement = "Kotlin") }
}
```

```text title="输出"
Hello, Kotlin!
Hello, Kotlin!
Hello, !
Hey, world!
Hey world!
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L1025)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
