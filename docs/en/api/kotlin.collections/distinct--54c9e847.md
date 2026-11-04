# distinct

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a list containing only distinct elements from the given array.

Among equal elements of the given array, only the first one will be present in the resulting list.
The elements in the resulting list are in the same order as they were in the source array.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

## Declarations and overloads

### 1. Common

```kotlin
public fun <T> Array<out T>.distinct(): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13362)

### 2. Common

```kotlin
public fun ByteArray.distinct(): List<Byte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13374)

Returns a list containing only distinct elements from the given array.

The elements in the resulting list are in the same order as they were in the source array.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

### 3. Common

```kotlin
public fun ShortArray.distinct(): List<Short>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13385)

Returns a list containing only distinct elements from the given array.

The elements in the resulting list are in the same order as they were in the source array.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

### 4. Common

```kotlin
public fun IntArray.distinct(): List<Int>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13396)

Returns a list containing only distinct elements from the given array.

The elements in the resulting list are in the same order as they were in the source array.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

### 5. Common

```kotlin
public fun LongArray.distinct(): List<Long>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13407)

Returns a list containing only distinct elements from the given array.

The elements in the resulting list are in the same order as they were in the source array.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

### 6. Common

```kotlin
public fun FloatArray.distinct(): List<Float>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13418)

Returns a list containing only distinct elements from the given array.

The elements in the resulting list are in the same order as they were in the source array.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

### 7. Common

```kotlin
public fun DoubleArray.distinct(): List<Double>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13429)

Returns a list containing only distinct elements from the given array.

The elements in the resulting list are in the same order as they were in the source array.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

### 8. Common

```kotlin
public fun BooleanArray.distinct(): List<Boolean>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13440)

Returns a list containing only distinct elements from the given array.

The elements in the resulting list are in the same order as they were in the source array.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

### 9. Common

```kotlin
public fun CharArray.distinct(): List<Char>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13451)

Returns a list containing only distinct elements from the given array.

The elements in the resulting list are in the same order as they were in the source array.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

### 10. Common

```kotlin
public fun <T> Iterable<T>.distinct(): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1833)

Returns a list containing only distinct elements from the given collection.

Among equal elements of the given collection, only the first one will be present in the resulting list.
The elements in the resulting list are in the same order as they were in the source collection.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = listOf('a', 'A', 'b', 'B', 'A', 'a')
    println(list.distinct())
    println(list.distinctBy { it.uppercaseChar() })
}
```

```text title="Output"
[a, A, b, B]
[a, b]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L819)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
