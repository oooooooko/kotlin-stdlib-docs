# lastOrNull

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the last element, or `null` if the array is empty.

@sample samples.collections.Collections.Elements.last

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Array<out T>.lastOrNull(): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2375)

### 2. Common

```kotlin
public fun ByteArray.lastOrNull(): Byte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2384)

### 3. Common

```kotlin
public fun ShortArray.lastOrNull(): Short?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2393)

### 4. Common

```kotlin
public fun IntArray.lastOrNull(): Int?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2402)

### 5. Common

```kotlin
public fun LongArray.lastOrNull(): Long?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2411)

### 6. Common

```kotlin
public fun FloatArray.lastOrNull(): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2420)

### 7. Common

```kotlin
public fun DoubleArray.lastOrNull(): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2429)

### 8. Common

```kotlin
public fun BooleanArray.lastOrNull(): Boolean?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2438)

### 9. Common

```kotlin
public fun CharArray.lastOrNull(): Char?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2447)

### 10. Common

```kotlin
public inline fun <T> Array<out T>.lastOrNull(predicate: (T) -> Boolean): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2456)

Returns the last element matching the given `predicate`, or `null` if no such element was found.

@sample samples.collections.Collections.Elements.last

### 11. Common

```kotlin
public inline fun ByteArray.lastOrNull(predicate: (Byte) -> Boolean): Byte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2469)

Returns the last element matching the given `predicate`, or `null` if no such element was found.

@sample samples.collections.Collections.Elements.last

### 12. Common

```kotlin
public inline fun ShortArray.lastOrNull(predicate: (Short) -> Boolean): Short?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2482)

Returns the last element matching the given `predicate`, or `null` if no such element was found.

@sample samples.collections.Collections.Elements.last

### 13. Common

```kotlin
public inline fun IntArray.lastOrNull(predicate: (Int) -> Boolean): Int?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2495)

Returns the last element matching the given `predicate`, or `null` if no such element was found.

@sample samples.collections.Collections.Elements.last

### 14. Common

```kotlin
public inline fun LongArray.lastOrNull(predicate: (Long) -> Boolean): Long?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2508)

Returns the last element matching the given `predicate`, or `null` if no such element was found.

@sample samples.collections.Collections.Elements.last

### 15. Common

```kotlin
public inline fun FloatArray.lastOrNull(predicate: (Float) -> Boolean): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2521)

Returns the last element matching the given `predicate`, or `null` if no such element was found.

@sample samples.collections.Collections.Elements.last

### 16. Common

```kotlin
public inline fun DoubleArray.lastOrNull(predicate: (Double) -> Boolean): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2534)

Returns the last element matching the given `predicate`, or `null` if no such element was found.

@sample samples.collections.Collections.Elements.last

### 17. Common

```kotlin
public inline fun BooleanArray.lastOrNull(predicate: (Boolean) -> Boolean): Boolean?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2547)

Returns the last element matching the given `predicate`, or `null` if no such element was found.

@sample samples.collections.Collections.Elements.last

### 18. Common

```kotlin
public inline fun CharArray.lastOrNull(predicate: (Char) -> Boolean): Char?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2560)

Returns the last element matching the given `predicate`, or `null` if no such element was found.

@sample samples.collections.Collections.Elements.last

### 19. Common

```kotlin
public fun <T> Iterable<T>.lastOrNull(): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L496)

Returns the last element, or `null` if the collection is empty.

@sample samples.collections.Collections.Elements.last

### 20. Common

```kotlin
public fun <T> List<T>.lastOrNull(): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L516)

Returns the last element, or `null` if the list is empty.

@sample samples.collections.Collections.Elements.last

### 21. Common

```kotlin
public inline fun <T> Iterable<T>.lastOrNull(predicate: (T) -> Boolean): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L525)

Returns the last element matching the given `predicate`, or `null` if no such element was found.

@sample samples.collections.Collections.Elements.last

### 22. Common

```kotlin
public inline fun <T> List<T>.lastOrNull(predicate: (T) -> Boolean): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L540)

Returns the last element matching the given `predicate`, or `null` if no such element was found.

@sample samples.collections.Collections.Elements.last

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.lastOrNull(): UInt?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1131)

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.lastOrNull(): ULong?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1142)

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.lastOrNull(): UByte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1153)

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.lastOrNull(): UShort?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1164)

### 27. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.lastOrNull(predicate: (UInt) -> Boolean): UInt?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1175)

Returns the last element matching the given `predicate`, or `null` if no such element was found.

@sample samples.collections.Collections.Elements.last

### 28. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.lastOrNull(predicate: (ULong) -> Boolean): ULong?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1191)

Returns the last element matching the given `predicate`, or `null` if no such element was found.

@sample samples.collections.Collections.Elements.last

### 29. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.lastOrNull(predicate: (UByte) -> Boolean): UByte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1207)

Returns the last element matching the given `predicate`, or `null` if no such element was found.

@sample samples.collections.Collections.Elements.last

### 30. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.lastOrNull(predicate: (UShort) -> Boolean): UShort?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1223)

Returns the last element matching the given `predicate`, or `null` if no such element was found.

@sample samples.collections.Collections.Elements.last

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val list = listOf(1, 2, 3, 4)
    println(list.last())
    println(list.last { it % 2 == 1 })
    println(list.lastOrNull { it < 0 })
    assertFails { list.last { it < 0 } }

    val emptyList = emptyList<Int>()
    println(emptyList.lastOrNull())
    assertFails { emptyList.last() }
}
```

```text title="Output"
4
3
null
null
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1368)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
