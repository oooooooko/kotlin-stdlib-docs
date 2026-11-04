# singleOrNull

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns single element, or `null` if the array is empty or has more than one element.

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Array<out T>.singleOrNull(): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3212)

### 2. Common

```kotlin
public fun ByteArray.singleOrNull(): Byte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3219)

### 3. Common

```kotlin
public fun ShortArray.singleOrNull(): Short?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3226)

### 4. Common

```kotlin
public fun IntArray.singleOrNull(): Int?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3233)

### 5. Common

```kotlin
public fun LongArray.singleOrNull(): Long?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3240)

### 6. Common

```kotlin
public fun FloatArray.singleOrNull(): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3247)

### 7. Common

```kotlin
public fun DoubleArray.singleOrNull(): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3254)

### 8. Common

```kotlin
public fun BooleanArray.singleOrNull(): Boolean?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3261)

### 9. Common

```kotlin
public fun CharArray.singleOrNull(): Char?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3268)

### 10. Common

```kotlin
public inline fun <T> Array<out T>.singleOrNull(predicate: (T) -> Boolean): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3275)

Returns the single element matching the given `predicate`, or `null` if element was not found or more than one element was found.

### 11. Common

```kotlin
public inline fun ByteArray.singleOrNull(predicate: (Byte) -> Boolean): Byte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3292)

Returns the single element matching the given `predicate`, or `null` if element was not found or more than one element was found.

### 12. Common

```kotlin
public inline fun ShortArray.singleOrNull(predicate: (Short) -> Boolean): Short?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3309)

Returns the single element matching the given `predicate`, or `null` if element was not found or more than one element was found.

### 13. Common

```kotlin
public inline fun IntArray.singleOrNull(predicate: (Int) -> Boolean): Int?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3326)

Returns the single element matching the given `predicate`, or `null` if element was not found or more than one element was found.

### 14. Common

```kotlin
public inline fun LongArray.singleOrNull(predicate: (Long) -> Boolean): Long?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3343)

Returns the single element matching the given `predicate`, or `null` if element was not found or more than one element was found.

### 15. Common

```kotlin
public inline fun FloatArray.singleOrNull(predicate: (Float) -> Boolean): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3360)

Returns the single element matching the given `predicate`, or `null` if element was not found or more than one element was found.

### 16. Common

```kotlin
public inline fun DoubleArray.singleOrNull(predicate: (Double) -> Boolean): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3377)

Returns the single element matching the given `predicate`, or `null` if element was not found or more than one element was found.

### 17. Common

```kotlin
public inline fun BooleanArray.singleOrNull(predicate: (Boolean) -> Boolean): Boolean?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3394)

Returns the single element matching the given `predicate`, or `null` if element was not found or more than one element was found.

### 18. Common

```kotlin
public inline fun CharArray.singleOrNull(predicate: (Char) -> Boolean): Char?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3411)

Returns the single element matching the given `predicate`, or `null` if element was not found or more than one element was found.

### 19. Common

```kotlin
public fun <T> Iterable<T>.singleOrNull(): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L643)

Returns single element, or `null` if the collection is empty or has more than one element.

### 20. Common

```kotlin
public fun <T> List<T>.singleOrNull(): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L661)

Returns single element, or `null` if the list is empty or has more than one element.

### 21. Common

```kotlin
public inline fun <T> Iterable<T>.singleOrNull(predicate: (T) -> Boolean): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L668)

Returns the single element matching the given `predicate`, or `null` if element was not found or more than one element was found.

### 22. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.singleOrNull(): UInt?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1547)

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.singleOrNull(): ULong?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1556)

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.singleOrNull(): UByte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1565)

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.singleOrNull(): UShort?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1574)

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.singleOrNull(predicate: (UInt) -> Boolean): UInt?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1583)

Returns the single element matching the given `predicate`, or `null` if element was not found or more than one element was found.

### 27. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.singleOrNull(predicate: (ULong) -> Boolean): ULong?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1603)

Returns the single element matching the given `predicate`, or `null` if element was not found or more than one element was found.

### 28. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.singleOrNull(predicate: (UByte) -> Boolean): UByte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1623)

Returns the single element matching the given `predicate`, or `null` if element was not found or more than one element was found.

### 29. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.singleOrNull(predicate: (UShort) -> Boolean): UShort?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1643)

Returns the single element matching the given `predicate`, or `null` if element was not found or more than one element was found.

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
    val result = source.`singleOrNull`()
    println(result)
}
```

```text title="Output"
null
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
