# onEachIndexed

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Performs the given `action` on each element, providing sequential index with the element,
and returns the array itself afterwards.
@param `action` function that takes the index of an element and the element itself
and performs the action on the element.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun <T> Array<out T>.onEachIndexed(action: (index: Int, T) -> Unit): Array<out T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22489)

### 2. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun ByteArray.onEachIndexed(action: (index: Int, Byte) -> Unit): ByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22501)

### 3. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun ShortArray.onEachIndexed(action: (index: Int, Short) -> Unit): ShortArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22513)

### 4. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun IntArray.onEachIndexed(action: (index: Int, Int) -> Unit): IntArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22525)

### 5. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun LongArray.onEachIndexed(action: (index: Int, Long) -> Unit): LongArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22537)

### 6. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun FloatArray.onEachIndexed(action: (index: Int, Float) -> Unit): FloatArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22549)

### 7. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun DoubleArray.onEachIndexed(action: (index: Int, Double) -> Unit): DoubleArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22561)

### 8. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun BooleanArray.onEachIndexed(action: (index: Int, Boolean) -> Unit): BooleanArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22573)

### 9. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun CharArray.onEachIndexed(action: (index: Int, Char) -> Unit): CharArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22585)

### 10. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <T, C : Iterable<T>> C.onEachIndexed(action: (index: Int, T) -> Unit): C
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3089)

Performs the given `action` on each element, providing sequential index with the element,
and returns the collection itself afterwards.
@param `action` function that takes the index of an element and the element itself
and performs the action on the element.

### 11. Common

```kotlin
@SinceKotlin("1.4")
public inline fun <K, V, M : Map<out K, V>> M.onEachIndexed(action: (index: Int, Map.Entry<K, V>) -> Unit): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L648)

Performs the given `action` on each entry, providing sequential index with the entry,
and returns the map itself afterwards.
@param `action` function that takes the index of an entry and the entry itself
and performs the action on the entry.

### 12. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.onEachIndexed(action: (index: Int, UInt) -> Unit): UIntArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9883)

### 13. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.onEachIndexed(action: (index: Int, ULong) -> Unit): ULongArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9896)

### 14. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.onEachIndexed(action: (index: Int, UByte) -> Unit): UByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9909)

### 15. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.onEachIndexed(action: (index: Int, UShort) -> Unit): UShortArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9922)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*

private class OperationOnRange<E, R>(
        val element: E,
        val fromIndex: Int,
        val toIndex: Int,
        val expectedResult: R
    )

private fun UIntArray.toUByteArray(): UByteArray {
    return UByteArray(size) { get(it).toUByte() }
}

private fun UIntArray.toUShortArray(): UShortArray {
    return UShortArray(size) { get(it).toUShort() }
}

private fun UIntArray.toULongArray(): ULongArray {
    return ULongArray(size) { get(it).toULong() }
}

fun main() {

        println(mutableListOf<UInt>().apply { uintArrayOf(1u, 2u, 3u).onEachIndexed { i, e -> add(i.toUInt() + e) } })
        println(mutableListOf<UInt>().apply { ubyteArrayOf(1u, 2u, 3u).onEachIndexed { i, e -> add(i.toUByte() + e) } })
        println(mutableListOf<UInt>().apply { ushortArrayOf(1u, 2u, 3u).onEachIndexed { i, e -> add(i.toUShort() + e) } })
        println(mutableListOf<ULong>().apply { ulongArrayOf(1u, 2u, 3u).onEachIndexed { i, e -> add(i.toULong() + e) } })

        val empty = arrayOf<UInt>()
        println(empty === empty.onEachIndexed { i, e -> fail("Should be unreachable: $i, $e") })

        // Identity equality for arguments of types ULongArray and ULongArray is forbidden
//        val nonEmpty = ulongArrayOf(1, 2, 3)
//        assertSame(nonEmpty, nonEmpty.onEachIndexed { _, _ -> })
    
}
```

```text title="Output"
[1, 3, 5]
[1, 3, 5]
[1, 3, 5]
[1, 3, 5]
true
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/UnsignedArraysTest.kt#L1067)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
