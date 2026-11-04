# Base64.decodeIntoByteArray

`kotlin.io.encoding` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

解码指定 `source` 阵列或其子阵列中的符号,并将由此生成的字节写入 `destination` 阵列。返回已写入的字节数。

输入符号中铺设布的要求、禁止或可选性由为这`Base64`例设定的`PaddingOption`确定。

@param 源码从 @param 目的地解码符号的数组。 @param 目的地数组将字节写入. @param 目的地数组 。 `destination` 目标数组的起始索引将默认写入 0。 @param 开始输入要解码的子数组的起始( 包括) 。 @param 终点数组将结尾( 排他) 插入子数组的解码, 默认写出 `source` 矩阵的大小 。

`startIndex`或`endIndex`不在`source`阵列指数范围内时,@throws指数外出外出外出,但有例外。
@throws非法 参数`startIndex > endIndex`.
@throws 指数外观 例外 当产生的字节不适应`destination`阵列时 从指定的 `destinationOffset` 开始
当该索引超出`destination` 矩阵指数范围时。
@throws 非法参数例外,当解码符号没有按照`PaddingOption`的要求加盖时
设置此 `Base64` 实例, 或挂牌后有额外符号时 。

@return 以 `destination` 矩阵中写入的字节数 。

@sample 样本.io.encoding.Base64Samples. decodeIntoByte 箭头来自ByteAraySample

??? note "查看英文原文"

    Decodes symbols from the specified `source` array or its subrange and writes resulting bytes into the `destination` array.
    Returns the number of bytes written.
    
    The requirement, prohibition, or optionality of padding in the input symbols
    is determined by the `PaddingOption` set for this `Base64` instance.
    
    @param source the array to decode symbols from.
    @param destination the array to write bytes into.
    @param destinationOffset the starting index in the `destination` array to write bytes to, 0 by default.
    @param startIndex the beginning (inclusive) of the subrange to decode, 0 by default.
    @param endIndex the end (exclusive) of the subrange to decode, size of the `source` array by default.
    
    @throws IndexOutOfBoundsException when `startIndex` or `endIndex` is out of range of `source` array indices.
    @throws IllegalArgumentException when `startIndex > endIndex`.
    @throws IndexOutOfBoundsException when the resulting bytes don't fit into the `destination` array starting at the specified `destinationOffset`,
    or when that index is out of the `destination` array indices range.
    @throws IllegalArgumentException when the symbols for decoding are not padded as required by the `PaddingOption`
      set for this `Base64` instance, or when there are extra symbols after the padding.
    
    @return the number of bytes written into `destination` array.
    
    @sample samples.io.encoding.Base64Samples.decodeIntoByteArrayFromByteArraySample

## 声明与重载

### 1. Common

```kotlin
public fun decodeIntoByteArray(
        source: ByteArray,
        destination: ByteArray,
        destinationOffset: Int = 0,
        startIndex: Int = 0,
        endIndex: Int = source.size
    ): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L297)

### 2. Common

```kotlin
public fun decodeIntoByteArray(
        source: CharSequence,
        destination: ByteArray,
        destinationOffset: Int = 0,
        startIndex: Int = 0,
        endIndex: Int = source.length
    ): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L359)

解码指定 `source` 字符序列或其子字符串中的符号,并将由此产生的字节写入 `destination` 矩阵。返回已写入的字节数。

输入符号中铺设布的要求、禁止或可选性由为这`Base64`例设定的`PaddingOption`确定。

@param 源代码为字符序列,以解码符号。 @param 目的地为 @param 目的, 数组将字节写入 。 `destination` 目的 。 `destination` 数组的起始索引将默认写字节为 0。 @param 开始 。 包括 子字符串的起始( 包括) , 默认写字节为 0 。 @param endIndex 结尾( 排他) 子字符串的结尾( 排他) , 默认写解码长度为 `source` 。

@throws 指数外溢值,但 `startIndex` 或 `endIndex` 的值在`source` 指数范围之外。 @throws 非法参数外溢值在`startIndex > endIndex` @throws 指数外溢值在 `destination` 指定`destinationOffset` 开始的`destination` 阵列中不匹配,或该指数在 `destination` 阵列指数范围之外。 @throws 非法参数除外,当解码符号没有按照 `PaddingOption` 设定的 `Base64` 例的要求被加注时,或者当挂接后有额外的符号时。

@return 以 `destination` 矩阵中写入的字节数 。

@sample 样本.io.encoding.Base64Samples.decode IntoByte 阵列样本

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    val outputBuffer = ByteArray(1024)
    // {data:\"ZW5jb2RlZA==\"}
    val data = byteArrayOf(
        123, 100, 97, 116, 97,
        58, 34, 90, 87, 53, 106,
        98, 50, 82, 108, 90, 65,
        61, 61, 34, 125
    )
    val from = data.indexOf('"'.code.toByte()) + 1
    val until = data.lastIndexOf('"'.code.toByte())

    // decode subrange of input data into buffer and remember how many bytes were written
    val bytesWritten = Base64.decodeIntoByteArray(data, destination = outputBuffer, startIndex = from, endIndex = until)
    println(outputBuffer.decodeToString(endIndex = bytesWritten))
}
```

```text title="输出"
encoded
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L365)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    val outputBuffer = ByteArray(1024)
    val inputChunks = listOf("Q2h1bmsx", "U2Vjb25kQ2h1bms=", "Y2h1bmsjMw==")

    var bufferPosition = 0
    val chunkIterator = inputChunks.iterator()
    while (bufferPosition < outputBuffer.size && chunkIterator.hasNext()) {
        val chunk = chunkIterator.next()
        // fill buffer with data decoded from base64-encoded chunks
        // and increment current position by the number of decoded bytes
        bufferPosition += Base64.decodeIntoByteArray(
            chunk,
            destination = outputBuffer,
            destinationOffset = bufferPosition
        )
    }
    // consume outputBuffer
    println(outputBuffer.decodeToString(endIndex = bufferPosition))
}
```

```text title="输出"
Chunk1SecondChunkchunk#3
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L344)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
