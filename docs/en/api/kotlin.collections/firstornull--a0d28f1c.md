# firstOrNull

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the first element, or `null` if the array is empty.

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Array<out T>.firstOrNull(): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1334)

### 2. Common

```kotlin
public fun ByteArray.firstOrNull(): Byte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1341)

### 3. Common

```kotlin
public fun ShortArray.firstOrNull(): Short?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1348)

### 4. Common

```kotlin
public fun IntArray.firstOrNull(): Int?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1355)

### 5. Common

```kotlin
public fun LongArray.firstOrNull(): Long?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1362)

### 6. Common

```kotlin
public fun FloatArray.firstOrNull(): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1369)

### 7. Common

```kotlin
public fun DoubleArray.firstOrNull(): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1376)

### 8. Common

```kotlin
public fun BooleanArray.firstOrNull(): Boolean?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1383)

### 9. Common

```kotlin
public fun CharArray.firstOrNull(): Char?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1390)

### 10. Common

```kotlin
public inline fun <T> Array<out T>.firstOrNull(predicate: (T) -> Boolean): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1397)

Returns the first element matching the given `predicate`, or `null` if element was not found.

### 11. Common

```kotlin
public inline fun ByteArray.firstOrNull(predicate: (Byte) -> Boolean): Byte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1405)

Returns the first element matching the given `predicate`, or `null` if element was not found.

### 12. Common

```kotlin
public inline fun ShortArray.firstOrNull(predicate: (Short) -> Boolean): Short?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1413)

Returns the first element matching the given `predicate`, or `null` if element was not found.

### 13. Common

```kotlin
public inline fun IntArray.firstOrNull(predicate: (Int) -> Boolean): Int?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1421)

Returns the first element matching the given `predicate`, or `null` if element was not found.

### 14. Common

```kotlin
public inline fun LongArray.firstOrNull(predicate: (Long) -> Boolean): Long?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1429)

Returns the first element matching the given `predicate`, or `null` if element was not found.

### 15. Common

```kotlin
public inline fun FloatArray.firstOrNull(predicate: (Float) -> Boolean): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1437)

Returns the first element matching the given `predicate`, or `null` if element was not found.

### 16. Common

```kotlin
public inline fun DoubleArray.firstOrNull(predicate: (Double) -> Boolean): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1445)

Returns the first element matching the given `predicate`, or `null` if element was not found.

### 17. Common

```kotlin
public inline fun BooleanArray.firstOrNull(predicate: (Boolean) -> Boolean): Boolean?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1453)

Returns the first element matching the given `predicate`, or `null` if element was not found.

### 18. Common

```kotlin
public inline fun CharArray.firstOrNull(predicate: (Char) -> Boolean): Char?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1461)

Returns the first element matching the given `predicate`, or `null` if element was not found.

### 19. Common

```kotlin
public fun <T> Iterable<T>.firstOrNull(): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L265)

Returns the first element, or `null` if the collection is empty.

### 20. Common

```kotlin
public fun <T> List<T>.firstOrNull(): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L285)

Returns the first element, or `null` if the list is empty.

### 21. Common

```kotlin
public inline fun <T> Iterable<T>.firstOrNull(predicate: (T) -> Boolean): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L292)

Returns the first element matching the given `predicate`, or `null` if element was not found.

### 22. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.firstOrNull(): UInt?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L659)

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.firstOrNull(): ULong?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L668)

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.firstOrNull(): UByte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L677)

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.firstOrNull(): UShort?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L686)

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.firstOrNull(predicate: (UInt) -> Boolean): UInt?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L695)

Returns the first element matching the given `predicate`, or `null` if element was not found.

### 27. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.firstOrNull(predicate: (ULong) -> Boolean): ULong?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L706)

Returns the first element matching the given `predicate`, or `null` if element was not found.

### 28. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.firstOrNull(predicate: (UByte) -> Boolean): UByte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L717)

Returns the first element matching the given `predicate`, or `null` if element was not found.

### 29. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.firstOrNull(predicate: (UShort) -> Boolean): UShort?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L728)

Returns the first element matching the given `predicate`, or `null` if element was not found.

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
    val result = source.`firstOrNull`()
    println(result)
}
```

```text title="Output"
1
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
