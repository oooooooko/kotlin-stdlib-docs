# isSortedWith

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果数组中每个元素小于或等于 `true` 返回
以下列元素为单位,根据指定的`comparator`。

如果数组的元素少于两个元素,则返回`true`。

将按顺序用`Comparator.compare`对元素进行比较,如果对相邻元素的每一对,前一元素不大于下一元素,则将数组视为排序。

@sample 样本. 生成. issorated. IS 类组阵列样本. is scoted with commonted

??? note "查看英文原文"

    Returns `true` if each element in the array is less than or equal
    to the following element according to the specified `comparator`.
    
    Returns `true` if the array has fewer than two elements.
    
    The elements are compared sequentially using `Comparator.compare`,
    and the array is considered sorted if for each pair of adjacent elements
    the preceding element is not greater than the following one.
    
    @sample samples.generated.issorted.IsSortedArraySamples.isSortedWith

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.4")
public fun <T> Array<out T>.isSortedWith(comparator: Comparator<in T>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6426)

### 2. Common

```kotlin
@SinceKotlin("2.4")
public fun ByteArray.isSortedWith(comparator: Comparator<in Byte>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6446)

如果数组中每个元素小于或等于 `true` 返回
以下列元素为单位,根据指定的`comparator`。

如果数组的元素少于两个元素,则返回`true`。

将按顺序用`Comparator.compare`对元素进行比较,如果对相邻元素的每一对,前一元素不大于下一元素,则将数组视为排序。

@sample 样本. 生成. issorated. is sortedByte 亚射线样本. is sorted with

### 3. Common

```kotlin
@SinceKotlin("2.4")
public fun ShortArray.isSortedWith(comparator: Comparator<in Short>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6466)

如果数组中每个元素小于或等于 `true` 返回
以下列元素为单位,根据指定的`comparator`。

如果数组的元素少于两个元素,则返回`true`。

将按顺序用`Comparator.compare`对元素进行比较,如果对相邻元素的每一对,前一元素不大于下一元素,则将数组视为排序。

@sample 样本. 生成. issorated. Is 类集短线阵列样本. is sortedShortAraySamples

### 4. Common

```kotlin
@SinceKotlin("2.4")
public fun IntArray.isSortedWith(comparator: Comparator<in Int>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6486)

如果数组中每个元素小于或等于 `true` 返回
以下列元素为单位,根据指定的`comparator`。

如果数组的元素少于两个元素,则返回`true`。

将按顺序用`Comparator.compare`对元素进行比较,如果对相邻元素的每一对,前一元素不大于下一元素,则将数组视为排序。

@sample 样本. 生成. issorated. IS 分类的 内部阵列样本. is scoted with coolted

### 5. Common

```kotlin
@SinceKotlin("2.4")
public fun LongArray.isSortedWith(comparator: Comparator<in Long>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6506)

如果数组中每个元素小于或等于 `true` 返回
以下列元素为单位,根据指定的`comparator`。

如果数组的元素少于两个元素,则返回`true`。

将按顺序用`Comparator.compare`对元素进行比较,如果对相邻元素的每一对,前一元素不大于下一元素,则将数组视为排序。

@sample 样本. 生成. issorated. IS 分类式长阵列样本. is sorted LongAraySamples

### 6. Common

```kotlin
@SinceKotlin("2.4")
public fun FloatArray.isSortedWith(comparator: Comparator<in Float>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6526)

如果数组中每个元素小于或等于 `true` 返回
以下列元素为单位,根据指定的`comparator`。

如果数组的元素少于两个元素,则返回`true`。

将按顺序用`Comparator.compare`对元素进行比较,如果对相邻元素的每一对,前一元素不大于下一元素,则将数组视为排序。

@sample 样本. 生成. issorated.  Iss 分类的Float 阵列样本. is scoordted with

### 7. Common

```kotlin
@SinceKotlin("2.4")
public fun DoubleArray.isSortedWith(comparator: Comparator<in Double>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6546)

如果数组中每个元素小于或等于 `true` 返回
以下列元素为单位,根据指定的`comparator`。

如果数组的元素少于两个元素,则返回`true`。

将按顺序用`Comparator.compare`对元素进行比较,如果对相邻元素的每一对,前一元素不大于下一元素,则将数组视为排序。

@sample 样本. 生成. issorated. IS 分类多排不列亚雷样本. is scoted Double ArraySamples

### 8. Common

```kotlin
@SinceKotlin("2.4")
public fun BooleanArray.isSortedWith(comparator: Comparator<in Boolean>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6566)

如果数组中每个元素小于或等于 `true` 返回
以下列元素为单位,根据指定的`comparator`。

如果数组的元素少于两个元素,则返回`true`。

将按顺序用`Comparator.compare`对元素进行比较,如果对相邻元素的每一对,前一元素不大于下一元素,则将数组视为排序。

@sample 样本. 由 egrod. ssss 组成。Is Sorted Boolean Array 样本。

### 9. Common

```kotlin
@SinceKotlin("2.4")
public fun CharArray.isSortedWith(comparator: Comparator<in Char>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6586)

