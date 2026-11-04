# groupByTo

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将每个元素都应用到给定的 `keySelector` 函数返回的键的原始数组的组元素组,并将每个与相应元素列表相关的关键组都放在`destination`地图上。

@return `destination` 地图

@sample 样本、采集、采集、变形、组别

??? note "查看英文原文"

    Groups elements of the original array by the key returned by the given `keySelector` function
    applied to each element and puts to the `destination` map each group key associated with a list of corresponding elements.
    
    @return The `destination` map.
    
    @sample samples.collections.Collections.Transformations.groupBy

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, K, M : MutableMap<in K, MutableList<T>>> Array<out T>.groupByTo(destination: M, keySelector: (T) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12496)

### 2. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, MutableList<Byte>>> ByteArray.groupByTo(destination: M, keySelector: (Byte) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12514)

### 3. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, MutableList<Short>>> ShortArray.groupByTo(destination: M, keySelector: (Short) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12532)

### 4. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, MutableList<Int>>> IntArray.groupByTo(destination: M, keySelector: (Int) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12550)

### 5. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, MutableList<Long>>> LongArray.groupByTo(destination: M, keySelector: (Long) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12568)

### 6. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, MutableList<Float>>> FloatArray.groupByTo(destination: M, keySelector: (Float) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12586)

### 7. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, MutableList<Double>>> DoubleArray.groupByTo(destination: M, keySelector: (Double) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12604)

### 8. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, MutableList<Boolean>>> BooleanArray.groupByTo(destination: M, keySelector: (Boolean) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12622)

### 9. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, MutableList<Char>>> CharArray.groupByTo(destination: M, keySelector: (Char) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12640)

### 10. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, K, V, M : MutableMap<in K, MutableList<V>>> Array<out T>.groupByTo(destination: M, keySelector: (T) -> K, valueTransform: (T) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12658)

适用于原始数组中每个元素的 `valueTransform` 函数返回的组值
键时的键,根据给定的 `keySelector` 函数返回的键,该函数适用于元素
并给 `destination` 地图下每个组键, 与相应的值列表相关联。

@return `destination` 地图

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 11. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> ByteArray.groupByTo(destination: M, keySelector: (Byte) -> K, valueTransform: (Byte) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12677)

适用于原始数组中每个元素的 `valueTransform` 函数返回的组值
键时的键,根据给定的 `keySelector` 函数返回的键,该函数适用于元素
并给 `destination` 地图下每个组键, 与相应的值列表相关联。

@return `destination` 地图

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 12. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> ShortArray.groupByTo(destination: M, keySelector: (Short) -> K, valueTransform: (Short) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12696)

适用于原始数组中每个元素的 `valueTransform` 函数返回的组值
键时的键,根据给定的 `keySelector` 函数返回的键,该函数适用于元素
并给 `destination` 地图下每个组键, 与相应的值列表相关联。

@return `destination` 地图

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 13. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> IntArray.groupByTo(destination: M, keySelector: (Int) -> K, valueTransform: (Int) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12715)

适用于原始数组中每个元素的 `valueTransform` 函数返回的组值
键时的键,根据给定的 `keySelector` 函数返回的键,该函数适用于元素
并给 `destination` 地图下每个组键, 与相应的值列表相关联。

@return `destination` 地图

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 14. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> LongArray.groupByTo(destination: M, keySelector: (Long) -> K, valueTransform: (Long) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12734)

适用于原始数组中每个元素的 `valueTransform` 函数返回的组值
键时的键,根据给定的 `keySelector` 函数返回的键,该函数适用于元素
并给 `destination` 地图下每个组键, 与相应的值列表相关联。

@return `destination` 地图

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 15. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> FloatArray.groupByTo(destination: M, keySelector: (Float) -> K, valueTransform: (Float) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12753)

适用于原始数组中每个元素的 `valueTransform` 函数返回的组值
键时的键,根据给定的 `keySelector` 函数返回的键,该函数适用于元素
并给 `destination` 地图下每个组键, 与相应的值列表相关联。

@return `destination` 地图

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 16. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> DoubleArray.groupByTo(destination: M, keySelector: (Double) -> K, valueTransform: (Double) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12772)

