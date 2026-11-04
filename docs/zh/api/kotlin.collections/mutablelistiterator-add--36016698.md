# MutableListIterator.add

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

在元素返回 `next` 之前,在元素返回 `next` 之前,在元素返回`previous`之前,在元素返回`previous`之后,在元素返回之前,立即将指定的元素`element`添加到基本收藏中。 (如果收藏不含元素,新元素成为收藏中的唯一元素。 )在隐含光标之前插入新元素:随后拨打 `next` 时不受影响,随后拨打`previous`时返回新元素。 (此调用增加一个数值\,该数值将通过拨打返回 `nextIndex` 或 `previousIndex` 时返回。 )

??? note "查看英文原文"

    Adds the specified element `element` into the underlying collection immediately before the element that would be
    returned by `next`, if any, and after the element that would be returned by `previous`, if any.
    (If the collection contains no elements, the new element becomes the sole element in the collection.)
    The new element is inserted before the implicit cursor: a subsequent call to `next` would be unaffected,
    and a subsequent call to `previous` would return the new element. (This call increases by one the value \
    that would be returned by a call to `nextIndex` or `previousIndex`.)

## 声明与重载

### 1. Common

```kotlin
public fun add(element: T): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Iterator.kt#L104)

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
    val source = mutableListOf(1, 2, 3).listIterator()
    val result = source.`add`(1)
    println(result)
}
```

```text title="输出"
kotlin.Unit
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
