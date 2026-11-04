# allDistinctBy

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if all values produced by applying the given `selector` function to the
elements in the array are distinct from each other.

Returns `true` for an empty array.

The `selector` values are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate `selector` value is found.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.alldistinct.AllDistinctArraySamples.allDistinctBy

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <T, K> Array<out T>.allDistinctBy(selector: (T) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14493)

### 2. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> ByteArray.allDistinctBy(selector: (Byte) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14518)

Returns `true` if all values produced by applying the given `selector` function to the
elements in the array are distinct from each other.

Returns `true` for an empty array.

The `selector` values are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate `selector` value is found.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.alldistinct.AllDistinctByteArraySamples.allDistinctBy

### 3. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> ShortArray.allDistinctBy(selector: (Short) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14543)

Returns `true` if all values produced by applying the given `selector` function to the
elements in the array are distinct from each other.

Returns `true` for an empty array.

The `selector` values are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate `selector` value is found.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.alldistinct.AllDistinctShortArraySamples.allDistinctBy

### 4. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> IntArray.allDistinctBy(selector: (Int) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14568)

Returns `true` if all values produced by applying the given `selector` function to the
elements in the array are distinct from each other.

Returns `true` for an empty array.

The `selector` values are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate `selector` value is found.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.alldistinct.AllDistinctIntArraySamples.allDistinctBy

### 5. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> LongArray.allDistinctBy(selector: (Long) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14593)

Returns `true` if all values produced by applying the given `selector` function to the
elements in the array are distinct from each other.

Returns `true` for an empty array.

The `selector` values are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate `selector` value is found.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.alldistinct.AllDistinctLongArraySamples.allDistinctBy

### 6. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> FloatArray.allDistinctBy(selector: (Float) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14618)

Returns `true` if all values produced by applying the given `selector` function to the
elements in the array are distinct from each other.

Returns `true` for an empty array.

The `selector` values are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate `selector` value is found.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.alldistinct.AllDistinctFloatArraySamples.allDistinctBy

### 7. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> DoubleArray.allDistinctBy(selector: (Double) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14643)

Returns `true` if all values produced by applying the given `selector` function to the
elements in the array are distinct from each other.

Returns `true` for an empty array.

The `selector` values are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate `selector` value is found.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.alldistinct.AllDistinctDoubleArraySamples.allDistinctBy

### 8. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> BooleanArray.allDistinctBy(selector: (Boolean) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14668)

Returns `true` if all values produced by applying the given `selector` function to the
elements in the array are distinct from each other.

Returns `true` for an empty array.

The `selector` values are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate `selector` value is found.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.alldistinct.AllDistinctBooleanArraySamples.allDistinctBy

### 9. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> CharArray.allDistinctBy(selector: (Char) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14693)

Returns `true` if all values produced by applying the given `selector` function to the
elements in the array are distinct from each other.

Returns `true` for an empty array.

The `selector` values are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate `selector` value is found.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.alldistinct.AllDistinctCharArraySamples.allDistinctBy

### 10. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <T, K> Iterable<T>.allDistinctBy(selector: (T) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1979)

Returns `true` if all values produced by applying the given `selector` function to the
elements in the collection are distinct from each other.

Returns `true` for an empty collection.

The `selector` values are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate `selector` value is found.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.alldistinct.AllDistinctIterablesSamples.allDistinctBy

### 11. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public inline fun <K> UIntArray.allDistinctBy(selector: (UInt) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6139)

Returns `true` if all values produced by applying the given `selector` function to the
elements in the array are distinct from each other.

Returns `true` for an empty array.

The `selector` values are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate `selector` value is found.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.alldistinct.AllDistinctUIntArraySamples.allDistinctBy

### 12. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public inline fun <K> ULongArray.allDistinctBy(selector: (ULong) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6165)

Returns `true` if all values produced by applying the given `selector` function to the
elements in the array are distinct from each other.

Returns `true` for an empty array.

The `selector` values are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate `selector` value is found.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.alldistinct.AllDistinctULongArraySamples.allDistinctBy

### 13. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public inline fun <K> UByteArray.allDistinctBy(selector: (UByte) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6191)

Returns `true` if all values produced by applying the given `selector` function to the
elements in the array are distinct from each other.

Returns `true` for an empty array.

The `selector` values are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate `selector` value is found.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.alldistinct.AllDistinctUByteArraySamples.allDistinctBy

### 14. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public inline fun <K> UShortArray.allDistinctBy(selector: (UShort) -> K): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6217)

Returns `true` if all values produced by applying the given `selector` function to the
elements in the array are distinct from each other.

Returns `true` for an empty array.

The `selector` values are compared using structural equality (`==`).
The operation returns `false` as soon as a duplicate `selector` value is found.

For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.

