# isSortedBy

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果数组中的每一元素产生`selector`值,且该值小于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上一个元素的`selector`值不大于下一个元素的`selector`值,则该数组被视为分拣。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 生成. issorated. ISS 类组阵列样本. is SortedBy

??? note "查看英文原文"

    Returns `true` if each element in the array yields a `selector` value
    that is less than or equal to the `selector` value of the following element
    according to the natural sort order of the selector values.
    
    Returns `true` if the array has fewer than two elements.
    
    The `selector` values of adjacent elements are compared sequentially using `compareValues`,
    and the array is considered sorted if for each pair of adjacent elements
    the `selector` value of the preceding element is not greater than that of the following one.
    
    If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.
    
    @sample samples.generated.issorted.IsSortedArraySamples.isSortedBy

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <T, R : Comparable<R>> Array<out T>.isSortedBy(selector: (T) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5742)

### 2. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> ByteArray.isSortedBy(selector: (Byte) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5769)

如果数组中的每一元素产生`selector`值,且该值小于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上一个元素的`selector`值不大于下一个元素的`selector`值,则该数组被视为分拣。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由 egrod. sss 组成。Is 类集Byte 阵列样本。is SortedBy

### 3. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> ShortArray.isSortedBy(selector: (Short) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5796)

如果数组中的每一元素产生`selector`值,且该值小于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上一个元素的`selector`值不大于下一个元素的`selector`值,则该数组被视为分拣。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由. ssssssss 类集。Is 类集ShortAraySamples.is SortedBy

### 4. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> IntArray.isSortedBy(selector: (Int) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5823)

如果数组中的每一元素产生`selector`值,且该值小于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上一个元素的`selector`值不大于下一个元素的`selector`值,则该数组被视为分拣。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由 egrod. sssss 类集的 内部阵列样本.is SortedBy

### 5. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> LongArray.isSortedBy(selector: (Long) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5850)

如果数组中的每一元素产生`selector`值,且该值小于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上一个元素的`selector`值不大于下一个元素的`selector`值,则该数组被视为分拣。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 生成. issorated. ISS 分类式长阵列样本.is SortedBy

### 6. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> FloatArray.isSortedBy(selector: (Float) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5877)

如果数组中的每一元素产生`selector`值,且该值小于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上一个元素的`selector`值不大于下一个元素的`selector`值,则该数组被视为分拣。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由 egrod. ssss 组成。Is SortedFloat 阵列样本.is SortedBy

### 7. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> DoubleArray.isSortedBy(selector: (Double) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5904)

如果数组中的每一元素产生`selector`值,且该值小于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上一个元素的`selector`值不大于下一个元素的`selector`值,则该数组被视为分拣。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由 essssssssss 类集多排不列亚雷样本.issssortedBy

### 8. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> BooleanArray.isSortedBy(selector: (Boolean) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5931)

如果数组中的每一元素产生`selector`值,且该值小于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上一个元素的`selector`值不大于下一个元素的`selector`值,则该数组被视为分拣。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由生成的. ssorted Boolean Array 样本.is SortedBy

### 9. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <R : Comparable<R>> CharArray.isSortedBy(selector: (Char) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5958)

如果数组中的每一元素产生`selector`值,且该值小于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上一个元素的`selector`值不大于下一个元素的`selector`值,则该数组被视为分拣。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由 egrod. ssss 组成。Is SortedCharAray 样本.is SortedBy

### 10. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <T, R : Comparable<R>> Iterable<T>.isSortedBy(selector: (T) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1010)

如果采集中的每个元素的值为`selector`,则返回`true`,如果根据选择值的自然排序,每个元素的值低于或等于以下元素的`selector`,则返回`true`。

如果收藏的元素少于两个,则返回`true`。

相邻元素的`selector`值按顺序使用`compareValues`进行比较,如果对相邻元素的每一对的上一个元素的`selector`值不大于下一个元素的`selector`值,则该采集被视为分类。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

请注意,结果取决于收藏的迭代顺序。 大约 `Iterable` 项执行的迭代顺序可能不稳定( 从一次引用改为下一次),在这种情况下,该函数可能会返回不一致的结果。

@sample 样本. 生成. is sortedBy.

### 11. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public inline fun <R : Comparable<R>> UIntArray.isSortedBy(selector: (UInt) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2839)

