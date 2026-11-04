# isSortedDescending

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果数组中每个元素根据其自然排序顺序大于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

将按顺序用`Comparable.compareTo`对元素进行比较,如果对每对相邻元素而言,前一元素不少于下一元素,则将数组按降序排序。

对于浮动点类型(`Double`、 `Float` ),`NaN`被认为大于任何其他价值(包括正无限),`-0.0`被认为低于`0.0`,与`Double.compareTo`和`Float.compareTo`一致。

@sample 样本. 生成. issorated. Iss 类组阵列样本.is SorttedDescering

??? note "查看英文原文"

    Returns `true` if each element in the array is greater than or equal
    to the following element according to their natural sort order.
    
    Returns `true` if the array has fewer than two elements.
    
    The elements are compared sequentially using `Comparable.compareTo`,
    and the array is considered sorted in descending order if for each
    pair of adjacent elements the preceding element is not less than the following one.
    
    For elements of floating-point types (`Double`, `Float`), `NaN` is considered greater
    than any other value (including positive infinity), and `-0.0` is considered less than `0.0`,
    consistent with `Double.compareTo` and `Float.compareTo`.
    
    @sample samples.generated.issorted.IsSortedArraySamples.isSortedDescending

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.4")
public fun <T : Comparable<T>> Array<out T>.isSortedDescending(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6237)

### 2. Common

```kotlin
@SinceKotlin("2.4")
public fun ByteArray.isSortedDescending(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6258)

如果数组中每个元素根据其自然排序顺序大于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每对相邻元素而言,前一元素不少于下一元素,则按下游顺序对这些元素进行顺序比较,并将数组视为按下游顺序排序。

@sample 样本. 由. ssssssss 生成。Is 类集Byte 阵列样本。is SorttedDescing

### 3. Common

```kotlin
@SinceKotlin("2.4")
public fun ShortArray.isSortedDescending(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6278)

如果数组中每个元素根据其自然排序顺序大于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每对相邻元素而言,前一元素不少于下一元素,则按下游顺序对这些元素进行顺序比较,并将数组视为按下游顺序排序。

@sample 样本. 由. sssssssss 类集的短线阵列样本。 is SorttedDesculting

### 4. Common

```kotlin
@SinceKotlin("2.4")
public fun IntArray.isSortedDescending(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6298)

如果数组中每个元素根据其自然排序顺序大于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每对相邻元素而言,前一元素不少于下一元素,则按下游顺序对这些元素进行顺序比较,并将数组视为按下游顺序排序。

@sample 样本. 由. sssssssssssorted IntAraySamples.issssssslatedDiscing 集中显示

### 5. Common

```kotlin
@SinceKotlin("2.4")
public fun LongArray.isSortedDescending(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6318)

如果数组中每个元素根据其自然排序顺序大于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每对相邻元素而言,前一元素不少于下一元素,则按下游顺序对这些元素进行顺序比较,并将数组视为按下游顺序排序。

@sample 样本. 由 esssssssssss 类组Long 阵列样本.isssssssledLong 拖拉样

### 6. Common

```kotlin
@SinceKotlin("2.4")
public fun FloatArray.isSortedDescending(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6338)

如果数组中每个元素根据其自然排序顺序大于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

将按顺序用`Float.compareTo`对元素进行比较,如果对每对相邻元素而言,前一元素不少于下一元素,则将数组按降序排序。

对于浮动点阵列,`NaN`被认为大于任何其他值(包括正无限),`-0.0`被认为低于`0.0`,与`Float.compareTo`一致。

@sample 样本. 由 ssortedFloat 阵列样本 。 is SorttedDescing

### 7. Common

```kotlin
@SinceKotlin("2.4")
public fun DoubleArray.isSortedDescending(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6362)

如果数组中每个元素根据其自然排序顺序大于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

将按顺序用`Double.compareTo`对元素进行比较,如果对每对相邻元素而言,前一元素不少于下一元素,则将数组按降序排序。

对于浮动点阵列,`NaN`被认为大于任何其他值(包括正无限),`-0.0`被认为低于`0.0`,与`Double.compareTo`一致。

@sample 样本. 由. ssssssssss 类集多排不列亚射线样本.isssssslatedDouble ArraySamples.isssslatedDescerting

### 8. Common

```kotlin
@SinceKotlin("2.4")
public fun BooleanArray.isSortedDescending(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6386)

如果数组中每个元素根据其自然排序顺序大于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每对相邻元素而言,前一元素不少于下一元素,则按下游顺序对这些元素进行顺序比较,并将数组视为按下游顺序排序。

@sample 样本. 由生成 。 IsS 类组 Boolean 阵列样本.is SorttedDescing

### 9. Common

```kotlin
@SinceKotlin("2.4")
public fun CharArray.isSortedDescending(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6406)

