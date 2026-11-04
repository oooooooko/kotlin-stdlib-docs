# sequenceOf

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

创建返回指定值的序列。

@sample 样本、采集资料、序列、建筑、价值序列

??? note "查看英文原文"

    Creates a sequence that returns the specified values.
    
    @sample samples.collections.Sequences.Building.sequenceOfValues

## 声明与重载

### 1. Common

```kotlin
public fun <T> sequenceOf(vararg elements: T): Sequence<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L33)

### 2. Common

```kotlin
@SinceKotlin("2.2")
public fun <T> sequenceOf(element: T): Sequence<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L40)

创建包含一个单元素的`Sequence`。

@param元素, 元素为在结果序列中包含的单元素。 @return 序列仅包含指定的 `element` . @sample 样本。 收藏。 序列。 建筑. 序列squesteuceof SingleValue

### 3. Common

```kotlin
@SinceKotlin("2.2")
@InlineOnly
public inline fun <T> sequenceOf(): Sequence<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sequences.kt#L62)

创建 `Sequence` 空的 。

@return 空序列。 @sample 样本。 采集。 序列。 建筑。 序列

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
import kotlin.sequences.*

fun main() {
    val result = `sequenceOf`(1)
    println(result.toList())
}
```

```text title="输出"
[1]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
