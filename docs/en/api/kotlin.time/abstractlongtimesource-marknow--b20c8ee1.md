# AbstractLongTimeSource.markNow

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Declarations and overloads

### 1. Common

```kotlin
override fun markNow(): ComparableTimeMark
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSources.kt#L87)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*
import kotlin.time.*
import kotlin.time.Duration.Companion.nanoseconds



fun main() {

        for (enormousDuration in listOf(Duration.INFINITE, Double.MAX_VALUE.nanoseconds, Long.MAX_VALUE.nanoseconds * 2)) {
            assertFailsWith<IllegalStateException>(enormousDuration.toString()) { TestTimeSource() += enormousDuration }
            assertFailsWith<IllegalStateException>((-enormousDuration).toString()) { TestTimeSource() += -enormousDuration }
        }

        val moderatePositiveDuration = Long.MAX_VALUE.nanoseconds / 1.5
        val borderlineQuarterPositiveDuration = (Long.MAX_VALUE / 4).nanoseconds // precise number of ns
        val borderlineQuarterNegativeDuration = (Long.MIN_VALUE / 4).nanoseconds
        run {
            val timeSource = TestTimeSource()
            timeSource += moderatePositiveDuration
            assertFailsWith<IllegalStateException>("Should overflow positive") { timeSource += moderatePositiveDuration }
        }
        run {
            val timeSource = TestTimeSource()
            repeat(4) { timeSource += borderlineQuarterPositiveDuration }
            assertFailsWith<IllegalStateException>("Should overflow positive") { timeSource += 4.nanoseconds }
        }
        run {
            val timeSource = TestTimeSource()
            repeat(4) { timeSource += borderlineQuarterNegativeDuration }
            assertFailsWith<IllegalStateException>("Should overflow negative") { timeSource += -4.nanoseconds }
        }

        run {
            val timeSource = TestTimeSource()
            timeSource += moderatePositiveDuration
            val mark = timeSource.markNow()
            // does not overflow even if duration doesn't fit in long, but the result fits
            timeSource += -moderatePositiveDuration - Long.MAX_VALUE.nanoseconds
            println(mark.elapsedNow())
        }
    
}
```

```text title="Output"
-(177919d 23h 38m 48.09s)
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/time/TestTimeSourceTest.kt#L14)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
