# remove

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

从此地图中删除指定的密钥及其相应的值。

@return 与密钥相关的上一个值,如果地图上没有密钥,则为 `null` 。

能够克服 `remove` 的防排限制,这需要通过 `K` 型钥匙。

??? note "查看英文原文"

    Removes the specified key and its corresponding value from this map.
    
    @return the previous value associated with the key, or `null` if the key was not present in the map.
    
    Allows to overcome type-safety restriction of `remove` that requires to pass a key of type `K`.

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun <@kotlin.internal.OnlyInputTypes K, V> MutableMap<out K, V>.remove(key: K): V?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L289)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun <@kotlin.internal.OnlyInputTypes T> MutableCollection<out T>.remove(element: T): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L11)

从此收藏中删除指定元素的单个实例, 如果有的话 。

能够克服 `remove` 型安全限制,要求通过`E`型的元素。

如果成功删除元素, @return `true` ;如果收藏中没有`false`,则`false`。

### 3. Common

```kotlin
@Deprecated("Use removeAt(index) instead.", ReplaceWith("removeAt(index)"), level = DeprecationLevel.ERROR)
@kotlin.internal.InlineOnly
public inline fun <T> MutableList<T>.remove(index: Int): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MutableCollections.kt#L248)

从此列表中删除指定 `index` 上的元素。 在 Kotlin 中, 需要使用 `MutableList.removeAt` 函数代替 。

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
    val source = linkedMapOf("a" to 1, "b" to 2)
    val result = source.`remove`("a")
    println(result)
}
```

```text title="输出"
1
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
