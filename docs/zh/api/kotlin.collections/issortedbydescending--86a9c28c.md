# isSortedByDescending

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果数组中的每一元素产生`selector`值,且该值大于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上方元素的`selector`值不少于下方元素的`selector`值,则该数组按下方顺序排序。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由. sssssssssss 类组阵列样本.issSortedByDiscing

??? note "查看英文原文"

    Returns `true` if each element in the array yields a `selector` value
    that is greater than or equal to the `selector` value of the following element
    according to the natural sort order of the selector values.
    
    Returns `true` if the array has fewer than two elements.
    
    The `selector` values of adjacent elements are compared sequentially using `compareValues`,
    and the array is considered sorted in descending order if for each pair
    of adjacent elements the `selector` value of the preceding element is not less
    than that of the following one.
    
    If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.
    
    @sample samples.generated.issorted.IsSortedArraySamples.isSortedByDescending

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <T, R : Comparable<R>> Array<out T>.isSortedByDescending(selector: (T) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5985)

### 2. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> ByteArray.isSortedByDescending(selector: (Byte) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6013)

如果数组中的每一元素产生`selector`值,且该值大于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上方元素的`selector`值不少于下方元素的`selector`值,则该数组按下方顺序排序。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由. ssssssss 分类的Byte 阵列样本。 is SortedByDiscing

### 3. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> ShortArray.isSortedByDescending(selector: (Short) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6041)

如果数组中的每一元素产生`selector`值,且该值大于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上方元素的`selector`值不少于下方元素的`selector`值,则该数组按下方顺序排序。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由. sssssssortedShort 阵列样本.isSortedByDiscing

### 4. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> IntArray.isSortedByDescending(selector: (Int) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6069)

如果数组中的每一元素产生`selector`值,且该值大于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上方元素的`selector`值不少于下方元素的`selector`值,则该数组按下方顺序排序。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由. ssssssssssorted IntAraySamples.issSortedByDiscing 类集

### 5. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> LongArray.isSortedByDescending(selector: (Long) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6097)

如果数组中的每一元素产生`selector`值,且该值大于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上方元素的`selector`值不少于下方元素的`selector`值,则该数组按下方顺序排序。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由生成的. issored. IsS 类组Long 阵列样本.is SortedByDiscing

### 6. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> FloatArray.isSortedByDescending(selector: (Float) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6125)

如果数组中的每一元素产生`selector`值,且该值大于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上方元素的`selector`值不少于下方元素的`selector`值,则该数组按下方顺序排序。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由. sssssssss 组成。Iss 组化浮阵阵列样本。is SortedByDiscing

### 7. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> DoubleArray.isSortedByDescending(selector: (Double) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6153)

如果数组中的每一元素产生`selector`值,且该值大于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上方元素的`selector`值不少于下方元素的`selector`值,则该数组按下方顺序排序。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由. sssssssssortedDouble 亚光样本.issSortedByDiscing

### 8. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> BooleanArray.isSortedByDescending(selector: (Boolean) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6181)

如果数组中的每一元素产生`selector`值,且该值大于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上方元素的`selector`值不少于下方元素的`selector`值,则该数组按下方顺序排序。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由生成 。 IsS 类组 Boolean 阵列样本. is SortedByDiscing

### 9. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> CharArray.isSortedByDescending(selector: (Char) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6209)

如果数组中的每一元素产生`selector`值,且该值大于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上方元素的`selector`值不少于下方元素的`selector`值,则该数组按下方顺序排序。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由 essssssortedCharAraySamples.iss sortedByDiscing 样本 由 ortedByDiscing 样本 由 ortedCharAraySamples 样本 和 esering 样本 生成

### 10. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <T, R : Comparable<R>> Iterable<T>.isSortedByDescending(selector: (T) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1047)

如果采集中的每个元素的值为`selector`,则返回`true`,如果根据选择值的自然排序,每个元素的值大于或等于以下元素的`selector`,则返回`true`。

如果收藏的元素少于两个,则返回`true`。

相邻元素的`selector`值按顺序使用`compareValues`进行比较,如果对相邻元素的每一对的上一个元素的`selector`值不低于下一个元素的`selector`值,则该采集量按下游顺序排序。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

请注意,结果取决于收藏的迭代顺序。 大约 `Iterable` 项执行的迭代顺序可能不稳定( 从一次引用改为下一次),在这种情况下,该函数可能会返回不一致的结果。

@sample 样本. 由. sssssssssssssssssssssssssssssssssssssslvedByDiscing sssssssssssssssssssssssssssslvedBySysdecing 。 生成的. isssssssserviced.

