# any

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果数组至少有一个元素,则返回 `true` 。

@sample 样本、采集的样本、采集的样本、采集的样本、分类的样本、

??? note "查看英文原文"

    Returns `true` if array has at least one element.
    
    @sample samples.collections.Collections.Aggregates.any

## 声明与重载

### 1. Common

```kotlin
public fun <T> Array<out T>.any(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15222)

### 2. Common

```kotlin
public fun ByteArray.any(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15231)

### 3. Common

```kotlin
public fun ShortArray.any(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15240)

### 4. Common

```kotlin
public fun IntArray.any(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15249)

### 5. Common

```kotlin
public fun LongArray.any(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15258)

### 6. Common

```kotlin
public fun FloatArray.any(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15267)

### 7. Common

```kotlin
public fun DoubleArray.any(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15276)

### 8. Common

```kotlin
public fun BooleanArray.any(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15285)

### 9. Common

```kotlin
public fun CharArray.any(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15294)

### 10. Common

```kotlin
public inline fun <T> Array<out T>.any(predicate: (T) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15303)

如果至少有一个元素与给定的`predicate`值相符,则返回`true`。

@sample 样本、采集的样本、采集的采集资料、分类、任何

### 11. Common

```kotlin
public inline fun ByteArray.any(predicate: (Byte) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15313)

如果至少有一个元素与给定的`predicate`值相符,则返回`true`。

@sample 样本、采集的样本、采集的采集资料、分类、任何

### 12. Common

```kotlin
public inline fun ShortArray.any(predicate: (Short) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15323)

如果至少有一个元素与给定的`predicate`值相符,则返回`true`。

@sample 样本、采集的样本、采集的采集资料、分类、任何

### 13. Common

```kotlin
public inline fun IntArray.any(predicate: (Int) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15333)

如果至少有一个元素与给定的`predicate`值相符,则返回`true`。

@sample 样本、采集的样本、采集的采集资料、分类、任何

### 14. Common

```kotlin
public inline fun LongArray.any(predicate: (Long) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15343)

如果至少有一个元素与给定的`predicate`值相符,则返回`true`。

@sample 样本、采集的样本、采集的采集资料、分类、任何

### 15. Common

```kotlin
public inline fun FloatArray.any(predicate: (Float) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15353)

如果至少有一个元素与给定的`predicate`值相符,则返回`true`。

@sample 样本、采集的样本、采集的采集资料、分类、任何

### 16. Common

```kotlin
public inline fun DoubleArray.any(predicate: (Double) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15363)

如果至少有一个元素与给定的`predicate`值相符,则返回`true`。

@sample 样本、采集的样本、采集的采集资料、分类、任何

### 17. Common

```kotlin
public inline fun BooleanArray.any(predicate: (Boolean) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15373)

如果至少有一个元素与给定的`predicate`值相符,则返回`true`。

@sample 样本、采集的样本、采集的采集资料、分类、任何

### 18. Common

```kotlin
public inline fun CharArray.any(predicate: (Char) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15383)

如果至少有一个元素与给定的`predicate`值相符,则返回`true`。

@sample 样本、采集的样本、采集的采集资料、分类、任何

### 19. Common

```kotlin
public fun <T> Iterable<T>.any(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2075)

如果收藏至少有一个元素,则返回`true`。

@sample 样本、采集的样本、采集的样本、采集的样本、分类的样本、

### 20. Common

```kotlin
public inline fun <T> Iterable<T>.any(predicate: (T) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2085)

如果至少有一个元素与给定的`predicate`值相符,则返回`true`。

@sample 样本、采集的样本、采集的采集资料、分类、任何

### 21. Common

```kotlin
public fun <K, V> Map<out K, V>.any(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L178)

如果地图至少有一个条目,则返回`true`。

@sample 样本、采集的样本、采集的样本、采集的样本、分类的样本、

### 22. Common

```kotlin
public inline fun <K, V> Map<out K, V>.any(predicate: (Map.Entry<K, V>) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L187)

如果至少有一个条目与给定的`predicate`相符,则返回`true`。

@sample 样本、采集的样本、采集的采集资料、分类、任何

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.any(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6471)

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.any(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6483)

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.any(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6495)

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.any(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6507)

### 27. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.any(predicate: (UInt) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6519)

如果至少有一个元素与给定的`predicate`值相符,则返回`true`。

@sample 样本、采集的样本、采集的采集资料、分类、任何

### 28. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.any(predicate: (ULong) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6532)

如果至少有一个元素与给定的`predicate`值相符,则返回`true`。

@sample 样本、采集的样本、采集的采集资料、分类、任何

### 29. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.any(predicate: (UByte) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6545)

如果至少有一个元素与给定的`predicate`值相符,则返回`true`。

@sample 样本、采集的样本、采集的采集资料、分类、任何

### 30. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.any(predicate: (UShort) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6558)

如果至少有一个元素与给定的`predicate`值相符,则返回`true`。

@sample 样本、采集的样本、采集的采集资料、分类、任何

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val emptyList = emptyList<Int>()
    println(emptyList.any())

    val nonEmptyList = listOf(1, 2, 3)
    println(nonEmptyList.any())
}
```

```text title="输出"
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1020)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val isEven: (Int) -> Boolean = { it % 2 == 0 }
    val zeroToTen = 0..10
    println(zeroToTen.any { isEven(it) })
    println(zeroToTen.any(isEven))

    val odds = zeroToTen.map { it * 2 + 1 }
    println(odds.any { isEven(it) })

    val emptyList = emptyList<Int>()
    println(emptyList.any { true })
}
```

```text title="输出"
true
true
false
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1029)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
