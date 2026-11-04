# Base64.PaddingOption

`kotlin.io.encoding` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

列举可能用于 Base64 编码和解码的拼贴选项。

此enum 类的常数可以传递到 `withPadding` 函数, 以创建带有指定键盘选项的新的 Base64 实例。 每个粘贴选项都以下列方式影响 Base64 实例的编码和解码操作 :


- - - - - - - - - - - - - - - - - - - - -
需要 `PaddingOption.PRESENT`  Emit
`PaddingOption.ABSENT`  Omit
`PaddingOption.PRESENT_OPTIONAL`  Emit
`PaddingOption.ABSENT_OPTIONAL`  Omit

这些选项为处理垫字( `'='` )提供了灵活性,并使得与各种基地64图书馆和协议兼容。

@sample 样本.i.e.encoding.Base64样本.

??? note "查看英文原文"

    An enumeration of the possible padding options for Base64 encoding and decoding.
    
    Constants of this enum class can be passed to the `withPadding` function to create a new Base64 instance
    with the specified padding option. Each padding option affects the encode and decode operations of the
    Base64 instance in the following way:
    
    | PaddingOption                    | On encode    | On decode                |
    |----------------------------------|--------------|--------------------------|
    | `PaddingOption.PRESENT`          | Emit padding | Padding is required      |
    | `PaddingOption.ABSENT`           | Omit padding | Padding must not present |
    | `PaddingOption.PRESENT_OPTIONAL` | Emit padding | Padding is optional      |
    | `PaddingOption.ABSENT_OPTIONAL`  | Omit padding | Padding is optional      |
    
    These options provide flexibility in handling the padding characters (`'='`) and enable compatibility with
    various Base64 libraries and protocols.
    
    @sample samples.io.encoding.Base64Samples.paddingOptionSample

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.0")
    public enum class PaddingOption
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L70)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*
import kotlin.test.*



fun main() {
    val format = HexFormat {
        upperCase = true
        bytes.byteSeparator = " "
    }

    val bytes = byteArrayOf(0xDE.toByte(), 0x2D, 0x02, 0xC0.toByte())

    // The Base64.Default instance is configured with PaddingOption.PRESENT
    println(Base64.Default.encode(bytes))
    println(Base64.Default.decode("3i0CwA==").toHexString(format))
    // PaddingOption.PRESENT requires the decode input to be properly padded
    assertFailsWith<IllegalArgumentException> {
        Base64.Default.decode("3i0CwA")
    }

    // Create a new instance with PaddingOption.ABSENT that uses the Base64.Default alphabet
    val base64AbsentPadding = Base64.Default.withPadding(Base64.PaddingOption.ABSENT)

    println(base64AbsentPadding.encode(bytes))
    println(base64AbsentPadding.decode("3i0CwA").toHexString(format))
    // PaddingOption.ABSENT requires the decode input not to be padded
    assertFailsWith<IllegalArgumentException> {
        base64AbsentPadding.decode("3i0CwA==")
    }

    // Create a new instance with PaddingOption.PRESENT_OPTIONAL that uses the Base64.Default alphabet
    val base64PresentOptionalPadding = Base64.Default.withPadding(Base64.PaddingOption.PRESENT_OPTIONAL)

    println(base64PresentOptionalPadding.encode(bytes))
    // PaddingOption.PRESENT_OPTIONAL allows both padded and unpadded decode inputs
    println(base64PresentOptionalPadding.decode("3i0CwA==").toHexString(format))
    println(base64PresentOptionalPadding.decode("3i0CwA").toHexString(format))
    // However, partially padded input is prohibited
    assertFailsWith<IllegalArgumentException> {
        base64PresentOptionalPadding.decode("3i0CwA=")
    }

    // Create a new instance with PaddingOption.ABSENT_OPTIONAL that uses the Base64.Default alphabet
    val base64AbsentOptionalPadding = Base64.Default.withPadding(Base64.PaddingOption.ABSENT_OPTIONAL)

    println(base64AbsentOptionalPadding.encode(bytes))
    // PaddingOption.ABSENT_OPTIONAL allows both padded and unpadded decode inputs
    println(base64AbsentOptionalPadding.decode("3i0CwA").toHexString(format))
    println(base64AbsentOptionalPadding.decode("3i0CwA==").toHexString(format))
    // However, partially padded input is prohibited
    assertFailsWith<IllegalArgumentException> {
        base64AbsentOptionalPadding.decode("3i0CwA=")
    }
}
```

```text title="输出"
3i0CwA==
DE 2D 02 C0
3i0CwA
DE 2D 02 C0
3i0CwA==
DE 2D 02 C0
DE 2D 02 C0
3i0CwA
DE 2D 02 C0
DE 2D 02 C0
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L50)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
