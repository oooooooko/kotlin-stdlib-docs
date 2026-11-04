# AtomicLongArray.exchangeAt

`kotlin.concurrent.atomics` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将`new value``newValue` 存放在给定`index`的`AtomicLongArray` 成`AtomicLongArray`元素的原子
返回元素的旧值。

@throws 索引外观,但 `index` 超出此数组界限的除外。

@sample 样本. 共流. 原子学. 原子学. 原子学. 长长阵列. 交换

??? note "查看英文原文"

    Atomically stores the `new value``newValue` into the element of this `AtomicLongArray` at the given `index`
    and returns the old value of the element.
    
    @throws IndexOutOfBoundsException if the `index` is out of bounds of this array.
    
    @sample samples.concurrent.atomics.AtomicLongArray.exchangeAt

## 声明与重载

### 1. Common

```kotlin
public fun exchangeAt(index: Int, newValue: Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L341)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.atomics.AtomicArray
import kotlin.test.assertFailsWith



fun main() {
    val a = AtomicLongArray(longArrayOf(1, 2, 3))
    println(a.exchangeAt(1, 7))
    println(a.loadAt(1))
    println(a.toString())
}
```

```text title="输出"
2
7
[1, 7, 3]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomicArrays.kt#L215)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
