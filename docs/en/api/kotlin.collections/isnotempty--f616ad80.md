# isNotEmpty

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns `true` if the array is not empty.

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Array<out T>.isNotEmpty(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9414)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun ByteArray.isNotEmpty(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9422)

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun ShortArray.isNotEmpty(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9430)

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun IntArray.isNotEmpty(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9438)

### 5. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun LongArray.isNotEmpty(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9446)

### 6. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun FloatArray.isNotEmpty(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9454)

### 7. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun DoubleArray.isNotEmpty(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9462)

### 8. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun BooleanArray.isNotEmpty(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9470)

### 9. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharArray.isNotEmpty(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9478)

### 10. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Collection<T>.isNotEmpty(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L239)

Returns `true` if the collection is not empty.
@sample samples.collections.Collections.Collections.collectionIsNotEmpty

### 11. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <K, V> Map<out K, V>.isNotEmpty(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L199)

Returns `true` if this map is not empty.
@sample samples.collections.Maps.Usage.mapIsNotEmpty

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val empty = emptyList<Any>()
    println(empty.isNotEmpty())

    val collection = listOf('a', 'b', 'c')
    println(collection.isNotEmpty())
}
```

```text title="Output"
false
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L26)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
