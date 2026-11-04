# associateBy

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

a `Map` 返回包含从对每个元素应用的 `keySelector` 函数返回的按键索引的给定数组中得出的元素。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

返回的地图保留原始数组的条目迭代顺序。

@sample 样本收集。 阵列、变形、 联合原始物的阵列

??? note "查看英文原文"

    Returns a `Map` containing the elements from the given array indexed by the key
    returned from `keySelector` function applied to each element.
    
    If any two elements would have the same key returned by `keySelector` the last one gets added to the map.
    
    The returned map preserves the entry iteration order of the original array.
    
    @sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesBy

## 声明与重载

### 1. Common

```kotlin
public inline fun <T, K> Array<out T>.associateBy(keySelector: (T) -> K): Map<K, T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10232)

### 2. Common

```kotlin
public inline fun <K> ByteArray.associateBy(keySelector: (Byte) -> K): Map<K, Byte>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10247)

### 3. Common

```kotlin
public inline fun <K> ShortArray.associateBy(keySelector: (Short) -> K): Map<K, Short>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10262)

### 4. Common

```kotlin
public inline fun <K> IntArray.associateBy(keySelector: (Int) -> K): Map<K, Int>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10277)

### 5. Common

```kotlin
public inline fun <K> LongArray.associateBy(keySelector: (Long) -> K): Map<K, Long>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10292)

### 6. Common

```kotlin
public inline fun <K> FloatArray.associateBy(keySelector: (Float) -> K): Map<K, Float>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10307)

### 7. Common

```kotlin
public inline fun <K> DoubleArray.associateBy(keySelector: (Double) -> K): Map<K, Double>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10322)

### 8. Common

```kotlin
public inline fun <K> BooleanArray.associateBy(keySelector: (Boolean) -> K): Map<K, Boolean>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10337)

### 9. Common

```kotlin
public inline fun <K> CharArray.associateBy(keySelector: (Char) -> K): Map<K, Char>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10352)

### 10. Common

```kotlin
public inline fun <T, K, V> Array<out T>.associateBy(keySelector: (T) -> K, valueTransform: (T) -> V): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10367)

a `Map` 返回包含`valueTransform` 提供的数值,并用 `keySelector` 函数索引适用于给定阵列元素。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

返回的地图保留原始数组的条目迭代顺序。

@sample 样本收集. 阵列. 变形. 联合原始物的阵列 与变异法相连接

### 11. Common

```kotlin
public inline fun <K, V> ByteArray.associateBy(keySelector: (Byte) -> K, valueTransform: (Byte) -> V): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10381)

a `Map` 返回包含`valueTransform` 提供的数值,并用 `keySelector` 函数索引适用于给定阵列元素。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

返回的地图保留原始数组的条目迭代顺序。

@sample 样本收集. 阵列. 变形. 联合原始物的阵列 与变异法相连接

### 12. Common

```kotlin
public inline fun <K, V> ShortArray.associateBy(keySelector: (Short) -> K, valueTransform: (Short) -> V): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10395)

a `Map` 返回包含`valueTransform` 提供的数值,并用 `keySelector` 函数索引适用于给定阵列元素。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

返回的地图保留原始数组的条目迭代顺序。

@sample 样本收集. 阵列. 变形. 联合原始物的阵列 与变异法相连接

### 13. Common

```kotlin
public inline fun <K, V> IntArray.associateBy(keySelector: (Int) -> K, valueTransform: (Int) -> V): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10409)

a `Map` 返回包含`valueTransform` 提供的数值,并用 `keySelector` 函数索引适用于给定阵列元素。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

返回的地图保留原始数组的条目迭代顺序。

@sample 样本收集. 阵列. 变形. 联合原始物的阵列 与变异法相连接

### 14. Common

```kotlin
public inline fun <K, V> LongArray.associateBy(keySelector: (Long) -> K, valueTransform: (Long) -> V): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10423)

