# Base64.Default.Mime

`kotlin.io.encoding` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

由 [ `RFC 2045 section 6.8` ] (https://www.rfc-editor.org/rfc/rfc2045#section-6.8), base64) 指定的编码内容- 传输- 编码 。

使用RFC 2045 表1中“Base64 字母” 来编码和解码,包括`'A'..'Z'`、`'a'..'z'`、`'+'`和`'/'`字符。

此例配置为套接字选项, 设置为 `PaddingOption.PRESENT`。 使用 `withPadding` 函数创建新例, 必要时使用不同的套接字选项 。

编码操作每76个符号就增加 CRLF。 编码输出的结尾处没有添加线条分隔符。 解码操作忽略了底部64 字母以外的所有线条分隔符和其他字符 。

@sample 样本.i.e.encoding.Base64Samples.mime EncodingSample

??? note "查看英文原文"

    The encoding specified by [`RFC 2045 section 6.8`](https://www.rfc-editor.org/rfc/rfc2045#section-6.8),
    Base64 Content-Transfer-Encoding.
    
    Uses "The Base64 Alphabet" as specified in Table 1 of RFC 2045 for encoding and decoding,
    consisting of `'A'..'Z'`, `'a'..'z'`, `'+'` and `'/'` characters.
    
    This instance is configured with the padding option set to `PaddingOption.PRESENT`.
    Use the `withPadding` function to create a new instance with a different padding option if necessary.
    
    Encode operation adds CRLF every 76 symbols. No line separator is added to the end of the encoded output.
    Decode operation ignores all line separators and other characters outside the base64 alphabet.
    
    @sample samples.io.encoding.Base64Samples.mimeEncodingSample

## 声明与重载

### 1. Common

```kotlin
public val Mime: Base64
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L738)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    val encoded = Base64.Mime.encode("Hello? :> ".encodeToByteArray())
    println(encoded)

    // Mime encoding ignores all characters not belonging to its alphabet
    val decoded = Base64.Mime.decode("Y@{mFz!Z!TY}0")
    println(decoded.decodeToString())

    // let's encode some long text
    val sourceText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, " +
            "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " +
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris " +
            "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in " +
            "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla " +
            "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa" +
            " qui officia deserunt mollit anim id est laborum."

    val encodedText = Base64.Mime.encode(sourceText.encodeToByteArray())
    println(encodedText)

    val encodedLines = encodedText.lines()
    println("${encodedLines.count()} lines, at most ${encodedLines.maxOf { it.length }} characters each")

    println(sourceText == Base64.Mime.decode(encodedText).decodeToString())
}
```

```text title="输出"
SGVsbG8/IDo+IA==
base64
TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdCwg
c2VkIGRvIGVpdXNtb2QgdGVtcG9yIGluY2lkaWR1bnQgdXQgbGFib3JlIGV0IGRvbG9yZSBtYWdu
YSBhbGlxdWEuIFV0IGVuaW0gYWQgbWluaW0gdmVuaWFtLCBxdWlzIG5vc3RydWQgZXhlcmNpdGF0
aW9uIHVsbGFtY28gbGFib3JpcyBuaXNpIHV0IGFsaXF1aXAgZXggZWEgY29tbW9kbyBjb25zZXF1
YXQuIER1aXMgYXV0ZSBpcnVyZSBkb2xvciBpbiByZXByZWhlbmRlcml0IGluIHZvbHVwdGF0ZSB2
ZWxpdCBlc3NlIGNpbGx1bSBkb2xvcmUgZXUgZnVnaWF0IG51bGxhIHBhcmlhdHVyLiBFeGNlcHRl
dXIgc2ludCBvY2NhZWNhdCBjdXBpZGF0YXQgbm9uIHByb2lkZW50LCBzdW50IGluIGN1bHBhIHF1
aSBvZmZpY2lhIGRlc2VydW50IG1vbGxpdCBhbmltIGlkIGVzdCBsYWJvcnVtLg==
8 lines, at most 76 characters each
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L192)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
