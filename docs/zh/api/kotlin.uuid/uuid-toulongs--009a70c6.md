# Uuid.toULongs

`kotlin.uuid` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

执行指定的代码块,以两个 `ULong` 值的形式提供访问 uid 位元的功能。

3⁄4 ̄ ̧漯B
例如,确定是否该Uud
[IETF variant (variant 2)](https://www.rfc-editor.org/rfc/rfc9562.html#section-4.1):```kotlin
val isIetfVariant = uuid.toULongs { _, leastSignificantBits ->
    (leastSignificantBits shr 62) == 2uL
}
```

`action` 将获得两个 `ULong` 参数: - `mostSignificantBits`: 以大东字节顺序显示的64位这个uuid中最重要的64位。 - `leastSignificantBits`: 以大东字节顺序显示的64位uuid中最小的64位。

例如,对于`550e8400-e29b-41d4-a716-446655440000`,细分如下: - `mostSignificantBits = 0x550e8400e29b41d4uL` .. - `leastSignificantBits = 0xa716446655440000uL` .

@param 动作 A 函数, 需要 2 `ULong` 参数( 最有价值的比特, 最不重要的比特) 。 此函数保证被精确地命名为一次 。 @return 函数是 `action` 的结果 。

来自乌隆的 @see Uuid.

??? note "查看英文原文"

    Executes a specified block of code, providing access to the uuid's bits in the form of two `ULong` values.
    
    This function is intended for use when one needs to perform bitwise operations with the uuid.
    For example, to identify whether this uuid is of the
    [IETF variant (variant 2)](https://www.rfc-editor.org/rfc/rfc9562.html#section-4.1):
    ```kotlin
    val isIetfVariant = uuid.toULongs { _, leastSignificantBits ->
        (leastSignificantBits shr 62) == 2uL
    }
    ```
    
    The `action` will receive two `ULong` arguments:
      - `mostSignificantBits`: The most significant 64 bits of this uuid presented in big-endian byte order.
      - `leastSignificantBits`: The least significant 64 bits of this uuid presented in big-endian byte order.
    
    For example, for the uuid `550e8400-e29b-41d4-a716-446655440000`, the breakdown is the following:
      - `mostSignificantBits = 0x550e8400e29b41d4uL`.
      - `leastSignificantBits = 0xa716446655440000uL`.
    
    @param action A function that takes two `ULong` arguments (mostSignificantBits, leastSignificantBits).
      This function is guaranteed to be called exactly once.
    @return The result of `action`.
    
    @see Uuid.fromULongs

## 声明与重载

### 1. Common

```kotlin
@InlineOnly
    public inline fun <T> toULongs(action: (mostSignificantBits: ULong, leastSignificantBits: ULong) -> T): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L94)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.comparisons.naturalOrder
import kotlin.random.Random
import kotlin.test.*
import kotlin.time.Clock
import kotlin.time.Duration.Companion.milliseconds
import kotlin.time.Instant
import kotlin.uuid.Uuid

private val mostSignificantBits = 0x550e8400e29b41d4uL

private val leastSignificantBits = 0xa716446655440000uL

private val uuidByteArray = byteArrayOf(
        0x55, 0x0e, 0x84.toByte(), 0x00, 0xe2.toByte(), 0x9b.toByte(), 0x41, 0xd4.toByte(),
        0xa7.toByte(), 0x16, 0x44, 0x66, 0x55, 0x44, 0x00, 0x00
    )

private val uuid = Uuid.fromULongs(mostSignificantBits, leastSignificantBits)

private val uuidString = "550e8400-e29b-41d4-a716-446655440000"

private val uuidHexString = "550e8400e29b41d4a716446655440000"

private val uuidStringNil = "00000000-0000-0000-0000-000000000000"

private val uuidHexStringNil = "00000000000000000000000000000000"

private val uuidMax = Uuid.fromLongs(-1, -1)

private val uuidStringMax = "ffffffff-ffff-ffff-ffff-ffffffffffff"

private val uuidHexStringMax = "ffffffffffffffffffffffffffffffff"

private val Uuid.isIetfVariant: Boolean
        get() = toULongs { _, leastSignificantBits -> (leastSignificantBits shr 62) == 2uL }

private val Uuid.version: Int
        get() = toULongs { mostSignificantBits, _ -> ((mostSignificantBits shr 12) and 0xFuL).toInt() }

private fun String.mixedcase(): String = map {
        if (Random.nextBoolean()) it.uppercase() else it.lowercase()
    }.joinToString("")

private class NonMonotonicClock : Clock {
        private var currentTime = Clock.System.now()

        override fun now(): Instant = currentTime

        fun inc(millis: Long = 1L) {
            currentTime = currentTime + millis.milliseconds
        }
    }

fun main() {

        val onceInPlace: Boolean
        val isIetfVariant = uuid.toULongs { mostSignificantBits, leastSignificantBits ->
            println(mostSignificantBits)
            println(leastSignificantBits)
            onceInPlace = true
            (leastSignificantBits shr 62) == 2uL
        }
        println(onceInPlace)
        println(isIetfVariant)

        Uuid.NIL.toULongs { mostSignificantBits, leastSignificantBits ->
            println(mostSignificantBits)
            println(leastSignificantBits)
        }

        Uuid.parse(uuidStringMax).toULongs { mostSignificantBits, leastSignificantBits ->
            println(mostSignificantBits)
            println(leastSignificantBits)
        }
    
}
```

```text title="输出"
6128981282234515924
12039885860129472512
true
true
0
0
18446744073709551615
18446744073709551615
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/uuid/UuidTest.kt#L306)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
