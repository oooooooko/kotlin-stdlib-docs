# isSorted

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果数组中每个元素根据其自然排序顺序小于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

将按顺序用`Comparable.compareTo`对元素进行比较,如果对相邻元素的每一对,前一元素不大于下一元素,则将数组视为排序。

对于浮动点类型(`Double`、 `Float` ),`NaN`被认为大于任何其他价值(包括正无限),`-0.0`被认为低于`0.0`,与`Double.compareTo`和`Float.compareTo`一致。

@sample 样本. 生成. issorated. IS 类组阵列样本. is sorted

??? note "查看英文原文"

    Returns `true` if each element in the array is less than or equal
    to the following element according to their natural sort order.
    
    Returns `true` if the array has fewer than two elements.
    
    The elements are compared sequentially using `Comparable.compareTo`,
    and the array is considered sorted if for each pair of adjacent elements
    the preceding element is not greater than the following one.
    
    For elements of floating-point types (`Double`, `Float`), `NaN` is considered greater
    than any other value (including positive infinity), and `-0.0` is considered less than `0.0`,
    consistent with `Double.compareTo` and `Float.compareTo`.
    
    @sample samples.generated.issorted.IsSortedArraySamples.isSorted

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.4")
public fun <T : Comparable<T>> Array<out T>.isSorted(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5553)

### 2. Common

```kotlin
@SinceKotlin("2.4")
public fun ByteArray.isSorted(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5574)

如果数组中每个元素根据其自然排序顺序小于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每一对相邻元素的上一个元素不大于下一个元素,则按顺序比较各元素,并视为对数组进行排序。

@sample 样本. 由 egrod. sss 分类产生。Is 类集Byte 阵列样本。is SortedByte AraySamples.is

### 3. Common

```kotlin
@SinceKotlin("2.4")
public fun ShortArray.isSorted(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5594)

如果数组中每个元素根据其自然排序顺序小于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每一对相邻元素的上一个元素不大于下一个元素,则按顺序比较各元素,并视为对数组进行排序。

@sample 样本. 由. sss分类产生。Is 类集短阵列样本.is 分类

### 4. Common

```kotlin
@SinceKotlin("2.4")
public fun IntArray.isSorted(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5614)

如果数组中每个元素根据其自然排序顺序小于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每一对相邻元素的上一个元素不大于下一个元素,则按顺序比较各元素,并视为对数组进行排序。

@sample 样本. 生成. issorated. Is 分类的 IntAray 样本. is sorted

### 5. Common

```kotlin
@SinceKotlin("2.4")
public fun LongArray.isSorted(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5634)

如果数组中每个元素根据其自然排序顺序小于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每一对相邻元素的上一个元素不大于下一个元素,则按顺序比较各元素,并视为对数组进行排序。

@sample 样本. 生成. issored. IsS 分类式长阵列样本.is 分类式

### 6. Common

```kotlin
@SinceKotlin("2.4")
public fun FloatArray.isSorted(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5654)

如果数组中每个元素根据其自然排序顺序小于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

将按顺序用`Float.compareTo`对元素进行比较,如果对相邻元素的每一对,前一元素不大于下一元素,则将数组视为排序。

对于浮动点阵列,`NaN`被认为大于任何其他值(包括正无限),`-0.0`被认为低于`0.0`,与`Float.compareTo`一致。

@sample 样本. 由 egrod. sssss 生成。Is SortedFloat 阵列样本.is Sorted

### 7. Common

```kotlin
@SinceKotlin("2.4")
public fun DoubleArray.isSorted(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5678)

如果数组中每个元素根据其自然排序顺序小于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

将按顺序用`Double.compareTo`对元素进行比较,如果对相邻元素的每一对,前一元素不大于下一元素,则将数组视为排序。

对于浮动点阵列,`NaN`被认为大于任何其他值(包括正无限),`-0.0`被认为低于`0.0`,与`Double.compareTo`一致。

@sample 样本. 生成. issorated. IS 分类多排多排亚性阵列样本.is 分类

### 8. Common

