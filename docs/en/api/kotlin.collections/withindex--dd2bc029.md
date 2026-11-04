# withIndex

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a lazy `Iterable` that wraps each element of the original array
into an `IndexedValue` containing the index of that element and the element itself.

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Array<out T>.withIndex(): Iterable<IndexedValue<T>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13290)

### 2. Common

```kotlin
public fun ByteArray.withIndex(): Iterable<IndexedValue<Byte>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13298)

### 3. Common

```kotlin
public fun ShortArray.withIndex(): Iterable<IndexedValue<Short>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13306)

### 4. Common

```kotlin
public fun IntArray.withIndex(): Iterable<IndexedValue<Int>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13314)

### 5. Common

```kotlin
public fun LongArray.withIndex(): Iterable<IndexedValue<Long>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13322)

### 6. Common

```kotlin
public fun FloatArray.withIndex(): Iterable<IndexedValue<Float>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13330)

### 7. Common

```kotlin
public fun DoubleArray.withIndex(): Iterable<IndexedValue<Double>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13338)

### 8. Common

```kotlin
public fun BooleanArray.withIndex(): Iterable<IndexedValue<Boolean>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13346)

### 9. Common

```kotlin
public fun CharArray.withIndex(): Iterable<IndexedValue<Char>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13354)

### 10. Common

```kotlin
public fun <T> Iterable<T>.withIndex(): Iterable<IndexedValue<T>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1825)

Returns a lazy `Iterable` that wraps each element of the original collection
into an `IndexedValue` containing the index of that element and the element itself.

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.withIndex(): Iterable<IndexedValue<UInt>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5935)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.withIndex(): Iterable<IndexedValue<ULong>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5945)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.withIndex(): Iterable<IndexedValue<UByte>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5955)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.withIndex(): Iterable<IndexedValue<UShort>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5965)

### 15. Common

```kotlin
public fun <T> Iterator<T>.withIndex(): Iterator<IndexedValue<T>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Iterators.kt#L19)

Returns an `Iterator` that wraps each element produced by the original iterator
into an `IndexedValue` containing the index of that element and the element itself.

@sample samples.collections.Iterators.withIndexIterator

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    val iterator = ('a'..'c').iterator()

    for ((index, value) in iterator.withIndex()) {
        println("The element at $index is $value")
    }
}
```

```text title="Output"
The element at 0 is a
The element at 1 is b
The element at 2 is c
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/iterators.kt#L55)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
