# Uuid.Companion.fromByteArray

`kotlin.uuid` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

从包含 128 位元的字节数组中创建 uid 。

`byteArray` 中的每一字节顺序代表下8个字节,从第一个字节中最重要的8个字节开始,到最后一个字节中最小的8个字节。

@param 字节阵列A 16字节阵列,包含uuid位数。 @throws 非法参数例外 如果 `byteArray` 的大小不完全16 @return,则根据指定的位数新建一个uid。

@see 生物资源采集的800 000001 Uuid.toByteAray @sample 样本。

??? note "查看英文原文"

    Creates a uuid from a byte array containing 128 bits split into 16 bytes.
    
    Each byte in the `byteArray` sequentially represents
    the next 8 bits of the uuid, starting from the most significant 8 bits
    in the first byte to the least significant 8 bits in the last byte.
    
    @param byteArray A 16-byte array containing the uuid bits.
    @throws IllegalArgumentException If the size of the `byteArray` is not exactly 16.
    @return A new uuid based on the specified bits.
    
    @see Uuid.toByteArray
    @sample samples.uuid.Uuids.fromByteArray

## 声明与重载

### 1. Common

```kotlin
public fun fromByteArray(byteArray: ByteArray): Uuid
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L336)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val byteArray = byteArrayOf(
        0x55, 0x0e, 0x84.toByte(), 0x00, 0xe2.toByte(), 0x9b.toByte(), 0x41, 0xd4.toByte(),
        0xa7.toByte(), 0x16, 0x44, 0x66, 0x55, 0x44, 0x00, 0x00
    )
    val uuid = Uuid.fromByteArray(byteArray)
    println(uuid)
}
```

```text title="输出"
550e8400-e29b-41d4-a716-446655440000
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L146)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
