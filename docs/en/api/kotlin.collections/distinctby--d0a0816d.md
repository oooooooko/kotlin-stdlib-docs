# distinctBy

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a list containing only elements from the given array
having distinct keys returned by the given `selector` function.

Among elements of the given array with equal keys, only the first one will be present in the resulting list.
The elements in the resulting list are in the same order as they were in the source array.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <T, K> Array<out T>.distinctBy(selector: (T) -> K): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13462)

### 2. Common

```kotlin
public inline fun <K> ByteArray.distinctBy(selector: (Byte) -> K): List<Byte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13482)

Returns a list containing only elements from the given array
having distinct keys returned by the given `selector` function.

The elements in the resulting list are in the same order as they were in the source array.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

### 3. Common

```kotlin
public inline fun <K> ShortArray.distinctBy(selector: (Short) -> K): List<Short>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13501)

Returns a list containing only elements from the given array
having distinct keys returned by the given `selector` function.

The elements in the resulting list are in the same order as they were in the source array.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

### 4. Common

```kotlin
public inline fun <K> IntArray.distinctBy(selector: (Int) -> K): List<Int>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13520)

Returns a list containing only elements from the given array
having distinct keys returned by the given `selector` function.

The elements in the resulting list are in the same order as they were in the source array.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

### 5. Common

```kotlin
public inline fun <K> LongArray.distinctBy(selector: (Long) -> K): List<Long>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13539)

Returns a list containing only elements from the given array
having distinct keys returned by the given `selector` function.

The elements in the resulting list are in the same order as they were in the source array.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

### 6. Common

```kotlin
public inline fun <K> FloatArray.distinctBy(selector: (Float) -> K): List<Float>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13558)

Returns a list containing only elements from the given array
having distinct keys returned by the given `selector` function.

The elements in the resulting list are in the same order as they were in the source array.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

### 7. Common

```kotlin
public inline fun <K> DoubleArray.distinctBy(selector: (Double) -> K): List<Double>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13577)

Returns a list containing only elements from the given array
having distinct keys returned by the given `selector` function.

The elements in the resulting list are in the same order as they were in the source array.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

### 8. Common

```kotlin
public inline fun <K> BooleanArray.distinctBy(selector: (Boolean) -> K): List<Boolean>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13596)

Returns a list containing only elements from the given array
having distinct keys returned by the given `selector` function.

The elements in the resulting list are in the same order as they were in the source array.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

### 9. Common

```kotlin
public inline fun <K> CharArray.distinctBy(selector: (Char) -> K): List<Char>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13615)

Returns a list containing only elements from the given array
having distinct keys returned by the given `selector` function.

The elements in the resulting list are in the same order as they were in the source array.

@sample samples.collections.Collections.Transformations.distinctAndDistinctBy

### 10. Common

```kotlin
public inline fun <T, K> Iterable<T>.distinctBy(selector: (T) -> K): List<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1845)

Returns a list containing only elements from the given collection
having distinct keys returned by the given `selector` function.

Among elements of the given collection with equal keys, only the first one will be present in the resulting list.
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