如果数组中的每一元素产生`selector`值,且该值小于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上一个元素的`selector`值不大于下一个元素的`selector`值,则该数组被视为分拣。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 生成. issorated. is sortedBy 类组的 类组半半成单体 Aray 样本.

### 12. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public inline fun <R : Comparable<R>> ULongArray.isSortedBy(selector: (ULong) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2867)

如果数组中的每一元素产生`selector`值,且该值小于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上一个元素的`selector`值不大于下一个元素的`selector`值,则该数组被视为分拣。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由 egrod. ssss 分类为 Uong 阵列样本.is SortedBy

### 13. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public inline fun <R : Comparable<R>> UByteArray.isSortedBy(selector: (UByte) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2895)

如果数组中的每一元素产生`selector`值,且该值小于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上一个元素的`selector`值不大于下一个元素的`selector`值,则该数组被视为分拣。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由 egrod. ss 类集成的 ABBYte 阵列样本.is SortedBy

### 14. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalUnsignedTypes
public inline fun <R : Comparable<R>> UShortArray.isSortedBy(selector: (UShort) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2923)

如果数组中的每一元素产生`selector`值,且该值小于或等于以下元素的`selector`值,则返回`true`。

如果数组的元素少于两个元素,则返回`true`。

相邻元素的`selector`值按顺序用`compareValues`进行比较,如果对相邻元素的每一对的上一个元素的`selector`值不大于下一个元素的`selector`值,则该数组被视为分拣。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

@sample 样本. 由. ssssssssortedUShort 阵列样本.isssortedBy

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(arrayOf<String>().isSortedBy { it.length })
    println(arrayOf("c").isSortedBy { it.length })

    val values = arrayOf("c", "bb", "aaa")
    println(values.isSortedBy { it.length })
    println(values.isSortedBy { it })
    println(arrayOf("a", "b").isSortedBy { if (it == "a") null else it })
    println(arrayOf(null, "a", "b").isSortedBy { it })
    println(arrayOf(null, "c", "bb").isSortedBy { it?.length })
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
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedArraySamples.kt#L62)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(byteArrayOf().isSortedBy { it * it })
    println(byteArrayOf(1).isSortedBy { it * it })

    val values = byteArrayOf(1, -2, 3, -4, 5)
    println(values.isSortedBy { it * it })
    println(values.isSortedBy { abs(it.toInt()) })
    println(values.isSortedBy { it })
    println(byteArrayOf(1, 2).isSortedBy { if (it.toInt() == 1) null else it })
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

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedByteArraySamples.kt#L56)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(shortArrayOf().isSortedBy { it * it })
    println(shortArrayOf(1).isSortedBy { it * it })

    val values = shortArrayOf(1, -2, 3, -4, 5)
    println(values.isSortedBy { it * it })
    println(values.isSortedBy { abs(it.toInt()) })
    println(values.isSortedBy { it })
    println(shortArrayOf(1, 2).isSortedBy { if (it.toInt() == 1) null else it })
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

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedShortArraySamples.kt#L56)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(intArrayOf().isSortedBy { it * it })
    println(intArrayOf(1).isSortedBy { it * it })

    val values = intArrayOf(1, -2, 3, -4, 5)
    println(values.isSortedBy { it * it })
    println(values.isSortedBy { abs(it) })
    println(values.isSortedBy { it })
    println(intArrayOf(1, 2).isSortedBy { if (it == 1) null else it })
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

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIntArraySamples.kt#L56)

### 示例 5 · JVM

```kotlin title="示例 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(longArrayOf().isSortedBy { it * it })
    println(longArrayOf(1L).isSortedBy { it * it })

    val values = longArrayOf(1L, -2L, 3L, -4L, 5L)
    println(values.isSortedBy { it * it })
    println(values.isSortedBy { abs(it) })
    println(values.isSortedBy { it })
    println(longArrayOf(1L, 2L).isSortedBy { if (it == 1L) null else it })
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

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedLongArraySamples.kt#L56)

### 示例 6 · JVM

```kotlin title="示例 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(floatArrayOf().isSortedBy { it * it })
    println(floatArrayOf(-0.5f).isSortedBy { it * it })

    val values = floatArrayOf(-0.5f, 1.0f, -1.5f, 2.0f)
    println(values.isSortedBy { it * it })
    println(values.isSortedBy { abs(it) })
    println(values.isSortedBy { it })
    println(floatArrayOf(1.0f, 2.5f).isSortedBy { if (it == 1.0f) null else it })
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

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedFloatArraySamples.kt#L56)