### 11. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public inline fun <R : Comparable<R>> UIntArray.isSortedByDescending(selector: (UInt) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2951)

如果数组中的每一元素产生`selector`值,且该值大于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上方元素的`selector`值不少于下方元素的`selector`值,则该数组按下方顺序排序。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由生成. sssortedunt 亚射线样本. is SorttedByDiscing

### 12. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public inline fun <R : Comparable<R>> ULongArray.isSortedByDescending(selector: (ULong) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2980)

如果数组中的每一元素产生`selector`值,且该值大于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上方元素的`selector`值不少于下方元素的`selector`值,则该数组按下方顺序排序。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由. ssssssss 排序的Uong 阵列样本。 is SortedByDiscing

### 13. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public inline fun <R : Comparable<R>> UByteArray.isSortedByDescending(selector: (UByte) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3009)

如果数组中的每一元素产生`selector`值,且该值大于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上方元素的`selector`值不少于下方元素的`selector`值,则该数组按下方顺序排序。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由 esssssss 类集Ubtyte 阵列样本.is SortedByDiscing

### 14. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public inline fun <R : Comparable<R>> UShortArray.isSortedByDescending(selector: (UShort) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3038)

如果数组中的每一元素产生`selector`值,且该值大于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上方元素的`selector`值不少于下方元素的`selector`值,则该数组按下方顺序排序。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由. sssssssoredUShort 阵列样本. is SortedByDiscing

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(arrayOf<String>().isSortedByDescending { it.length })
    println(arrayOf("aaa").isSortedByDescending { it.length })

    val values = arrayOf("aaa", "bb", "c")
    println(values.isSortedByDescending { it.length })
    println(values.isSortedByDescending { it })
    println(arrayOf("b", "a").isSortedByDescending { if (it == "a") null else it })
    println(arrayOf("aaa", "bb", null).isSortedByDescending { it?.length })
}
```

```text title="输出"
true
true
true
false
true
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedArraySamples.kt#L75)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(byteArrayOf().isSortedByDescending { it * it })
    println(byteArrayOf(5).isSortedByDescending { it * it })

    val values = byteArrayOf(5, -4, 3, -2, 1)
    println(values.isSortedByDescending { it * it })
    println(values.isSortedByDescending { abs(it.toInt()) })
    println(values.isSortedByDescending { it })
    println(byteArrayOf(2, 1).isSortedByDescending { if (it.toInt() == 1) null else it })
}
```

```text title="输出"
true
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedByteArraySamples.kt#L68)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(shortArrayOf().isSortedByDescending { it * it })
    println(shortArrayOf(5).isSortedByDescending { it * it })

    val values = shortArrayOf(5, -4, 3, -2, 1)
    println(values.isSortedByDescending { it * it })
    println(values.isSortedByDescending { abs(it.toInt()) })
    println(values.isSortedByDescending { it })
    println(shortArrayOf(2, 1).isSortedByDescending { if (it.toInt() == 1) null else it })
}
```

```text title="输出"
true
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedShortArraySamples.kt#L68)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(intArrayOf().isSortedByDescending { it * it })
    println(intArrayOf(5).isSortedByDescending { it * it })

    val values = intArrayOf(5, -4, 3, -2, 1)
    println(values.isSortedByDescending { it * it })
    println(values.isSortedByDescending { abs(it) })
    println(values.isSortedByDescending { it })
    println(intArrayOf(2, 1).isSortedByDescending { if (it == 1) null else it })
}
```

```text title="输出"
true
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIntArraySamples.kt#L68)

### 示例 5 · JVM

```kotlin title="示例 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(longArrayOf().isSortedByDescending { it * it })
    println(longArrayOf(5L).isSortedByDescending { it * it })

    val values = longArrayOf(5L, -4L, 3L, -2L, 1L)
    println(values.isSortedByDescending { it * it })
    println(values.isSortedByDescending { abs(it) })
    println(values.isSortedByDescending { it })
    println(longArrayOf(2L, 1L).isSortedByDescending { if (it == 1L) null else it })
}
```

```text title="输出"
true
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedLongArraySamples.kt#L68)

### 示例 6 · JVM

```kotlin title="示例 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(floatArrayOf().isSortedByDescending { it * it })
    println(floatArrayOf(2.0f).isSortedByDescending { it * it })

    val values = floatArrayOf(2.0f, -1.5f, 1.0f, -0.5f)
    println(values.isSortedByDescending { it * it })
    println(values.isSortedByDescending { abs(it) })
    println(values.isSortedByDescending { it })
    println(floatArrayOf(2.5f, 1.0f).isSortedByDescending { if (it == 1.0f) null else it })
}
```

```text title="输出"
true
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedFloatArraySamples.kt#L68)

