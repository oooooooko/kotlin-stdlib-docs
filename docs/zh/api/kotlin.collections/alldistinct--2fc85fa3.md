# allDistinct

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果数组中的所有元素彼此不同,即没有两个元素相等,则返回`true`。

返回`true`的空数组。

使用结构平等( `==` )对这些元素进行比较,一旦发现重复元素,操作就会返回 `false` 。

对于浮动点类型( `Double` , `Float` ),`NaN` 的值为 `NaN` ,`-0.0`的值为`Double.equals`和`Float.equals`,不等于`0.0`。

@sample 样本, 生成. 全部 。 所有 Distinct 阵列样本, 全部 Distinct

??? note "查看英文原文"

    Returns `true` if all elements in the array are distinct from each other,
    that is, no two elements are equal.
    
    Returns `true` for an empty array.
    
    The elements are compared using structural equality (`==`).
    The operation returns `false` as soon as a duplicate element is found.
    
    For elements of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
    and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.
    
    @sample samples.generated.alldistinct.AllDistinctArraySamples.allDistinct

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun <T> Array<out T>.allDistinct(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14283)

### 2. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun ByteArray.allDistinct(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14308)

如果数组中的所有元素彼此不同,即没有两个元素相等,则返回`true`。

返回`true`的空数组。

使用结构平等( `==` )对这些元素进行比较,一旦发现重复元素,操作就会返回 `false` 。

@sample 样本. 生成. all distinctByte 分布式标本. all distict

### 3. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun ShortArray.allDistinct(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14332)

如果数组中的所有元素彼此不同,即没有两个元素相等,则返回`true`。

返回`true`的空数组。

使用结构平等( `==` )对这些元素进行比较,一旦发现重复元素,操作就会返回 `false` 。

@sample 样本, 生成. all distict - 短短的阵列样本。 all distict

### 4. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun IntArray.allDistinct(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14356)

如果数组中的所有元素彼此不同,即没有两个元素相等,则返回`true`。

返回`true`的空数组。

使用结构平等( `==` )对这些元素进行比较,一旦发现重复元素,操作就会返回 `false` 。

@sample 样本. 生成. all distinct IntAraySamples. all distinct

### 5. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun LongArray.allDistinct(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14378)

如果数组中的所有元素彼此不同,即没有两个元素相等,则返回`true`。

返回`true`的空数组。

使用结构平等( `==` )对这些元素进行比较,一旦发现重复元素,操作就会返回 `false` 。

@sample 样本, 生成. all distinctLong 光束样本。 所有 DistinctLong 都生成了

### 6. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun FloatArray.allDistinct(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14400)

如果数组中的所有元素彼此不同,即没有两个元素相等,则返回`true`。

返回`true`的空数组。

使用与 `Float.equals` 一致的平等语义来比较这些元素。一旦发现重复元素,操作将返回 `false` 。

`NaN` 被认为等于 `NaN` ,`-0.0`被认为不等于 `0.0` ,与`Float.equals`一致。

@sample 样本, 生成. all distinct.

### 7. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun DoubleArray.allDistinct(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14425)

如果数组中的所有元素彼此不同,即没有两个元素相等,则返回`true`。

返回`true`的空数组。

使用与 `Double.equals` 一致的平等语义来比较这些元素。一旦发现重复元素,操作将返回 `false` 。

`NaN` 被认为等于 `NaN` ,`-0.0`被认为不等于 `0.0` ,与`Double.equals`一致。

@sample 样本. 生成. all distinctDouble ArraySamples.all distinct 全部 Distinct 都生成

### 8. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun BooleanArray.allDistinct(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14450)

如果数组中的所有元素彼此不同,即没有两个元素相等,则返回`true`。

返回`true`的空数组。

使用结构平等( `==` )对这些元素进行比较,一旦发现重复元素,操作就会返回 `false` 。

@sample 样本, 生成的样本。 所有 DistinctBoolean 的阿雷标本。 全部 Distinct

### 9. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun CharArray.allDistinct(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14469)

如果数组中的所有元素彼此不同,即没有两个元素相等,则返回`true`。

返回`true`的空数组。