a `Map` 返回包含`valueTransform` 提供的数值,并用 `keySelector` 函数索引适用于给定阵列元素。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

返回的地图保留原始数组的条目迭代顺序。

@sample 样本收集. 阵列. 变形. 联合原始物的阵列 与变异法相连接

### 15. Common

```kotlin
public inline fun <K, V> FloatArray.associateBy(keySelector: (Float) -> K, valueTransform: (Float) -> V): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10437)

a `Map` 返回包含`valueTransform` 提供的数值,并用 `keySelector` 函数索引适用于给定阵列元素。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

返回的地图保留原始数组的条目迭代顺序。

@sample 样本收集. 阵列. 变形. 联合原始物的阵列 与变异法相连接

### 16. Common

```kotlin
public inline fun <K, V> DoubleArray.associateBy(keySelector: (Double) -> K, valueTransform: (Double) -> V): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10451)

a `Map` 返回包含`valueTransform` 提供的数值,并用 `keySelector` 函数索引适用于给定阵列元素。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

返回的地图保留原始数组的条目迭代顺序。

@sample 样本收集. 阵列. 变形. 联合原始物的阵列 与变异法相连接

### 17. Common

```kotlin
public inline fun <K, V> BooleanArray.associateBy(keySelector: (Boolean) -> K, valueTransform: (Boolean) -> V): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10465)

a `Map` 返回包含`valueTransform` 提供的数值,并用 `keySelector` 函数索引适用于给定阵列元素。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

返回的地图保留原始数组的条目迭代顺序。

@sample 样本收集. 阵列. 变形. 联合原始物的阵列 与变异法相连接

### 18. Common

```kotlin
public inline fun <K, V> CharArray.associateBy(keySelector: (Char) -> K, valueTransform: (Char) -> V): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10479)

a `Map` 返回包含`valueTransform` 提供的数值,并用 `keySelector` 函数索引适用于给定阵列元素。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

返回的地图保留原始数组的条目迭代顺序。

@sample 样本收集. 阵列. 变形. 联合原始物的阵列 与变异法相连接

### 19. Common

```kotlin
public inline fun <T, K> Iterable<T>.associateBy(keySelector: (T) -> K): Map<K, T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1368)

a `Map` 返回包含从对每个元素适用的`keySelector`函数返回的按键索引的给定收藏中元素的`Map`。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

归还的地图保留了原始收藏的条目迭代顺序。

@sample 样本、采集、采集、转化、关联

### 20. Common

```kotlin
public inline fun <T, K, V> Iterable<T>.associateBy(keySelector: (T) -> K, valueTransform: (T) -> V): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1383)

a `Map` 返回包含`valueTransform` 提供的数值,并用 `keySelector` 函数索引适用于特定收藏的元素。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

归还的地图保留了原始收藏的条目迭代顺序。

@sample 样本、采集、采集、变异、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    data class Person(val firstName: String, val lastName: String) {
        override fun toString(): String = "$firstName $lastName"
    }

    val scientists = listOf(Person("Grace", "Hopper"), Person("Jacob", "Bernoulli"), Person("Johann", "Bernoulli"))

    val byLastName = scientists.associateBy { it.lastName }

    // Jacob Bernoulli does not occur in the map because only the last pair with the same key gets added
    println(byLastName)
}
```

```text title="输出"
{Hopper=Grace Hopper, Bernoulli=Johann Bernoulli}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L718)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    data class Person(val firstName: String, val lastName: String)

    val scientists = listOf(Person("Grace", "Hopper"), Person("Jacob", "Bernoulli"), Person("Johann", "Bernoulli"))

    val byLastName = scientists.associateBy({ it.lastName }, { it.firstName })

    // Jacob Bernoulli does not occur in the map because only the last pair with the same key gets added
    println(byLastName)
}
```

```text title="输出"
{Hopper=Grace, Bernoulli=Johann}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L732)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
