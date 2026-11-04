# AbstractMutableList.modCount

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

清单中结构修改的次数。

如果修改改变清单大小,或者以进行中的迭代可能返回不正确的结果的方式改变清单,则修改被视为结构性的。

此值可用于由 `iterator` 和 `listIterator` 返回的迭代器使用
提供在迭代期间检测到同时修改时的故障快速行为。
本案中`ConcurrentModificationException`将被抛出

??? note "查看英文原文"

    The number of times this list is structurally modified.
    
    A modification is considered to be structural if it changes the list size,
    or otherwise changes it in a way that iterations in progress may return incorrect results.
    
    This value can be used by iterators returned by `iterator` and `listIterator`
    to provide fail-fast behavior when a concurrent modification is detected during iteration.
    `ConcurrentModificationException` will be thrown in this case.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.0")
    protected var modCount: Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/AbstractMutableList.kt#L14)

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
    val source = object : AbstractMutableList<Int>() { private val data = mutableListOf(1, 2, 3); override val size get() = data.size; override fun get(index: Int) = data[index]; override fun set(index: Int, element: Int) = data.set(index, element); override fun add(index: Int, element: Int) { data.add(index, element) }; override fun removeAt(index: Int) = data.removeAt(index) ; fun demonstrate() = `modCount` }
    val result = source.demonstrate()
    println(result)
}
```

```text title="输出"
0
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
