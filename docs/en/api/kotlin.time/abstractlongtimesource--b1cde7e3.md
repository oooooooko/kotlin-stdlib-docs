# AbstractLongTimeSource

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

An abstract class used to implement time sources that return their readings as `Long` values in the specified `unit`.

Time marks returned by this time source can be compared for difference with other time marks
obtained from the same time source.

@property unit The unit in which this time source's readings are expressed.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.9")
@WasExperimental(ExperimentalTime::class)
public abstract class AbstractLongTimeSource(protected val unit: DurationUnit) : TimeSource.WithComparableMarks
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSources.kt#L18)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.time.*
class ManualClock : AbstractLongTimeSource(DurationUnit.MILLISECONDS) {
    var reading = 0L
    override fun read(): Long = reading
    fun unitName(): String = unit.name
}
fun main() {
    val clock = ManualClock()
    val mark = clock.markNow()
    clock.reading = 25L
    println(clock.unitName())
    println(mark.elapsedNow())
}
```

```text title="Output"
MILLISECONDS
25ms
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
