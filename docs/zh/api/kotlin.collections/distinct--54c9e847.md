# distinct

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个仅包含从给定数组中不同元素的列表。

在给定数组的相等元素中,结果列表中将只显示第一个元素。结果列表中元素的顺序与源数组中的元素相同。

@sample 样本 采集 采集 变异 分异和分异

??? note "查看英文原文"

    Returns a list containing only distinct elements from the given array.
    
    Among equal elements of the given array, only the first one will be present in the resulting list.
    The elements in the resulting list are in the same order as they were in the source array.
    
    @sample samples.collections.Collections.Transformations.distinctAndDistinctBy

## 声明与重载

### 1. Common

```kotlin
public fun <T> Array<out T>.distinct(): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13362)

### 2. Common

```kotlin
public fun ByteArray.distinct(): List<Byte>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13374)

返回一个仅包含从给定数组中不同元素的列表。

结果列表中的元素与源数组中的元素顺序相同。

@sample 样本 采集 采集 变异 分异和分异

### 3. Common

```kotlin
public fun ShortArray.distinct(): List<Short>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13385)

返回一个仅包含从给定数组中不同元素的列表。

结果列表中的元素与源数组中的元素顺序相同。

@sample 样本 采集 采集 变异 分异和分异

### 4. Common

```kotlin
public fun IntArray.distinct(): List<Int>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13396)

返回一个仅包含从给定数组中不同元素的列表。

结果列表中的元素与源数组中的元素顺序相同。

@sample 样本 采集 采集 变异 分异和分异

### 5. Common

```kotlin
public fun LongArray.distinct(): List<Long>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13407)

返回一个仅包含从给定数组中不同元素的列表。

结果列表中的元素与源数组中的元素顺序相同。

@sample 样本 采集 采集 变异 分异和分异

### 6. Common

```kotlin
public fun FloatArray.distinct(): List<Float>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13418)

返回一个仅包含从给定数组中不同元素的列表。

结果列表中的元素与源数组中的元素顺序相同。

@sample 样本 采集 采集 变异 分异和分异

### 7. Common

```kotlin
public fun DoubleArray.distinct(): List<Double>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13429)

返回一个仅包含从给定数组中不同元素的列表。

结果列表中的元素与源数组中的元素顺序相同。

@sample 样本 采集 采集 变异 分异和分异

### 8. Common

```kotlin
public fun BooleanArray.distinct(): List<Boolean>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13440)

返回一个仅包含从给定数组中不同元素的列表。

结果列表中的元素与源数组中的元素顺序相同。

@sample 样本 采集 采集 变异 分异和分异

### 9. Common

```kotlin
public fun CharArray.distinct(): List<Char>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13451)

返回一个仅包含从给定数组中不同元素的列表。

结果列表中的元素与源数组中的元素顺序相同。

@sample 样本 采集 采集 变异 分异和分异

### 10. Common

```kotlin
public fun <T> Iterable<T>.distinct(): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1833)

返回一个仅包含与给定收藏不同元素的列表 。

在所给收藏的相同元素中,只有第一个元素会出现在所产生的列表中,而该列表中的各个元素的顺序与源集中的元素的顺序相同。

@sample 样本 采集 采集 变异 分异和分异

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = listOf('a', 'A', 'b', 'B', 'A', 'a')
    println(list.distinct())
    println(list.distinctBy { it.uppercaseChar() })
}
```

```text title="输出"
[a, A, b, B]
[a, b]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L819)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
