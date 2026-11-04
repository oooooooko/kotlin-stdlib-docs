# allEqualBy

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if all elements in the array yield the same value
produced by the given `selector` function.

Returns `true` for an empty array.

The `selector` values are compared sequentially using structural equality (`==`),
and all elements are considered equal by the `selector` value if the `selector`
value of the first element equals the `selector` value of every subsequent element.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.allequal.AllEqualArraySamples.allEqualBy

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <T, K> Array<out T>.allEqualBy(selector: (T) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14925)

### 2. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> ByteArray.allEqualBy(selector: (Byte) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14958)

Returns `true` if all elements in the array yield the same value
produced by the given `selector` function.

Returns `true` for an empty array.

The `selector` values are compared sequentially using structural equality (`==`),
and all elements are considered equal by the `selector` value if the `selector`
value of the first element equals the `selector` value of every subsequent element.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.allequal.AllEqualByteArraySamples.allEqualBy

### 3. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> ShortArray.allEqualBy(selector: (Short) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14991)

Returns `true` if all elements in the array yield the same value
produced by the given `selector` function.

Returns `true` for an empty array.

The `selector` values are compared sequentially using structural equality (`==`),
and all elements are considered equal by the `selector` value if the `selector`
value of the first element equals the `selector` value of every subsequent element.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.allequal.AllEqualShortArraySamples.allEqualBy

### 4. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> IntArray.allEqualBy(selector: (Int) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15024)

Returns `true` if all elements in the array yield the same value
produced by the given `selector` function.

Returns `true` for an empty array.

The `selector` values are compared sequentially using structural equality (`==`),
and all elements are considered equal by the `selector` value if the `selector`
value of the first element equals the `selector` value of every subsequent element.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.allequal.AllEqualIntArraySamples.allEqualBy

### 5. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> LongArray.allEqualBy(selector: (Long) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15057)

Returns `true` if all elements in the array yield the same value
produced by the given `selector` function.

Returns `true` for an empty array.

The `selector` values are compared sequentially using structural equality (`==`),
and all elements are considered equal by the `selector` value if the `selector`
value of the first element equals the `selector` value of every subsequent element.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.allequal.AllEqualLongArraySamples.allEqualBy

### 6. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> FloatArray.allEqualBy(selector: (Float) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15090)

Returns `true` if all elements in the array yield the same value
produced by the given `selector` function.

Returns `true` for an empty array.

The `selector` values are compared sequentially using structural equality (`==`),
and all elements are considered equal by the `selector` value if the `selector`
value of the first element equals the `selector` value of every subsequent element.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.allequal.AllEqualFloatArraySamples.allEqualBy

### 7. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> DoubleArray.allEqualBy(selector: (Double) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15123)

Returns `true` if all elements in the array yield the same value
produced by the given `selector` function.

Returns `true` for an empty array.

The `selector` values are compared sequentially using structural equality (`==`),
and all elements are considered equal by the `selector` value if the `selector`
value of the first element equals the `selector` value of every subsequent element.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.allequal.AllEqualDoubleArraySamples.allEqualBy

### 8. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> BooleanArray.allEqualBy(selector: (Boolean) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15156)

Returns `true` if all elements in the array yield the same value
produced by the given `selector` function.

Returns `true` for an empty array.

The `selector` values are compared sequentially using structural equality (`==`),
and all elements are considered equal by the `selector` value if the `selector`
value of the first element equals the `selector` value of every subsequent element.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.allequal.AllEqualBooleanArraySamples.allEqualBy

### 9. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> CharArray.allEqualBy(selector: (Char) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15189)

Returns `true` if all elements in the array yield the same value
produced by the given `selector` function.

Returns `true` for an empty array.

The `selector` values are compared sequentially using structural equality (`==`),
and all elements are considered equal by the `selector` value if the `selector`
value of the first element equals the `selector` value of every subsequent element.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.allequal.AllEqualCharArraySamples.allEqualBy

### 10. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <T, K> Iterable<T>.allEqualBy(selector: (T) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2035)

