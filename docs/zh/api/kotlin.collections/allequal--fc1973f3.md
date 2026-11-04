# allEqual

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果数组中的所有元素彼此相等,则返回 `true` 。

返回`true`的空数组。

以结构平等(`==`)按顺序比较这些要素,如果第一个要素等于随后的每个要素,所有要素都被视为平等。

对于浮动点类型( `Double` , `Float` ),`NaN` 的值为 `NaN` ,`-0.0`的值为`Double.equals`和`Float.equals`,不等于`0.0`。

@sample 样本. 生成. 等同。 所有平面阵列样本. allEqual

??? note "查看英文原文"

    Returns `true` if all elements in the array are equal to each other.
    
    Returns `true` for an empty array.
    
    The elements are compared sequentially using structural equality (`==`),
    and all elements are considered equal if the first element equals
    every subsequent element.
    
    For elements of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
    and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.
    
    @sample samples.generated.allequal.AllEqualArraySamples.allEqual

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun <T> Array<out T>.allEqual(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14718)

### 2. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun ByteArray.allEqual(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14743)

如果数组中的所有元素彼此相等,则返回 `true` 。

返回`true`的空数组。

以结构平等(`==`)按顺序比较这些要素,如果第一个要素等于随后的每个要素,所有要素都被视为平等。

@sample 样本. 生成. eall等。 所有平基- yte AraySamples.allEqual

### 3. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun ShortArray.allEqual(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14765)

如果数组中的所有元素彼此相等,则返回 `true` 。

返回`true`的空数组。

以结构平等(`==`)按顺序比较这些要素,如果第一个要素等于随后的每个要素,所有要素都被视为平等。

@sample 样本. 生成. 等同。 所有等同的短光电阵列样本。 allEqual

### 4. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun IntArray.allEqual(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14787)

如果数组中的所有元素彼此相等,则返回 `true` 。

返回`true`的空数组。

以结构平等(`==`)按顺序比较这些要素,如果第一个要素等于随后的每个要素,所有要素都被视为平等。

@sample 样本. 生成. eall相等。 全部平整阵列样本. allEqual

### 5. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun LongArray.allEqual(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14809)

如果数组中的所有元素彼此相等,则返回 `true` 。

返回`true`的空数组。

以结构平等(`==`)按顺序比较这些要素,如果第一个要素等于随后的每个要素,所有要素都被视为平等。

@sample 样本. 生成. 等同。 AllEqualLongArraySamples.allEqual

### 6. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun FloatArray.allEqual(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14831)

如果数组中的所有元素彼此相等,则返回 `true` 。

返回`true`的空数组。

以与`Float.equals`一致的平等语义按顺序比较这些元素,如果第一个元素等于随后的每一个元素,所有元素都被视为平等。

`NaN` 被认为等于 `NaN` ,`-0.0`被认为不等于 `0.0` ,与`Float.equals`一致。

@sample 样本. 生成. 等同。 所有平面面阵列阵列样本. allEqual

### 7. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun DoubleArray.allEqual(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14856)

如果数组中的所有元素彼此相等,则返回 `true` 。

返回`true`的空数组。

以与`Double.equals`一致的平等语义按顺序比较这些元素,如果第一个元素等于随后的每一个元素,所有元素都被视为平等。

`NaN` 被认为等于 `NaN` ,`-0.0`被认为不等于 `0.0` ,与`Double.equals`一致。

@sample 样本. 生成. 等同。 所有等同的多相相异的AraySamples.allEqual

### 8. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun BooleanArray.allEqual(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14881)

如果数组中的所有元素彼此相等,则返回 `true` 。

返回`true`的空数组。

以结构平等(`==`)按顺序比较这些要素,如果第一个要素等于随后的每个要素,所有要素都被视为平等。

@sample 样本. 生成. 等同。

### 9. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun CharArray.allEqual(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14903)

如果数组中的所有元素彼此相等,则返回 `true` 。

返回`true`的空数组。

以结构平等(`==`)按顺序比较这些要素,如果第一个要素等于随后的每个要素,所有要素都被视为平等。

@sample 样本. 生成. 等同。 AllEqualCharAraySamples.allEqual

### 10. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun <T> Iterable<T>.allEqual(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2009)

如果收藏中的所有元素彼此相等,则返回`true`。

空收藏返回`true`。

以结构平等(`==`)按顺序比较这些要素,如果第一个要素等于随后的每个要素,所有要素都被视为平等。

对于浮动点类型( `Double` , `Float` ),`NaN` 的值为 `NaN` ,`-0.0`的值为`Double.equals`和`Float.equals`,不等于`0.0`。

@sample 样本. 生成. 等同。 所有平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、 平等、

### 11. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public fun UIntArray.allEqual(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6243)

如果数组中的所有元素彼此相等,则返回 `true` 。

返回`true`的空数组。

以结构平等(`==`)按顺序比较这些要素,如果第一个要素等于随后的每个要素,所有要素都被视为平等。

@sample 样本. 生成. equality. 所有等同的 平面阵列样本.allEqual

### 12. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public fun ULongArray.allEqual(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6266)

如果数组中的所有元素彼此相等,则返回 `true` 。

返回`true`的空数组。

以结构平等(`==`)按顺序比较这些要素,如果第一个要素等于随后的每个要素,所有要素都被视为平等。

@sample 样本. 生成. eall等。 AllEqualULongArraySamples.allEqual

### 13. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public fun UByteArray.allEqual(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6289)

如果数组中的所有元素彼此相等,则返回 `true` 。

返回`true`的空数组。

以结构平等(`==`)按顺序比较这些要素,如果第一个要素等于随后的每个要素,所有要素都被视为平等。

@sample 样本. 生成. 等同。 AllEqualUByte ArraySamples.allEqual

