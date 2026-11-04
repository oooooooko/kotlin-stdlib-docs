# contentEquals

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Checks if the two specified arrays are *structurally* equal to one another.

Two arrays are considered structurally equal if they have the same size, and elements at corresponding indices are equal.
Elements are compared for equality using the `equals``Any.equals` function.
For floating point numbers, this means `NaN` is equal to itself and `-0.0` is not equal to `0.0`.

The arrays are also considered structurally equal if both are `null`.

If the arrays contain nested arrays, use `contentDeepEquals` to recursively compare their elements.

@param other the array to compare with this array.
@return `true` if the two arrays are structurally equal, `false` otherwise.

@sample samples.collections.Arrays.ContentOperations.arrayContentEquals

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun <T> Array<out T>?.contentEquals(other: Array<out T>?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8227)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun ByteArray?.contentEquals(other: ByteArray?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8246)

Checks if the two specified arrays are *structurally* equal to one another.

Two arrays are considered structurally equal if they have the same size, and elements at corresponding indices are equal.

The arrays are also considered structurally equal if both are `null`.

@param other the array to compare with this array.
@return `true` if the two arrays are structurally equal, `false` otherwise.

@sample samples.collections.Arrays.ContentOperations.intArrayContentEquals

### 3. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun ShortArray?.contentEquals(other: ShortArray?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8261)

Checks if the two specified arrays are *structurally* equal to one another.

Two arrays are considered structurally equal if they have the same size, and elements at corresponding indices are equal.

The arrays are also considered structurally equal if both are `null`.

@param other the array to compare with this array.
@return `true` if the two arrays are structurally equal, `false` otherwise.

@sample samples.collections.Arrays.ContentOperations.intArrayContentEquals

### 4. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun IntArray?.contentEquals(other: IntArray?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8276)

Checks if the two specified arrays are *structurally* equal to one another.

Two arrays are considered structurally equal if they have the same size, and elements at corresponding indices are equal.

The arrays are also considered structurally equal if both are `null`.

@param other the array to compare with this array.
@return `true` if the two arrays are structurally equal, `false` otherwise.

@sample samples.collections.Arrays.ContentOperations.intArrayContentEquals

### 5. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun LongArray?.contentEquals(other: LongArray?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8291)

Checks if the two specified arrays are *structurally* equal to one another.

Two arrays are considered structurally equal if they have the same size, and elements at corresponding indices are equal.

The arrays are also considered structurally equal if both are `null`.

@param other the array to compare with this array.
@return `true` if the two arrays are structurally equal, `false` otherwise.

@sample samples.collections.Arrays.ContentOperations.intArrayContentEquals

### 6. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun FloatArray?.contentEquals(other: FloatArray?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8306)

Checks if the two specified arrays are *structurally* equal to one another.

Two arrays are considered structurally equal if they have the same size, and elements at corresponding indices are equal.
Elements are compared for equality using the `equals``Any.equals` function.
This means `NaN` is equal to itself and `-0.0` is not equal to `0.0`.

The arrays are also considered structurally equal if both are `null`.

@param other the array to compare with this array.
@return `true` if the two arrays are structurally equal, `false` otherwise.

@sample samples.collections.Arrays.ContentOperations.doubleArrayContentEquals

### 7. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun DoubleArray?.contentEquals(other: DoubleArray?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8323)

Checks if the two specified arrays are *structurally* equal to one another.

Two arrays are considered structurally equal if they have the same size, and elements at corresponding indices are equal.
Elements are compared for equality using the `equals``Any.equals` function.
This means `NaN` is equal to itself and `-0.0` is not equal to `0.0`.

The arrays are also considered structurally equal if both are `null`.

@param other the array to compare with this array.
@return `true` if the two arrays are structurally equal, `false` otherwise.

@sample samples.collections.Arrays.ContentOperations.doubleArrayContentEquals

### 8. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun BooleanArray?.contentEquals(other: BooleanArray?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8340)

Checks if the two specified arrays are *structurally* equal to one another.

Two arrays are considered structurally equal if they have the same size, and elements at corresponding indices are equal.

The arrays are also considered structurally equal if both are `null`.

@param other the array to compare with this array.
@return `true` if the two arrays are structurally equal, `false` otherwise.

@sample samples.collections.Arrays.ContentOperations.booleanArrayContentEquals

### 9. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun CharArray?.contentEquals(other: CharArray?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8355)

Checks if the two specified arrays are *structurally* equal to one another.

Two arrays are considered structurally equal if they have the same size, and elements at corresponding indices are equal.

The arrays are also considered structurally equal if both are `null`.

@param other the array to compare with this array.
@return `true` if the two arrays are structurally equal, `false` otherwise.

@sample samples.collections.Arrays.ContentOperations.charArrayContentEquals

### 10. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public infix fun UIntArray?.contentEquals(other: UIntArray?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3891)

Checks if the two specified arrays are *structurally* equal to one another.

Two arrays are considered structurally equal if they have the same size, and elements at corresponding indices are equal.

The arrays are also considered structurally equal if both are `null`.

@param other the array to compare with this array.
@return `true` if the two arrays are structurally equal, `false` otherwise.

@sample samples.collections.Arrays.ContentOperations.intArrayContentEquals

### 11. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public infix fun ULongArray?.contentEquals(other: ULongArray?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3909)

Checks if the two specified arrays are *structurally* equal to one another.

Two arrays are considered structurally equal if they have the same size, and elements at corresponding indices are equal.

The arrays are also considered structurally equal if both are `null`.

@param other the array to compare with this array.
@return `true` if the two arrays are structurally equal, `false` otherwise.

@sample samples.collections.Arrays.ContentOperations.intArrayContentEquals

### 12. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public infix fun UByteArray?.contentEquals(other: UByteArray?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3927)

Checks if the two specified arrays are *structurally* equal to one another.

Two arrays are considered structurally equal if they have the same size, and elements at corresponding indices are equal.

The arrays are also considered structurally equal if both are `null`.

@param other the array to compare with this array.
@return `true` if the two arrays are structurally equal, `false` otherwise.

@sample samples.collections.Arrays.ContentOperations.intArrayContentEquals

### 13. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public infix fun UShortArray?.contentEquals(other: UShortArray?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3945)

Checks if the two specified arrays are *structurally* equal to one another.

Two arrays are considered structurally equal if they have the same size, and elements at corresponding indices are equal.

The arrays are also considered structurally equal if both are `null`.

@param other the array to compare with this array.
@return `true` if the two arrays are structurally equal, `false` otherwise.

@sample samples.collections.Arrays.ContentOperations.intArrayContentEquals

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.collections.*

fun main() {
    val source = arrayOf(1, 2, 3)
    val result = source.`contentEquals`(arrayOf(1, 2, 3))
    println(result)
}
```

```text title="Output"
true
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