适用于原始数组中每个元素的 `valueTransform` 函数返回的组值
键时的键,根据给定的 `keySelector` 函数返回的键,该函数适用于元素
并给 `destination` 地图下每个组键, 与相应的值列表相关联。

@return `destination` 地图

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 17. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> BooleanArray.groupByTo(destination: M, keySelector: (Boolean) -> K, valueTransform: (Boolean) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12791)

适用于原始数组中每个元素的 `valueTransform` 函数返回的组值
键时的键,根据给定的 `keySelector` 函数返回的键,该函数适用于元素
并给 `destination` 地图下每个组键, 与相应的值列表相关联。

@return `destination` 地图

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 18. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> CharArray.groupByTo(destination: M, keySelector: (Char) -> K, valueTransform: (Char) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12810)

适用于原始数组中每个元素的 `valueTransform` 函数返回的组值
键时的键,根据给定的 `keySelector` 函数返回的键,该函数适用于元素
并给 `destination` 地图下每个组键, 与相应的值列表相关联。

@return `destination` 地图

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 19. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, K, M : MutableMap<in K, MutableList<T>>> Iterable<T>.groupByTo(destination: M, keySelector: (T) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1687)

由给定`keySelector`函数返回的键子返回的原始收藏的组元素组,适用于每个元素,并将每个元素组的关键与相应元素列表相关联,放在`destination`地图上。

@return `destination` 地图

@sample 样本、采集、采集、变形、组别

### 20. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, K, V, M : MutableMap<in K, MutableList<V>>> Iterable<T>.groupByTo(destination: M, keySelector: (T) -> K, valueTransform: (T) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1705)

`valueTransform` 函数返回的组值, 以 `valueTransform` 函数返回的键对原始收藏的每个元素应用, 并给给 `keySelector` 函数返回的键对元素应用, 并将每个与相应值列表相关的组键都放置到 `destination` 地图上。

@return `destination` 地图

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 21. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, M : MutableMap<in K, MutableList<UInt>>> UIntArray.groupByTo(destination: M, keySelector: (UInt) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5535)

### 22. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, M : MutableMap<in K, MutableList<ULong>>> ULongArray.groupByTo(destination: M, keySelector: (ULong) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5556)

### 23. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, M : MutableMap<in K, MutableList<UByte>>> UByteArray.groupByTo(destination: M, keySelector: (UByte) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5577)

### 24. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, M : MutableMap<in K, MutableList<UShort>>> UShortArray.groupByTo(destination: M, keySelector: (UShort) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5598)

### 25. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> UIntArray.groupByTo(destination: M, keySelector: (UInt) -> K, valueTransform: (UInt) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5619)

适用于原始数组中每个元素的 `valueTransform` 函数返回的组值
键时的键,根据给定的 `keySelector` 函数返回的键,该函数适用于元素
并给 `destination` 地图下每个组键, 与相应的值列表相关联。

@return `destination` 地图

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 26. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> ULongArray.groupByTo(destination: M, keySelector: (ULong) -> K, valueTransform: (ULong) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5641)

适用于原始数组中每个元素的 `valueTransform` 函数返回的组值
键时的键,根据给定的 `keySelector` 函数返回的键,该函数适用于元素
并给 `destination` 地图下每个组键, 与相应的值列表相关联。

@return `destination` 地图

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 27. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> UByteArray.groupByTo(destination: M, keySelector: (UByte) -> K, valueTransform: (UByte) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5663)

适用于原始数组中每个元素的 `valueTransform` 函数返回的组值
键时的键,根据给定的 `keySelector` 函数返回的键,该函数适用于元素
并给 `destination` 地图下每个组键, 与相应的值列表相关联。

@return `destination` 地图

@sample 样本、采集、采集、转换、ByKeys和Vales组

### 28. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <K, V, M : MutableMap<in K, MutableList<V>>> UShortArray.groupByTo(destination: M, keySelector: (UShort) -> K, valueTransform: (UShort) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5685)

适用于原始数组中每个元素的 `valueTransform` 函数返回的组值
键时的键,根据给定的 `keySelector` 函数返回的键,该函数适用于元素
并给 `destination` 地图下每个组键, 与相应的值列表相关联。

@return `destination` 地图

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
