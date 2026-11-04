# substring

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回此字符串的子字符串,该字符串以指定的 `startIndex` 开始,并一直持续到字符串的结尾。

@param 开始指数 Index 初始指数(包括)

@throws 指数外在值除以负值为`startIndex`时的数值,或超过字符串长度的数值。

@sample 样本. text. strings. 源于 StartIndex 的子物质

??? note "查看英文原文"

    Returns a substring of this string that starts at the specified `startIndex` and continues to the end of the string.
    
    @param startIndex the start index (inclusive).
    
    @throws IndexOutOfBoundsException when `startIndex` is negative or exceeds the length if the string.
    
    @sample samples.text.Strings.substringFromStartIndex

## 声明与重载

### 1. Common

```kotlin
public expect fun String.substring(startIndex: Int): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L382)

### 2. Common

```kotlin
public expect fun String.substring(startIndex: Int, endIndex: Int): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L393)

返回从 `startIndex` 开始至`endIndex`之前结束的该字符串的子字符串。

@param 开始 Index 初始指数(包括) @param 结尾 Index 最终指数(不包括)

@throws 指数外在值除以负值`startIndex`, `endIndex` 超过长度,如果字符串超过,或者如果`startIndex`大于80 000005,则超过长度。

@sample 样本. 文本. 链条. substring By Start和EndIndicas

### 3. Common

```kotlin
public fun String.substring(range: IntRange): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L400)

返回给定的`range`指数指定的子字符串。

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharSequence.substring(startIndex: Int, endIndex: Int = length): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L422)

返回从 `startIndex` 开始至`endIndex`之前结束的从此字符序列序列范围开始的字符串子字符串。

@param 开始 Index 启动指数( 包括) 。 @param 结束Index 最终指数( 排他性) 。 如果未指定, 则使用字符序列的长度 。

### 5. Common

```kotlin
public fun CharSequence.substring(range: IntRange): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L431)

返回本字符序列中指定的`range`的字符串索引中的字符串子字符串。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val str = "abcde"
    println(str.substring(0))
    println(str.substring(1))
    // startIndex exceeds the string length
    assertFailsWith<IndexOutOfBoundsException> { str.substring(6) }
}
```

```text title="输出"
abcde
bcde
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L854)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val str = "abcde"
    println(str.substring(0, 0))
    println(str.substring(0, 1))
    println(str.substring(5, 5))
    // endIndex exceeds string length
    assertFailsWith<IndexOutOfBoundsException> { str.substring(0, 6) }
    // endIndex is smaller than the startIndex
    assertFailsWith<IndexOutOfBoundsException> { str.substring(1, 0) }
}
```

```text title="输出"

a
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L863)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