如果数组中每个元素小于或等于 `true` 返回
以下列元素为单位,根据指定的`comparator`。

如果数组的元素少于两个元素,则返回`true`。

将按顺序用`Comparator.compare`对元素进行比较,如果对相邻元素的每一对,前一元素不大于下一元素,则将数组视为排序。

与@sample样本的 混合

### 10. Common

```kotlin
@SinceKotlin("2.4")
public fun <T> Iterable<T>.isSortedWith(comparator: Comparator<in T>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1113)

如果收藏中的每一元素小于或等于按照指定的 `comparator` 计算的以下元素,则返回`true`。

如果收藏的元素少于两个,则返回`true`。

将按顺序用`Comparator.compare`对各元素进行比较,如果对相邻元素的每一对,前一元素不大于下一元素,则将认为收藏是分拣的。

请注意,结果取决于收藏的迭代顺序。 大约 `Iterable` 项执行的迭代顺序可能不稳定( 从一次引用改为下一次),在这种情况下,该函数可能会返回不一致的结果。

@sample 样本. 生成. issss sortedIterables 样本. 与

### 11. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun UIntArray.isSortedWith(comparator: Comparator<in UInt>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3151)

如果数组中每个元素小于或等于 `true` 返回
以下列元素为单位,根据指定的`comparator`。

如果数组的元素少于两个元素,则返回`true`。

将按顺序用`Comparator.compare`对元素进行比较,如果对相邻元素的每一对,前一元素不大于下一元素,则将数组视为排序。

@sample 样本. 生成. issorated. is sortedUint AraySamples. 与

### 12. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun ULongArray.isSortedWith(comparator: Comparator<in ULong>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3172)

如果数组中每个元素小于或等于 `true` 返回
以下列元素为单位,根据指定的`comparator`。

如果数组的元素少于两个元素,则返回`true`。

将按顺序用`Comparator.compare`对元素进行比较,如果对相邻元素的每一对,前一元素不大于下一元素,则将数组视为排序。

@sample 样本. 生成. issorated. IS 分类的Uong 阵列样本。

### 13. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun UByteArray.isSortedWith(comparator: Comparator<in UByte>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3193)

如果数组中每个元素小于或等于 `true` 返回
以下列元素为单位,根据指定的`comparator`。

如果数组的元素少于两个元素,则返回`true`。

将按顺序用`Comparator.compare`对元素进行比较,如果对相邻元素的每一对,前一元素不大于下一元素,则将数组视为排序。

@sample 样本. 由 egrod. ss 类集。Is SortedUByte Array 样本. is Sorted with

### 14. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun UShortArray.isSortedWith(comparator: Comparator<in UShort>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3214)

如果数组中每个元素小于或等于 `true` 返回
以下列元素为单位,根据指定的`comparator`。

如果数组的元素少于两个元素,则返回`true`。

将按顺序用`Comparator.compare`对元素进行比较,如果对相邻元素的每一对,前一元素不大于下一元素,则将数组视为排序。

与@sample样本的 排序

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(arrayOf<String>().isSortedWith(naturalOrder()))
    println(arrayOf("apple").isSortedWith(naturalOrder()))

    val sorted = arrayOf("apple", "banana", "cherry")
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = arrayOf("cherry", "banana", "apple")
    println(reversed.isSortedWith(reverseOrder()))

    val caseInsensitive = arrayOf("Apple", "banana", "Cherry")
    println(caseInsensitive.isSortedWith(String.CASE_INSENSITIVE_ORDER))

    val withNulls = arrayOf(null, "apple", "banana")
    println(withNulls.isSortedWith(nullsFirst(naturalOrder())))
    println(withNulls.isSortedWith(nullsLast(naturalOrder())))
}
```

```text title="输出"
true
true
true
false
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedArraySamples.kt#L42)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(byteArrayOf().isSortedWith(naturalOrder()))
    println(byteArrayOf(1).isSortedWith(naturalOrder()))

    val sorted = byteArrayOf(1, 2, 3, 4, 5)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = byteArrayOf(5, 4, 3, 2, 1)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedByteArraySamples.kt#L43)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(shortArrayOf().isSortedWith(naturalOrder()))
    println(shortArrayOf(1).isSortedWith(naturalOrder()))

    val sorted = shortArrayOf(1, 2, 3, 4, 5)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = shortArrayOf(5, 4, 3, 2, 1)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedShortArraySamples.kt#L43)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(intArrayOf().isSortedWith(naturalOrder()))
    println(intArrayOf(1).isSortedWith(naturalOrder()))

    val sorted = intArrayOf(1, 2, 3, 4, 5)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = intArrayOf(5, 4, 3, 2, 1)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIntArraySamples.kt#L43)

### 示例 5 · JVM

```kotlin title="示例 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(longArrayOf().isSortedWith(naturalOrder()))
    println(longArrayOf(1L).isSortedWith(naturalOrder()))

    val sorted = longArrayOf(1L, 2L, 3L, 4L, 5L)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = longArrayOf(5L, 4L, 3L, 2L, 1L)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedLongArraySamples.kt#L43)

