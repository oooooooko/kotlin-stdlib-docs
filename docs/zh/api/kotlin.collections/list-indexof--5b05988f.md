# List.indexOf

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回列表中指定元素首次出现的索引,如果列表中没有指定元素,则返回 `-1` 。

对于含有超过`Int.MAX_VALUE`元素的清单,此函数的结果未说明。

@sample 样本、采集的样本、采集的样本、清单、索引

??? note "查看英文原文"

    Returns the index of the first occurrence of the specified element in the list, or `-1` if the specified
    element is not contained in the list.
    
    For lists containing more than `Int.MAX_VALUE` elements, a result of this function is unspecified.
    
    @sample samples.collections.Collections.Lists.indexOf

## 声明与重载

### 1. Common

```kotlin
public fun indexOf(element: @UnsafeVariance E): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L240)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = listOf('a', 'b', 'c', 'a')
    println(list.indexOf('a'))
    println(list.indexOf('b'))
    println(list.indexOf('e'))
}
```

```text title="输出"
0
1
-1
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L445)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