@sample samples.generated.alldistinct.AllDistinctUShortArraySamples.allDistinctBy

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(arrayOf<String>().allDistinctBy { it.length })
    println(arrayOf("apple").allDistinctBy { it.length })

    val values = arrayOf("apple", "mango", "peach")
    println(values.allDistinctBy { it.length })
    println(values.allDistinctBy { it })
}
```

```text title="Output"
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctArraySamples.kt#L30)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(byteArrayOf().allDistinctBy { it * it })
    println(byteArrayOf(1).allDistinctBy { it * it })

    val values = byteArrayOf(1, -1, 2)
    println(values.allDistinctBy { it * it })
    println(values.allDistinctBy { it })
}
```

```text title="Output"
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctByteArraySamples.kt#L30)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(shortArrayOf().allDistinctBy { it * it })
    println(shortArrayOf(1).allDistinctBy { it * it })

    val values = shortArrayOf(1, -1, 2)
    println(values.allDistinctBy { it * it })
    println(values.allDistinctBy { it })
}
```

```text title="Output"
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctShortArraySamples.kt#L30)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(intArrayOf().allDistinctBy { it * it })
    println(intArrayOf(1).allDistinctBy { it * it })

    val values = intArrayOf(1, -1, 2)
    println(values.allDistinctBy { it * it })
    println(values.allDistinctBy { it })
}
```

```text title="Output"
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctIntArraySamples.kt#L30)

### Example 5 · JVM

```kotlin title="Example 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(longArrayOf().allDistinctBy { it * it })
    println(longArrayOf(1L).allDistinctBy { it * it })

    val values = longArrayOf(1L, -1L, 2L)
    println(values.allDistinctBy { it * it })
    println(values.allDistinctBy { it })
}
```

```text title="Output"
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctLongArraySamples.kt#L30)

### Example 6 · JVM

```kotlin title="Example 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(floatArrayOf().allDistinctBy { it * it })
    println(floatArrayOf(1.0f).allDistinctBy { it * it })

    val values = floatArrayOf(1.0f, -1.0f, 2.0f)
    println(values.allDistinctBy { it * it })
    println(values.allDistinctBy { it })
}
```

```text title="Output"
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctFloatArraySamples.kt#L33)

### Example 7 · JVM

```kotlin title="Example 7" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(doubleArrayOf().allDistinctBy { it * it })
    println(doubleArrayOf(1.0).allDistinctBy { it * it })

    val values = doubleArrayOf(1.0, -1.0, 2.0)
    println(values.allDistinctBy { it * it })
    println(values.allDistinctBy { it })
}
```

```text title="Output"
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctDoubleArraySamples.kt#L33)

### Example 8 · JVM

```kotlin title="Example 8" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(booleanArrayOf().allDistinctBy { if (it) 1 else 0 })
    println(booleanArrayOf(true).allDistinctBy { if (it) 1 else 0 })

    val values = booleanArrayOf(true, false)
    println(values.allDistinctBy { if (it) 1 else 0 })
    println(values.allDistinctBy { 0 })
}
```

```text title="Output"
true
true
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctBooleanArraySamples.kt#L30)

### Example 9 · JVM

```kotlin title="Example 9" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(charArrayOf().allDistinctBy { it.uppercaseChar() })
    println(charArrayOf('a').allDistinctBy { it.uppercaseChar() })

    val values = charArrayOf('a', 'A', 'b')
    println(values.allDistinctBy { it.uppercaseChar() })
    println(values.allDistinctBy { it })
}
```

```text title="Output"
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctCharArraySamples.kt#L30)

### Example 10 · JVM

```kotlin title="Example 10" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(listOf<String>().allDistinctBy { it.length })
    println(listOf("apple").allDistinctBy { it.length })

    val values = listOf("apple", "mango", "peach")
    println(values.allDistinctBy { it.length })
    println(values.allDistinctBy { it })
}
```

```text title="Output"
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctIterablesSamples.kt#L30)

### Example 11 · JVM

```kotlin title="Example 11" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(uintArrayOf().allDistinctBy { it % 2u })
    println(uintArrayOf(1u).allDistinctBy { it % 2u })

    val values = uintArrayOf(1u, 3u, 2u)
    println(values.allDistinctBy { it % 2u })
    println(values.allDistinctBy { it })
}
```

```text title="Output"
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctUIntArraySamples.kt#L30)

### Example 12 · JVM

```kotlin title="Example 12" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ulongArrayOf().allDistinctBy { it % 2uL })
    println(ulongArrayOf(1uL).allDistinctBy { it % 2uL })

    val values = ulongArrayOf(1uL, 3uL, 2uL)
    println(values.allDistinctBy { it % 2uL })
    println(values.allDistinctBy { it })
}
```

```text title="Output"
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctULongArraySamples.kt#L30)

### Example 13 · JVM

```kotlin title="Example 13" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ubyteArrayOf().allDistinctBy { it.toUInt() % 2u })
    println(ubyteArrayOf(1u).allDistinctBy { it.toUInt() % 2u })

    val values = ubyteArrayOf(1u, 3u, 2u)
    println(values.allDistinctBy { it.toUInt() % 2u })
    println(values.allDistinctBy { it })
}
```

```text title="Output"
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctUByteArraySamples.kt#L30)

### Example 14 · JVM

```kotlin title="Example 14" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ushortArrayOf().allDistinctBy { it.toUInt() % 2u })
    println(ushortArrayOf(1u).allDistinctBy { it.toUInt() % 2u })

    val values = ushortArrayOf(1u, 3u, 2u)
    println(values.allDistinctBy { it.toUInt() % 2u })
    println(values.allDistinctBy { it })
}
```

```text title="Output"
true
true
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctUShortArraySamples.kt#L30)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
