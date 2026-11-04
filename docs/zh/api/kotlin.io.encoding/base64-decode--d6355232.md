# Base64.decode

`kotlin.io.encoding` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

解码指定`source` 矩阵或其子序列的符号。返回 `ByteArray` , 包含由此产生的字节。

输入符号中铺设布的要求、禁止或可选性由为这`Base64`例设定的`PaddingOption`确定。

@param 源为用于解码符号的数组,从 @param 开头 Index 开始( 包括) 开始解码, 默认为 0。 @param 结束 Index 结束于 解码的子数组的结尾( 排他) , 默认为 `source` 矩阵的大小 。

`startIndex`或`endIndex`不在`source`阵列指数范围内时,@throws指数外出外出外出,但有例外。
@throws非法 参数`startIndex > endIndex`.
@throws 非法参数例外,当解码符号没有按照`PaddingOption`的要求加盖时
设置此 `Base64` 实例, 或挂牌后有额外符号时 。

@return a `ByteArray` 加上由此产生的字节。

@sample 样本.io.encoding.Base64Samples. 解码来自Byte 阵列样本

??? note "查看英文原文"

    Decodes symbols from the specified `source` array or its subrange.
    Returns a `ByteArray` containing the resulting bytes.
    
    The requirement, prohibition, or optionality of padding in the input symbols
    is determined by the `PaddingOption` set for this `Base64` instance.
    
    @param source the array to decode symbols from.
    @param startIndex the beginning (inclusive) of the subrange to decode, 0 by default.
    @param endIndex the end (exclusive) of the subrange to decode, size of the `source` array by default.
    
    @throws IndexOutOfBoundsException when `startIndex` or `endIndex` is out of range of `source` array indices.
    @throws IllegalArgumentException when `startIndex > endIndex`.
    @throws IllegalArgumentException when the symbols for decoding are not padded as required by the `PaddingOption`
      set for this `Base64` instance, or when there are extra symbols after the padding.
    
    @return a `ByteArray` with the resulting bytes.
    
    @sample samples.io.encoding.Base64Samples.decodeFromByteArraySample

## 声明与重载

### 1. Common

```kotlin
public fun decode(source: ByteArray, startIndex: Int = 0, endIndex: Int = source.size): ByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L264)

### 2. Common

```kotlin
public fun decode(source: CharSequence, startIndex: Int = 0, endIndex: Int = source.length): ByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L334)

解码指定 `source` 字符序列或其子字符串中的符号。返回包含所生成字节的`ByteArray`。

输入符号中铺设布的要求、禁止或可选性由为这`Base64`例设定的`PaddingOption`确定。

@param 源代码为解码符号的字符序列,从 @param 开始 INdex 开始( 包括) 开始到解码, 默认为 0。 @param 结束 INdex 结束 ( 排他) 结束 到解码, 默认为 `source` 长度 。

@throws 指数外出值,但 `startIndex` 或 `endIndex` 指数范围在 `source` 指数之外的情况除外。 @throws 非法设备除外,当`startIndex > endIndex` @throws 非法设备外出值没有按照为`Base64` 案例设定的 8,0000008 设定的`PaddingOption` 的符号进行加注时,或者当在铺设后有额外符号时,非法设备外出值除外。

@return a `ByteArray` 加上由此产生的字节。

@sample 样本.io.encoding.Base64Samples.从StringSample解码

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    // get a byte array filled with data, for instance, by reading it from a network
    val data = byteArrayOf(0x61, 0x47, 0x56, 0x73, 0x62, 0x47, 0x38, 0x3d)
    // decode data from the array
    println(Base64.decode(data).contentEquals("hello".encodeToByteArray()))

    val dataInTheMiddle = byteArrayOf(0x00, 0x00, 0x61, 0x47, 0x56, 0x73, 0x62, 0x47, 0x38, 0x3d, 0x00, 0x00)
    // decode base64-encoded data from the middle of a buffer
    val decoded = Base64.decode(dataInTheMiddle, startIndex = 2, endIndex = 10)
    println(decoded.contentEquals("hello".encodeToByteArray()))
}
```

```text title="输出"
true
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L317)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    println(Base64.decode("/wD+AP0=").contentEquals(byteArrayOf(-1, 0, -2, 0, -3)))

    val embeddedB64 = "Data is: \"/wD+AP0=\""
    // find '"' indices and extract base64-encoded data in between
    val decoded = Base64.decode(
        embeddedB64,
        startIndex = embeddedB64.indexOf('"') + 1,
        endIndex = embeddedB64.lastIndexOf('"')
    )
    println(decoded.contentEquals(byteArrayOf(-1, 0, -2, 0, -3)))
}
```

```text title="输出"
true
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L330)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
