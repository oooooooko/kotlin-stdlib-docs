# groupBy

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

以给定 `keySelector` 函数返回的键返回的原始数组的元素组,对每个元素适用,并返回一个地图,其中每个组的键与相应元素列表相关联。

返回的地图保留了原始数组产生的键的输入迭代顺序。

@sample 样本、采集、采集、变形、组别

??? note "查看英文原文"

    Groups elements of the original array by the key returned by the given `keySelector` function
    applied to each element and returns a map where each group key is associated with a list of corresponding elements.
    
    The returned map preserves the entry iteration order of the keys produced from the original array.
    
    @sample samples.collections.Collections.Transformations.groupBy

## 声明与重载

### 1. Common

```kotlin
public inline fun <T, K> Array<out T>.groupBy(keySelector: (T) -> K): Map<K, List<T>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12271)

### 2. Common

```kotlin
public inline fun <K> ByteArray.groupBy(keySelector: (Byte) -> K): Map<K, List<Byte>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12283)

### 3. Common

```kotlin
public inline fun <K> ShortArray.groupBy(keySelector: (Short) -> K): Map<K, List<Short>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12295)

### 4. Common

```kotlin
public inline fun <K> IntArray.groupBy(keySelector: (Int) -> K): Map<K, List<Int>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12307)

### 5. Common

```kotlin
public inline fun <K> LongArray.groupBy(keySelector: (Long) -> K): Map<K, List<Long>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12319)

### 6. Common

```kotlin
public inline fun <K> FloatArray.groupBy(keySelector: (Float) -> K): Map<K, List<Float>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12331)

### 7. Common

```kotlin
public inline fun <K> DoubleArray.groupBy(keySelector: (Double) -> K): Map<K, List<Double>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12343)

### 8. Common

```kotlin
public inline fun <K> BooleanArray.groupBy(keySelector: (Boolean) -> K): Map<K, List<Boolean>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12355)

### 9. Common

```kotlin
public inline fun <K> CharArray.groupBy(keySelector: (Char) -> K): Map<K, List<Char>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12367)

### 10. Common

```kotlin
public inline fun <T, K, V> Array<out T>.groupBy(keySelector: (T) -> K, valueTransform: (T) -> V): Map<K, List<V>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12379)

`valueTransform` 函数返回的组值, 以 `valueTransform` 函数返回的键对原始数组的每个元素应用, 以给定 `keySelector` 函数返回的键对元素应用, 返回一个地图, 将每个组键与相应值列表联系起来 。

返回的地图保留了原始数组产生的键的输入迭代顺序。

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 11. Common

```kotlin
public inline fun <K, V> ByteArray.groupBy(keySelector: (Byte) -> K, valueTransform: (Byte) -> V): Map<K, List<V>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12392)

`valueTransform` 函数返回的组值, 以 `valueTransform` 函数返回的键对原始数组的每个元素应用, 以给定 `keySelector` 函数返回的键对元素应用, 返回一个地图, 将每个组键与相应值列表联系起来 。

返回的地图保留了原始数组产生的键的输入迭代顺序。

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 12. Common

```kotlin
public inline fun <K, V> ShortArray.groupBy(keySelector: (Short) -> K, valueTransform: (Short) -> V): Map<K, List<V>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12405)

`valueTransform` 函数返回的组值, 以 `valueTransform` 函数返回的键对原始数组的每个元素应用, 以给定 `keySelector` 函数返回的键对元素应用, 返回一个地图, 将每个组键与相应值列表联系起来 。

返回的地图保留了原始数组产生的键的输入迭代顺序。

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 13. Common

```kotlin
public inline fun <K, V> IntArray.groupBy(keySelector: (Int) -> K, valueTransform: (Int) -> V): Map<K, List<V>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12418)

`valueTransform` 函数返回的组值, 以 `valueTransform` 函数返回的键对原始数组的每个元素应用, 以给定 `keySelector` 函数返回的键对元素应用, 返回一个地图, 将每个组键与相应值列表联系起来 。

返回的地图保留了原始数组产生的键的输入迭代顺序。

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 14. Common

```kotlin
public inline fun <K, V> LongArray.groupBy(keySelector: (Long) -> K, valueTransform: (Long) -> V): Map<K, List<V>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12431)

`valueTransform` 函数返回的组值, 以 `valueTransform` 函数返回的键对原始数组的每个元素应用, 以给定 `keySelector` 函数返回的键对元素应用, 返回一个地图, 将每个组键与相应值列表联系起来 。

返回的地图保留了原始数组产生的键的输入迭代顺序。

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 15. Common

```kotlin
public inline fun <K, V> FloatArray.groupBy(keySelector: (Float) -> K, valueTransform: (Float) -> V): Map<K, List<V>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12444)

`valueTransform` 函数返回的组值, 以 `valueTransform` 函数返回的键对原始数组的每个元素应用, 以给定 `keySelector` 函数返回的键对元素应用, 返回一个地图, 将每个组键与相应值列表联系起来 。

返回的地图保留了原始数组产生的键的输入迭代顺序。

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 16. Common

```kotlin
public inline fun <K, V> DoubleArray.groupBy(keySelector: (Double) -> K, valueTransform: (Double) -> V): Map<K, List<V>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12457)

`valueTransform` 函数返回的组值, 以 `valueTransform` 函数返回的键对原始数组的每个元素应用, 以给定 `keySelector` 函数返回的键对元素应用, 返回一个地图, 将每个组键与相应值列表联系起来 。

