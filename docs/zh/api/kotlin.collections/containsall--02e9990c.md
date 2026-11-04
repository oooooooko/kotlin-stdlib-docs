# containsAll

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

检查指定收藏库中的所有元素是否都包含在此收藏中 。

能够克服 `containsAll` 的防排限制,要求通过 `Collection<E>` . @sample . 样本的收集。 收集。 收集。 收集。 收集。 收集 包含所有

??? note "查看英文原文"

    Checks if all elements in the specified collection are contained in this collection.
    
    Allows to overcome type-safety restriction of `containsAll` that requires to pass a collection of type `Collection<E>`.
    @sample samples.collections.Collections.Collections.collectionContainsAll

## 声明与重载

### 1. Common

```kotlin
@Suppress("EXTENSION_SHADOWED_BY_MEMBER") // false warning, extension takes precedence in some cases
@kotlin.internal.InlineOnly
public inline fun <@kotlin.internal.OnlyInputTypes T> Collection<T>.containsAll(elements: Collection<T>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L290)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val collection = mutableListOf('a', 'b')
    val test = listOf('a', 'b', 'c')
    println(collection.containsAll(test))

    collection.add('c')
    println(collection.containsAll(test))
}
```

```text title="输出"
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L71)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
