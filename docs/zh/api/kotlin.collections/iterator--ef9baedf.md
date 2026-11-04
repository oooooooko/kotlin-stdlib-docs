# iterator

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回给定的迭代器本身。 这样可以使用 `for` 环循环. @sample 样本中的迭代器实例。 收藏. Extractors. terator.

??? note "查看英文原文"

    Returns the given iterator itself. This allows to use an instance of iterator in a `for` loop.
    @sample samples.collections.Iterators.iterator

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun <T> Iterator<T>.iterator(): Iterator<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Iterators.kt#L12)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun <K, V> Map<out K, V>.iterator(): Iterator<Map.Entry<K, V>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L537)

`Map` 条目的返回值为`Iterator`。

@sample 样本采集 用于整个项目的地图

### 3. Common

```kotlin
@kotlin.jvm.JvmName("mutableIterator")
@kotlin.internal.InlineOnly
public inline operator fun <K, V> MutableMap<K, V>.iterator(): MutableIterator<MutableMap.MutableEntry<K, V>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L545)

a `MutableMap` 的变音条目返回`MutableIterator`。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    val mutableList = mutableListOf(1, 2, 3)
    val mutableIterator = mutableList.iterator()

    // iterator() extension is called here
    for (e in mutableIterator) {
        if (e % 2 == 0) {
            // we can remove items from the iterator without getting ConcurrentModificationException
            // because it's the same iterator that is iterated with for loop
            mutableIterator.remove()
        }

        println("The element is $e")
    }
}
```

```text title="输出"
The element is 1
The element is 2
The element is 3
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/iterators.kt#L38)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
