# Base64.Default

`kotlin.io.encoding` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

由[ `RFC 4648 section 4` ] (https://www.rfc-editor.org/rfc/rfc4648#section-4), base 64编码)指定的“ base64” 编码 。

使用RFC 4648表1中“64字母”中的“基础字母”来编码和解码,包括 `'A'..'Z'` 、 `'a'..'z'` 、 `'+'` 和 `'/'` 字符。

此例配置为套接字选项, 设置为 `PaddingOption.PRESENT`。 使用 `withPadding` 函数创建新例, 必要时使用不同的套接字选项 。

编码操作不添加任何线性分隔符。如果在基数64字母表外遇到字符,则解码操作会丢弃。

@sample 样本.io.encoding.Base64Samples.default EncordingSample 默认编码样本

??? note "查看英文原文"

    The "base64" encoding specified by [`RFC 4648 section 4`](https://www.rfc-editor.org/rfc/rfc4648#section-4),
    Base 64 Encoding.
    
    Uses "The Base 64 Alphabet" as specified in Table 1 of RFC 4648 for encoding and decoding, consisting of
    `'A'..'Z'`, `'a'..'z'`, `'+'` and `'/'` characters.
    
    This instance is configured with the padding option set to `PaddingOption.PRESENT`.
    Use the `withPadding` function to create a new instance with a different padding option if necessary.
    
    Encode operation does not add any line separator character.
    Decode operation throws if it encounters a character outside the base64 alphabet.
    
    @sample samples.io.encoding.Base64Samples.defaultEncodingSample

## 声明与重载

### 1. Common

```kotlin
public companion object Default : Base64(isUrlSafe = false, isMimeScheme = false, mimeLineLength = -1, paddingOption = PaddingOption.PRESENT)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L692)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    val encoded = Base64.Default.encode("Hello? :> ".encodeToByteArray())
    println(encoded)
}
```

```text title="输出"
SGVsbG8/IDo+IA==
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L186)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