### 14. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public fun UShortArray.allEqual(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6312)

如果数组中的所有元素彼此相等,则返回 `true` 。

返回`true`的空数组。

以结构平等(`==`)按顺序比较这些要素,如果第一个要素等于随后的每个要素,所有要素都被视为平等。

@sample 样本. 生成. 等同。 AllEqualUShort ArraySamples.allEqual

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(arrayOf<String>().allEqual())
    println(arrayOf("apple").allEqual())

    val sameValues = arrayOf("apple", "apple", "apple")
    println(sameValues.allEqual())

    val mixedValues = arrayOf("apple", "apple", "orange")
    println(mixedValues.allEqual())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualArraySamples.kt#L18)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(byteArrayOf().allEqual())
    println(byteArrayOf(1).allEqual())

    val sameValues = byteArrayOf(1, 1, 1)
    println(sameValues.allEqual())

    val mixedValues = byteArrayOf(1, 1, 2)
    println(mixedValues.allEqual())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualByteArraySamples.kt#L19)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(shortArrayOf().allEqual())
    println(shortArrayOf(1).allEqual())

    val sameValues = shortArrayOf(1, 1, 1)
    println(sameValues.allEqual())

    val mixedValues = shortArrayOf(1, 1, 2)
    println(mixedValues.allEqual())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualShortArraySamples.kt#L19)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(intArrayOf().allEqual())
    println(intArrayOf(1).allEqual())

    val sameValues = intArrayOf(1, 1, 1)
    println(sameValues.allEqual())

    val mixedValues = intArrayOf(1, 1, 2)
    println(mixedValues.allEqual())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualIntArraySamples.kt#L19)

### 示例 5 · JVM

```kotlin title="示例 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(longArrayOf().allEqual())
    println(longArrayOf(1L).allEqual())

    val sameValues = longArrayOf(1L, 1L, 1L)
    println(sameValues.allEqual())

    val mixedValues = longArrayOf(1L, 1L, 2L)
    println(mixedValues.allEqual())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualLongArraySamples.kt#L19)

### 示例 6 · JVM

```kotlin title="示例 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(floatArrayOf().allEqual())
    println(floatArrayOf(1.0f).allEqual())

    val sameValues = floatArrayOf(1.0f, 1.0f, 1.0f)
    println(sameValues.allEqual())

    val mixedValues = floatArrayOf(1.0f, 1.0f, 2.0f)
    println(mixedValues.allEqual())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualFloatArraySamples.kt#L19)

### 示例 7 · JVM

```kotlin title="示例 7" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(doubleArrayOf().allEqual())
    println(doubleArrayOf(1.0).allEqual())

    val sameValues = doubleArrayOf(1.0, 1.0, 1.0)
    println(sameValues.allEqual())

    val mixedValues = doubleArrayOf(1.0, 1.0, 2.0)
    println(mixedValues.allEqual())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualDoubleArraySamples.kt#L19)

### 示例 8 · JVM

```kotlin title="示例 8" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(booleanArrayOf().allEqual())
    println(booleanArrayOf(true).allEqual())

    val sameValues = booleanArrayOf(true, true, true)
    println(sameValues.allEqual())

    val mixedValues = booleanArrayOf(true, true, false)
    println(mixedValues.allEqual())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualBooleanArraySamples.kt#L18)

### 示例 9 · JVM

```kotlin title="示例 9" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(charArrayOf().allEqual())
    println(charArrayOf('a').allEqual())

    val sameValues = charArrayOf('a', 'a', 'a')
    println(sameValues.allEqual())

    val mixedValues = charArrayOf('a', 'a', 'b')
    println(mixedValues.allEqual())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualCharArraySamples.kt#L18)

### 示例 10 · JVM

```kotlin title="示例 10" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(listOf<String>().allEqual())
    println(listOf("apple").allEqual())

    val sameValues = listOf("apple", "apple", "apple")
    println(sameValues.allEqual())

    val mixedValues = listOf("apple", "apple", "orange")
    println(mixedValues.allEqual())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualIterablesSamples.kt#L18)

### 示例 11 · JVM

```kotlin title="示例 11" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(uintArrayOf().allEqual())
    println(uintArrayOf(1u).allEqual())

    val sameValues = uintArrayOf(1u, 1u, 1u)
    println(sameValues.allEqual())

    val mixedValues = uintArrayOf(1u, 1u, 2u)
    println(mixedValues.allEqual())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualUIntArraySamples.kt#L18)

### 示例 12 · JVM

```kotlin title="示例 12" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ulongArrayOf().allEqual())
    println(ulongArrayOf(1uL).allEqual())

    val sameValues = ulongArrayOf(1uL, 1uL, 1uL)
    println(sameValues.allEqual())

    val mixedValues = ulongArrayOf(1uL, 1uL, 2uL)
    println(mixedValues.allEqual())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualULongArraySamples.kt#L18)

### 示例 13 · JVM

```kotlin title="示例 13" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ubyteArrayOf().allEqual())
    println(ubyteArrayOf(1u).allEqual())

    val sameValues = ubyteArrayOf(1u, 1u, 1u)
    println(sameValues.allEqual())

    val mixedValues = ubyteArrayOf(1u, 1u, 2u)
    println(mixedValues.allEqual())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualUByteArraySamples.kt#L18)

### 示例 14 · JVM

```kotlin title="示例 14" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ushortArrayOf().allEqual())
    println(ushortArrayOf(1u).allEqual())

    val sameValues = ushortArrayOf(1u, 1u, 1u)
    println(sameValues.allEqual())

    val mixedValues = ushortArrayOf(1u, 1u, 2u)
    println(mixedValues.allEqual())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualUShortArraySamples.kt#L18)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
