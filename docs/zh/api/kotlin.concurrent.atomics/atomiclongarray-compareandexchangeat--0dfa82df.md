# AtomicLongArray.compareAndExchangeAt

`kotlin.concurrent.atomics` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将`new value``newValue` 存放在给定`index`的`AtomicLongArray` 成`AtomicLongArray`元素的原子
如果当前值等于 `expected value`Z`expectedValue`, 且返回元素的旧值, 则该值在任何情形下都等于 `expected value`Z`expectedValue`。

数值比较按数值进行。

@throws 索引外观,但 `index` 超出此数组界限的除外。

@sample 样本. 共流. 原子学. 原子学LongArray. 比较和ExchangeAt

??? note "查看英文原文"

    Atomically stores the `new value``newValue` into the element of this `AtomicLongArray` at the given `index`
    if the current value equals the `expected value``expectedValue` and returns the old value of the element in any case.
    
    Comparison of values is done by value.
    
    @throws IndexOutOfBoundsException if the `index` is out of bounds of this array.
    
    @sample samples.concurrent.atomics.AtomicLongArray.compareAndExchangeAt

## 声明与重载

### 1. Common

```kotlin
public fun compareAndExchangeAt(index: Int, expectedValue: Long, newValue: Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L367)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.atomics.AtomicArray
import kotlin.test.assertFailsWith



fun main() {
    val a = AtomicLongArray(longArrayOf(1, 2, 3))
    // Current value of a[1] is 2, it is equal to the expected value 2 ->
    // compareAndExchangeAt succeeds, stores the new value 7 to a[1] and returns the old value 2.
    println(a.compareAndExchangeAt(index = 1, expectedValue = 2, newValue = 7))
    println(a.loadAt(1))
    println(a.toString())

    // Current value of a[2] is 3, it is not equal to the expected value 4 ->
    // compareAndExchangeAt fails, does not store the new value to a[2] and returns the current value 3.
    println(a.compareAndExchangeAt(index = 2, expectedValue = 4, newValue = 25))
    println(a.loadAt(2))
    println(a.toString())
}
```

```text title="输出"
2
7
[1, 7, 3]
3
3
[1, 7, 3]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomicArrays.kt#L237)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
