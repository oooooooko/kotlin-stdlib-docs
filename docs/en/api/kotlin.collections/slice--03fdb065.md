# slice

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a list containing elements at indices in the specified `indices` range.

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Array<out T>.slice(indices: IntRange): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4566)

### 2. Common

```kotlin
public fun ByteArray.slice(indices: IntRange): List<Byte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4574)

### 3. Common

```kotlin
public fun ShortArray.slice(indices: IntRange): List<Short>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4582)

### 4. Common

```kotlin
public fun IntArray.slice(indices: IntRange): List<Int>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4590)

### 5. Common

```kotlin
public fun LongArray.slice(indices: IntRange): List<Long>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4598)

### 6. Common

```kotlin
public fun FloatArray.slice(indices: IntRange): List<Float>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4606)

### 7. Common

```kotlin
public fun DoubleArray.slice(indices: IntRange): List<Double>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4614)

### 8. Common

```kotlin
public fun BooleanArray.slice(indices: IntRange): List<Boolean>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4622)

### 9. Common

```kotlin
public fun CharArray.slice(indices: IntRange): List<Char>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4630)

### 10. Common

```kotlin
public fun <T> Array<out T>.slice(indices: Iterable<Int>): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4638)

Returns a list containing elements at specified `indices`.

### 11. Common

```kotlin
public fun ByteArray.slice(indices: Iterable<Int>): List<Byte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4651)

Returns a list containing elements at specified `indices`.

### 12. Common

```kotlin
public fun ShortArray.slice(indices: Iterable<Int>): List<Short>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4664)

Returns a list containing elements at specified `indices`.

### 13. Common

```kotlin
public fun IntArray.slice(indices: Iterable<Int>): List<Int>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4677)

Returns a list containing elements at specified `indices`.

### 14. Common

```kotlin
public fun LongArray.slice(indices: Iterable<Int>): List<Long>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4690)

Returns a list containing elements at specified `indices`.

### 15. Common

```kotlin
public fun FloatArray.slice(indices: Iterable<Int>): List<Float>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4703)

Returns a list containing elements at specified `indices`.

### 16. Common

```kotlin
public fun DoubleArray.slice(indices: Iterable<Int>): List<Double>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4716)

Returns a list containing elements at specified `indices`.

### 17. Common

```kotlin
public fun BooleanArray.slice(indices: Iterable<Int>): List<Boolean>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4729)

Returns a list containing elements at specified `indices`.

### 18. Common

```kotlin
public fun CharArray.slice(indices: Iterable<Int>): List<Char>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4742)

Returns a list containing elements at specified `indices`.

### 19. Common

```kotlin
public fun <T> List<T>.slice(indices: IntRange): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L877)

### 20. Common

```kotlin
public fun <T> List<T>.slice(indices: Iterable<Int>): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L885)

Returns a list containing elements at specified `indices`.

### 21. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.slice(indices: IntRange): List<UInt>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2263)

### 22. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.slice(indices: IntRange): List<ULong>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2273)

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.slice(indices: IntRange): List<UByte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2283)

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.slice(indices: IntRange): List<UShort>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2293)

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.slice(indices: Iterable<Int>): List<UInt>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2303)

Returns a list containing elements at specified `indices`.

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.slice(indices: Iterable<Int>): List<ULong>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2318)

Returns a list containing elements at specified `indices`.

### 27. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.slice(indices: Iterable<Int>): List<UByte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2333)

Returns a list containing elements at specified `indices`.

### 28. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.slice(indices: Iterable<Int>): List<UShort>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2348)

Returns a list containing elements at specified `indices`.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*

val data = listOf("foo", "bar")

val empty = listOf<String>()

fun main() {

        val list = listOf('A', 'B', 'C', 'D')

        println(list.slice(IntRange.EMPTY))

        // ABCD
        // 0123
        println(list.slice(1..3))
        println(list.slice(3 downTo 1))

        val iter = listOf(2, 0, 3)
        println(list.slice(iter))

        for (range in listOf(-1 until 0, 0 until 2, 2..2)) {
            val bounds = "range: $range"
            val exClass = IndexOutOfBoundsException::class
            assertFailsWith(exClass, bounds) { listOf("x").slice(range) }
            assertFailsWith(exClass, bounds) { listOf("x").slice(range.asIterable()) }
        }
    
}
```

```text title="Output"
[]
[B, C, D]
[D, C, B]
[C, A, D]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/ListSpecificTest.kt#L26)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
