# none

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果数组没有元素,则返回 `true` 。

@sample 样本、采集的样本、采集的样本、采集的样本、分类的样本、无

??? note "查看英文原文"

    Returns `true` if the array has no elements.
    
    @sample samples.collections.Collections.Aggregates.none

## 声明与重载

### 1. Common

```kotlin
public fun <T> Array<out T>.none(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22237)

### 2. Common

```kotlin
public fun ByteArray.none(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22246)

### 3. Common

```kotlin
public fun ShortArray.none(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22255)

### 4. Common

```kotlin
public fun IntArray.none(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22264)

### 5. Common

```kotlin
public fun LongArray.none(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22273)

### 6. Common

```kotlin
public fun FloatArray.none(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22282)

### 7. Common

```kotlin
public fun DoubleArray.none(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22291)

### 8. Common

```kotlin
public fun BooleanArray.none(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22300)

### 9. Common

```kotlin
public fun CharArray.none(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22309)

### 10. Common

```kotlin
public inline fun <T> Array<out T>.none(predicate: (T) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22318)

如果没有元素与给定的`predicate`匹配,则返回`true`。

@sample 样本、采集的样本、采集的采集资料

### 11. Common

```kotlin
public inline fun ByteArray.none(predicate: (Byte) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22328)

如果没有元素与给定的`predicate`匹配,则返回`true`。

@sample 样本、采集的样本、采集的采集资料

### 12. Common

```kotlin
public inline fun ShortArray.none(predicate: (Short) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22338)

如果没有元素与给定的`predicate`匹配,则返回`true`。

@sample 样本、采集的样本、采集的采集资料

### 13. Common

```kotlin
public inline fun IntArray.none(predicate: (Int) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22348)

如果没有元素与给定的`predicate`匹配,则返回`true`。

@sample 样本、采集的样本、采集的采集资料

### 14. Common

```kotlin
public inline fun LongArray.none(predicate: (Long) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22358)

如果没有元素与给定的`predicate`匹配,则返回`true`。

@sample 样本、采集的样本、采集的采集资料

### 15. Common

```kotlin
public inline fun FloatArray.none(predicate: (Float) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22368)

如果没有元素与给定的`predicate`匹配,则返回`true`。

@sample 样本、采集的样本、采集的采集资料

### 16. Common

```kotlin
public inline fun DoubleArray.none(predicate: (Double) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22378)

如果没有元素与给定的`predicate`匹配,则返回`true`。

@sample 样本、采集的样本、采集的采集资料

### 17. Common

```kotlin
public inline fun BooleanArray.none(predicate: (Boolean) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22388)

如果没有元素与给定的`predicate`匹配,则返回`true`。

@sample 样本、采集的样本、采集的采集资料

### 18. Common

```kotlin
public inline fun CharArray.none(predicate: (Char) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22398)

如果没有元素与给定的`predicate`匹配,则返回`true`。

@sample 样本、采集的样本、采集的采集资料

### 19. Common

```kotlin
public fun <T> Iterable<T>.none(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3060)

如果收藏没有元素,则返回`true`。

@sample 样本、采集的样本、采集的样本、采集的样本、分类的样本、无

### 20. Common

```kotlin
public inline fun <T> Iterable<T>.none(predicate: (T) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3070)

如果没有元素与给定的`predicate`匹配,则返回`true`。

@sample 样本、采集的样本、采集的采集资料

### 21. Common

```kotlin
public fun <K, V> Map<out K, V>.none(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L620)

如果地图没有输入,则返回`true`。

@sample 样本、采集的样本、采集的样本、采集的样本、分类的样本、无

### 22. Common

```kotlin
public inline fun <K, V> Map<out K, V>.none(predicate: (Map.Entry<K, V>) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L629)

如果没有符合给定的 `predicate`的条目,则返回`true`。

@sample 样本、采集的样本、采集的采集资料

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.none(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9743)

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.none(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9755)

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.none(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9767)

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.none(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9779)

### 27. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.none(predicate: (UInt) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9791)

如果没有元素与给定的`predicate`匹配,则返回`true`。

@sample 样本、采集的样本、采集的采集资料

### 28. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.none(predicate: (ULong) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9804)

如果没有元素与给定的`predicate`匹配,则返回`true`。

@sample 样本、采集的样本、采集的采集资料

### 29. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.none(predicate: (UByte) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9817)

如果没有元素与给定的`predicate`匹配,则返回`true`。

@sample 样本、采集的样本、采集的采集资料

### 30. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.none(predicate: (UShort) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9830)

如果没有元素与给定的`predicate`匹配,则返回`true`。

@sample 样本、采集的样本、采集的采集资料

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val emptyList = emptyList<Int>()
    println(emptyList.none())

    val nonEmptyList = listOf("one", "two", "three")
    println(nonEmptyList.none())
}
```

```text title="输出"
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L997)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val isEven: (Int) -> Boolean = { it % 2 == 0 }
    val zeroToTen = 0..10
    println(zeroToTen.none { isEven(it) })
    println(zeroToTen.none(isEven))

    val odds = zeroToTen.map { it * 2 + 1 }
    println(odds.none { isEven(it) })

    val emptyList = emptyList<Int>()
    println(emptyList.none { true })
}
```

```text title="输出"
false
false
true
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1006)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
