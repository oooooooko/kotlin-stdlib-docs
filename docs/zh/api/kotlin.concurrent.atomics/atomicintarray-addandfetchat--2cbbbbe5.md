# AtomicIntArray.addAndFetchAt

`kotlin.concurrent.atomics` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

原子在给定`index`时将给定的`delta`加到`AtomicIntArray`的元素中,并返回元素的新值。

@throws 索引外观,但 `index` 超出此数组界限的除外。

@sample 样本. 共流. 原子学. 原子电图阵列. 添加和FetchAT

??? note "查看英文原文"

    Atomically adds the given `delta` to the element of this `AtomicIntArray` at the given `index` and returns the new value of the element.
    
    @throws IndexOutOfBoundsException if the `index` is out of bounds of this array.
    
    @sample samples.concurrent.atomics.AtomicIntArray.addAndFetchAt

## 声明与重载

### 1. Common

```kotlin
public fun addAndFetchAt(index: Int, delta: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L119)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.atomics.AtomicArray
import kotlin.test.assertFailsWith



fun main() {
    val a = AtomicIntArray(intArrayOf(1, 2, 3))
    // Returns the new value after the addition.
    println(a.addAndFetchAt(1, 10))
    println(a.loadAt(1))
    println(a.toString())
}
```

```text title="输出"
12
12
[1, 12, 3]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomicArrays.kt#L100)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
