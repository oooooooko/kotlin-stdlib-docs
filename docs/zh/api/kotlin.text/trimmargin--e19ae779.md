# trimMargin

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

字符串中主要的白空字符 Trims 领先的白空字符,然后从源字符串的每一行中取 `marginPrefix` ,如果第一行和最后一行为空白,则删除这些行(注意`isBlank`与 `isEmpty` )。

一条线如果除了第一和最后一空线之外 不含 `marginPrefix` , 就不会影响一条线。

原字符串中的线条可以与 `\r\n` (CRLF)、`\n`(LF)、 `\r` (CR)字符分隔,但是,由此产生的字符串中的线条将完全与 `\n` (LF)字符分隔。

@param 边距前缀非空白字符串,用作边距分隔符。默认值为 `|` (管道字符)。

@sample 样本. 文本. strings. trimmMgin @see 3imm 鼠标 @see kotlin. text. isWhitespace

??? note "查看英文原文"

    Trims leading whitespace characters followed by `marginPrefix` from every line of a source string and removes
    the first and the last lines if they are blank (note the difference in `isBlank` vs. `isEmpty`).
    
    Doesn't affect a line if it doesn't contain `marginPrefix` except the first and the last blank lines.
    
    The lines in the original string can be separated with `\r\n` (CRLF), `\n` (LF), or `\r` (CR) characters, however, the lines in the
    resulting string will be separated solely with `\n` (LF) character.
    
    @param marginPrefix non-blank string, which is used as a margin delimiter. Default is `|` (pipe character).
    
    @sample samples.text.Strings.trimMargin
    @see trimIndent
    @see kotlin.text.isWhitespace

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.IntrinsicConstEvaluation
public fun String.trimMargin(marginPrefix: String = "|"): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Indent.kt#L11)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val withoutMargin1 = """ABC
                    |123
                    |456""".trimMargin()
    println(withoutMargin1)

    val withoutMargin2 = """
        #XYZ
        #foo
        #bar
    """.trimMargin("#")
    println(withoutMargin2)
}
```

```text title="输出"
ABC
123
456
XYZ
foo
bar
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L48)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
