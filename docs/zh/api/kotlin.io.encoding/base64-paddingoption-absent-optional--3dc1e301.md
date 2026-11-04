# Base64.PaddingOption.ABSENT_OPTIONAL

`kotlin.io.encoding` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

不要在编码上加页, 允许在解码上加选用页。

当编码时,结果不是加码。解码时,输入可以是加码,也可以是加码。如果输入含有一个加页字符,则必须显示正确的加页字符数量。加页字符`'='`标记编码数据的结尾,禁止随后的符号。

@sample 样本.i.e.encoding.Base64样本.

??? note "查看英文原文"

    Do not pad on encode, allow optional padding on decode.
    
    When encoding, the result is not padded.
    When decoding, the input may be either padded or unpadded. If the input contains a padding character,
    the correct amount of padding character(s) must be present. The padding character `'='`
    marks the end of the encoded data, and subsequent symbols are prohibited.
    
    @sample samples.io.encoding.Base64Samples.paddingOptionAbsentOptionalSample

## 声明与重载

### 1. Common

```kotlin
ABSENT_OPTIONAL
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L126)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*
import kotlin.test.*



fun main() {
    val format = HexFormat { upperCase = true; bytes.byteSeparator = " " }
    val bytes = byteArrayOf(0xDE.toByte(), 0x2D, 0x02, 0xC0.toByte())

    val base64AbsentOptionalPadding = Base64.Default.withPadding(Base64.PaddingOption.ABSENT_OPTIONAL)

    // PaddingOption.ABSENT_OPTIONAL does not pad on encode
    println(base64AbsentOptionalPadding.encode(bytes))
    // It allows both padded and unpadded decode inputs
    println(base64AbsentOptionalPadding.decode("3i0CwA").toHexString(format))
    println(base64AbsentOptionalPadding.decode("3i0CwA==").toHexString(format))
    // However, partially padded input is prohibited
    assertFailsWith<IllegalArgumentException> {
        base64AbsentOptionalPadding.decode("3i0CwA=")
    }
}
```

```text title="输出"
3i0CwA
DE 2D 02 C0
DE 2D 02 C0
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L168)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