如果数组中每个元素根据其自然排序顺序大于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每对相邻元素而言,前一元素不少于下一元素,则按下游顺序对这些元素进行顺序比较,并将数组视为按下游顺序排序。

@sample 样本. 由 esssssssss 类集的夏夏阵列样本。 is SorttedDESLANSLATION 样本。

### 10. Common

```kotlin
@SinceKotlin("2.4")
public fun <T : Comparable<T>> Iterable<T>.isSortedDescending(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1087)

如果收藏中的每一元素根据其自然排序大于或等于下列元素,则返回`true`。

如果收藏的元素少于两个,则返回`true`。

将按顺序用`Comparable.compareTo`对各元素进行比较,如果对每对相邻元素而言,前一元素不少于下一元素,则将收藏按降序排序。

请注意,结果取决于收藏的迭代顺序。 大约 `Iterable` 项执行的迭代顺序可能不稳定( 从一次引用改为下一次),在这种情况下,该函数可能会返回不一致的结果。

对于浮动点类型(`Double`、 `Float` ),`NaN`被认为大于任何其他价值(包括正无限),`-0.0`被认为低于`0.0`,与`Double.compareTo`和`Float.compareTo`一致。

@sample 样本. 由. sssssssssssssssssssssssssssssssssssssslatedDESSSSSerting 样本。

### 11. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun UIntArray.isSortedDescending(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3067)

如果数组中每个元素根据其自然排序顺序大于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每对相邻元素而言,前一元素不少于下一元素,则按下游顺序对这些元素进行顺序比较,并将数组视为按下游顺序排序。

@sample 样本. 由生成. sssorted. is SortedUint AraySamples. is SorttedDescing 样本。 由 as 类组化的 亚光线样本 。

### 12. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun ULongArray.isSortedDescending(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3088)

如果数组中每个元素根据其自然排序顺序大于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每对相邻元素而言,前一元素不少于下一元素,则按下游顺序对这些元素进行顺序比较,并将数组视为按下游顺序排序。

@sample 样本. 由 ssssssortedUong 阵列样本.isssslatedDescing

### 13. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun UByteArray.isSortedDescending(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3109)

如果数组中每个元素根据其自然排序顺序大于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每对相邻元素而言,前一元素不少于下一元素,则按下游顺序对这些元素进行顺序比较,并将数组视为按下游顺序排序。

@sample 样本. 由 essssssss 类集Ubyte 阵列样本.is SorttedDescing

### 14. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public fun UShortArray.isSortedDescending(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3130)

如果数组中每个元素根据其自然排序顺序大于或等于以下元素,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

如果对每对相邻元素而言,前一元素不少于下一元素,则按下游顺序对这些元素进行顺序比较,并将数组视为按下游顺序排序。

@sample 样本. 由. ssssssssortedUShort 阵列样本.isssss sortedUSshortDraySamples.isssslatedDescing 样本。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(arrayOf<String>().isSortedDescending())
    println(arrayOf("cherry").isSortedDescending())

    val sorted = arrayOf("cherry", "banana", "apple")
    println(sorted.isSortedDescending())

    val unsorted = arrayOf("banana", "cherry", "apple")
    println(unsorted.isSortedDescending())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedArraySamples.kt#L30)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(byteArrayOf().isSortedDescending())
    println(byteArrayOf(5).isSortedDescending())

    val sorted = byteArrayOf(5, 4, 3, 2, 1)
    println(sorted.isSortedDescending())

    val unsorted = byteArrayOf(4, 5, 3, 2, 1)
    println(unsorted.isSortedDescending())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedByteArraySamples.kt#L31)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(shortArrayOf().isSortedDescending())
    println(shortArrayOf(5).isSortedDescending())

    val sorted = shortArrayOf(5, 4, 3, 2, 1)
    println(sorted.isSortedDescending())

    val unsorted = shortArrayOf(4, 5, 3, 2, 1)
    println(unsorted.isSortedDescending())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedShortArraySamples.kt#L31)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(intArrayOf().isSortedDescending())
    println(intArrayOf(5).isSortedDescending())

    val sorted = intArrayOf(5, 4, 3, 2, 1)
    println(sorted.isSortedDescending())

    val unsorted = intArrayOf(4, 5, 3, 2, 1)
    println(unsorted.isSortedDescending())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIntArraySamples.kt#L31)

### 示例 5 · JVM

```kotlin title="示例 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(longArrayOf().isSortedDescending())
    println(longArrayOf(5L).isSortedDescending())

    val sorted = longArrayOf(5L, 4L, 3L, 2L, 1L)
    println(sorted.isSortedDescending())

    val unsorted = longArrayOf(4L, 5L, 3L, 2L, 1L)
    println(unsorted.isSortedDescending())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedLongArraySamples.kt#L31)

