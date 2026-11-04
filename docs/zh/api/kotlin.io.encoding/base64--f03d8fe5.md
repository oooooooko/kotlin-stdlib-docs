# Base64

`kotlin.io.encoding` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

提供 Base64 编码和解码功能。 由 [ `RFC 4648` ] (https://www.rfc-editor.org/rfc/rfc4648)) 和其他一些 RFC 定义的 Base64 编码将任意的二进制数据转换成一系列可打印字符。

例如, `0xC0 0xFF 0xEE` 字节的序列将转换为`"wP/u"`字符串,使用[`RFC 4648`] (https://www.rfc-editor.org/rfc/rfc4648).) 定义的 Base64 编码,该字符串将产生原始字节序列。

** Base64不是一个加密方案,在需要确保数据或数据混淆时不应使用。 **

特定Base64方案使用的字符构成64个普通字符的字母表和额外的挂牌字符。

几乎所有的Base64编码方法 都有一个字母字母的前62个字符
中,`'A'..'Z'`是`'a'..'z'`,后面是`'a'..'z'`,但最后两个字符可能有所不同。
[`RFC 4648 section 4`](https://www.rfc-editor.org/rfc/rfc4648#section-4) 定义使用
`'+'`和`'/'`是最后两个字符,而URL安全字母表的定义为
[`RFC 4648 section 5`](https://www.rfc-editor.org/rfc/rfc4648#section-5)使用`'-'`和`'_'`代替。

当解码时,一个Base64 方案通常只接受其字母表中的字符,任何其他字符的存在都被视为错误(此规则的例外情形见`Base64.Mime`),这也意味着如果其字母不同,一个Base64 方案无法解码另一个Base64 方案编码的数据。

除了字母中的64个字符外, Base64-encodd data 也可能在结尾处包含一两个插入字符 `'='` 。 Base64 分割数据,需要将其编码成块块三字节长,然后转换成四个字符序列(这意味着每个字符编码六字组数据六字组)。如果构成输入数据的字节数不是三个字组的倍数(例如,输入只包括五个字组),数据将首先被零位元加起来,然后才转换成Base64-alphabet字符。如果进行插入,则生成的字符串将增加 `'='` 。该数据可以由零、两或四个字组组成,因此编码数据将分别包含零、一或两个字组字符(`'='`),因此,在生成的字符组中加入挂字组字符组取决于为 Base64 实例设定的 `PaddingOption` 。

此类不应通过调用其构建器来继承或即时处理。 但是, 此类的预设实例可以使用。 随物对象 `Base64.Default` 是 `Base64` 默认实例。 另有 `Base64.UrlSafe` 和 `Base64.Mime` 实例。 所有预设实例的挂贴选项设置为 `PaddingOption.PRESENT` 。 使用 `withPadding` 函数可以创建带有不同挂贴选项的新实例 。

@sample 样本.io.encoding.Base64Samples.encode和Decode @sample 样本.i.encoding.Base64Samples.encoding differences @sample 样本.i.encoding.Base64Samples.pating.

??? note "查看英文原文"

    Provides Base64 encoding and decoding functionality.
    Base64 encoding, as defined by the [`RFC 4648`](https://www.rfc-editor.org/rfc/rfc4648) and a few other RFCs,
    transforms arbitrary binary data into a sequence of printable characters.
    
    For example, a sequence of bytes `0xC0 0xFF 0xEE` will be transformed to a string `"wP/u"` using a Base64 encoding
    defined by the [`RFC 4648`](https://www.rfc-editor.org/rfc/rfc4648). Decoding that string will result in the original
    byte sequence.
    
    **Base64 is not an encryption scheme and should not be used when data needs to be secured or obfuscated.**
    
    Characters used by a particular Base64 scheme form an alphabet of 64 regular characters and
    an extra padding character.
    
    Almost all Base64 encoding schemes share the same first 62 characters of an alphabet,
    which are `'A'..'Z'` followed by `'a'..'z'`, but the last two characters may vary.
    [`RFC 4648 section 4`](https://www.rfc-editor.org/rfc/rfc4648#section-4) defines an alphabet that uses
    `'+'` and `'/'` as the last two characters, while the URL-safe alphabet defined in
    [`RFC 4648 section 5`](https://www.rfc-editor.org/rfc/rfc4648#section-5) uses `'-'` and `'_'` instead.
    
    When decoding, a Base64 scheme usually accepts only characters from its alphabet, presence of any other characters
    is treated as an error (see `Base64.Mime` for an exception to this rule). That also implies
    that a Base64 scheme could not decode data encoded by another Base64 scheme if their alphabets differ.
    
    In addition to 64 characters from the alphabet,
    Base64-encoded data may also contain one or two padding characters `'='` at its end.
    Base64 splits data that needs to be encoded into chunks three bytes long, which are then transformed into
    a sequence of four characters (meaning that every character encodes six bits of data).
    If the number of bytes constituting input data is not a multiple of three (for instance, input consists of only five bytes),
    the data will be padded by zero bits first and only then transformed into Base64-alphabet characters.
    If padding takes place, the resulting string is augmented by `'='`. The padding could consist of zero, two or
    four bits, thus encoded data will contain zero, one or two padding characters (`'='`), respectively.
    The inclusion of padding characters in the resulting string depends on the `PaddingOption` set for the Base64 instance.
    
    This class is not supposed to be inherited or instantiated by calling its constructor.
    However, predefined instances of this class are available for use.
    The companion object `Base64.Default` is the default instance of `Base64`.
    There are also `Base64.UrlSafe` and `Base64.Mime` instances.
    The padding option for all predefined instances is set to `PaddingOption.PRESENT`.
    New instances with different padding options can be created using the `withPadding` function.
    
    @sample samples.io.encoding.Base64Samples.encodeAndDecode
    @sample samples.io.encoding.Base64Samples.encodingDifferences
    @sample samples.io.encoding.Base64Samples.padding

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.2")
@WasExperimental(ExperimentalEncodingApi::class)
public open class Base64 private constructor(
    internal val isUrlSafe: Boolean,
    internal val isMimeScheme: Boolean,
    internal val mimeLineLength: Int,
    internal val paddingOption: PaddingOption
)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L10)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    val encoded = Base64.Default.encode("Hello, World!".encodeToByteArray())
    println(encoded)

    val decoded = Base64.Default.decode(encoded)
    println(decoded.decodeToString())
}
```

```text title="输出"
SGVsbG8sIFdvcmxkIQ==
Hello, World!
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L14)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*
import kotlin.test.*



fun main() {
    // Default encoding uses '/' and '+' as the last two characters of the Base64 alphabet
    println(Base64.Default.encode(byteArrayOf(-1, 0, -2, 0)))
    // Mime's alphabet is the same as Default's
    println(Base64.Mime.encode(byteArrayOf(-1, 0, -2, 0)))
    // UrlSafe encoding uses '_' and '-' as the last two Base64 alphabet characters
    println(Base64.UrlSafe.encode(byteArrayOf(-1, 0, -2, 0)))

    // UrlSafe uses `-` and `_`, so the following string could not be decoded
    assertFailsWith<IllegalArgumentException> {
        Base64.UrlSafe.decode("/wD+AA==")
    }
}
```

```text title="输出"
/wD+AA==
/wD+AA==
_wD-AA==
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L35)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    // "base".length == 4, which is not multiple of 3;
    // base64-encoded data padded with 4 bits
    println(Base64.Default.encode("base".encodeToByteArray()))
    // "base6".length == 5, which is not multiple of 3;
    // base64-encoded data padded with 2 bits
    println(Base64.Default.encode("base6".encodeToByteArray()))
    // "base64".length == 6, which is the multiple of 3, so no padding is required
    println(Base64.Default.encode("base64".encodeToByteArray()))
}
```

```text title="输出"
YmFzZQ==
YmFzZTY=
YmFzZTY0
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L23)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