使用结构平等( `==` )对这些元素进行比较,一旦发现重复元素,操作就会返回 `false` 。

@sample 样本, 生成. all distinctCharAraySamples. all distinct

### 10. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun <T> Iterable<T>.allDistinct(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1950)

如果收藏中的所有元素彼此不同,即没有两个元素是相等的,则返回`true`。

空收藏返回`true`。

使用结构平等( `==` )对这些元素进行比较,一旦发现重复元素,操作就会返回 `false` 。

对于浮动点类型( `Double` , `Float` ),`NaN` 的值为 `NaN` ,`-0.0`的值为`Double.equals`和`Float.equals`,不等于`0.0`。

@sample 样本, 生成. 全部 。 所有 Distinciterables 样本。 all distinct

### 11. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public fun UIntArray.allDistinct(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6043)

如果数组中的所有元素彼此不同,即没有两个元素相等,则返回`true`。

返回`true`的空数组。

使用结构平等( `==` )对这些元素进行比较,一旦发现重复元素,操作就会返回 `false` 。

@sample 样本, 生成. all distinctUint ArraySamples. all distict

### 12. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public fun ULongArray.allDistinct(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6066)

如果数组中的所有元素彼此不同,即没有两个元素相等,则返回`true`。

返回`true`的空数组。

使用结构平等( `==` )对这些元素进行比较,一旦发现重复元素,操作就会返回 `false` 。

@sample 样本, 生成. all distinctULong 光电阵列样本。 所有 Distinct

### 13. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public fun UByteArray.allDistinct(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6089)

如果数组中的所有元素彼此不同,即没有两个元素相等,则返回`true`。

返回`true`的空数组。

使用结构平等( `==` )对这些元素进行比较,一旦发现重复元素,操作就会返回 `false` 。

@sample 样本, 生成. 全部 。 所有 DistinctUByte ARay 样本。

### 14. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public fun UShortArray.allDistinct(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6114)

如果数组中的所有元素彼此不同,即没有两个元素相等,则返回`true`。

返回`true`的空数组。

使用结构平等( `==` )对这些元素进行比较,一旦发现重复元素,操作就会返回 `false` 。

@sample 样本, 生成. 全部。 所有 DistinctUShort Aray 样本。 全部 Distinct

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(arrayOf<String>().allDistinct())
    println(arrayOf("apple").allDistinct())

    val distinctValues = arrayOf("apple", "mango", "peach")
    println(distinctValues.allDistinct())

    val duplicateValues = arrayOf("apple", "mango", "apple")
    println(duplicateValues.allDistinct())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctArraySamples.kt#L18)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(byteArrayOf().allDistinct())
    println(byteArrayOf(1).allDistinct())

    val distinctValues = byteArrayOf(1, 2, 3)
    println(distinctValues.allDistinct())

    val duplicateValues = byteArrayOf(1, 2, 1)
    println(duplicateValues.allDistinct())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctByteArraySamples.kt#L18)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(shortArrayOf().allDistinct())
    println(shortArrayOf(1).allDistinct())

    val distinctValues = shortArrayOf(1, 2, 3)
    println(distinctValues.allDistinct())

    val duplicateValues = shortArrayOf(1, 2, 1)
    println(duplicateValues.allDistinct())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctShortArraySamples.kt#L18)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(intArrayOf().allDistinct())
    println(intArrayOf(1).allDistinct())

    val distinctValues = intArrayOf(1, 2, 3)
    println(distinctValues.allDistinct())

    val duplicateValues = intArrayOf(1, 2, 1)
    println(duplicateValues.allDistinct())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctIntArraySamples.kt#L18)

### 示例 5 · JVM

```kotlin title="示例 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(longArrayOf().allDistinct())
    println(longArrayOf(1L).allDistinct())

    val distinctValues = longArrayOf(1L, 2L, 3L)
    println(distinctValues.allDistinct())

    val duplicateValues = longArrayOf(1L, 2L, 1L)
    println(duplicateValues.allDistinct())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctLongArraySamples.kt#L18)

### 示例 6 · JVM

```kotlin title="示例 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(floatArrayOf().allDistinct())
    println(floatArrayOf(1.0f).allDistinct())

    val distinctValues = floatArrayOf(1.0f, 2.0f, 3.0f)
    println(distinctValues.allDistinct())

    val duplicateValues = floatArrayOf(1.0f, 2.0f, 1.0f)
    println(duplicateValues.allDistinct())

    println(floatArrayOf(Float.NaN, Float.NaN).allDistinct())
    println(floatArrayOf(0.0f, -0.0f).allDistinct())
}
```

```text title="输出"
true
true
true
false
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctFloatArraySamples.kt#L18)