### 示例 6 · JVM

```kotlin title="示例 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(floatArrayOf().isSortedDescending())
    println(floatArrayOf(3.14f).isSortedDescending())

    val sorted = floatArrayOf(3.14f, 2.5f, 1.0f)
    println(sorted.isSortedDescending())

    val unsorted = floatArrayOf(2.5f, 3.14f, 1.0f)
    println(unsorted.isSortedDescending())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedFloatArraySamples.kt#L31)

### 示例 7 · JVM

```kotlin title="示例 7" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(doubleArrayOf().isSortedDescending())
    println(doubleArrayOf(3.14).isSortedDescending())

    val sorted = doubleArrayOf(3.14, 2.5, 1.0)
    println(sorted.isSortedDescending())

    val unsorted = doubleArrayOf(2.5, 3.14, 1.0)
    println(unsorted.isSortedDescending())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedDoubleArraySamples.kt#L31)

### 示例 8 · JVM

```kotlin title="示例 8" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(booleanArrayOf().isSortedDescending())
    println(booleanArrayOf(true).isSortedDescending())

    val sorted = booleanArrayOf(true, false, false)
    println(sorted.isSortedDescending())

    val unsorted = booleanArrayOf(false, true, false)
    println(unsorted.isSortedDescending())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedBooleanArraySamples.kt#L30)

### 示例 9 · JVM

```kotlin title="示例 9" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(charArrayOf().isSortedDescending())
    println(charArrayOf('c').isSortedDescending())

    val sorted = charArrayOf('c', 'b', 'a')
    println(sorted.isSortedDescending())

    val unsorted = charArrayOf('b', 'c', 'a')
    println(unsorted.isSortedDescending())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedCharArraySamples.kt#L30)

### 示例 10 · JVM

```kotlin title="示例 10" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(listOf<String>().isSortedDescending())
    println(listOf("cherry").isSortedDescending())

    val sorted = listOf("cherry", "banana", "apple")
    println(sorted.isSortedDescending())

    val unsorted = listOf("banana", "cherry", "apple")
    println(unsorted.isSortedDescending())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIterablesSamples.kt#L30)

### 示例 11 · JVM

```kotlin title="示例 11" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(uintArrayOf().isSortedDescending())
    println(uintArrayOf(5u).isSortedDescending())

    val sorted = uintArrayOf(5u, 4u, 3u, 2u, 1u)
    println(sorted.isSortedDescending())

    val unsorted = uintArrayOf(4u, 5u, 3u, 2u, 1u)
    println(unsorted.isSortedDescending())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUIntArraySamples.kt#L30)

### 示例 12 · JVM

```kotlin title="示例 12" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ulongArrayOf().isSortedDescending())
    println(ulongArrayOf(5uL).isSortedDescending())

    val sorted = ulongArrayOf(5uL, 4uL, 3uL, 2uL, 1uL)
    println(sorted.isSortedDescending())

    val unsorted = ulongArrayOf(4uL, 5uL, 3uL, 2uL, 1uL)
    println(unsorted.isSortedDescending())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedULongArraySamples.kt#L30)

### 示例 13 · JVM

```kotlin title="示例 13" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ubyteArrayOf().isSortedDescending())
    println(ubyteArrayOf(5u).isSortedDescending())

    val sorted = ubyteArrayOf(5u, 4u, 3u, 2u, 1u)
    println(sorted.isSortedDescending())

    val unsorted = ubyteArrayOf(4u, 5u, 3u, 2u, 1u)
    println(unsorted.isSortedDescending())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUByteArraySamples.kt#L30)

### 示例 14 · JVM

```kotlin title="示例 14" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ushortArrayOf().isSortedDescending())
    println(ushortArrayOf(5u).isSortedDescending())

    val sorted = ushortArrayOf(5u, 4u, 3u, 2u, 1u)
    println(sorted.isSortedDescending())

    val unsorted = ushortArrayOf(4u, 5u, 3u, 2u, 1u)
    println(unsorted.isSortedDescending())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUShortArraySamples.kt#L30)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
