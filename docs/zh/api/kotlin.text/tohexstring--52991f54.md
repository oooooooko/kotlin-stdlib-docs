# toHexString

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

使用指定的 `format` 格式在此数组中格式字节。

请注意, `format` 实例中只有 `HexFormat.upperCase` 和 `HexFormat.bytes` 属性影响此字节数组的格式结果。

数组中的每一字节转换为两个十六进制位数。 第一个位数代表最重要的四位数,
第二位数代表字节中最小的四位数。 `HexFormat.upperCase` 财产确定
转换时使用大写(`0-9`,`A-F`)或小写(`0-9`,`a-f`)的十六进制数字。
`HexFormat.bytes` 属性指定了每个字节表示符头前缀和后缀的字符串,并定义了
如何安排这些陈述。

现有格式选项及其对格式化的影响详情请查阅`HexFormat.BytesHexFormat`。

@param 格式为 `HexFormat` 格式,用于格式化,默认为 `HexFormat.Default`。 @return 格式化此数组的结果是使用指定的 `format` 格式化该数组。

@throws 非法采购,如果结果长度超过 `String` 的最高容量,则不在此限。

@sample 样本. text. HexFormats. Extensions. byte 字节Array ToHexString 样本. text. HexFormats. 扩展. 字节 箭纹

??? note "查看英文原文"

    Formats bytes in this array using the specified `format`.
    
    Note that only the `HexFormat.upperCase` and `HexFormat.bytes` properties of the `format` instance affect
    the formatting result of this byte array.
    
    Each byte in the array is converted into two hexadecimal digits. The first digit represents the most significant 4 bits,
    and the second digit represents the least significant 4 bits of the byte. The `HexFormat.upperCase` property determines whether
    upper-case (`0-9`, `A-F`) or lower-case (`0-9`, `a-f`) hexadecimal digits are used for this conversion.
    The `HexFormat.bytes` property specifies the strings that prefix and suffix each byte representation, and defines
    how these representations are arranged.
    
    Refer to `HexFormat.BytesHexFormat` for details about the available format options and their impact on formatting.
    
    @param format the `HexFormat` to use for formatting, `HexFormat.Default` by default.
    @return the result of formatting this array using the specified `format`.
    
    @throws IllegalArgumentException if the result length exceeds the maximum capacity of `String`.
    
    @sample samples.text.HexFormats.Extensions.byteArrayToHexString

## 声明与重载

### 1. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
public fun ByteArray.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexExtensions.kt#L60)

### 2. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
public fun ByteArray.toHexString(
    startIndex: Int = 0,
    endIndex: Int = size,
    format: HexFormat = HexFormat.Default
): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexExtensions.kt#L85)

使用指定的 `format` 格式在此数组中格式字节。

请注意, `format` 实例中只有 `HexFormat.upperCase` 和 `HexFormat.bytes` 属性影响此字节数组的格式结果。

数组中的每一字节转换为两个十六进制位数。 第一个位数代表最重要的四位数,
第二位数代表字节中最小的四位数。 `HexFormat.upperCase` 财产确定
转换时使用大写(`0-9`,`A-F`)或小写(`0-9`,`a-f`)的十六进制数字。
`HexFormat.bytes` 属性指定了每个字节表示符头前缀和后缀的字符串,并定义了
如何安排这些陈述。

现有格式选项及其对格式化的影响详情请查阅`HexFormat.BytesHexFormat`。

@param 开始 CDDEX 子组合的起始( 包括) 格式, 默认为 0 。
@param 端端 子组合的结尾( 排他性) , 以格式化为目的, 默认情况下此数组的大小 。
@param 格式为 `HexFormat` ,默认用于格式化,`HexFormat.Default`。
@return 是使用指定的 `format` 格式化此数组的结果 。

@throws 指数外的值为`startIndex` 或 `endIndex` ,但该数组指数范围以外的值时除外。 @throws 非法设备除外,当`startIndex > endIndex`. @throws 非法设备超过`String`的最大容量时除外。

@sample 样本. text. HexFormats. Extensions. byte 字节Array ToHexString 样本. text. HexFormats. 扩展. 字节 箭纹

### 3. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
public fun Byte.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexExtensions.kt#L634)

使用指定的 `format` 格式化此`Byte` 值。

请注意, `format` 实例中只有 `HexFormat.upperCase` 和 `HexFormat.number` 属性影响这个数值的格式结果。