```kotlin
@SinceKotlin("2.4")
public fun BooleanArray.isSorted(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5702)

如果数组中每个元素根据其自然排序顺序小于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每一对相邻元素的上一个元素不大于下一个元素,则按顺序比较各元素,并视为对数组进行排序。

@sample 样本. 由生成的. 分类。 IsS 类组 Boolean 阵列样本. is sorted

### 9. Common

```kotlin
@SinceKotlin("2.4")
public fun CharArray.isSorted(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5722)

如果数组中每个元素根据其自然排序顺序小于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每一对相邻元素的上一个元素不大于下一个元素,则按顺序比较各元素,并视为对数组进行排序。

@sample 样本. 由 egrod. ssss 生成。Is SortedCharAray 样本.is Sorted

### 10. Common

```kotlin
@SinceKotlin("2.4")
public fun <T : Comparable<T>> Iterable<T>.isSorted(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L984)

如果收藏中的每一元素根据其自然种类顺序少于或等于下列元素,则返回`true`。

如果收藏的元素少于两个,则返回`true`。

将按顺序用`Comparable.compareTo`对各元素进行比较,如果对相邻元素的每一对,前一元素不大于下一元素,则将认为收藏是分拣的。

请注意,结果取决于收藏的迭代顺序。 大约 `Iterable` 项执行的迭代顺序可能不稳定( 从一次引用改为下一次),在这种情况下,该函数可能会返回不一致的结果。

对于浮动点类型(`Double`、 `Float` ),`NaN`被认为大于任何其他价值(包括正无限),`-0.0`被认为低于`0.0`,与`Double.compareTo`和`Float.compareTo`一致。

@sample 样本. 生成. isssssss 类集。Iss SOTIDEIE可选物品样本. is SOTITED

### 11. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun UIntArray.isSorted(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2755)

如果数组中每个元素根据其自然排序顺序小于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每一对相邻元素的上一个元素不大于下一个元素,则按顺序比较各元素,并视为对数组进行排序。

@sample 样本. 生成. issored. is sorted

### 12. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun ULongArray.isSorted(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2776)

如果数组中每个元素根据其自然排序顺序小于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每一对相邻元素的上一个元素不大于下一个元素,则按顺序比较各元素,并视为对数组进行排序。

@sample 样本. 生成. issorated. IS 分类的Uong 阵列样本。

### 13. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun UByteArray.isSorted(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2797)

如果数组中每个元素根据其自然排序顺序小于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每一对相邻元素的上一个元素不大于下一个元素,则按顺序比较各元素,并视为对数组进行排序。

@sample 样本. 由 egrod. sss 组成。Is SortedUByte Array 样本.is Sorted

### 14. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun UShortArray.isSorted(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2818)

如果数组中每个元素根据其自然排序顺序小于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每一对相邻元素的上一个元素不大于下一个元素,则按顺序比较各元素,并视为对数组进行排序。

@sample 样本. 生成. issored. Is Sorted Ushort 阵列样本. is Sorted

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(arrayOf<String>().isSorted())
    println(arrayOf("apple").isSorted())

    val sorted = arrayOf("apple", "banana", "cherry")
    println(sorted.isSorted())

    val unsorted = arrayOf("banana", "apple", "cherry")
    println(unsorted.isSorted())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedArraySamples.kt#L18)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(byteArrayOf().isSorted())
    println(byteArrayOf(1).isSorted())

    val sorted = byteArrayOf(1, 2, 3, 4, 5)
    println(sorted.isSorted())

    val unsorted = byteArrayOf(2, 1, 3, 4, 5)
    println(unsorted.isSorted())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedByteArraySamples.kt#L19)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(shortArrayOf().isSorted())
    println(shortArrayOf(1).isSorted())

    val sorted = shortArrayOf(1, 2, 3, 4, 5)
    println(sorted.isSorted())

    val unsorted = shortArrayOf(2, 1, 3, 4, 5)
    println(unsorted.isSorted())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedShortArraySamples.kt#L19)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(intArrayOf().isSorted())
    println(intArrayOf(1).isSorted())

    val sorted = intArrayOf(1, 2, 3, 4, 5)
    println(sorted.isSorted())

    val unsorted = intArrayOf(2, 1, 3, 4, 5)
    println(unsorted.isSorted())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIntArraySamples.kt#L19)

### 示例 5 · JVM

```kotlin title="示例 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(longArrayOf().isSorted())
    println(longArrayOf(1L).isSorted())

    val sorted = longArrayOf(1L, 2L, 3L, 4L, 5L)
    println(sorted.isSorted())

    val unsorted = longArrayOf(2L, 1L, 3L, 4L, 5L)
    println(unsorted.isSorted())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedLongArraySamples.kt#L19)

