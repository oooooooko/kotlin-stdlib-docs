# Base64.PaddingOption.PRESENT

`kotlin.io.encoding` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

密码上的帕德 需要密码上的粘贴

当编码时,结果会以 `'='` 加到一个四个符号的组合。在解码时,需要正确的加注输入。输入字符为 `'='` ,标记编码数据的结尾,禁止随后的符号。

这是Base64编码的卡通形式。

@sample 样本.i.e.encoding.Base64Samples.papting optionsamples 选项样本

??? note "查看英文原文"

    Pad on encode, require padding on decode.
    
    When encoding, the result is padded with `'='` to reach an integral multiple of 4 symbols.
    When decoding, correctly padded input is required. The padding character `'='` marks the end
    of the encoded data, and subsequent symbols are prohibited.
    
    This represents the canonical form of Base64 encoding.
    
    @sample samples.io.encoding.Base64Samples.paddingOptionPresentSample

## 声明与重载

### 1. Common

```kotlin
PRESENT,
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L91)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*
import kotlin.test.*



fun main() {
    val format = HexFormat { upperCase = true; bytes.byteSeparator = " " }
    val bytes = byteArrayOf(0xDE.toByte(), 0x2D, 0x02, 0xC0.toByte())

    // The predefined Base64 instances are configured with PaddingOption.PRESENT.
    // Hence, the same instance is returned.
    val isSameInstance = Base64.Default.withPadding(Base64.PaddingOption.PRESENT) === Base64.Default
    println(isSameInstance)

    // PaddingOption.PRESENT pads on encode, and requires padded input on decode
    println(Base64.Default.encode(bytes))
    println(Base64.Default.decode("3i0CwA==").toHexString(format))
    // PaddingOption.PRESENT requires the decode input to be properly padded
    assertFailsWith<IllegalArgumentException> {
        Base64.Default.decode("3i0CwA")
    }
}
```

```text title="输出"
true
3i0CwA==
DE 2D 02 C0
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L115)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
