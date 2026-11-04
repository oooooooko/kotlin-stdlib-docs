# ArrayList.constructor

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

创建新的 `ArrayList` 空。

??? note "查看英文原文"

    Creates a new empty `ArrayList`.

## 声明与重载

### 1. Common

```kotlin
public constructor()
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/ArrayList.kt#L54)

### 2. Common

```kotlin
public constructor(initialCapacity: Int)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/ArrayList.kt#L59)

创建具有指定初始容量的新的`ArrayList`空位。

能力是列表中能够存储在当前支持存储中的元素的最大数量。 当列表完整且无法添加新元素时, 能力会扩大, 通常会创建更大的支持存储 。

@param 初始能力 创建清单的初始能力 。
请注意,这一论点只是执行的提示,可以忽略。

@throws 非法设备,如果`initialCapacity`为负数,则不在此列。

### 3. Common

```kotlin
public constructor(elements: Collection<E>)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/ArrayList.kt#L73)

创建一个包含指定收藏元素的`ArrayList`新收藏。

创建列表中元素的迭代顺序与指定收藏中元素的迭代顺序相同。

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
    val value = arrayListOf(1, 2, 3)
    println(value)
}
```

```text title="输出"
[1, 2, 3]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