Returns `true` if all elements in the collection yield the same value
produced by the given `selector` function.

Returns `true` for an empty collection.

The `selector` values are compared sequentially using structural equality (`==`),
and all elements are considered equal by the `selector` value if the `selector`
value of the first element equals the `selector` value of every subsequent element.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.allequal.AllEqualIterablesSamples.allEqualBy

### 11. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public inline fun <K> UIntArray.allEqualBy(selector: (UInt) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6335)

Returns `true` if all elements in the array yield the same value
produced by the given `selector` function.

Returns `true` for an empty array.

The `selector` values are compared sequentially using structural equality (`==`),
and all elements are considered equal by the `selector` value if the `selector`
value of the first element equals the `selector` value of every subsequent element.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.allequal.AllEqualUIntArraySamples.allEqualBy

### 12. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public inline fun <K> ULongArray.allEqualBy(selector: (ULong) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6369)

Returns `true` if all elements in the array yield the same value
produced by the given `selector` function.

Returns `true` for an empty array.

The `selector` values are compared sequentially using structural equality (`==`),
and all elements are considered equal by the `selector` value if the `selector`
value of the first element equals the `selector` value of every subsequent element.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.allequal.AllEqualULongArraySamples.allEqualBy

### 13. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public inline fun <K> UByteArray.allEqualBy(selector: (UByte) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6403)

Returns `true` if all elements in the array yield the same value
produced by the given `selector` function.

Returns `true` for an empty array.

The `selector` values are compared sequentially using structural equality (`==`),
and all elements are considered equal by the `selector` value if the `selector`
value of the first element equals the `selector` value of every subsequent element.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.allequal.AllEqualUByteArraySamples.allEqualBy

### 14. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public inline fun <K> UShortArray.allEqualBy(selector: (UShort) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6437)

Returns `true` if all elements in the array yield the same value
produced by the given `selector` function.

Returns `true` for an empty array.

The `selector` values are compared sequentially using structural equality (`==`),
and all elements are considered equal by the `selector` value if the `selector`
value of the first element equals the `selector` value of every subsequent element.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.allequal.AllEqualUShortArraySamples.allEqualBy

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(arrayOf<String>().allEqualBy { it.length })
    println(arrayOf("apple").allEqualBy { it.length })

    val values = arrayOf("apple", "mango", "peach")
    println(values.allEqualBy { it.length })
    println(values.allEqualBy { it })
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualArraySamples.kt#L30)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(byteArrayOf().allEqualBy { it * it })
    println(byteArrayOf(1).allEqualBy { it * it })

    val values = byteArrayOf(1, -1, 1)
    println(values.allEqualBy { it * it })
    println(values.allEqualBy { abs(it.toInt()) })
    println(values.allEqualBy { it * it * it })
}
```

```text title="Output"
true
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualByteArraySamples.kt#L31)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(shortArrayOf().allEqualBy { it * it })
    println(shortArrayOf(1).allEqualBy { it * it })

    val values = shortArrayOf(1, -1, 1)
    println(values.allEqualBy { it * it })
    println(values.allEqualBy { abs(it.toInt()) })
    println(values.allEqualBy { it * it * it })
}
```

```text title="Output"
true
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualShortArraySamples.kt#L31)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(intArrayOf().allEqualBy { it * it })
    println(intArrayOf(1).allEqualBy { it * it })

    val values = intArrayOf(1, -1, 1)
    println(values.allEqualBy { it * it })
    println(values.allEqualBy { abs(it) })
    println(values.allEqualBy { it * it * it })
}
```

```text title="Output"
true
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualIntArraySamples.kt#L31)

### Example 5 · JVM

```kotlin title="Example 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(longArrayOf().allEqualBy { it * it })
    println(longArrayOf(1L).allEqualBy { it * it })

    val values = longArrayOf(1L, -1L, 1L)
    println(values.allEqualBy { it * it })
    println(values.allEqualBy { abs(it) })
    println(values.allEqualBy { it * it * it })
}
```

