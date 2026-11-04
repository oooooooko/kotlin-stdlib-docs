# all

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果所有元素都与给定的`predicate`相符,则返回`true`。

请注意,如果数组不含元素,函数返回 `true` ,因为其中没有元素_不匹配前提。请在 [“虚伪的真理”] (https://en.wikipedia.org/wiki/Vacuous_truth) 文章)中更详细地解释这一逻辑概念。

@sample 样本、采集的样本、采集的样本、采集的样本、分类的样本

??? note "查看英文原文"

    Returns `true` if all elements match the given `predicate`.
    
    Note that if the array contains no elements, the function returns `true`
    because there are no elements in it that _do not_ match the predicate.
    See a more detailed explanation of this logic concept in ["Vacuous truth"](https://en.wikipedia.org/wiki/Vacuous_truth) article.
    
    @sample samples.collections.Collections.Aggregates.all

## 声明与重载

### 1. Common

```kotlin
public inline fun <T> Array<out T>.all(predicate: (T) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14157)

### 2. Common

```kotlin
public inline fun ByteArray.all(predicate: (Byte) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14171)

### 3. Common

```kotlin
public inline fun ShortArray.all(predicate: (Short) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14185)

### 4. Common

```kotlin
public inline fun IntArray.all(predicate: (Int) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14199)

### 5. Common

```kotlin
public inline fun LongArray.all(predicate: (Long) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14213)

### 6. Common

```kotlin
public inline fun FloatArray.all(predicate: (Float) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14227)

### 7. Common

```kotlin
public inline fun DoubleArray.all(predicate: (Double) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14241)

### 8. Common

```kotlin
public inline fun BooleanArray.all(predicate: (Boolean) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14255)

### 9. Common

```kotlin
public inline fun CharArray.all(predicate: (Char) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14269)

### 10. Common

```kotlin
public inline fun <T> Iterable<T>.all(predicate: (T) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1935)

如果所有元素都与给定的`predicate`相符,则返回`true`。

请注意,如果收藏中不含元素,函数返回 `true` , 因为其中没有元素_ 与前提匹配。 请在 [“ 虚伪的真理 ” (https://en.wikipedia.org/wiki/Vacuous_truth) 文章) 中更详细地解释这一逻辑概念。

@sample 样本、采集的样本、采集的样本、采集的样本、分类的样本

### 11. Common

```kotlin
public inline fun <K, V> Map<out K, V>.all(predicate: (Map.Entry<K, V>) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L163)

如果所有条目都与给定的 `predicate` 相符,则返回`true`。

请注意,如果地图中没有条目,函数返回 `true` ,因为其中没有条目_不匹配前提。请在 [“虚伪的真理”] (https://en.wikipedia.org/wiki/Vacuous_truth) 文章)中更详细地解释这一逻辑概念。

@sample 样本、采集的样本、采集的样本、采集的样本、分类的样本

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.all(predicate: (UInt) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5975)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.all(predicate: (ULong) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5992)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.all(predicate: (UByte) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6009)

### 15. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.all(predicate: (UShort) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6026)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val isEven: (Int) -> Boolean = { it % 2 == 0 }
    val zeroToTen = 0..10
    println(zeroToTen.all { isEven(it) })
    println(zeroToTen.all(isEven))

    val evens = zeroToTen.map { it * 2 }
    println(evens.all { isEven(it) })

    val emptyList = emptyList<Int>()
    println(emptyList.all { false })
}
```

```text title="输出"
false
false
true
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L983)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