### 示例 7 · JVM

```kotlin title="示例 7" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(doubleArrayOf().isSortedBy { it * it })
    println(doubleArrayOf(-0.5).isSortedBy { it * it })

    val values = doubleArrayOf(-0.5, 1.0, -1.5, 2.0)
    println(values.isSortedBy { it * it })
    println(values.isSortedBy { abs(it) })
    println(values.isSortedBy { it })
    println(doubleArrayOf(1.0, 2.5).isSortedBy { if (it == 1.0) null else it })
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

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedDoubleArraySamples.kt#L56)

### 示例 8 · JVM

```kotlin title="示例 8" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(booleanArrayOf().isSortedBy { it.compareTo(false) })
    println(booleanArrayOf(false).isSortedBy { it.compareTo(false) })

    val values = booleanArrayOf(false, false, true)
    println(values.isSortedBy { it.compareTo(false) })
    println(values.isSortedBy { it })
    println(values.isSortedBy { !it })
    println(booleanArrayOf(false, true).isSortedBy { if (it == false) null else it })
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

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedBooleanArraySamples.kt#L55)

### 示例 9 · JVM

```kotlin title="示例 9" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(charArrayOf().isSortedBy { it.uppercaseChar() })
    println(charArrayOf('A').isSortedBy { it.uppercaseChar() })

    val values = charArrayOf('A', 'b', 'C')
    println(values.isSortedBy { it.uppercaseChar() })
    println(values.isSortedBy { it.lowercaseChar() })
    println(values.isSortedBy { it })
    println(charArrayOf('a', 'b').isSortedBy { if (it == 'a') null else it })
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

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedCharArraySamples.kt#L55)

### 示例 10 · JVM

```kotlin title="示例 10" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(listOf<String>().isSortedBy { it.length })
    println(listOf("c").isSortedBy { it.length })

    val values = listOf("c", "bb", "aaa")
    println(values.isSortedBy { it.length })
    println(values.isSortedBy { it })
    println(listOf("a", "b").isSortedBy { if (it == "a") null else it })
    println(listOf(null, "a", "b").isSortedBy { it })
    println(listOf(null, "c", "bb").isSortedBy { it?.length })
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
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedIterablesSamples.kt#L62)

### 示例 11 · JVM

```kotlin title="示例 11" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(uintArrayOf().isSortedBy { it % 3u })
    println(uintArrayOf(3u).isSortedBy { it % 3u })

    val values = uintArrayOf(3u, 1u, 4u, 2u)
    println(values.isSortedBy { it % 3u })
    println(values.isSortedBy { it })
    println(uintArrayOf(1u, 2u).isSortedBy { if (it == 1u) null else it })
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUIntArraySamples.kt#L55)

### 示例 12 · JVM

```kotlin title="示例 12" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ulongArrayOf().isSortedBy { it % 3uL })
    println(ulongArrayOf(3uL).isSortedBy { it % 3uL })

    val values = ulongArrayOf(3uL, 1uL, 4uL, 2uL)
    println(values.isSortedBy { it % 3uL })
    println(values.isSortedBy { it })
    println(ulongArrayOf(1uL, 2uL).isSortedBy { if (it == 1uL) null else it })
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedULongArraySamples.kt#L55)

### 示例 13 · JVM

```kotlin title="示例 13" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ubyteArrayOf().isSortedBy { it.toUInt() % 3u })
    println(ubyteArrayOf(3u).isSortedBy { it.toUInt() % 3u })

    val values = ubyteArrayOf(3u, 1u, 4u, 2u)
    println(values.isSortedBy { it.toUInt() % 3u })
    println(values.isSortedBy { it })
    println(ubyteArrayOf(1u, 2u).isSortedBy { if (it.toUInt() == 1u) null else it })
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUByteArraySamples.kt#L55)

### 示例 14 · JVM

```kotlin title="示例 14" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ushortArrayOf().isSortedBy { it.toUInt() % 3u })
    println(ushortArrayOf(3u).isSortedBy { it.toUInt() % 3u })

    val values = ushortArrayOf(3u, 1u, 4u, 2u)
    println(values.isSortedBy { it.toUInt() % 3u })
    println(values.isSortedBy { it })
    println(ushortArrayOf(1u, 2u).isSortedBy { if (it.toUInt() == 1u) null else it })
}
```

```text title="输出"
true
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedUShortArraySamples.kt#L55)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
