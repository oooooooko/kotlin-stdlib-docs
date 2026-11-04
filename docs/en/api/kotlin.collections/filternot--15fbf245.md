# filterNot

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a list containing all elements not matching the given `predicate`.

@sample samples.collections.Collections.Filtering.filter

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <T> Array<out T>.filterNot(predicate: (T) -> Boolean): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4267)

### 2. Common

```kotlin
public inline fun ByteArray.filterNot(predicate: (Byte) -> Boolean): List<Byte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4276)

### 3. Common

```kotlin
public inline fun ShortArray.filterNot(predicate: (Short) -> Boolean): List<Short>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4285)

### 4. Common

```kotlin
public inline fun IntArray.filterNot(predicate: (Int) -> Boolean): List<Int>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4294)

### 5. Common

```kotlin
public inline fun LongArray.filterNot(predicate: (Long) -> Boolean): List<Long>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4303)

### 6. Common

```kotlin
public inline fun FloatArray.filterNot(predicate: (Float) -> Boolean): List<Float>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4312)

### 7. Common

```kotlin
public inline fun DoubleArray.filterNot(predicate: (Double) -> Boolean): List<Double>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4321)

### 8. Common

```kotlin
public inline fun BooleanArray.filterNot(predicate: (Boolean) -> Boolean): List<Boolean>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4330)

### 9. Common

```kotlin
public inline fun CharArray.filterNot(predicate: (Char) -> Boolean): List<Char>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4339)

### 10. Common

```kotlin
public inline fun <T> Iterable<T>.filterNot(predicate: (T) -> Boolean): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L826)

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.filterNot(predicate: (UInt) -> Boolean): List<UInt>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2103)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.filterNot(predicate: (ULong) -> Boolean): List<ULong>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2115)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.filterNot(predicate: (UByte) -> Boolean): List<UByte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2127)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.filterNot(predicate: (UShort) -> Boolean): List<UShort>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2139)

### 15. Common

```kotlin
public inline fun <K, V> Map<out K, V>.filterNot(predicate: (Map.Entry<K, V>) -> Boolean): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L703)

Returns a new map containing all key-value pairs not matching the given `predicate`.

The returned map preserves the entry iteration order of the original map.
@sample samples.collections.Maps.Filtering.filterNot

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val numbers: List<Int> = listOf(1, 2, 3, 4, 5, 6, 7)
    val evenNumbers = numbers.filter { it % 2 == 0 }
    val notMultiplesOf3 = numbers.filterNot { number -> number % 3 == 0 }

    println(evenNumbers)
    println(notMultiplesOf3)
}
```

```text title="Output"
[2, 4, 6]
[1, 2, 4, 5, 7]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1565)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