### 示例 6 · JVM

```kotlin title="示例 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(floatArrayOf().isSorted())
    println(floatArrayOf(1.0f).isSorted())

    val sorted = floatArrayOf(1.0f, 2.5f, 3.14f)
    println(sorted.isSorted())

    val unsorted = floatArrayOf(2.5f, 1.0f, 3.14f)
    println(unsorted.isSorted())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedFloatArraySamples.kt#L19)

### 示例 7 · JVM

```kotlin title="示例 7" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(doubleArrayOf().isSorted())
    println(doubleArrayOf(1.0).isSorted())

    val sorted = doubleArrayOf(1.0, 2.5, 3.14)
    println(sorted.isSorted())

    val unsorted = doubleArrayOf(2.5, 1.0, 3.14)
    println(unsorted.isSorted())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedDoubleArraySamples.kt#L19)

### 示例 8 · JVM

```kotlin title="示例 8" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(booleanArrayOf().isSorted())
    println(booleanArrayOf(false).isSorted())

    val sorted = booleanArrayOf(false, false, true)
    println(sorted.isSorted())

    val unsorted = booleanArrayOf(false, true, false)
    println(unsorted.isSorted())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedBooleanArraySamples.kt#L18)

### 示例 9 · JVM

```kotlin title="示例 9" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(charArrayOf().isSorted())
    println(charArrayOf('a').isSorted())

    val sorted = charArrayOf('a', 'b', 'c')
    println(sorted.isSorted())

    val unsorted = charArrayOf('b', 'a', 'c')
    println(unsorted.isSorted())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedCharArraySamples.kt#L18)

### 示例 10 · JVM

```kotlin title="示例 10" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(listOf<String>().isSorted())
    println(listOf("apple").isSorted())

    val sorted = listOf("apple", "banana", "cherry")
    println(sorted.isSorted())

    val unsorted = listOf("banana", "apple", "cherry")
    println(unsorted.isSorted())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIterablesSamples.kt#L18)

### 示例 11 · JVM

```kotlin title="示例 11" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(uintArrayOf().isSorted())
    println(uintArrayOf(1u).isSorted())

    val sorted = uintArrayOf(1u, 2u, 3u, 4u, 5u)
    println(sorted.isSorted())

    val unsorted = uintArrayOf(2u, 1u, 3u, 4u, 5u)
    println(unsorted.isSorted())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUIntArraySamples.kt#L18)

### 示例 12 · JVM

```kotlin title="示例 12" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ulongArrayOf().isSorted())
    println(ulongArrayOf(1uL).isSorted())

    val sorted = ulongArrayOf(1uL, 2uL, 3uL, 4uL, 5uL)
    println(sorted.isSorted())

    val unsorted = ulongArrayOf(2uL, 1uL, 3uL, 4uL, 5uL)
    println(unsorted.isSorted())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedULongArraySamples.kt#L18)

### 示例 13 · JVM

```kotlin title="示例 13" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ubyteArrayOf().isSorted())
    println(ubyteArrayOf(1u).isSorted())

    val sorted = ubyteArrayOf(1u, 2u, 3u, 4u, 5u)
    println(sorted.isSorted())

    val unsorted = ubyteArrayOf(2u, 1u, 3u, 4u, 5u)
    println(unsorted.isSorted())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUByteArraySamples.kt#L18)

### 示例 14 · JVM

```kotlin title="示例 14" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ushortArrayOf().isSorted())
    println(ushortArrayOf(1u).isSorted())

    val sorted = ushortArrayOf(1u, 2u, 3u, 4u, 5u)
    println(sorted.isSorted())

    val unsorted = ushortArrayOf(2u, 1u, 3u, 4u, 5u)
    println(unsorted.isSorted())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUShortArraySamples.kt#L18)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
