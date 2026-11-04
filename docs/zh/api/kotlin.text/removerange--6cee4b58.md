# removeRange

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

a `CharSequence` 返回从此字符序列中删除指定子序列后获得的 `CharSequence` 。

@param 开始 Index 将子序列的起始( 包括) 切除为 @param 结尾处 。

@throws 指数外溢值或 `IllegalArgumentException` ,当 `startIndex` 或 `endIndex` 超出此字符序列指数的范围时,或当`startIndex > endIndex`时,则 @throws 。

@sample 样本.text.Strings.removeRangeCharce

??? note "查看英文原文"

    Returns a `CharSequence` obtained by removing the specified subsequence from this char sequence.
    
    @param startIndex the beginning (inclusive) of the subsequence to remove.
    @param endIndex the end (exclusive) of the subsequence to remove.
    
    @throws IndexOutOfBoundsException or `IllegalArgumentException` when `startIndex` or `endIndex` is out of range of this char sequence indices
      or when `startIndex > endIndex`.
    
    @sample samples.text.Strings.removeRangeCharSequence

## 声明与重载

### 1. Common

```kotlin
public fun CharSequence.removeRange(startIndex: Int, endIndex: Int): CharSequence
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L559)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun String.removeRange(startIndex: Int, endIndex: Int): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L583)

返回从此字符串中删除指定子字符串后获得的 `String` 。

@param 开始 INdex 子字符串的起始( 包括) 要删除的子字符串的起始( 包括) 。 @param 结尾的起始 Index 要删除的子字符串的结尾( 排他) 。

@throws 指数外在值为 `startIndex` 或 `endIndex` 的,或 `IllegalArgumentException` 的,或 `endIndex` 的,则在 `startIndex` 或 `endIndex` 的这一字符串指数范围之外,或当 `startIndex > endIndex` 时,则在 `IllegalArgumentException` 的外在值为@throws 。

@sample 样本.text.Strings.removeRangeString 样本

### 3. Common

```kotlin
public fun CharSequence.removeRange(range: IntRange): CharSequence
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L598)

a `CharSequence` 返回从此字符序列中删除指定子序列后获得的 `CharSequence` 。

@param 范围为要删除的子序列的索引范围。 注意: `range` 中的 `IntRange.endInclusive` 指数字符也被删除。

@sample 样本.text.Strings.removeRangeCharce

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun String.removeRange(range: IntRange): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L608)

a `String` 返回从此字符序列中删除指定子字符串后获得的 `String` 。

@param 范围为要删除的子字符串的索引范围。 注意: `range` 中的 `IntRange.endInclusive` 指数字符也被删除。

@sample 样本.text.Strings.removeRangeString 样本

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val text = StringBuilder("Hello, world!")

    // Removing the range that correspond to the "world" subsequence
    println(text.removeRange(startIndex = 7, endIndex = 12))

    // Also possible to remove using a Range
    println(text.removeRange(7..11))

    // The original char sequence is not changed
    println(text)

    // Throws if startIndex is greater than endIndex
    assertFails { text.removeRange(startIndex = 7, endIndex = 4) }
    // Throws if startIndex or endIndex is out of range of the char sequence indices
    assertFails { text.removeRange(startIndex = 7, endIndex = 20) }
}
```

```text title="输出"
Hello, !
Hello, !
Hello, world!
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L980)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val text = "Hello, world!"

    // Removing the range that correspond to the "world" substring
    println(text.removeRange(startIndex = 7, endIndex = 12))

    // Also possible to remove using a Range
    println(text.removeRange(7..11))

    // The original string is not changed
    println(text)

    // Throws if startIndex is greater than endIndex
    assertFails { text.removeRange(startIndex = 7, endIndex = 4) }
    // Throws if startIndex or endIndex is out of range of the string indices
    assertFails { text.removeRange(startIndex = 7, endIndex = 20) }
}
```

```text title="输出"
Hello, !
Hello, !
Hello, world!
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L961)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
