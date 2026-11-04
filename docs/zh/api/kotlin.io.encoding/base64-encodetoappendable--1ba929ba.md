# Base64.encodeToAppendable

`kotlin.io.encoding` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

指定 `source` 矩阵或其子序列的编码字节,并将由此生成的符号附加到可附加的 `destination` 。返回可附加的目标。

编码结果是否加盖为 `'='` 取决于 `Base64` 实例的 `PaddingOption` 设置 。

@param 源于 @param 目标的数组编码字节。 @param 目标的附加符号附加到 @param 符号的附加值是 @param 开始 INdex 开始(包括) 子序列的起始值为 0 默认值为 @param endIndex 子序列的结尾值( 排他性) , 默认值为 `source` 矩阵的大小 。

@throws 指数外溢值,但 `startIndex` 或 `endIndex` 在`source`阵列指数范围之外时除外。 @throws 非法设备除外,当`startIndex > endIndex`时。

目的地可附加的@return。

@sample 样本.io.encoding.Base64Samples.encode 附录

??? note "查看英文原文"

    Encodes bytes from the specified `source` array or its subrange and appends resulting symbols to the `destination` appendable.
    Returns the destination appendable.
    
    Whether the encoding result is padded with `'='` depends on the `PaddingOption` set for this `Base64` instance.
    
    @param source the array to encode bytes from.
    @param destination the appendable to append symbols to.
    @param startIndex the beginning (inclusive) of the subrange to encode, 0 by default.
    @param endIndex the end (exclusive) of the subrange to encode, size of the `source` array by default.
    
    @throws IndexOutOfBoundsException when `startIndex` or `endIndex` is out of range of `source` array indices.
    @throws IllegalArgumentException when `startIndex > endIndex`.
    
    @return the destination appendable.
    
    @sample samples.io.encoding.Base64Samples.encodeToAppendableSample

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
    public fun <A : Appendable> encodeToAppendable(
        source: ByteArray,
        destination: A,
        startIndex: Int = 0,
        endIndex: Int = source.size
    ): A
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L234)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    val data = byteArrayOf(-1, 0, -2, 0, -3)

    val encoded = buildString {
        append("{ \"data\": \"")
        Base64.encodeToAppendable(data, destination = this)
        append("\" }")
    }
    println(encoded)

    val encodedFromSubRange = buildString {
        append("{ \"data\": \"")
        Base64.encodeToAppendable(data, destination = this, startIndex = 1, endIndex = 3)
        append("\" }")
    }
    println(encodedFromSubRange)
}
```

```text title="输出"
{ "data": "/wD+AP0=" }
{ "data": "AP4=" }
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L298)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