此函数将`Byte`值转换为十六进制表示法。 `HexFormat.upperCase` 属性将决定大写( `0-9`, `A-F`) 或小写( `0-9`, `a-f`) 是否用于此转换。 `HexFormat.number` 属性通过根据需要添加或删除前写零来调整十六进制表示法的长度,并指定前写和后写后的表示法的字符串。

现有格式选项及其对格式化的影响详情请查阅`HexFormat.NumberHexFormat`。

@param 格式为 `HexFormat` 格式,用于格式化,默认为 `HexFormat.Default`。 @return 格式化结果,使用指定的 `format` 格式化此值。

@sample 样本. text. HexFormats. Extensions. byte ToHexString 样本. text. HexFormats. 扩展. byte ToHexString 样本

### 4. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
public fun Short.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexExtensions.kt#L732)

使用指定的 `format` 格式化此`Short` 值。

请注意, `format` 实例中只有 `HexFormat.upperCase` 和 `HexFormat.number` 属性影响这个数值的格式结果。

此函数将`Short`值转换为十六进制表示法。 `HexFormat.upperCase` 属性将决定大写( `0-9`, `A-F`) 或小写( `0-9`, `a-f`) 是否用于此转换。 `HexFormat.number` 属性通过根据需要添加或删除前写零来调整十六进制表示法的长度,并指定前写和后写后的表示法的字符串。

现有格式选项及其对格式化的影响详情请查阅`HexFormat.NumberHexFormat`。

@param 格式为 `HexFormat` 格式,用于格式化,默认为 `HexFormat.Default`。 @return 格式化结果,使用指定的 `format` 格式化此值。

@sample 样本. text. HexFormats. Extensions. shortt ToHexString 样本. text. HexFormats. 扩展. 短期

### 5. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
public fun Int.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexExtensions.kt#L832)

使用指定的 `format` 格式化此`Int` 值。

请注意, `format` 实例中只有 `HexFormat.upperCase` 和 `HexFormat.number` 属性影响这个数值的格式结果。

此函数将`Int`值转换为十六进制表示法。 `HexFormat.upperCase` 属性将决定大写( `0-9`, `A-F`) 或小写( `0-9`, `a-f`) 是否用于此转换。 `HexFormat.number` 属性通过根据需要添加或删除前写零来调整十六进制表示法的长度,并指定前写和后写后的表示法的字符串。

现有格式选项及其对格式化的影响详情请查阅`HexFormat.NumberHexFormat`。

@param 格式为 `HexFormat` 格式,用于格式化,默认为 `HexFormat.Default`。 @return 格式化结果,使用指定的 `format` 格式化此值。

@sample 样本. text. HexFormats. Extensions.int ToHexString 样本. text. HexFormats. 扩展.int intHexString

### 6. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
public fun Long.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexExtensions.kt#L936)

使用指定的 `format` 格式化此`Long` 值。

请注意, `format` 实例中只有 `HexFormat.upperCase` 和 `HexFormat.number` 属性影响这个数值的格式结果。

此函数将`Long`值转换为十六进制表示法。 `HexFormat.upperCase` 属性将决定大写( `0-9`, `A-F`) 或小写( `0-9`, `a-f`) 是否用于此转换。 `HexFormat.number` 属性通过根据需要添加或删除前写零来调整十六进制表示法的长度,并指定前写和后写后的表示法的字符串。

现有格式选项及其对格式化的影响详情请查阅`HexFormat.NumberHexFormat`。

@param 格式为 `HexFormat` 格式,用于格式化,默认为 `HexFormat.Default`。 @return 格式化结果,使用指定的 `format` 格式化此值。

@sample 样本. text. HexFormats. Extensions. 长于 HexString

### 7. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
@ExperimentalUnsignedTypes
@InlineOnly
public inline fun UByteArray.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/UHexExtensions.kt#L12)

### 8. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
@ExperimentalUnsignedTypes
@InlineOnly
public inline fun UByteArray.toHexString(
    startIndex: Int = 0,
    endIndex: Int = size,
    format: HexFormat = HexFormat.Default
): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/UHexExtensions.kt#L39)

使用指定的 `format` 格式在此数组中格式字节。

请注意, `format` 实例中只有 `HexFormat.upperCase` 和 `HexFormat.bytes` 属性影响此字节数组的格式结果。

