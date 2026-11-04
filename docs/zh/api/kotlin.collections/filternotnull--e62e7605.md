# filterNotNull

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回包含所有不是 `null` 元素的列表 。

@sample 样本、采集的样本、采集的采集、采集的采集、过滤、过滤、过滤、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测、检测

??? note "查看英文原文"

    Returns a list containing all elements that are not `null`.
    
    @sample samples.collections.Collections.Filtering.filterNotNull

## 声明与重载

### 1. Common

```kotlin
public fun <T : Any> Array<out T?>.filterNotNull(): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4348)

### 2. Common

```kotlin
public fun <T : Any> Iterable<T?>.filterNotNull(): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L835)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val numbers: List<Int?> = listOf(1, 2, null, 4)
    val nonNullNumbers = numbers.filterNotNull()

    println(nonNullNumbers)
}
```

```text title="输出"
[1, 2, 4]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1590)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
