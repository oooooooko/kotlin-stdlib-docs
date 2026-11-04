# Base64.Default.UrlSafe

`kotlin.io.encoding` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

由 [`RFC 4648 section 5`] (https://www.rfc-editor.org/rfc/rfc4648#section-5), base 64) 指定的“ base64url” 编码, 以 URL 和 文件名安全字母编码 。

使用RFC 4648表2中“URL和文件名称安全基底64字母”中指定的“URL和文件名称安全基底64字母”编码和解码,包括`'A'..'Z'`、 `'a'..'z'` 、`'-'`和 `'_'` 字符。

此例配置为套接字选项, 设置为 `PaddingOption.PRESENT`。 使用 `withPadding` 函数创建新例, 必要时使用不同的套接字选项 。

编码操作不添加任何线性分隔符。如果在基质64url 字母表外出现字符,则解码操作会丢弃。

@sample 样本.io.encoding.Base64Samples.urlSafeEnccodingSample 样本

??? note "查看英文原文"

    The "base64url" encoding specified by [`RFC 4648 section 5`](https://www.rfc-editor.org/rfc/rfc4648#section-5),
    Base 64 Encoding with URL and Filename Safe Alphabet.
    
    Uses "The URL and Filename safe Base 64 Alphabet" as specified in Table 2 of RFC 4648 for encoding and decoding,
    consisting of `'A'..'Z'`, `'a'..'z'`, `'-'` and `'_'` characters.
    
    This instance is configured with the padding option set to `PaddingOption.PRESENT`.
    Use the `withPadding` function to create a new instance with a different padding option if necessary.
    
    Encode operation does not add any line separator character.
    Decode operation throws if it encounters a character outside the base64url alphabet.
    
    @sample samples.io.encoding.Base64Samples.urlSafeEncodingSample

## 声明与重载

### 1. Common

```kotlin
public val UrlSafe: Base64
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L721)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    val encoded = Base64.UrlSafe.encode("Hello? :> ".encodeToByteArray())
    println(encoded)
}
```

```text title="输出"
SGVsbG8_IDo-IA==
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L246)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
