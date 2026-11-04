# Uuid.Companion.fromULongs

`kotlin.uuid` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

从指定的 128 位元中创建一个用户名, 将其分为两个 64 位 ULong 。

此函数解释以大端字节顺序提供的`ULong`值。

@param 最有价值 最显著的64位数 最显著的 @param 最小的64位数 最小的64位数 最显著的64位数 @return 一个新的Uid 以指定的位数为基础 。

@see Uuid.toUongs @sample 样本.uuid.Uuids.来自ULongs

??? note "查看英文原文"

    Creates a uuid from specified 128 bits split into two 64-bit ULongs.
    
    This function interprets the provided `ULong` values in big-endian byte order.
    
    @param mostSignificantBits The most significant 64 bits of the uuid.
    @param leastSignificantBits The least significant 64 bits of the uuid.
    @return A new uuid based on the specified bits.
    
    @see Uuid.toULongs
    @sample samples.uuid.Uuids.fromULongs

## 声明与重载

### 1. Common

```kotlin
public fun fromULongs(mostSignificantBits: ULong, leastSignificantBits: ULong): Uuid
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L321)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid = Uuid.fromULongs(0x550E8400E29B41D4uL, 0xA716446655440000uL)
    println(uuid)
}
```

```text title="输出"
550e8400-e29b-41d4-a716-446655440000
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L140)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
