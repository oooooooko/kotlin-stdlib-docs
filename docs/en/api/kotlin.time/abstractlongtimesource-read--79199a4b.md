# AbstractLongTimeSource.read

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

This protected method should be overridden to return the current reading of the time source expressed as a `Long` number
in the unit specified by the `unit` property.

Note that the value returned by this method when `markNow` is called the first time is used as "zero" reading
and the difference from this "zero" reading is calculated for subsequent values.
Therefore, it's not recommended to return values farther than `±Long.MAX_VALUE` from the first returned reading
as this will cause this time source flip over future/past boundary for the returned time marks.

## Declarations and overloads

### 1. Common

```kotlin
protected abstract fun read(): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSources.kt#L29)

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
