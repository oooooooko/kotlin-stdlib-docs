# filterNot

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回包含所有与给定 `predicate` 不符的元素的列表 。

@sample 样本,采集的样本, 收集的样本,采集的样本, 采集的样本, 过滤的样本,过滤的样本

??? note "查看英文原文"

    Returns a list containing all elements not matching the given `predicate`.
    
    @sample samples.collections.Collections.Filtering.filter

## 声明与重载

### 1. Common

```kotlin
public inline fun <T> Array<out T>.filterNot(predicate: (T) -> Boolean): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4267)

### 2. Common

```kotlin
public inline fun ByteArray.filterNot(predicate: (Byte) -> Boolean): List<Byte>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4276)

### 3. Common

```kotlin
public inline fun ShortArray.filterNot(predicate: (Short) -> Boolean): List<Short>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4285)

### 4. Common

```kotlin
public inline fun IntArray.filterNot(predicate: (Int) -> Boolean): List<Int>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4294)

### 5. Common

```kotlin
public inline fun LongArray.filterNot(predicate: (Long) -> Boolean): List<Long>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4303)

### 6. Common

```kotlin
public inline fun FloatArray.filterNot(predicate: (Float) -> Boolean): List<Float>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4312)

### 7. Common

```kotlin
public inline fun DoubleArray.filterNot(predicate: (Double) -> Boolean): List<Double>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4321)

### 8. Common

```kotlin
public inline fun BooleanArray.filterNot(predicate: (Boolean) -> Boolean): List<Boolean>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4330)

### 9. Common

```kotlin
public inline fun CharArray.filterNot(predicate: (Char) -> Boolean): List<Char>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4339)

### 10. Common

```kotlin
public inline fun <T> Iterable<T>.filterNot(predicate: (T) -> Boolean): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L826)

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.filterNot(predicate: (UInt) -> Boolean): List<UInt>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2103)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.filterNot(predicate: (ULong) -> Boolean): List<ULong>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2115)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.filterNot(predicate: (UByte) -> Boolean): List<UByte>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2127)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.filterNot(predicate: (UShort) -> Boolean): List<UShort>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2139)

### 15. Common

```kotlin
public inline fun <K, V> Map<out K, V>.filterNot(predicate: (Map.Entry<K, V>) -> Boolean): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L703)

返回包含所有不符合给定 `predicate` 的密钥值对的新地图。

返回的地图保留原始地图的输入迭代顺序。 @sample 样本。 collects.maps. filting. filternot

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val numbers: List<Int> = listOf(1, 2, 3, 4, 5, 6, 7)
    val evenNumbers = numbers.filter { it % 2 == 0 }
    val notMultiplesOf3 = numbers.filterNot { number -> number % 3 == 0 }

    println(evenNumbers)
    println(notMultiplesOf3)
}
```

```text title="输出"
[2, 4, 6]
[1, 2, 4, 5, 7]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1565)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
