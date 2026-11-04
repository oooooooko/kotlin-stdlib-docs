# findLast

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the last element matching the given `predicate`, or `null` if no such element was found.

@sample samples.collections.Collections.Elements.find

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Array<out T>.findLast(predicate: (T) -> Boolean): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1034)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun ByteArray.findLast(predicate: (Byte) -> Boolean): Byte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1044)

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun ShortArray.findLast(predicate: (Short) -> Boolean): Short?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1054)

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun IntArray.findLast(predicate: (Int) -> Boolean): Int?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1064)

### 5. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun LongArray.findLast(predicate: (Long) -> Boolean): Long?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1074)

### 6. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun FloatArray.findLast(predicate: (Float) -> Boolean): Float?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1084)

### 7. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun DoubleArray.findLast(predicate: (Double) -> Boolean): Double?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1094)

### 8. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun BooleanArray.findLast(predicate: (Boolean) -> Boolean): Boolean?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1104)

### 9. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharArray.findLast(predicate: (Char) -> Boolean): Char?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1114)

### 10. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Iterable<T>.findLast(predicate: (T) -> Boolean): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L178)

### 11. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> List<T>.findLast(predicate: (T) -> Boolean): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L188)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.findLast(predicate: (UInt) -> Boolean): UInt?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L515)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.findLast(predicate: (ULong) -> Boolean): ULong?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L527)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.findLast(predicate: (UByte) -> Boolean): UByte?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L539)

### 15. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.findLast(predicate: (UShort) -> Boolean): UShort?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L551)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val numbers = listOf(1, 2, 3, 4, 5, 6, 7)
    val firstOdd = numbers.find { it % 2 != 0 }
    val lastEven = numbers.findLast { it % 2 == 0 }

    println(firstOdd)
    println(lastEven)
}
```

```text title="Output"
1
6
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1335)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
