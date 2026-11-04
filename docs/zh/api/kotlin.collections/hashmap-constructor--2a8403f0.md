# HashMap.constructor

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

创建新的 `HashMap` 空。

??? note "查看英文原文"

    Creates a new empty `HashMap`.

## 声明与重载

### 1. Common

```kotlin
public constructor()
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/HashMap.kt#L83)

### 2. Common

```kotlin
public constructor(initialCapacity: Int)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/HashMap.kt#L88)

创建具有指定初始容量的新的`HashMap`空位。

容量是地图能够存储在目前内部数据结构中的条目的最大数量。 当地图满载时, 能力会扩大, 通常会重建内部数据结构 。

@param 初始能力 : 所创建的地图初始能力 。
请注意,这一论点只是执行的提示,可以忽略。

@throws 非法设备,如果`initialCapacity`为负数,则不在此列。

### 3. Common

```kotlin
public constructor(initialCapacity: Int, loadFactor: Float)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/HashMap.kt#L102)

创建新的`HashMap`空,并带有指定的初始容量和负载系数。

容量是地图能够储存在目前内部数据结构中的条目的最大数量。负载系数是测量地图在能力扩大之前相对于其能力允许达到的完整程度,这通常导致内部数据结构的重建。

@param 初始能力 创建的地图初始能力 。 注意该参数只是执行的提示, 可以忽略它 。 @param 负载因素 显示创建的地图的负载系数 。 注意该参数只是执行的提示, 可以忽略它 。

@throws 非法设备,如果`initialCapacity`为负或`loadFactor`为非正则,则不在此列。

### 4. Common

```kotlin
public constructor(original: Map<out K, V>)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/HashMap.kt#L118)

创建一个新的`HashMap`, 填充指定的 `original` 地图的内容。

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
    val value = hashMapOf("a" to 1)
    println(value)
}
```

```text title="输出"
{a=1}
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