```text title="Output"
true
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualLongArraySamples.kt#L31)

### Example 6 · JVM

```kotlin title="Example 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(floatArrayOf().allEqualBy { it * it })
    println(floatArrayOf(1.0f).allEqualBy { it * it })

    val values = floatArrayOf(1.0f, -1.0f, 1.0f)
    println(values.allEqualBy { it * it })
    println(values.allEqualBy { abs(it) })
    println(values.allEqualBy { it * it * it })
}
```

```text title="Output"
true
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualFloatArraySamples.kt#L31)

### Example 7 · JVM

```kotlin title="Example 7" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(doubleArrayOf().allEqualBy { it * it })
    println(doubleArrayOf(1.0).allEqualBy { it * it })

    val values = doubleArrayOf(1.0, -1.0, 1.0)
    println(values.allEqualBy { it * it })
    println(values.allEqualBy { abs(it) })
    println(values.allEqualBy { it * it * it })
}
```

```text title="Output"
true
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualDoubleArraySamples.kt#L31)

### Example 8 · JVM

```kotlin title="Example 8" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(booleanArrayOf().allEqualBy { 0 })
    println(booleanArrayOf(true).allEqualBy { 0 })

    val values = booleanArrayOf(true, false, true)
    println(values.allEqualBy { 0 })
    println(values.allEqualBy { if (it) 1 else 0 })
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualBooleanArraySamples.kt#L30)

### Example 9 · JVM

```kotlin title="Example 9" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(charArrayOf().allEqualBy { it.uppercaseChar() })
    println(charArrayOf('a').allEqualBy { it.uppercaseChar() })

    val values = charArrayOf('a', 'A', 'a')
    println(values.allEqualBy { it.uppercaseChar() })
    println(values.allEqualBy { it.lowercaseChar() })
    println(values.allEqualBy { it })
}
```

```text title="Output"
true
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualCharArraySamples.kt#L30)

### Example 10 · JVM

```kotlin title="Example 10" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(listOf<String>().allEqualBy { it.length })
    println(listOf("apple").allEqualBy { it.length })

    val values = listOf("apple", "mango", "peach")
    println(values.allEqualBy { it.length })
    println(values.allEqualBy { it })
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualIterablesSamples.kt#L30)

### Example 11 · JVM

```kotlin title="Example 11" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(uintArrayOf().allEqualBy { it % 2u })
    println(uintArrayOf(1u).allEqualBy { it % 2u })

    val values = uintArrayOf(1u, 3u, 5u)
    println(values.allEqualBy { it % 2u })
    println(values.allEqualBy { it })
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualUIntArraySamples.kt#L30)

### Example 12 · JVM

```kotlin title="Example 12" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ulongArrayOf().allEqualBy { it % 2uL })
    println(ulongArrayOf(1uL).allEqualBy { it % 2uL })

    val values = ulongArrayOf(1uL, 3uL, 5uL)
    println(values.allEqualBy { it % 2uL })
    println(values.allEqualBy { it })
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualULongArraySamples.kt#L30)

### Example 13 · JVM

```kotlin title="Example 13" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ubyteArrayOf().allEqualBy { it.toUInt() % 2u })
    println(ubyteArrayOf(1u).allEqualBy { it.toUInt() % 2u })

    val values = ubyteArrayOf(1u, 3u, 5u)
    println(values.allEqualBy { it.toUInt() % 2u })
    println(values.allEqualBy { it })
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualUByteArraySamples.kt#L30)

### Example 14 · JVM

```kotlin title="Example 14" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ushortArrayOf().allEqualBy { it.toUInt() % 2u })
    println(ushortArrayOf(1u).allEqualBy { it.toUInt() % 2u })

    val values = ushortArrayOf(1u, 3u, 5u)
    println(values.allEqualBy { it.toUInt() % 2u })
    println(values.allEqualBy { it })
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualUShortArraySamples.kt#L30)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
