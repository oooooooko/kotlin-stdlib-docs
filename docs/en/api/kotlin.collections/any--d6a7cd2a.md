# any

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if array has at least one element.

@sample samples.collections.Collections.Aggregates.any

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Array<out T>.any(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15222)

### 2. Common

```kotlin
public fun ByteArray.any(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15231)

### 3. Common

```kotlin
public fun ShortArray.any(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15240)

### 4. Common

```kotlin
public fun IntArray.any(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15249)

### 5. Common

```kotlin
public fun LongArray.any(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15258)

### 6. Common

```kotlin
public fun FloatArray.any(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15267)

### 7. Common

```kotlin
public fun DoubleArray.any(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15276)

### 8. Common

```kotlin
public fun BooleanArray.any(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15285)

### 9. Common

```kotlin
public fun CharArray.any(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15294)

### 10. Common

```kotlin
public inline fun <T> Array<out T>.any(predicate: (T) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15303)

Returns `true` if at least one element matches the given `predicate`.

@sample samples.collections.Collections.Aggregates.anyWithPredicate

### 11. Common

```kotlin
public inline fun ByteArray.any(predicate: (Byte) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15313)

Returns `true` if at least one element matches the given `predicate`.

@sample samples.collections.Collections.Aggregates.anyWithPredicate

### 12. Common

```kotlin
public inline fun ShortArray.any(predicate: (Short) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15323)

Returns `true` if at least one element matches the given `predicate`.

@sample samples.collections.Collections.Aggregates.anyWithPredicate

### 13. Common

```kotlin
public inline fun IntArray.any(predicate: (Int) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15333)

Returns `true` if at least one element matches the given `predicate`.

@sample samples.collections.Collections.Aggregates.anyWithPredicate

### 14. Common

```kotlin
public inline fun LongArray.any(predicate: (Long) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15343)

Returns `true` if at least one element matches the given `predicate`.

@sample samples.collections.Collections.Aggregates.anyWithPredicate

### 15. Common

```kotlin
public inline fun FloatArray.any(predicate: (Float) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15353)

Returns `true` if at least one element matches the given `predicate`.

@sample samples.collections.Collections.Aggregates.anyWithPredicate

### 16. Common

```kotlin
public inline fun DoubleArray.any(predicate: (Double) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15363)

Returns `true` if at least one element matches the given `predicate`.

@sample samples.collections.Collections.Aggregates.anyWithPredicate

### 17. Common

```kotlin
public inline fun BooleanArray.any(predicate: (Boolean) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15373)

Returns `true` if at least one element matches the given `predicate`.

@sample samples.collections.Collections.Aggregates.anyWithPredicate

### 18. Common

```kotlin
public inline fun CharArray.any(predicate: (Char) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15383)

Returns `true` if at least one element matches the given `predicate`.

@sample samples.collections.Collections.Aggregates.anyWithPredicate

### 19. Common

```kotlin
public fun <T> Iterable<T>.any(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2075)

Returns `true` if collection has at least one element.

@sample samples.collections.Collections.Aggregates.any

### 20. Common

```kotlin
public inline fun <T> Iterable<T>.any(predicate: (T) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2085)

Returns `true` if at least one element matches the given `predicate`.

@sample samples.collections.Collections.Aggregates.anyWithPredicate

### 21. Common

```kotlin
public fun <K, V> Map<out K, V>.any(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L178)

Returns `true` if map has at least one entry.

@sample samples.collections.Collections.Aggregates.any

### 22. Common

```kotlin
public inline fun <K, V> Map<out K, V>.any(predicate: (Map.Entry<K, V>) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L187)

Returns `true` if at least one entry matches the given `predicate`.

@sample samples.collections.Collections.Aggregates.anyWithPredicate

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.any(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6471)

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.any(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6483)

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.any(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6495)

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.any(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6507)

### 27. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.any(predicate: (UInt) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6519)

Returns `true` if at least one element matches the given `predicate`.

@sample samples.collections.Collections.Aggregates.anyWithPredicate

### 28. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.any(predicate: (ULong) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6532)

Returns `true` if at least one element matches the given `predicate`.

@sample samples.collections.Collections.Aggregates.anyWithPredicate

### 29. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.any(predicate: (UByte) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6545)

Returns `true` if at least one element matches the given `predicate`.

@sample samples.collections.Collections.Aggregates.anyWithPredicate

### 30. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.any(predicate: (UShort) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6558)

Returns `true` if at least one element matches the given `predicate`.

@sample samples.collections.Collections.Aggregates.anyWithPredicate

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val emptyList = emptyList<Int>()
    println(emptyList.any())

    val nonEmptyList = listOf(1, 2, 3)
    println(nonEmptyList.any())
}
```

```text title="Output"
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1020)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val isEven: (Int) -> Boolean = { it % 2 == 0 }
    val zeroToTen = 0..10
    println(zeroToTen.any { isEven(it) })
    println(zeroToTen.any(isEven))

    val odds = zeroToTen.map { it * 2 + 1 }
    println(odds.any { isEven(it) })

    val emptyList = emptyList<Int>()
    println(emptyList.any { true })
}
```

```text title="Output"
true
true
false
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1029)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
