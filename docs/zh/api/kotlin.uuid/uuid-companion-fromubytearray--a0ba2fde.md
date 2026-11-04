# Uuid.Companion.fromUByteArray

`kotlin.uuid` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

从包含 128 位元的数组中创建一个 uid , 并将其分成 16 个未签名的字节 。

`ubyteArray` 中的每一未签名字节顺序代表下8位字节,从第一个字节中最重要的8位字节开始,到最后一个字节中最小8位字节。

@param ubyteArray A 16字节阵列,包含uuid位数。 @throws 非法参数例外,如果`ubyteArray`的大小不完全16 @return,则根据指定的位数,一个新的uid。

@see Uuid.toUbutyte ARray @sample 样本。

??? note "查看英文原文"

    Creates a uuid from an array containing 128 bits split into 16 unsigned bytes.
    
    Each unsigned byte in the `ubyteArray` sequentially represents
    the next 8 bits of the uuid, starting from the most significant 8 bits
    in the first byte to the least significant 8 bits in the last byte.
    
    @param ubyteArray A 16-byte array containing the uuid bits.
    @throws IllegalArgumentException If the size of the `ubyteArray` is not exactly 16.
    @return A new uuid based on the specified bits.
    
    @see Uuid.toUByteArray
    @sample samples.uuid.Uuids.fromUByteArray

## 声明与重载

### 1. Common

```kotlin
@ExperimentalUnsignedTypes
        public fun fromUByteArray(ubyteArray: UByteArray): Uuid
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L358)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val ubyteArray = ubyteArrayOf(
        0x55u, 0x0Eu, 0x84u, 0x00u, 0xE2u, 0x9Bu, 0x41u, 0xD4u,
        0xA7u, 0x16u, 0x44u, 0x66u, 0x55u, 0x44u, 0x00u, 0x00u
    )
    val uuid = Uuid.fromUByteArray(ubyteArray)
    println(uuid)
}
```

```text title="输出"
550e8400-e29b-41d4-a716-446655440000
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L156)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
