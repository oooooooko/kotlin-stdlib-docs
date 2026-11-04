# first

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the first element.

@throws NoSuchElementException if the array is empty.

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Array<out T>.first(): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1124)

### 2. Common

```kotlin
public fun ByteArray.first(): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1135)

### 3. Common

```kotlin
public fun ShortArray.first(): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1146)

### 4. Common

```kotlin
public fun IntArray.first(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1157)

### 5. Common

```kotlin
public fun LongArray.first(): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1168)

### 6. Common

```kotlin
public fun FloatArray.first(): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1179)

### 7. Common

```kotlin
public fun DoubleArray.first(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1190)

### 8. Common

```kotlin
public fun BooleanArray.first(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1201)

### 9. Common

```kotlin
public fun CharArray.first(): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1212)

### 10. Common

```kotlin
public inline fun <T> Array<out T>.first(predicate: (T) -> Boolean): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1223)

Returns the first element matching the given `predicate`.
@throws `NoSuchElementException` if no such element is found.

### 11. Common

```kotlin
public inline fun ByteArray.first(predicate: (Byte) -> Boolean): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1232)

Returns the first element matching the given `predicate`.
@throws `NoSuchElementException` if no such element is found.

### 12. Common

```kotlin
public inline fun ShortArray.first(predicate: (Short) -> Boolean): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1241)

Returns the first element matching the given `predicate`.
@throws `NoSuchElementException` if no such element is found.

### 13. Common

```kotlin
public inline fun IntArray.first(predicate: (Int) -> Boolean): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1250)

Returns the first element matching the given `predicate`.
@throws `NoSuchElementException` if no such element is found.

### 14. Common

```kotlin
public inline fun LongArray.first(predicate: (Long) -> Boolean): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1259)

Returns the first element matching the given `predicate`.
@throws `NoSuchElementException` if no such element is found.

### 15. Common

```kotlin
public inline fun FloatArray.first(predicate: (Float) -> Boolean): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1268)

Returns the first element matching the given `predicate`.
@throws `NoSuchElementException` if no such element is found.

### 16. Common

```kotlin
public inline fun DoubleArray.first(predicate: (Double) -> Boolean): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1277)

Returns the first element matching the given `predicate`.
@throws `NoSuchElementException` if no such element is found.

### 17. Common

```kotlin
public inline fun BooleanArray.first(predicate: (Boolean) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1286)

Returns the first element matching the given `predicate`.
@throws `NoSuchElementException` if no such element is found.

### 18. Common

```kotlin
public inline fun CharArray.first(predicate: (Char) -> Boolean): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1295)

Returns the first element matching the given `predicate`.
@throws `NoSuchElementException` if no such element is found.

### 19. Common

```kotlin
public fun <T> Iterable<T>.first(): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L198)

Returns the first element.

@throws NoSuchElementException if the collection is empty.

### 20. Common

```kotlin
public fun <T> List<T>.first(): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L215)

Returns the first element.

@throws NoSuchElementException if the list is empty.

### 21. Common

```kotlin
public inline fun <T> Iterable<T>.first(predicate: (T) -> Boolean): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L226)

Returns the first element matching the given `predicate`.
@throws `NoSuchElementException` if no such element is found.

### 22. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.first(): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L563)

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.first(): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L575)

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.first(): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L587)

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.first(): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L599)

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.first(predicate: (UInt) -> Boolean): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L611)

Returns the first element matching the given `predicate`.
@throws `NoSuchElementException` if no such element is found.

### 27. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.first(predicate: (ULong) -> Boolean): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L623)

Returns the first element matching the given `predicate`.
@throws `NoSuchElementException` if no such element is found.

### 28. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.first(predicate: (UByte) -> Boolean): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L635)

Returns the first element matching the given `predicate`.
@throws `NoSuchElementException` if no such element is found.

### 29. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.first(predicate: (UShort) -> Boolean): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L647)

Returns the first element matching the given `predicate`.
@throws `NoSuchElementException` if no such element is found.

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
    val result = source.`first`()
    println(result)
}
```

```text title="Output"
1
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