数组中的每一字节转换为两个十六进制位数。 第一个位数代表最重要的四位数,
第二位数代表字节中最小的四位数。 `HexFormat.upperCase` 财产确定
转换时使用大写(`0-9`,`A-F`)或小写(`0-9`,`a-f`)的十六进制数字。
`HexFormat.bytes` 属性指定了每个字节表示符头前缀和后缀的字符串,并定义了
如何安排这些陈述。

现有格式选项及其对格式化的影响详情请查阅`HexFormat.BytesHexFormat`。

@param 开始 CDDEX 子组合的起始( 包括) 格式, 默认为 0 。
@param 端端 子组合的结尾( 排他性) , 以格式化为目的, 默认情况下此数组的大小 。
@param 格式为 `HexFormat` ,默认用于格式化,`HexFormat.Default`。
@return 是使用指定的 `format` 格式化此数组的结果 。

@throws 指数外的值为`startIndex` 或 `endIndex` ,但该数组指数范围以外的值时除外。 @throws 非法设备除外,当`startIndex > endIndex`. @throws 非法设备超过`String`的最大容量时除外。

@sample 样本. text. HexFormats. Extensions. byte 字节Array ToHexString 样本. text. HexFormats. 扩展. 字节 箭纹

### 9. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
@InlineOnly
public inline fun UByte.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/UHexExtensions.kt#L102)

使用指定的 `format` 格式化此`UByte` 值。

请注意, `format` 实例中只有 `HexFormat.upperCase` 和 `HexFormat.number` 属性影响这个数值的格式结果。

此函数将`UByte`值转换为十六进制表示法。 `HexFormat.upperCase` 属性将决定大写( `0-9`, `A-F`) 或小写( `0-9`, `a-f`) 是否用于此转换。 `HexFormat.number` 属性通过根据需要添加或删除前写零来调整十六进制表示法的长度,并指定前写和后写后的表示法的字符串。

现有格式选项及其对格式化的影响详情请查阅`HexFormat.NumberHexFormat`。

@param 格式为 `HexFormat` 格式,用于格式化,默认为 `HexFormat.Default`。 @return 格式化结果,使用指定的 `format` 格式化此值。

@sample 样本. text. HexFormats. Extensions. byte ToHexString 样本. text. HexFormats. 扩展. byte ToHexString 样本

### 10. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
@InlineOnly
public inline fun UShort.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/UHexExtensions.kt#L156)

使用指定的 `format` 格式化此`UShort` 值。

请注意, `format` 实例中只有 `HexFormat.upperCase` 和 `HexFormat.number` 属性影响这个数值的格式结果。

此函数将`UShort`值转换为十六进制表示法。 `HexFormat.upperCase` 属性将决定大写( `0-9`, `A-F`) 或小写( `0-9`, `a-f`) 是否用于此转换。 `HexFormat.number` 属性通过根据需要添加或删除前写零来调整十六进制表示法的长度,并指定前写和后写后的表示法的字符串。

现有格式选项及其对格式化的影响详情请查阅`HexFormat.NumberHexFormat`。

@param 格式为 `HexFormat` 格式,用于格式化,默认为 `HexFormat.Default`。 @return 格式化结果,使用指定的 `format` 格式化此值。

@sample 样本. text. HexFormats. Extensions. shortt ToHexString 样本. text. HexFormats. 扩展. 短期

### 11. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
@InlineOnly
public inline fun UInt.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/UHexExtensions.kt#L210)

使用指定的 `format` 格式化此`UInt` 值。

请注意, `format` 实例中只有 `HexFormat.upperCase` 和 `HexFormat.number` 属性影响这个数值的格式结果。

此函数将`UInt`值转换为十六进制表示法。 `HexFormat.upperCase` 属性将决定大写( `0-9`, `A-F`) 或小写( `0-9`, `a-f`) 是否用于此转换。 `HexFormat.number` 属性通过根据需要添加或删除前写零来调整十六进制表示法的长度,并指定前写和后写后的表示法的字符串。

现有格式选项及其对格式化的影响详情请查阅`HexFormat.NumberHexFormat`。

@param 格式为 `HexFormat` 格式,用于格式化,默认为 `HexFormat.Default`。 @return 格式化结果,使用指定的 `format` 格式化此值。

@sample 样本. text. HexFormats. Extensions.int ToHexString 样本. text. HexFormats. 扩展.int intHexString

