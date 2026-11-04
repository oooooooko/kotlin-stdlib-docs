# AbstractDoubleTimeSource

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

An abstract class used to implement time sources that return their readings as `Double` values in the specified `unit`.

@property unit The unit in which this time source's readings are expressed.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalTime
@Deprecated(
    "Using AbstractDoubleTimeSource is no longer recommended, use AbstractLongTimeSource instead.",
    level = DeprecationLevel.ERROR
)
public abstract class AbstractDoubleTimeSource(protected val unit: DurationUnit) : TimeSource.WithComparableMarks
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSources.kt#L90)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.time.*
class ManualClock : AbstractDoubleTimeSource(DurationUnit.MILLISECONDS) {
    var reading = 0.0
    override fun read(): Double = reading
    fun unitName(): String = unit.name
}
fun main() {
    val clock = ManualClock()
    val mark = clock.markNow()
    clock.reading = 25.0
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
