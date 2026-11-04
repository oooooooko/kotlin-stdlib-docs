# BooleanIterator

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

一种循环器, 其值序列为 `Boolean` 类型 。

这是一种替代 `Iterator<Boolean>` 的替代方法,它提供了 `next(): T` 方法的专门版本:`nextBoolean(): Boolean`,由汇编者专门处理,以避免将特定平台的框框转换为绩效优化。

举例来说:

```kotlin
class BooleanContainer(private val data: BooleanArray) {

    // BooleanIterator instead of Iterator<Boolean> in the signature
    operator fun iterator(): BooleanIterator = object : BooleanIterator() {
        private var idx = 0

        override fun nextBoolean(): Boolean {
            if (!hasNext()) throw NoSuchElementException()
            return data`idx++`
        }

        override fun hasNext(): Boolean = idx < data.size
    }
}

for (element in BooleanContainer(booleanArrayOf(true, false, true))) {
    ... handle element ...
}
```循环迭代期间不执行拳击转换。 注意迭代器本身仍会被分配 。

??? note "查看英文原文"

    An iterator over a sequence of values of type `Boolean`.
    
    This is a substitute for `Iterator<Boolean>` that provides a specialized version of `next(): T` method: `nextBoolean(): Boolean`
    and has a special handling by the compiler to avoid platform-specific boxing conversions as a performance optimization.
    
    In the following example:
    
    ```kotlin
    class BooleanContainer(private val data: BooleanArray) {
    
        // BooleanIterator instead of Iterator<Boolean> in the signature
        operator fun iterator(): BooleanIterator = object : BooleanIterator() {
            private var idx = 0
    
            override fun nextBoolean(): Boolean {
                if (!hasNext()) throw NoSuchElementException()
                return data`idx++`
            }
    
            override fun hasNext(): Boolean = idx < data.size
        }
    }
    
    for (element in BooleanContainer(booleanArrayOf(true, false, true))) {
        ... handle element ...
    }
    ```
    No boxing conversion is performed during the for-loop iteration.
    Note that the iterator itself will still be allocated.

## 声明与重载

### 1. Common

```kotlin
public abstract class BooleanIterator : Iterator<Boolean>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/PrimitiveIterators.kt#L306)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.collections.*

fun main() {
    val value = booleanArrayOf(true, false, true).iterator()
    println(value.next())
}
```

```text title="输出"
true
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