返回的地图保留了原始数组产生的键的输入迭代顺序。

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 17. Common

```kotlin
public inline fun <K, V> BooleanArray.groupBy(keySelector: (Boolean) -> K, valueTransform: (Boolean) -> V): Map<K, List<V>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12470)

`valueTransform` 函数返回的组值, 以 `valueTransform` 函数返回的键对原始数组的每个元素应用, 以给定 `keySelector` 函数返回的键对元素应用, 返回一个地图, 将每个组键与相应值列表联系起来 。

返回的地图保留了原始数组产生的键的输入迭代顺序。

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 18. Common

```kotlin
public inline fun <K, V> CharArray.groupBy(keySelector: (Char) -> K, valueTransform: (Char) -> V): Map<K, List<V>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12483)

`valueTransform` 函数返回的组值, 以 `valueTransform` 函数返回的键对原始数组的每个元素应用, 以给定 `keySelector` 函数返回的键对元素应用, 返回一个地图, 将每个组键与相应值列表联系起来 。

返回的地图保留了原始数组产生的键的输入迭代顺序。

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 19. Common

```kotlin
public inline fun <T, K> Iterable<T>.groupBy(keySelector: (T) -> K): Map<K, List<T>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1662)

以给定 `keySelector` 函数返回的键返回的原始收藏的组元素组, 适用于每个元素, 并返回一个地图, 每个组合键与相应元素列表相关联 。

归还的地图保留了原始收藏中生成的钥匙的输入迭代顺序。

@sample 样本、采集、采集、变形、组别

### 20. Common

```kotlin
public inline fun <T, K, V> Iterable<T>.groupBy(keySelector: (T) -> K, valueTransform: (T) -> V): Map<K, List<V>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1674)

`valueTransform` 函数返回的组值, 以 `valueTransform` 函数返回的键对原始收藏的每个元素应用, 以给定 `keySelector` 函数返回的键对元素应用, 返回一个地图, 将每个组键与相应值列表联系起来 。

归还的地图保留了原始收藏中生成的钥匙的输入迭代顺序。

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 21. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K> UIntArray.groupBy(keySelector: (UInt) -> K): Map<K, List<UInt>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5411)

### 22. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K> ULongArray.groupBy(keySelector: (ULong) -> K): Map<K, List<ULong>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5426)

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K> UByteArray.groupBy(keySelector: (UByte) -> K): Map<K, List<UByte>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5441)

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K> UShortArray.groupBy(keySelector: (UShort) -> K): Map<K, List<UShort>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5456)

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, V> UIntArray.groupBy(keySelector: (UInt) -> K, valueTransform: (UInt) -> V): Map<K, List<V>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5471)

`valueTransform` 函数返回的组值, 以 `valueTransform` 函数返回的键对原始数组的每个元素应用, 以给定 `keySelector` 函数返回的键对元素应用, 返回一个地图, 将每个组键与相应值列表联系起来 。

返回的地图保留了原始数组产生的键的输入迭代顺序。

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, V> ULongArray.groupBy(keySelector: (ULong) -> K, valueTransform: (ULong) -> V): Map<K, List<V>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5487)

`valueTransform` 函数返回的组值, 以 `valueTransform` 函数返回的键对原始数组的每个元素应用, 以给定 `keySelector` 函数返回的键对元素应用, 返回一个地图, 将每个组键与相应值列表联系起来 。

返回的地图保留了原始数组产生的键的输入迭代顺序。

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 27. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, V> UByteArray.groupBy(keySelector: (UByte) -> K, valueTransform: (UByte) -> V): Map<K, List<V>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5503)

`valueTransform` 函数返回的组值, 以 `valueTransform` 函数返回的键对原始数组的每个元素应用, 以给定 `keySelector` 函数返回的键对元素应用, 返回一个地图, 将每个组键与相应值列表联系起来 。

返回的地图保留了原始数组产生的键的输入迭代顺序。

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 28. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, V> UShortArray.groupBy(keySelector: (UShort) -> K, valueTransform: (UShort) -> V): Map<K, List<V>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5519)

`valueTransform` 函数返回的组值, 以 `valueTransform` 函数返回的键对原始数组的每个元素应用, 以给定 `keySelector` 函数返回的键对元素应用, 返回一个地图, 将每个组键与相应值列表联系起来 。

返回的地图保留了原始数组产生的键的输入迭代顺序。

@sample 样本、采集、采集、转换、ByKeys和Vales组

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val words = listOf("a", "abc", "ab", "def", "abcd")
    val byLength = words.groupBy { it.length }

    println(byLength.keys)
    println(byLength.values)

    val mutableByLength: MutableMap<Int, MutableList<String>> = words.groupByTo(mutableMapOf()) { it.length }
    // same content as in byLength map, but the map is mutable
    println(mutableByLength == byLength)
}
```

```text title="输出"
[1, 3, 2, 4]
[[a], [abc, def], [ab], [abcd]]
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L826)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val nameToTeam = listOf("Alice" to "Marketing", "Bob" to "Sales", "Carol" to "Marketing")
    val namesByTeam = nameToTeam.groupBy({ it.second }, { it.first })
    println(namesByTeam)

    val mutableNamesByTeam = nameToTeam.groupByTo(HashMap(), { it.second }, { it.first })
    // same content as in namesByTeam map, but the map is mutable
    println(mutableNamesByTeam == namesByTeam)
}
```

```text title="输出"
{Marketing=[Alice, Carol], Sales=[Bob]}
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L839)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
