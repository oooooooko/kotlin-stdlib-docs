# elementAt

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns an element at the given `index` or throws an `IndexOutOfBoundsException` if the `index` is out of bounds of this array.

@sample samples.collections.Collections.Elements.elementAt

## Declarations and overloads

### 1. Common

```kotlin
public expect fun <T> Array<out T>.elementAt(index: Int): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L674)

### 2. Common

```kotlin
public expect fun ByteArray.elementAt(index: Int): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L681)

### 3. Common

```kotlin
public expect fun ShortArray.elementAt(index: Int): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L688)

### 4. Common

```kotlin
public expect fun IntArray.elementAt(index: Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L695)

### 5. Common

```kotlin
public expect fun LongArray.elementAt(index: Int): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L702)

### 6. Common

```kotlin
public expect fun FloatArray.elementAt(index: Int): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L709)

### 7. Common

```kotlin
public expect fun DoubleArray.elementAt(index: Int): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L716)

### 8. Common

```kotlin
public expect fun BooleanArray.elementAt(index: Int): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L723)

### 9. Common

```kotlin
public expect fun CharArray.elementAt(index: Int): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L730)

### 10. Common

```kotlin
public fun <T> Iterable<T>.elementAt(index: Int): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L81)

Returns an element at the given `index` or throws an `IndexOutOfBoundsException` if the `index` is out of bounds of this collection.

@sample samples.collections.Collections.Elements.elementAt

### 11. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> List<T>.elementAt(index: Int): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L92)

Returns an element at the given `index` or throws an `IndexOutOfBoundsException` if the `index` is out of bounds of this list.

@sample samples.collections.Collections.Elements.elementAt

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public expect fun UIntArray.elementAt(index: Int): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L323)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public expect fun ULongArray.elementAt(index: Int): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L332)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public expect fun UByteArray.elementAt(index: Int): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L341)

### 15. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public expect fun UShortArray.elementAt(index: Int): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L350)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val list = listOf(1, 2, 3)
    println(list.elementAt(0))
    println(list.elementAt(2))
    assertFailsWith<IndexOutOfBoundsException> { list.elementAt(3) }

    val emptyList = emptyList<Int>()
    assertFailsWith<IndexOutOfBoundsException> { emptyList.elementAt(0) }
}
```

```text title="Output"
1
3
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1302)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
