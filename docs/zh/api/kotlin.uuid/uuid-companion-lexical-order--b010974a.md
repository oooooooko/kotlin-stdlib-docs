# Uuid.Companion.LEXICAL_ORDER

`kotlin.uuid` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

`Comparator`A 词汇上命令UUD。

注:
`Uuid`是`Comparable`类型,`compareTo`功能确立词汇顺序。
当`Uuid`不具有可比性时,就采用了`LEXICAL_ORDER`。
现在,该弹药已经过期,今后将予以释放。
代之以使用“自然命令<Uuid>”()```naturalOrder`, which is equivalent to `LEXICAL_ORDER`.

This comparator compares the given two 128-bit uuids bit by bit sequentially,
starting from the most significant bit to the least significant.
uuid `a` is considered less than `b` if, at the first position where corresponding bits
of the two uuids differ, the bit in `a` is zero and the bit in `b` is one.
Conversely, `a` is considered greater than `b` if, at the first differing position,
the bit in `a` is one and the bit in `b` is zero.
If no differing bits are found, the two uuids are considered equal.

The result of the comparison of uuids `a` and `b` by this comparator is equivalent to:
```kotlin a.to String ().compareto(b.to String ())

??? note "查看英文原文"

    A `Comparator` that lexically orders uuids.
    
    Note:
      `Uuid` is a `Comparable` type, and its `compareTo` function establishes lexical order.
      `LEXICAL_ORDER` was introduced when `Uuid`s were not comparable.
      It is now deprecated and will be removed in a future release.
      Instead, use ``naturalOrder<Uuid>()```naturalOrder`, which is equivalent to `LEXICAL_ORDER`.
    
    This comparator compares the given two 128-bit uuids bit by bit sequentially,
    starting from the most significant bit to the least significant.
    uuid `a` is considered less than `b` if, at the first position where corresponding bits
    of the two uuids differ, the bit in `a` is zero and the bit in `b` is one.
    Conversely, `a` is considered greater than `b` if, at the first differing position,
    the bit in `a` is one and the bit in `b` is zero.
    If no differing bits are found, the two uuids are considered equal.
    
    The result of the comparison of uuids `a` and `b` by this comparator is equivalent to:
    ```kotlin
    a.toString().compareTo(b.toString())
    ```

## 声明与重载

### 1. Common

```kotlin
@ExperimentalUuidApi
        @Deprecated("Use naturalOrder<Uuid>() instead", ReplaceWith("naturalOrder<Uuid>()", imports = ["kotlin.comparisons.naturalOrder"]))
        @DeprecatedSinceKotlin(warningSince = "2.1", errorSince = "2.4")
        public val LEXICAL_ORDER: Comparator<Uuid>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L745)

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

        val maxUuid = Uuid.parse(uuidStringMax)

        // TODO: Once LEXICAL_ORDER is dropped, test Uuid.compareTo directly instead
        @Suppress("DEPRECATION_ERROR")
        for (lexicalOrder in listOf(Uuid.LEXICAL_ORDER, naturalOrder())) {
            for (id in listOf(uuid, Uuid.NIL, maxUuid)) {
                println(lexicalOrder.compare(id, id))
            }

            println(lexicalOrder.compare(Uuid.NIL, uuid) < 0)
            println(lexicalOrder.compare(Uuid.NIL, maxUuid) < 0)

            println(lexicalOrder.compare(uuid, Uuid.NIL) > 0)
            println(lexicalOrder.compare(uuid, maxUuid) < 0)

            println(lexicalOrder.compare(maxUuid, Uuid.NIL) > 0)
            println(lexicalOrder.compare(maxUuid, uuid) > 0)
        }
    
}
```

```text title="输出"
0
0
0
true
true
true
true
true
true
0
0
0
true
true
true
true
true
true
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/uuid/UuidTest.kt#L261)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
