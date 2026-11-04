# Uuid.toByteArray

`kotlin.uuid` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回此 uuid 的字节数组表示法。

返回的数组包含16字节。数组中每个字节依次代表 uuid 的下八个字节,从第一个字节中最重要的八个字节开始,到最后一个字节中最小的八个字节。

@see Uuid. from ByteAray @sample 样本.uuuid.uuuids.toByteAray.

??? note "查看英文原文"

    Returns a byte array representation of this uuid.
    
    The returned array contains 16 bytes. Each byte in the array sequentially represents
    the next 8 bits of the uuid, starting from the most significant 8 bits
    in the first byte to the least significant 8 bits in the last byte.
    
    @see Uuid.fromByteArray
    @sample samples.uuid.Uuids.toByteArray

## 声明与重载

### 1. Common

```kotlin
public fun toByteArray(): ByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L203)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid = Uuid.fromULongs(0x550E8400E29B41D4uL, 0xA716446655440000uL)
    println(uuid.toByteArray().joinToString { it.toHexString() })
}
```

```text title="输出"
55, 0e, 84, 00, e2, 9b, 41, d4, a7, 16, 44, 66, 55, 44, 00, 00
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L106)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
