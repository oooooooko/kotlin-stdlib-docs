# none

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if the array has no elements.

@sample samples.collections.Collections.Aggregates.none

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Array<out T>.none(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22237)

### 2. Common

```kotlin
public fun ByteArray.none(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22246)

### 3. Common

```kotlin
public fun ShortArray.none(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22255)

### 4. Common

```kotlin
public fun IntArray.none(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22264)

### 5. Common

```kotlin
public fun LongArray.none(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22273)

### 6. Common

```kotlin
public fun FloatArray.none(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22282)

### 7. Common

```kotlin
public fun DoubleArray.none(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22291)

### 8. Common

```kotlin
public fun BooleanArray.none(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22300)

### 9. Common

```kotlin
public fun CharArray.none(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22309)

### 10. Common

```kotlin
public inline fun <T> Array<out T>.none(predicate: (T) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22318)

Returns `true` if no elements match the given `predicate`.

@sample samples.collections.Collections.Aggregates.noneWithPredicate

### 11. Common

```kotlin
public inline fun ByteArray.none(predicate: (Byte) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22328)

Returns `true` if no elements match the given `predicate`.

@sample samples.collections.Collections.Aggregates.noneWithPredicate

### 12. Common

```kotlin
public inline fun ShortArray.none(predicate: (Short) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22338)

Returns `true` if no elements match the given `predicate`.

@sample samples.collections.Collections.Aggregates.noneWithPredicate

### 13. Common

```kotlin
public inline fun IntArray.none(predicate: (Int) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22348)

Returns `true` if no elements match the given `predicate`.

@sample samples.collections.Collections.Aggregates.noneWithPredicate

### 14. Common

```kotlin
public inline fun LongArray.none(predicate: (Long) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22358)

Returns `true` if no elements match the given `predicate`.

@sample samples.collections.Collections.Aggregates.noneWithPredicate

### 15. Common

```kotlin
public inline fun FloatArray.none(predicate: (Float) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22368)

Returns `true` if no elements match the given `predicate`.

@sample samples.collections.Collections.Aggregates.noneWithPredicate

### 16. Common

```kotlin
public inline fun DoubleArray.none(predicate: (Double) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22378)

Returns `true` if no elements match the given `predicate`.

@sample samples.collections.Collections.Aggregates.noneWithPredicate

### 17. Common

```kotlin
public inline fun BooleanArray.none(predicate: (Boolean) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22388)

Returns `true` if no elements match the given `predicate`.

@sample samples.collections.Collections.Aggregates.noneWithPredicate

### 18. Common

```kotlin
public inline fun CharArray.none(predicate: (Char) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22398)

Returns `true` if no elements match the given `predicate`.

@sample samples.collections.Collections.Aggregates.noneWithPredicate

### 19. Common

```kotlin
public fun <T> Iterable<T>.none(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3060)

Returns `true` if the collection has no elements.

@sample samples.collections.Collections.Aggregates.none

### 20. Common

```kotlin
public inline fun <T> Iterable<T>.none(predicate: (T) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3070)

Returns `true` if no elements match the given `predicate`.

@sample samples.collections.Collections.Aggregates.noneWithPredicate

### 21. Common

```kotlin
public fun <K, V> Map<out K, V>.none(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L620)

Returns `true` if the map has no entries.

@sample samples.collections.Collections.Aggregates.none

### 22. Common

```kotlin
public inline fun <K, V> Map<out K, V>.none(predicate: (Map.Entry<K, V>) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L629)

Returns `true` if no entries match the given `predicate`.

@sample samples.collections.Collections.Aggregates.noneWithPredicate

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.none(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9743)

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.none(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9755)

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.none(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9767)

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.none(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9779)

### 27. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.none(predicate: (UInt) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9791)

Returns `true` if no elements match the given `predicate`.

@sample samples.collections.Collections.Aggregates.noneWithPredicate

### 28. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.none(predicate: (ULong) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9804)

Returns `true` if no elements match the given `predicate`.

@sample samples.collections.Collections.Aggregates.noneWithPredicate

### 29. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.none(predicate: (UByte) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9817)

Returns `true` if no elements match the given `predicate`.

@sample samples.collections.Collections.Aggregates.noneWithPredicate

### 30. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.none(predicate: (UShort) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9830)

Returns `true` if no elements match the given `predicate`.

@sample samples.collections.Collections.Aggregates.noneWithPredicate

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val emptyList = emptyList<Int>()
    println(emptyList.none())

    val nonEmptyList = listOf("one", "two", "three")
    println(nonEmptyList.none())
}
```

```text title="Output"
true
false
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L997)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val isEven: (Int) -> Boolean = { it % 2 == 0 }
    val zeroToTen = 0..10
    println(zeroToTen.none { isEven(it) })
    println(zeroToTen.none(isEven))

    val odds = zeroToTen.map { it * 2 + 1 }
    println(odds.none { isEven(it) })

    val emptyList = emptyList<Int>()
    println(emptyList.none { true })
}
```

```text title="Output"
false
false
true
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1006)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