### 示例 7 · JVM

```kotlin title="示例 7" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(doubleArrayOf().allDistinct())
    println(doubleArrayOf(1.0).allDistinct())

    val distinctValues = doubleArrayOf(1.0, 2.0, 3.0)
    println(distinctValues.allDistinct())

    val duplicateValues = doubleArrayOf(1.0, 2.0, 1.0)
    println(duplicateValues.allDistinct())

    println(doubleArrayOf(Double.NaN, Double.NaN).allDistinct())
    println(doubleArrayOf(0.0, -0.0).allDistinct())
}
```

```text title="输出"
true
true
true
false
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctDoubleArraySamples.kt#L18)

### 示例 8 · JVM

```kotlin title="示例 8" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(booleanArrayOf().allDistinct())
    println(booleanArrayOf(true).allDistinct())

    val distinctValues = booleanArrayOf(true, false)
    println(distinctValues.allDistinct())

    val duplicateValues = booleanArrayOf(true, false, true)
    println(duplicateValues.allDistinct())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctBooleanArraySamples.kt#L18)

### 示例 9 · JVM

```kotlin title="示例 9" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(charArrayOf().allDistinct())
    println(charArrayOf('a').allDistinct())

    val distinctValues = charArrayOf('a', 'b', 'c')
    println(distinctValues.allDistinct())

    val duplicateValues = charArrayOf('a', 'b', 'a')
    println(duplicateValues.allDistinct())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctCharArraySamples.kt#L18)

### 示例 10 · JVM

```kotlin title="示例 10" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(listOf<String>().allDistinct())
    println(listOf("apple").allDistinct())

    val distinctValues = listOf("apple", "mango", "peach")
    println(distinctValues.allDistinct())

    val duplicateValues = listOf("apple", "mango", "apple")
    println(duplicateValues.allDistinct())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctIterablesSamples.kt#L18)

### 示例 11 · JVM

```kotlin title="示例 11" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(uintArrayOf().allDistinct())
    println(uintArrayOf(1u).allDistinct())

    val distinctValues = uintArrayOf(1u, 2u, 3u)
    println(distinctValues.allDistinct())

    val duplicateValues = uintArrayOf(1u, 2u, 1u)
    println(duplicateValues.allDistinct())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctUIntArraySamples.kt#L18)

### 示例 12 · JVM

```kotlin title="示例 12" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ulongArrayOf().allDistinct())
    println(ulongArrayOf(1uL).allDistinct())

    val distinctValues = ulongArrayOf(1uL, 2uL, 3uL)
    println(distinctValues.allDistinct())

    val duplicateValues = ulongArrayOf(1uL, 2uL, 1uL)
    println(duplicateValues.allDistinct())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctULongArraySamples.kt#L18)

### 示例 13 · JVM

```kotlin title="示例 13" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ubyteArrayOf().allDistinct())
    println(ubyteArrayOf(1u).allDistinct())

    val distinctValues = ubyteArrayOf(1u, 2u, 3u)
    println(distinctValues.allDistinct())

    val duplicateValues = ubyteArrayOf(1u, 2u, 1u)
    println(duplicateValues.allDistinct())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctUByteArraySamples.kt#L18)

### 示例 14 · JVM

```kotlin title="示例 14" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ushortArrayOf().allDistinct())
    println(ushortArrayOf(1u).allDistinct())

    val distinctValues = ushortArrayOf(1u, 2u, 3u)
    println(distinctValues.allDistinct())

    val duplicateValues = ushortArrayOf(1u, 2u, 1u)
    println(duplicateValues.allDistinct())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctUShortArraySamples.kt#L18)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
