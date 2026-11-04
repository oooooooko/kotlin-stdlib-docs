# AtomicIntArray.compareAndSetAt

`kotlin.concurrent.atomics` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将`new value``newValue` 存放在给定`index`的`AtomicIntArray` 成`AtomicIntArray`元素的原子
如果当前值等于 `expected value`Z`expectedValue`,则该值等于 `expected value``expectedValue`。
如果操作成功且只有在元素的当前值不等于预期值时才返回真实值, 而只有当此操作成功且错误时才会返回真实值 。

这个操作有所谓的强语义, 意思是如果并且只有在当前和预期值不相等时, 它才会返回虚假的 。

数值比较按数值进行。

@throws 索引外观,但 `index` 超出此数组界限的除外。

@sample 样本. 共流. 原子学. 亚tomic IntAray. 比较和SetAt

??? note "查看英文原文"

    Atomically stores the `new value``newValue` into the element of this `AtomicIntArray` at the given `index`
    if the current value equals the `expected value``expectedValue`.
    Returns true if the operation was successful and false only if the current value of the element was not equal to the expected value.
    
    This operation has so-called strong semantics,
    meaning that it returns false if and only if current and expected values are not equal.
    
    Comparison of values is done by value.
    
    @throws IndexOutOfBoundsException if the `index` is out of bounds of this array.
    
    @sample samples.concurrent.atomics.AtomicIntArray.compareAndSetAt

## 声明与重载

### 1. Common

```kotlin
public fun compareAndSetAt(index: Int, expectedValue: Int, newValue: Int): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L82)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.atomics.AtomicArray
import kotlin.test.assertFailsWith



fun main() {
    val a = AtomicIntArray(intArrayOf(1, 2, 3))
    // Current value of a[1] is 2, it is equal to the expected value 2 -> compareAndSetAt succeeds.
    println(a.compareAndSetAt(index = 1, expectedValue = 2, newValue = 7))
    println(a.loadAt(1))
    println(a.toString())

    // Current value of a[2] is 3, it is not equal to the expected value 4 -> compareAndSetAt fails.
    println(a.compareAndSetAt(index = 2, expectedValue = 4, newValue = 25))
    println(a.loadAt(2))
    println(a.toString())
}
```

```text title="输出"
true
7
[1, 7, 3]
false
3
[1, 7, 3]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomicArrays.kt#L61)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