### 示例 6 · JVM

```kotlin title="示例 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(floatArrayOf().isSortedWith(naturalOrder()))
    println(floatArrayOf(1.0f).isSortedWith(naturalOrder()))

    val sorted = floatArrayOf(1.0f, 2.5f, 3.14f)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = floatArrayOf(3.14f, 2.5f, 1.0f)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedFloatArraySamples.kt#L43)

### 示例 7 · JVM

```kotlin title="示例 7" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(doubleArrayOf().isSortedWith(naturalOrder()))
    println(doubleArrayOf(1.0).isSortedWith(naturalOrder()))

    val sorted = doubleArrayOf(1.0, 2.5, 3.14)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = doubleArrayOf(3.14, 2.5, 1.0)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedDoubleArraySamples.kt#L43)

### 示例 8 · JVM

```kotlin title="示例 8" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(booleanArrayOf().isSortedWith(naturalOrder()))
    println(booleanArrayOf(false).isSortedWith(naturalOrder()))

    val sorted = booleanArrayOf(false, false, true)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = booleanArrayOf(true, false, false)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedBooleanArraySamples.kt#L42)

### 示例 9 · JVM

```kotlin title="示例 9" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(charArrayOf().isSortedWith(naturalOrder()))
    println(charArrayOf('a').isSortedWith(naturalOrder()))

    val sorted = charArrayOf('a', 'b', 'c')
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = charArrayOf('c', 'b', 'a')
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedCharArraySamples.kt#L42)

### 示例 10 · JVM

```kotlin title="示例 10" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(listOf<String>().isSortedWith(naturalOrder()))
    println(listOf("apple").isSortedWith(naturalOrder()))

    val sorted = listOf("apple", "banana", "cherry")
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = listOf("cherry", "banana", "apple")
    println(reversed.isSortedWith(reverseOrder()))

    val caseInsensitive = listOf("Apple", "banana", "Cherry")
    println(caseInsensitive.isSortedWith(String.CASE_INSENSITIVE_ORDER))

    val withNulls = listOf(null, "apple", "banana")
    println(withNulls.isSortedWith(nullsFirst(naturalOrder())))
    println(withNulls.isSortedWith(nullsLast(naturalOrder())))
}
```

```text title="输出"
true
true
true
false
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIterablesSamples.kt#L42)

### 示例 11 · JVM

```kotlin title="示例 11" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(uintArrayOf().isSortedWith(naturalOrder()))
    println(uintArrayOf(1u).isSortedWith(naturalOrder()))

    val sorted = uintArrayOf(1u, 2u, 3u, 4u, 5u)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = uintArrayOf(5u, 4u, 3u, 2u, 1u)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUIntArraySamples.kt#L42)

### 示例 12 · JVM

```kotlin title="示例 12" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ulongArrayOf().isSortedWith(naturalOrder()))
    println(ulongArrayOf(1uL).isSortedWith(naturalOrder()))

    val sorted = ulongArrayOf(1uL, 2uL, 3uL, 4uL, 5uL)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = ulongArrayOf(5uL, 4uL, 3uL, 2uL, 1uL)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedULongArraySamples.kt#L42)

### 示例 13 · JVM

```kotlin title="示例 13" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ubyteArrayOf().isSortedWith(naturalOrder()))
    println(ubyteArrayOf(1u).isSortedWith(naturalOrder()))

    val sorted = ubyteArrayOf(1u, 2u, 3u, 4u, 5u)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = ubyteArrayOf(5u, 4u, 3u, 2u, 1u)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUByteArraySamples.kt#L42)

### 示例 14 · JVM

```kotlin title="示例 14" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ushortArrayOf().isSortedWith(naturalOrder()))
    println(ushortArrayOf(1u).isSortedWith(naturalOrder()))

    val sorted = ushortArrayOf(1u, 2u, 3u, 4u, 5u)
    println(sorted.isSortedWith(naturalOrder()))
    println(sorted.isSortedWith(reverseOrder()))

    val reversed = ushortArrayOf(5u, 4u, 3u, 2u, 1u)
    println(reversed.isSortedWith(reverseOrder()))
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUShortArraySamples.kt#L42)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
