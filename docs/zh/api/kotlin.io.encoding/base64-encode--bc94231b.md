# Base64.encode

`kotlin.io.encoding` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

指定 `source` 矩阵或其子序列的编码字节。返回带有由此产生的符号的字符串。

编码结果是否加盖为 `'='` 取决于 `Base64` 实例的 `PaddingOption` 设置 。

使用 `encodeToByteArray` 来获取 `ByteArray` 表格的输出 。

@param 源于 @param 开头 INdex 的子序列开始( 包括) 编码 , 默认为 0。 @param 尾端 Index 的子序列结束( 排他) , 默认为 `source` 矩阵的大小 。

@throws 指数外溢值,但 `startIndex` 或 `endIndex` 在`source`阵列指数范围之外时除外。 @throws 非法设备除外,当`startIndex > endIndex`时。

@return 字符串, 带有由此产生的符号 。

@sample 样本.io.encoding.Base64Samples.encode to StringSample 样本 样本编号: 样本编号: 样本编号: 样本编号: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本: 样本:

??? note "查看英文原文"

    Encodes bytes from the specified `source` array or its subrange.
    Returns a string with the resulting symbols.
    
    Whether the encoding result is padded with `'='` depends on the `PaddingOption` set for this `Base64` instance.
    
    Use `encodeToByteArray` to get the output in `ByteArray` form.
    
    @param source the array to encode bytes from.
    @param startIndex the beginning (inclusive) of the subrange to encode, 0 by default.
    @param endIndex the end (exclusive) of the subrange to encode, size of the `source` array by default.
    
    @throws IndexOutOfBoundsException when `startIndex` or `endIndex` is out of range of `source` array indices.
    @throws IllegalArgumentException when `startIndex > endIndex`.
    
    @return a string with the resulting symbols.
    
    @sample samples.io.encoding.Base64Samples.encodeToStringSample

## 声明与重载

### 1. Common

```kotlin
public fun encode(source: ByteArray, startIndex: Int = 0, endIndex: Int = source.size): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/io/encoding/Base64.kt#L211)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.io.encoding.*



fun main() {
    val data = byteArrayOf(-1, 0, -2, 0, -3)

    val encoded = Base64.encode(data)
    println(encoded)

    val encodedFromSubRange = Base64.encode(data, startIndex = 1, endIndex = 3)
    println(encodedFromSubRange)
}
```

```text title="输出"
/wD+AP0=
AP4=
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/io/encoding/base64.kt#L287)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
