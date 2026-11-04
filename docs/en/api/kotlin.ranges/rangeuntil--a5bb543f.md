# rangeUntil

`kotlin.ranges` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Creates an open-ended range from this `Comparable` value to the specified `that` value.

This value needs to be smaller than `that` value, otherwise the returned range will be empty.

@sample samples.ranges.Ranges.rangeUntilComparable

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun <T : Comparable<T>> T.rangeUntil(that: T): OpenEndRange<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ranges/Ranges.kt#L60)

### 2. Common

```kotlin
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun Double.rangeUntil(that: Double): OpenEndRange<Double>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ranges/Ranges.kt#L163)

Creates an open-ended range from this `Double` value to the specified `that` value.

Numbers are compared with the ends of this range according to IEEE-754.

@sample samples.ranges.Ranges.rangeUntilDouble

### 3. Common

```kotlin
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun Float.rangeUntil(that: Float): OpenEndRange<Float>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ranges/Ranges.kt#L248)

Creates an open-ended range from this `Float` value to the specified `that` value.

Numbers are compared with the ends of this range according to IEEE-754.

@sample samples.ranges.Ranges.rangeUntilFloat

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val start = Date.valueOf("2017-01-01")
    val end = Date.valueOf("2017-12-31")
    val range = start..<end
    println(range)

    println(Date.valueOf("2017-05-27") in range)
    println(Date.valueOf("2017-12-31") in range)
    println(Date.valueOf("2017-12-31") !in range)
}
```

```text title="Output"
2017-01-01..<2017-12-31
true
false
true
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L38)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val range = 1.0..<100.0
    println(range)

    println(3.14 in range)
    println(100.0 in range)
}
```

```text title="Output"
1.0..<100.0
true
false
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L59)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val range = 1f..<100f
    println(range)

    println(3.14f in range)
    println(100f in range)
}
```

```text title="Output"
1.0..<100.0
true
false
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L77)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
