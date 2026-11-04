# associate

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

a `Map` 返回由 `transform` 函数提供的包含关键值对数组元素的对数, 并包含对关键值对数。

如果两对中的任何一个有相同的键, 最后的键会被添加到地图上。

返回的地图保留原始数组的条目迭代顺序。

@sample 样本.采集物. 阵列. 变形. 联合原始武器

??? note "查看英文原文"

    Returns a `Map` containing key-value pairs provided by `transform` function
    applied to elements of the given array.
    
    If any of two pairs would have the same key the last one gets added to the map.
    
    The returned map preserves the entry iteration order of the original array.
    
    @sample samples.collections.Arrays.Transformations.associateArrayOfPrimitives

## 声明与重载

### 1. Common

```kotlin
public inline fun <T, K, V> Array<out T>.associate(transform: (T) -> Pair<K, V>): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10097)

### 2. Common

```kotlin
public inline fun <K, V> ByteArray.associate(transform: (Byte) -> Pair<K, V>): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10112)

### 3. Common

```kotlin
public inline fun <K, V> ShortArray.associate(transform: (Short) -> Pair<K, V>): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10127)

### 4. Common

```kotlin
public inline fun <K, V> IntArray.associate(transform: (Int) -> Pair<K, V>): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10142)

### 5. Common

```kotlin
public inline fun <K, V> LongArray.associate(transform: (Long) -> Pair<K, V>): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10157)

### 6. Common

```kotlin
public inline fun <K, V> FloatArray.associate(transform: (Float) -> Pair<K, V>): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10172)

### 7. Common

```kotlin
public inline fun <K, V> DoubleArray.associate(transform: (Double) -> Pair<K, V>): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10187)

### 8. Common

```kotlin
public inline fun <K, V> BooleanArray.associate(transform: (Boolean) -> Pair<K, V>): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10202)

### 9. Common

```kotlin
public inline fun <K, V> CharArray.associate(transform: (Char) -> Pair<K, V>): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10217)

### 10. Common

```kotlin
public inline fun <T, K, V> Iterable<T>.associate(transform: (T) -> Pair<K, V>): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1353)

a `Map` 返回由 `transform` 函数提供的包含关键值对配对的`Map`, 适用于特定收藏的元素。

如果两对中的任何一个有相同的键, 最后的键会被添加到地图上。

归还的地图保留了原始收藏的条目迭代顺序。

@sample 样本、采集、采集、转化、关联

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val names = listOf("Grace Hopper", "Jacob Bernoulli", "Johann Bernoulli")

    val byLastName = names.associate { it.split(" ").let { (firstName, lastName) -> lastName to firstName } }

    // Jacob Bernoulli does not occur in the map because only the last pair with the same key gets added
    println(byLastName)
}
```

```text title="输出"
{Hopper=Grace, Bernoulli=Johann}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L708)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
