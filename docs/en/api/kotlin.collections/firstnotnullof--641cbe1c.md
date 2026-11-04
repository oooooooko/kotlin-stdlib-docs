# firstNotNullOf

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the first non-null value produced by `transform` function being applied to elements of this array in iteration order,
or throws `NoSuchElementException` if no non-null value was produced.

@sample samples.collections.Collections.Transformations.firstNotNullOf

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun <T, R : Any> Array<out T>.firstNotNullOf(transform: (T) -> R?): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1304)

### 2. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun <T, R : Any> Iterable<T>.firstNotNullOf(transform: (T) -> R?): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L235)

Returns the first non-null value produced by `transform` function being applied to elements of this collection in iteration order,
or throws `NoSuchElementException` if no non-null value was produced.

@sample samples.collections.Collections.Transformations.firstNotNullOf

### 3. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun <K, V, R : Any> Map<out K, V>.firstNotNullOf(transform: (Map.Entry<K, V>) -> R?): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L22)

Returns the first non-null value produced by `transform` function being applied to entries of this map in iteration order,
or throws `NoSuchElementException` if no non-null value was produced.

@sample samples.collections.Collections.Transformations.firstNotNullOf

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    data class Rectangle(val height: Int, val width: Int) {
        val area: Int get() = height * width
    }

    val rectangles = listOf(
        Rectangle(3, 4),
        Rectangle(1, 8),
        Rectangle(6, 3),
        Rectangle(4, 3),
        Rectangle(5, 7)
    )

    val largeArea = rectangles.firstNotNullOf { it.area.takeIf { area -> area >= 15 } }
    val largeAreaOrNull = rectangles.firstNotNullOfOrNull { it.area.takeIf { area -> area >= 15 } }

    println(largeArea)
    println(largeAreaOrNull)

    assertFailsWith<NoSuchElementException> { val evenLargerArea = rectangles.firstNotNullOf { it.area.takeIf { area -> area >= 50 } } }
    val evenLargerAreaOrNull = rectangles.firstNotNullOfOrNull { it.area.takeIf { area -> area >= 50 } }

    println(evenLargerAreaOrNull)
}
```

```text title="Output"
18
18
null
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L954)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
