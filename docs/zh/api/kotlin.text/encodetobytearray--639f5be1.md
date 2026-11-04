# encodeToByteArray

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将此字符串编码为 UTF-8 编码的字节数组。

替换字节序列取代任何格式错误的字符序列。

@sample 样本. 文本. Strings. encode ToByte 阵列

??? note "查看英文原文"

    Encodes this string to an array of bytes in UTF-8 encoding.
    
    Any malformed char sequence is replaced by the replacement byte sequence.
    
    @sample samples.text.Strings.encodeToByteArray

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public expect fun String.encodeToByteArray(): ByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L348)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public expect fun String.encodeToByteArray(
    startIndex: Int = 0,
    endIndex: Int = this.length,
    throwOnInvalidSequence: Boolean = false
): ByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L358)

将此字符串或其子字符串编码为以 UTF-8 编码的字节数组。

@param 开始 Index 编码的子字符串开头(包括) 0 默认为 。 @param endIndex 编码的子字符串结尾(不包括) 。 @param 扔 OnInvalidSercece 指定对错误的字符序列是否排除或替换 。

@throws 指数外在值为`startIndex` 的,如果`startIndex` 低于0 或 `endIndex` 大于此字符串的长度,则除外。 @throws 非法说明,如果 `startIndex` 大于 `endIndex`, @throws 字符串包含错误的字符序列,且 `throwOnInvalidSequence` 是真的,则不在此列。

@sample 样本. 文本. Strings. encode ToByte 阵列

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val format = HexFormat { bytes { groupSeparator = " "; bytesPerGroup = 1 } }

    // \u00a0 is a non-breaking space
    val str = "Kòtlin\u00a02.1.255"

    // The original string contains 14 characters, but some of them are represented with multiple UTF-8 code units
    val byteArray = str.encodeToByteArray()
    println(byteArray.toHexString(format))

    // Replacing all "wide" characters with some ASCII ones results in a byte sequence matching the length of the string
    val byteArrayWithAsciiCharacters = str.replace("\u00a0", " ").replace("ò", "o").encodeToByteArray()
    println(byteArrayWithAsciiCharacters.toHexString(format))

    val byteArrayWithVersion = str.encodeToByteArray(startIndex = 7)
    println(byteArrayWithVersion.toHexString(format))

    val byteArrayWithoutTheVersion = str.encodeToByteArray(startIndex = 0, endIndex = 6)
    println(byteArrayWithoutTheVersion.toHexString(format))
}
```

```text title="输出"
4b c3 b2 74 6c 69 6e c2 a0 32 2e 31 2e 32 35 35
4b 6f 74 6c 69 6e 20 32 2e 31 2e 32 35 35
32 2e 31 2e 32 35 35
4b c3 b2 74 6c 69 6e
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L832)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
