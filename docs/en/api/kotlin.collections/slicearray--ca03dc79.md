# sliceArray

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns an array containing elements of this array at specified `indices`.

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Array<T>.sliceArray(indices: Collection<Int>): Array<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4755)

### 2. Common

```kotlin
public fun ByteArray.sliceArray(indices: Collection<Int>): ByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4767)

### 3. Common

```kotlin
public fun ShortArray.sliceArray(indices: Collection<Int>): ShortArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4779)

### 4. Common

```kotlin
public fun IntArray.sliceArray(indices: Collection<Int>): IntArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4791)

### 5. Common

```kotlin
public fun LongArray.sliceArray(indices: Collection<Int>): LongArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4803)

### 6. Common

```kotlin
public fun FloatArray.sliceArray(indices: Collection<Int>): FloatArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4815)

### 7. Common

```kotlin
public fun DoubleArray.sliceArray(indices: Collection<Int>): DoubleArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4827)

### 8. Common

```kotlin
public fun BooleanArray.sliceArray(indices: Collection<Int>): BooleanArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4839)

### 9. Common

```kotlin
public fun CharArray.sliceArray(indices: Collection<Int>): CharArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4851)

### 10. Common

```kotlin
public fun <T> Array<T>.sliceArray(indices: IntRange): Array<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4863)

Returns an array containing elements at indices in the specified `indices` range.

### 11. Common

```kotlin
public fun ByteArray.sliceArray(indices: IntRange): ByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4871)

Returns an array containing elements at indices in the specified `indices` range.

### 12. Common

```kotlin
public fun ShortArray.sliceArray(indices: IntRange): ShortArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4879)

Returns an array containing elements at indices in the specified `indices` range.

### 13. Common

```kotlin
public fun IntArray.sliceArray(indices: IntRange): IntArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4887)

Returns an array containing elements at indices in the specified `indices` range.

### 14. Common

```kotlin
public fun LongArray.sliceArray(indices: IntRange): LongArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4895)

Returns an array containing elements at indices in the specified `indices` range.

### 15. Common

```kotlin
public fun FloatArray.sliceArray(indices: IntRange): FloatArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4903)

Returns an array containing elements at indices in the specified `indices` range.

### 16. Common

```kotlin
public fun DoubleArray.sliceArray(indices: IntRange): DoubleArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4911)

Returns an array containing elements at indices in the specified `indices` range.

### 17. Common

```kotlin
public fun BooleanArray.sliceArray(indices: IntRange): BooleanArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4919)

Returns an array containing elements at indices in the specified `indices` range.

### 18. Common

```kotlin
public fun CharArray.sliceArray(indices: IntRange): CharArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4927)

Returns an array containing elements at indices in the specified `indices` range.

### 19. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.sliceArray(indices: Collection<Int>): UIntArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2363)

### 20. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.sliceArray(indices: Collection<Int>): ULongArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2372)

### 21. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.sliceArray(indices: Collection<Int>): UByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2381)

### 22. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.sliceArray(indices: Collection<Int>): UShortArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2390)

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.sliceArray(indices: IntRange): UIntArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2399)

Returns an array containing elements at indices in the specified `indices` range.

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.sliceArray(indices: IntRange): ULongArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2408)

Returns an array containing elements at indices in the specified `indices` range.

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.sliceArray(indices: IntRange): UByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2417)

Returns an array containing elements at indices in the specified `indices` range.

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.sliceArray(indices: IntRange): UShortArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2426)

Returns an array containing elements at indices in the specified `indices` range.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid = Uuid.parse("550e8400-e29b-41d4-a716-446655440000")
    val bytes = ByteArray(20)
    val buffer = java.nio.ByteBuffer.wrap(bytes)
    buffer.putUuid(index = 2, uuid)

    // The written 16 bytes are exactly equal to the uuid bytes
    val writtenBytes = bytes.sliceArray(2..<18)
    println(writtenBytes.contentEquals(uuid.toByteArray()))
}
```

```text title="Output"
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L47)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
