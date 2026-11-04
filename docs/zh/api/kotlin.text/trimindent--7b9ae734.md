# trimIndent

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

检测所有输入行的最小公分缩进,从每行中去除,如果第一行和最后一行为空白(通知差数为空白或空),则删除第一行和最后一行。

请注意,空白行不影响检测到的缩进水平。

如果有非空白线条没有主要空白字符( 完全不缩进) , 则通用缩进为 0, 因此此函数不会改变缩进 。

原字符串中的线条可以与 `\r\n` (CRLF)、`\n`(LF)、 `\r` (CR)字符分隔,但是,由此产生的字符串中的线条将完全与 `\n` (LF)字符分隔。

@sample 样本. 文本. strings. trrimm 缩写 @see 三角

??? note "查看英文原文"

    Detects a common minimal indent of all the input lines, removes it from every line and also removes the first and the last
    lines if they are blank (notice difference blank vs empty).
    
    Note that blank lines do not affect the detected indent level.
    
    In case if there are non-blank lines with no leading whitespace characters (no indent at all) then the
    common indent is 0, and therefore this function doesn't change the indentation.
    
    The lines in the original string can be separated with `\r\n` (CRLF), `\n` (LF), or `\r` (CR) characters, however, the lines in the
    resulting string will be separated solely with `\n` (LF) character.
    
    @sample samples.text.Strings.trimIndent
    @see trimMargin
    @see kotlin.text.isBlank

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.IntrinsicConstEvaluation
public fun String.trimIndent(): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Indent.kt#L53)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val withoutIndent =
            """
                ABC
                123
                456
            """.trimIndent()
    println(withoutIndent)
}
```

```text title="输出"
ABC
123
456
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L37)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
