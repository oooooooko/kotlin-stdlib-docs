# padStart

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个字符序列,该字符序列的内容在指定`length`的开头添加到带有指定字符或空间的字符序列。

@param 长度为 @param padChar , 字符字符串的长度如果小于指定的`length` 长度, 则用该字符串挂上字符串。 默认使用空间。 @return 返回长度至少为 `length` 的字符序列。 由 `this` 字符序列构成的字符序列预设, 预设为 `padChar` , 且达到该长度需要的倍数。 @sample 样本. text. strings.padStart

??? note "查看英文原文"

    Returns a char sequence with content of this char sequence padded at the beginning
    to the specified `length` with the specified character or space.
    
    @param length the desired string length.
    @param padChar the character to pad string with, if it has length less than the `length` specified. Space is used by default.
    @return Returns a char sequence of length at least `length` consisting of `this` char sequence prepended with `padChar` as many times
    as are necessary to reach that length.
    @sample samples.text.Strings.padStart

## 声明与重载

### 1. Common

```kotlin
public fun CharSequence.padStart(length: Int, padChar: Char = ' '): CharSequence
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L205)

### 2. Common

```kotlin
public fun String.padStart(length: Int, padChar: Char = ' '): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L228)

将字符串用指定字符或空格在开头处的指定 `length` 上标,以相片标为字符或空格。

@param 长度为 @param adchar , 字符串的字符串, 如果长度小于指定的 `length` 长度, 则用该字符串挂上字符串。 默认使用空间。 @return 返回至少 `length` 的长度字符串, 包括 `this` 字符串, 预设为 `padChar` , 且达到该长度需要的倍数 。 @sample 样本. text. Strings. padStart

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val padWithSpace = "125".padStart(5)
    println("'$padWithSpace'")

    val padWithChar = "a".padStart(5, '.')
    println("'$padWithChar'")

    // string is returned as is, when its length is greater than the specified
    val noPadding = "abcde".padStart(3)
    println("'$noPadding'")
}
```

```text title="输出"
'  125'
'....a'
'abcde'
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L291)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
