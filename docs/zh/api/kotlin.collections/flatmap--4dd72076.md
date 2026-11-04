# flatMap

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回从`transform`函数结果中得出的所有元素的单列列表,这些函数在原始数组的每个元素中被引用。

@sample 样本、采集、采集、变形、平流图

??? note "查看英文原文"

    Returns a single list of all elements yielded from results of `transform` function being invoked on each element of original array.
    
    @sample samples.collections.Collections.Transformations.flatMap

## 声明与重载

### 1. Common

```kotlin
public inline fun <T, R> Array<out T>.flatMap(transform: (T) -> Iterable<R>): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11713)

### 2. Common

```kotlin
public inline fun <R> ByteArray.flatMap(transform: (Byte) -> Iterable<R>): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11722)

### 3. Common

```kotlin
public inline fun <R> ShortArray.flatMap(transform: (Short) -> Iterable<R>): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11731)

### 4. Common

```kotlin
public inline fun <R> IntArray.flatMap(transform: (Int) -> Iterable<R>): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11740)

### 5. Common

```kotlin
public inline fun <R> LongArray.flatMap(transform: (Long) -> Iterable<R>): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11749)

### 6. Common

```kotlin
public inline fun <R> FloatArray.flatMap(transform: (Float) -> Iterable<R>): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11758)

### 7. Common

```kotlin
public inline fun <R> DoubleArray.flatMap(transform: (Double) -> Iterable<R>): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11767)

### 8. Common

```kotlin
public inline fun <R> BooleanArray.flatMap(transform: (Boolean) -> Iterable<R>): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11776)

### 9. Common

```kotlin
public inline fun <R> CharArray.flatMap(transform: (Char) -> Iterable<R>): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11785)

### 10. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.jvm.JvmName("flatMapSequence")
public inline fun <T, R> Array<out T>.flatMap(transform: (T) -> Sequence<R>): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11794)

### 11. Common

```kotlin
public inline fun <T, R> Iterable<T>.flatMap(transform: (T) -> Iterable<R>): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1544)

返回从`transform`函数结果中得出的所有元素的单列列表,这些函数在原始收藏的每个元素上都被引用。

@sample 样本、采集、采集、变形、平流图

### 12. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.jvm.JvmName("flatMapSequence")
public inline fun <T, R> Iterable<T>.flatMap(transform: (T) -> Sequence<R>): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1553)

返回从`transform`函数结果中得出的所有元素的单列列表,这些函数在原始收藏的每个元素上都被引用。

@sample 样本、采集、采集、变形、平流图

### 13. Common

```kotlin
public inline fun <K, V, R> Map<out K, V>.flatMap(transform: (Map.Entry<K, V>) -> Iterable<R>): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L72)

返回从原始地图每个条目引用的`transform`函数结果中得出的所有元素的单项清单。

@sample 样本采集 地图 变形图 平展图

### 14. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.jvm.JvmName("flatMapSequence")
public inline fun <K, V, R> Map<out K, V>.flatMap(transform: (Map.Entry<K, V>) -> Sequence<R>): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L81)

返回从原始地图每个条目引用的`transform`函数结果中得出的所有元素的单项清单。

@sample 样本、采集、采集、变形、平流图

### 15. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R> UIntArray.flatMap(transform: (UInt) -> Iterable<R>): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5167)

### 16. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R> ULongArray.flatMap(transform: (ULong) -> Iterable<R>): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5179)

### 17. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R> UByteArray.flatMap(transform: (UByte) -> Iterable<R>): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5191)

### 18. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R> UShortArray.flatMap(transform: (UShort) -> Iterable<R>): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5203)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = listOf("123", "45")
    println(list.flatMap { it.toList() })
}
```

```text title="输出"
[1, 2, 3, 4, 5]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L897)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
