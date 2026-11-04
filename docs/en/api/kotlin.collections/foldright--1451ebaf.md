# foldRight

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Accumulates value starting with `initial` value and applying `operation` from right to left
to each element and current accumulator value.

Returns the specified `initial` value if the array is empty.

@param `operation` function that takes an element and current accumulator value, and calculates the next accumulator value.

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <T, R> Array<out T>.foldRight(initial: R, operation: (T, acc: R) -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15816)

### 2. Common

```kotlin
public inline fun <R> ByteArray.foldRight(initial: R, operation: (Byte, acc: R) -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15833)

### 3. Common

```kotlin
public inline fun <R> ShortArray.foldRight(initial: R, operation: (Short, acc: R) -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15850)

### 4. Common

```kotlin
public inline fun <R> IntArray.foldRight(initial: R, operation: (Int, acc: R) -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15867)

### 5. Common

```kotlin
public inline fun <R> LongArray.foldRight(initial: R, operation: (Long, acc: R) -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15884)

### 6. Common

```kotlin
public inline fun <R> FloatArray.foldRight(initial: R, operation: (Float, acc: R) -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15901)

### 7. Common

```kotlin
public inline fun <R> DoubleArray.foldRight(initial: R, operation: (Double, acc: R) -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15918)

### 8. Common

```kotlin
public inline fun <R> BooleanArray.foldRight(initial: R, operation: (Boolean, acc: R) -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15935)

### 9. Common

```kotlin
public inline fun <R> CharArray.foldRight(initial: R, operation: (Char, acc: R) -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15952)

### 10. Common

```kotlin
public inline fun <T, R> List<T>.foldRight(initial: R, operation: (T, acc: R) -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2154)

Accumulates value starting with `initial` value and applying `operation` from right to left
to each element and current accumulator value.

Returns the specified `initial` value if the list is empty.

@param `operation` function that takes an element and current accumulator value, and calculates the next accumulator value.

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R> UIntArray.foldRight(initial: R, operation: (UInt, acc: R) -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6763)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R> ULongArray.foldRight(initial: R, operation: (ULong, acc: R) -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6783)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R> UByteArray.foldRight(initial: R, operation: (UByte, acc: R) -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6803)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R> UShortArray.foldRight(initial: R, operation: (UShort, acc: R) -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6823)

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
    val result = source.`foldRight`(1, { a, _ -> a })
    println(result)
}
```

```text title="Output"
1
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
