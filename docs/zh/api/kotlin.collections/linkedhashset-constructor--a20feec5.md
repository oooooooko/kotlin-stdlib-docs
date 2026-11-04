# LinkedHashSet.constructor

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

创建新的 `LinkedHashSet` 空。

??? note "查看英文原文"

    Creates a new empty `LinkedHashSet`.

## 声明与重载

### 1. Common

```kotlin
public constructor()
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/LinkedHashSet.kt#L87)

### 2. Common

```kotlin
public constructor(initialCapacity: Int)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/LinkedHashSet.kt#L92)

创建具有指定初始容量的新的`LinkedHashSet`空位。

能力是集能存储于当前内部数据结构中的最大元素数量。 当集被某个默认负载系数完全填充时,其容量会扩大,这通常会导致内部数据结构的重建。

@param 初始能力 : 创建集的初始能力 。
请注意,这一论点只是执行的提示,可以忽略。

@throws 非法设备,如果`initialCapacity`为负数,则不在此列。

### 3. Common

```kotlin
public constructor(initialCapacity: Int, loadFactor: Float)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/LinkedHashSet.kt#L106)

创建新的`LinkedHashSet`空,并带有指定的初始容量和负载系数。

能力是该数据集能够在目前的内部数据结构中存储的最多要素。负载系数是衡量该数据集在能力扩大之前相对于其能力而言能够达到多少完整,这通常会导致内部数据结构的重建。

@param 初始能力 创建集的初始能力 。 注意该参数只是执行的提示, 可以忽略它 。 @param 负载因素 设定集的负载系数 。 注意该参数只是执行的提示, 可以忽略它 。

@throws 非法设备,如果`initialCapacity`为负或`loadFactor`为非正则,则不在此列。

### 4. Common

```kotlin
public constructor(elements: Collection<E>)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/LinkedHashSet.kt#L122)

创建一个包含指定收藏元素的`LinkedHashSet`新收藏。

创建集中元素的迭代顺序与指定收藏中相同。

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
    val value = linkedSetOf(1, 2, 3)
    println(value)
}
```

```text title="输出"
[1, 2, 3]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