### 示例 7 · JVM

```kotlin title="示例 7" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(doubleArrayOf().isSortedByDescending { it * it })
    println(doubleArrayOf(2.0).isSortedByDescending { it * it })

    val values = doubleArrayOf(2.0, -1.5, 1.0, -0.5)
    println(values.isSortedByDescending { it * it })
    println(values.isSortedByDescending { abs(it) })
    println(values.isSortedByDescending { it })
    println(doubleArrayOf(2.5, 1.0).isSortedByDescending { if (it == 1.0) null else it })
}
```

```text title="输出"
true
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedDoubleArraySamples.kt#L68)

### 示例 8 · JVM

```kotlin title="示例 8" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(booleanArrayOf().isSortedByDescending { it.compareTo(false) })
    println(booleanArrayOf(true).isSortedByDescending { it.compareTo(false) })

    val values = booleanArrayOf(true, false, false)
    println(values.isSortedByDescending { it.compareTo(false) })
    println(values.isSortedByDescending { it })
    println(values.isSortedByDescending { !it })
    println(booleanArrayOf(true, false).isSortedByDescending { if (it == false) null else it })
}
```

```text title="输出"
true
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedBooleanArraySamples.kt#L67)

### 示例 9 · JVM

```kotlin title="示例 9" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(charArrayOf().isSortedByDescending { it.uppercaseChar() })
    println(charArrayOf('C').isSortedByDescending { it.uppercaseChar() })

    val values = charArrayOf('C', 'b', 'A')
    println(values.isSortedByDescending { it.uppercaseChar() })
    println(values.isSortedByDescending { it.lowercaseChar() })
    println(values.isSortedByDescending { it })
    println(charArrayOf('b', 'a').isSortedByDescending { if (it == 'a') null else it })
}
```

```text title="输出"
true
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedCharArraySamples.kt#L67)

### 示例 10 · JVM

```kotlin title="示例 10" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(listOf<String>().isSortedByDescending { it.length })
    println(listOf("aaa").isSortedByDescending { it.length })

    val values = listOf("aaa", "bb", "c")
    println(values.isSortedByDescending { it.length })
    println(values.isSortedByDescending { it })
    println(listOf("b", "a").isSortedByDescending { if (it == "a") null else it })
    println(listOf("aaa", "bb", null).isSortedByDescending { it?.length })
}
```

```text title="输出"
true
true
true
false
true
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIterablesSamples.kt#L75)

### 示例 11 · JVM

```kotlin title="示例 11" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(uintArrayOf().isSortedByDescending { it % 3u })
    println(uintArrayOf(2u).isSortedByDescending { it % 3u })

    val values = uintArrayOf(2u, 4u, 1u, 3u)
    println(values.isSortedByDescending { it % 3u })
    println(values.isSortedByDescending { it })
    println(uintArrayOf(2u, 1u).isSortedByDescending { if (it == 1u) null else it })
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUIntArraySamples.kt#L66)

### 示例 12 · JVM

```kotlin title="示例 12" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ulongArrayOf().isSortedByDescending { it % 3uL })
    println(ulongArrayOf(2uL).isSortedByDescending { it % 3uL })

    val values = ulongArrayOf(2uL, 4uL, 1uL, 3uL)
    println(values.isSortedByDescending { it % 3uL })
    println(values.isSortedByDescending { it })
    println(ulongArrayOf(2uL, 1uL).isSortedByDescending { if (it == 1uL) null else it })
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedULongArraySamples.kt#L66)

### 示例 13 · JVM

```kotlin title="示例 13" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ubyteArrayOf().isSortedByDescending { it.toUInt() % 3u })
    println(ubyteArrayOf(2u).isSortedByDescending { it.toUInt() % 3u })

    val values = ubyteArrayOf(2u, 4u, 1u, 3u)
    println(values.isSortedByDescending { it.toUInt() % 3u })
    println(values.isSortedByDescending { it })
    println(ubyteArrayOf(2u, 1u).isSortedByDescending { if (it.toUInt() == 1u) null else it })
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUByteArraySamples.kt#L66)

### 示例 14 · JVM

```kotlin title="示例 14" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ushortArrayOf().isSortedByDescending { it.toUInt() % 3u })
    println(ushortArrayOf(2u).isSortedByDescending { it.toUInt() % 3u })

    val values = ushortArrayOf(2u, 4u, 1u, 3u)
    println(values.isSortedByDescending { it.toUInt() % 3u })
    println(values.isSortedByDescending { it })
    println(ushortArrayOf(2u, 1u).isSortedByDescending { if (it.toUInt() == 1u) null else it })
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUShortArraySamples.kt#L66)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
