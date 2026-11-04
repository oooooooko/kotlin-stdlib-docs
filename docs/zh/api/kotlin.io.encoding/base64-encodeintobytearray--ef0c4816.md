# Base64.encodeIntoByteArray

`kotlin.io.encoding` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将指定的 `source` 矩阵或其子排列的字节编码成字元,并将由此生成的符号写入 `destination` 矩阵。返回写入的符号数。

编码结果是否加盖为 `'='` 取决于 `Base64` 实例的 `PaddingOption` 设置 。

@param 源于 @param 目的的数组编码字节。 @param 目的的数组将符号写入 。 @param 目的 将 `destination` 数组的起始索引切换成 0, 默认为 0。 @param 开始于 lndex 子序列的起始( 包括) 编码, 默认为 0。 8,00000006 endIndex 结束于 子序列的结尾( 排他) , 默认为 `source` 数组的大小 。

`startIndex`或`endIndex`不在`source`阵列指数范围内时,@throws指数外出外出外出,但有例外。
@throws非法 参数`startIndex > endIndex`.
@throws 指数外观除以下列情况为例外:所产生的符号不适应从指定的 `destinationOffset` 开始的 `destination` 阵列,
当该索引超出`destination` 矩阵指数范围时。

@return 以 `destination` 矩阵中写入的符号数 。

@sample 样本.io.encoding.Base64Samples.encode IntoByte 阵列取样

??? note "查看英文原文"

    Encodes bytes from the specified `source` array or its subrange and writes resulting symbols into the `destination` array.
    Returns the number of symbols written.
    
    Whether the encoding result is padded with `'='` depends on the `PaddingOption` set for this `Base64` instance.
    
    @param source the array to encode bytes from.
    @param destination the array to write symbols into.
    @param destinationOffset the starting index in the `destination` array to write symbols to, 0 by default.
    @param startIndex the beginning (inclusive) of the subrange to encode, 0 by default.
    @param endIndex the end (exclusive) of the subrange to encode, size of the `source` array by default.
    
    @throws IndexOutOfBoundsException when `startIndex` or `endIndex` is out of range of `source` array indices.
    @throws IllegalArgumentException when `startIndex > endIndex`.
    @throws IndexOutOfBoundsException when the resulting symbols don't fit into the `destination` array starting at the specified `destinationOffset`,
    or when that index is out of the `destination` array indices range.
    
    @return the number of symbols written into `destination` array.
    
    @sample samples.io.encoding.Base64Samples.encodeIntoByteArraySample

## 声明与重载

### 1. Common

```kotlin
public fun encodeIntoByteArray(
        source: ByteArray,
        destination: ByteArray,
        destinationOffset: Int = 0,
        startIndex: Int = 0,
        endIndex: Int = source.size
    ): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L180)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    val data = byteArrayOf(-1, 0, -2, 0, -3)
    val outputBuffer = ByteArray(1024)

    var bufferPosition = 0
    // encode data into buffer using Base64 encoding
    // and keep track of the number of bytes written
    bufferPosition += Base64.encodeIntoByteArray(data, outputBuffer)
    println(outputBuffer.decodeToString(endIndex = bufferPosition))

    outputBuffer[bufferPosition++] = '|'.code.toByte()

    // encode data subrange to the buffer, writing it from the given offset
    bufferPosition += Base64.encodeIntoByteArray(
        data,
        destination = outputBuffer,
        destinationOffset = bufferPosition,
        startIndex = 1,
        endIndex = 3
    )
    println(outputBuffer.decodeToString(endIndex = bufferPosition))
}
```

```text title="输出"
/wD+AP0=
/wD+AP0=|AP4=
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L263)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
