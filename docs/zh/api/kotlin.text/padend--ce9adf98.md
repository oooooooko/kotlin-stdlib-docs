# padEnd

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个字符序列,该字符序列的内容在指定的`length`的结尾处加插,并带有指定的字符或空间。

@param 长度为 @param adchar , 字符串的字符串, 如果长度小于指定的`length` 。 默认使用空间。 @return 返回长度至少为 `length` 的字符序列。 由`this` 字符序列组成, 与 `padChar` 相配, 与达到该长度所需的次数相匹配。 @sample 样本. text. Strings.padEnd

??? note "查看英文原文"

    Returns a char sequence with content of this char sequence padded at the end
    to the specified `length` with the specified character or space.
    
    @param length the desired string length.
    @param padChar the character to pad string with, if it has length less than the `length` specified. Space is used by default.
    @return Returns a char sequence of length at least `length` consisting of `this` char sequence appended with `padChar` as many times
    as are necessary to reach that length.
    @sample samples.text.Strings.padEnd

## 声明与重载

### 1. Common

```kotlin
public fun CharSequence.padEnd(length: Int, padChar: Char = ' '): CharSequence
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L240)

### 2. Common

```kotlin
public fun String.padEnd(length: Int, padChar: Char = ' '): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L263)

将字符串用指定字符或空格标定为 `length` 的字符串贴在结尾处。

@param 长度为 @param padChar , 字符串的字符串, 如果长度小于指定的 `length` 长度, 则用该字符键。 默认使用空间。 @return 返回至少 `length` 的长度字符串, 包括 `this` 字符串, 加上 `padChar` 个字符串, 并加上`padChar` 的倍数, 以达到此长度 。 @sample 样本. text. strings.padEnd

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val padWithSpace = "125".padEnd(5)
    println("'$padWithSpace'")

    val padWithChar = "a".padEnd(5, '.')
    println("'$padWithChar'")

    // string is returned as is, when its length is greater than the specified
    val noPadding = "abcde".padEnd(3)
    println("'$noPadding'")
}
```

```text title="输出"
'125  '
'a....'
'abcde'
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L304)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