### 12. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.2")
@InlineOnly
public inline fun ULong.toHexString(format: HexFormat = HexFormat.Default): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/UHexExtensions.kt#L264)

使用指定的 `format` 格式化此`ULong` 值。

请注意, `format` 实例中只有 `HexFormat.upperCase` 和 `HexFormat.number` 属性影响这个数值的格式结果。

此函数将`ULong`值转换为十六进制表示法。 `HexFormat.upperCase` 属性将决定大写( `0-9`, `A-F`) 或小写( `0-9`, `a-f`) 是否用于此转换。 `HexFormat.number` 属性通过根据需要添加或删除前写零来调整十六进制表示法的长度,并指定前写和后写后的表示法的字符串。

现有格式选项及其对格式化的影响详情请查阅`HexFormat.NumberHexFormat`。

@param 格式为 `HexFormat` 格式,用于格式化,默认为 `HexFormat.Default`。 @return 格式化结果,使用指定的 `format` 格式化此值。

@sample 样本. text. HexFormats. Extensions. 长于 HexString

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val data = byteArrayOf(0xDE.toByte(), 0x2D, 0x02, 0xC0.toByte(), 0x5C, 0x0E)

    // Using the default format
    println(data.toHexString())

    // Using a custom format
    val format = HexFormat {
        upperCase = true
        bytes {
            bytesPerLine = 4
            byteSeparator = " " // One space
            bytePrefix = "0x"
        }
    }
    println(data.toHexString(format))

    // Formatting a segment of the byte array
    println(data.toHexString(startIndex = 2, endIndex = 5, format))

    // Formatting unsigned bytes with the same binary representations yields the same string
    val unsignedData = data.toUByteArray()
    println(unsignedData.toHexString(format))
}
```

```text title="输出"
de2d02c05c0e
0xDE 0x2D 0x02 0xC0
0x5C 0x0E
0x02 0xC0 0x5C
0xDE 0x2D 0x02 0xC0
0x5C 0x0E
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L365)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    // Using the default format
    val value: Byte = 58
    println(value.toHexString())

    // Converts the Byte to an unsigned hexadecimal representation
    println((-1).toByte().toHexString())

    // Using a custom format
    val format = HexFormat {
        upperCase = true
        number {
            prefix = "\\u" // A Unicode escape prefix
            minLength = 4
        }
    }
    println(value.toHexString(format))

    // Formatting an unsigned value with the same binary representations yields the same string
    val uValue: UByte = 58u
    println(uValue.toHexString(format))
}
```

```text title="输出"
3a
ff
\u003A
\u003A
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L422)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    // Using the default format
    val value: Short = 58
    println(value.toHexString())

    // Converts the Short to an unsigned hexadecimal representation
    println((-1).toShort().toHexString())

    // Using a custom format
    val format = HexFormat {
        upperCase = true
        number {
            prefix = "0x"
            removeLeadingZeros = true
        }
    }
    println(value.toHexString(format))

    // Formatting an unsigned value with the same binary representations yields the same string
    val uValue: UShort = 58u
    println(uValue.toHexString(format))
}
```

```text title="输出"
003a
ffff
0x3A
0x3A
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L474)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    // Using the default format
    val value = 58
    println(value.toHexString())

    // Converts the Int to an unsigned hexadecimal representation
    println((-1).toHexString())

    // Using a custom format
    val format = HexFormat {
        upperCase = true
        number {
            prefix = "#"
            removeLeadingZeros = true
            minLength = 6
        }
    }
    println(value.toHexString(format))

    // Formatting an unsigned value with the same binary representations yields the same string
    val uValue = 58u
    println(uValue.toHexString(format))
}
```

```text title="输出"
0000003a
ffffffff
#00003A
#00003A
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L526)

### 示例 5 · JVM

```kotlin title="示例 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    // Using the default format
    val value = 58L
    println(value.toHexString())

    // Converts the Long to an unsigned hexadecimal representation
    println((-1L).toHexString())

    // Using a custom format
    val format = HexFormat {
        upperCase = true
        number.removeLeadingZeros = true
    }
    println(value.toHexString(format))

    // Formatting an unsigned value with the same binary representations yields the same string
    val uValue = 58uL
    println(uValue.toHexString(format))
}
```

```text title="输出"
000000000000003a
ffffffffffffffff
3A
3A
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L579)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
