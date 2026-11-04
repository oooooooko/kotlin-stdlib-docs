# filter

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个序列,该序列仅包含与给定的 `predicate` 匹配的元素。

操作是 _ 中间线 _ 和 _ 无国籍 。

@sample 样本,采集的样本, 收集的样本,采集的样本, 采集的样本, 过滤的样本,过滤的样本

??? note "查看英文原文"

    Returns a sequence containing only elements matching the given `predicate`.
    
    The operation is _intermediate_ and _stateless_.
    
    @sample samples.collections.Collections.Filtering.filter

## 声明与重载

### 1. Common

```kotlin
public fun <T> Sequence<T>.filter(predicate: (T) -> Boolean): Sequence<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L428)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val numbers: List<Int> = listOf(1, 2, 3, 4, 5, 6, 7)
    val evenNumbers = numbers.filter { it % 2 == 0 }
    val notMultiplesOf3 = numbers.filterNot { number -> number % 3 == 0 }

    println(evenNumbers)
    println(notMultiplesOf3)
}
```

```text title="输出"
[2, 4, 6]
[1, 2, 4, 5, 7]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1565)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
