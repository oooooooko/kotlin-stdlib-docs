# partition

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Splits the original array into a pair of lists,
where *first* list contains elements for which `predicate` yielded `true`,
while *second* list contains elements for which `predicate` yielded `false`.

@sample samples.collections.Arrays.Transformations.partitionArrayOfPrimitives

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <T> Array<out T>.partition(predicate: (T) -> Boolean): Pair<List<T>, List<T>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26273)

### 2. Common

```kotlin
public inline fun ByteArray.partition(predicate: (Byte) -> Boolean): Pair<List<Byte>, List<Byte>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26293)

### 3. Common

```kotlin
public inline fun ShortArray.partition(predicate: (Short) -> Boolean): Pair<List<Short>, List<Short>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26313)

### 4. Common

```kotlin
public inline fun IntArray.partition(predicate: (Int) -> Boolean): Pair<List<Int>, List<Int>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26333)

### 5. Common

```kotlin
public inline fun LongArray.partition(predicate: (Long) -> Boolean): Pair<List<Long>, List<Long>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26353)

### 6. Common

```kotlin
public inline fun FloatArray.partition(predicate: (Float) -> Boolean): Pair<List<Float>, List<Float>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26373)

### 7. Common

```kotlin
public inline fun DoubleArray.partition(predicate: (Double) -> Boolean): Pair<List<Double>, List<Double>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26393)

### 8. Common

```kotlin
public inline fun BooleanArray.partition(predicate: (Boolean) -> Boolean): Pair<List<Boolean>, List<Boolean>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26413)

### 9. Common

```kotlin
public inline fun CharArray.partition(predicate: (Char) -> Boolean): Pair<List<Char>, List<Char>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26433)

### 10. Common

```kotlin
public inline fun <T> Iterable<T>.partition(predicate: (T) -> Boolean): Pair<List<T>, List<T>>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3623)

Splits the original collection into a pair of lists,
where *first* list contains elements for which `predicate` yielded `true`,
while *second* list contains elements for which `predicate` yielded `false`.

@sample samples.collections.Iterables.Operations.partition

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    data class Person(val name: String, val age: Int) {
        override fun toString(): String {
            return "$name - $age"
        }
    }

    val list = listOf(Person("Tom", 18), Person("Andy", 32), Person("Sarah", 22))
    val result = list.partition { it.age < 30 }
    println(result)
}
```

```text title="Output"
([Tom - 18, Sarah - 22], [Andy - 32])
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/iterables.kt#L75)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
