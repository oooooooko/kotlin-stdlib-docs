# AbstractCollection.toArray

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回`Array<Any?>`型新阵列, 并包含此收藏的元素 。

??? note "查看英文原文"

    Returns new array of type `Array<Any?>` with the elements of this collection.

## 声明与重载

### 1. Common

```kotlin
@JsName("toArray")
    protected open fun toArray(): Array<Any?>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/AbstractCollection.kt#L30)

### 2. Common

```kotlin
protected open fun <T> toArray(array: Array<T>): Array<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/AbstractCollection.kt#L36)

填充所提供的 `array` 或创建相同类型的新阵列,并填充此收藏的元素 。

如果此收藏不适应提供的 `array` 中, 则会创建与此收藏相同的数组类型和大小的新数组, 并用此收藏元素填充。 否则, 指定的 `array` 将从索引 0 中填充。 收集元素后面的元素值将未指明 。

@return 包含此收藏全部元素的阵列 。

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
    val source = object : AbstractCollection<Int>() { override val size = 3; override fun iterator() = listOf(1, 2, 3).iterator() ; fun demonstrate() = `toArray`() }
    val result = source.demonstrate()
    println(result.contentToString())
}
```

```text title="输出"
[1, 2, 3]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
