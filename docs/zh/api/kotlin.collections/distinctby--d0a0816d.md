# distinctBy

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个列表, 仅包含给定数组中由给定 `selector` 函数返回的不同密钥的元素 。

在具有等键的给定数组元素中,只有第一个元素会出现在结果列表中。结果列表中的元素与源数组中的元素顺序相同。

@sample 样本 采集 采集 变异 分异和分异

??? note "查看英文原文"

    Returns a list containing only elements from the given array
    having distinct keys returned by the given `selector` function.
    
    Among elements of the given array with equal keys, only the first one will be present in the resulting list.
    The elements in the resulting list are in the same order as they were in the source array.
    
    @sample samples.collections.Collections.Transformations.distinctAndDistinctBy

## 声明与重载

### 1. Common

```kotlin
public inline fun <T, K> Array<out T>.distinctBy(selector: (T) -> K): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13462)

### 2. Common

```kotlin
public inline fun <K> ByteArray.distinctBy(selector: (Byte) -> K): List<Byte>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13482)

返回一个列表, 仅包含给定数组中由给定 `selector` 函数返回的不同密钥的元素 。

结果列表中的元素与源数组中的元素顺序相同。

@sample 样本 采集 采集 变异 分异和分异

### 3. Common

```kotlin
public inline fun <K> ShortArray.distinctBy(selector: (Short) -> K): List<Short>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13501)

返回一个列表, 仅包含给定数组中由给定 `selector` 函数返回的不同密钥的元素 。

结果列表中的元素与源数组中的元素顺序相同。

@sample 样本 采集 采集 变异 分异和分异

### 4. Common

```kotlin
public inline fun <K> IntArray.distinctBy(selector: (Int) -> K): List<Int>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13520)

返回一个列表, 仅包含给定数组中由给定 `selector` 函数返回的不同密钥的元素 。

结果列表中的元素与源数组中的元素顺序相同。

@sample 样本 采集 采集 变异 分异和分异

### 5. Common

```kotlin
public inline fun <K> LongArray.distinctBy(selector: (Long) -> K): List<Long>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13539)

返回一个列表, 仅包含给定数组中由给定 `selector` 函数返回的不同密钥的元素 。

结果列表中的元素与源数组中的元素顺序相同。

@sample 样本 采集 采集 变异 分异和分异

### 6. Common

```kotlin
public inline fun <K> FloatArray.distinctBy(selector: (Float) -> K): List<Float>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13558)

返回一个列表, 仅包含给定数组中由给定 `selector` 函数返回的不同密钥的元素 。

结果列表中的元素与源数组中的元素顺序相同。

@sample 样本 采集 采集 变异 分异和分异

### 7. Common

```kotlin
public inline fun <K> DoubleArray.distinctBy(selector: (Double) -> K): List<Double>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13577)

返回一个列表, 仅包含给定数组中由给定 `selector` 函数返回的不同密钥的元素 。

结果列表中的元素与源数组中的元素顺序相同。

@sample 样本 采集 采集 变异 分异和分异

### 8. Common

```kotlin
public inline fun <K> BooleanArray.distinctBy(selector: (Boolean) -> K): List<Boolean>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13596)

返回一个列表, 仅包含给定数组中由给定 `selector` 函数返回的不同密钥的元素 。

结果列表中的元素与源数组中的元素顺序相同。

@sample 样本 采集 采集 变异 分异和分异

### 9. Common

```kotlin
public inline fun <K> CharArray.distinctBy(selector: (Char) -> K): List<Char>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13615)

返回一个列表, 仅包含给定数组中由给定 `selector` 函数返回的不同密钥的元素 。

结果列表中的元素与源数组中的元素顺序相同。

@sample 样本 采集 采集 变异 分异和分异

### 10. Common

```kotlin
public inline fun <T, K> Iterable<T>.distinctBy(selector: (T) -> K): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1845)

返回一个列表, 列表仅包含给定收藏中含有由给定 `selector` 函数返回的有不同密钥元素的元素 。

在具有等键的给定收藏的元素中,只有第一个元素会出现在生成的列表中,而生成列表中的元素与源集中的元素顺序相同。

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
