# Uuid.compareTo

`kotlin.uuid` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

比较此词汇与 `other` 词汇顺序的词汇 。

如果这个 uuid 字典上等于指定的其他 uuid , 则返回零, 如果比另一个低, 返回负数, 如果比另一个大, 返回正数 。

此函数按位对两个 128 位 uud 位进行顺序比较, 从最显著的位数开始到最小的位数。 `this` uud 将小于 `other`, 如果在两个 uud 的对应位数不同的第一个位置, `this` 位数为零, 而 `other` 位数为一。 相反, 8,00000005 则被视为大于 `other` , 如果在第一个不同位置, `this` 位数为一, `other` 位数为零。 如果没有找到不同的位数, 则两个 uuud 被视为相等 。

比较结果为`this`和`other`uid,相当于:```kotlin
this.toString().compareTo(other.toString())
```

@sample 样本。

??? note "查看英文原文"

    Compares this uuid with the `other` uuid for lexical order.
    
    Returns zero if this uuid is lexically equal to the specified other uuid, a negative number
    if it's less than the other, or a positive number if it's greater than the other.
    
    This function compares the two 128-bit uuids bit by bit sequentially,
    starting from the most significant bit to the least significant.
    `this` uuid is considered less than `other` if, at the first position where corresponding bits
    of the two uuids differ, the bit in `this` is zero and the bit in `other` is one.
    Conversely, `this` is considered greater than `other` if, at the first differing position,
    the bit in `this` is one and the bit in `other` is zero.
    If no differing bits are found, the two uuids are considered equal.
    
    The result of the comparison of `this` and `other` uuids is equivalent to:
    ```kotlin
    this.toString().compareTo(other.toString())
    ```
    
    @sample samples.uuid.Uuids.compareTo

## 声明与重载

### 1. Common

```kotlin
override fun compareTo(other: Uuid): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L251)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid1 = Uuid.parse("49d6d991-c780-4eb5-8585-5169c25af912")
    val uuid2 = Uuid.parse("c0bac692-7208-4448-a8fe-3e3eb128db2a")
    val uuid3 = Uuid.parse("49d6d991-aa92-4da0-917e-527c69621cb7")

    println(uuid1 < uuid2)
    println(uuid1 > uuid3)

    val sortedUuids = listOf(uuid1, uuid2, uuid3).sorted()

    println(sortedUuids[0])
    println(sortedUuids[1])
    println(sortedUuids[2])
}
```

```text title="输出"
true
true
49d6d991-aa92-4da0-917e-527c69621cb7
49d6d991-c780-4eb5-8585-5169c25af912
c0bac692-7208-4448-a8fe-3e3eb128db2a
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L290)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
