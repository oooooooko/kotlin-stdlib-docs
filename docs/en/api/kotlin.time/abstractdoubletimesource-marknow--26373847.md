# AbstractDoubleTimeSource.markNow

`kotlin.time` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Declarations and overloads

### 1. Common

```kotlin
override fun markNow(): ComparableTimeMark
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSources.kt#L139)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.math.sign
import kotlin.test.*
import kotlin.time.*
import kotlin.time.Duration.Companion.microseconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds

private val units = DurationUnit.entries

private fun TimeMark.assertHasPassed(hasPassed: Boolean) {
        println(this.hasNotPassedNow())
        println(this.hasPassedNow())

        println(this.elapsedNow() < Duration.ZERO)
    }

fun testAdjustment(timeSource: TimeSource.WithComparableMarks) {
        val mark = timeSource.markNow()
        for (unit in units) {
            val markFuture1 = (mark + 1.toDuration(unit)).apply { assertHasPassed(false) }
            val markFuture2 = (mark - (-1).toDuration(unit)).apply { assertHasPassed(false) }
            assertDifferentMarks(markFuture1, mark, 1)
            assertDifferentMarks(markFuture2, mark, 1)

            val markPast1 = (mark - 1.toDuration(unit)).apply { assertHasPassed(true) }
            val markPast2 = (markFuture1 + (-2).toDuration(unit)).apply { assertHasPassed(true) }
            assertDifferentMarks(markPast1, mark, -1)
            assertDifferentMarks(markPast2, mark, -1)

            if (unit > DurationUnit.NANOSECONDS) {
                val d = 1.toDuration(unit)
                val h = d / 2
                val markH1 = mark + h
                val markH2 = mark + d - h
                assertEqualMarks(markH1, markH2)
            }
        }
    }

fun testAdjustmentBig(timeSource: TimeSource.WithComparableMarks) {
        val baseMark = timeSource.markNow()
        val longDuration = Long.MAX_VALUE.nanoseconds
        val long2Duration = longDuration + 1001.milliseconds

        val pastMark = baseMark - longDuration
        val futureMark = pastMark + long2Duration
        val sameMark = futureMark - (long2Duration - longDuration)

        val elapsedMark = timeSource.markNow()
        run {
            val iterations = 1..100
            for (i in iterations) {
                val elapsedDiff1 = (sameMark.elapsedNow() - baseMark.elapsedNow()).absoluteValue
                val elapsedDiff2 = (baseMark.elapsedNow() - sameMark.elapsedNow()).absoluteValue
                // some iterations of this assertion can fail due to an unpredictable delay between subsequent elapsedNow calls
                // but if the mark adjustment arithmetic was wrong, all of them will fail
                if (maxOf(elapsedDiff1, elapsedDiff2) < 1.milliseconds) break
                if (i == iterations.last) fail("$elapsedDiff1, $elapsedDiff2")
            }
        }
        // may not pass exactly for double-based value time marks in JS/WASM due to rounding
//        assertEquals(elapsedMark - baseMark, elapsedMark - sameMark, "$elapsedMark; $baseMark; $sameMark")
        val elapsedBaseDiff = elapsedMark - baseMark
        val elapsedSameDiff = elapsedMark - sameMark
        println((elapsedBaseDiff - elapsedSameDiff).absoluteValue < 1.milliseconds)
    }

fun testAdjustmentInfinite(timeSource: TimeSource.WithComparableMarks) {
        val baseMark = timeSource.markNow()
        val infiniteFutureMark = baseMark + Duration.INFINITE
        val infinitePastMark = baseMark - Duration.INFINITE

        assertDifferentMarks(infinitePastMark, baseMark, -1)
        assertDifferentMarks(infiniteFutureMark, baseMark, 1)
        assertDifferentMarks(infinitePastMark, infiniteFutureMark, -1)

        println(infiniteFutureMark - infinitePastMark)
        println(infiniteFutureMark - baseMark)
        println(infinitePastMark - baseMark)
        assertEqualMarks(infiniteFutureMark, infiniteFutureMark)
        assertEqualMarks(infinitePastMark, infinitePastMark)

        println(infiniteFutureMark.elapsedNow())
        println(infiniteFutureMark.hasNotPassedNow())

        println(infinitePastMark.elapsedNow())
        println(infinitePastMark.hasPassedNow())

        assertFailsWith<IllegalArgumentException> { infiniteFutureMark - Duration.INFINITE }
        assertFailsWith<IllegalArgumentException> { infinitePastMark + Duration.INFINITE }

        for (infiniteMark in listOf(infiniteFutureMark, infinitePastMark)) {
            for (offset in listOf(Duration.ZERO, 1.nanoseconds, 10.microseconds, 1.milliseconds, 15.seconds)) {
                assertEqualMarks(infiniteMark, infiniteMark + offset)
                assertEqualMarks(infiniteMark, infiniteMark - offset)
            }
        }
    }

fun testLongAdjustmentElapsedPrecision(timeSource: TimeSource.WithComparableMarks, wait: (Duration) -> Unit) {
        val baseMark = timeSource.markNow()
        val longDuration = Long.MAX_VALUE.nanoseconds
        val waitDuration = 20.milliseconds
        val pastMark = baseMark - longDuration
        wait(waitDuration)
        val elapsedMark = timeSource.markNow()
        val elapsed = pastMark.elapsedNow()
        val elapsedDiff = elapsedMark - pastMark
        println(elapsed > longDuration)
        println(elapsed >= longDuration + waitDuration)
        println(elapsedDiff >= longDuration + waitDuration)
        // 'elapsed' was measured later than time marks from 'elapsedDiff'
        println(elapsed >= elapsedDiff)
    }

private fun assertEqualMarks(mark1: ComparableTimeMark, mark2: ComparableTimeMark) {
        println(mark1 - mark2)
        println(mark2 - mark1)
        println(mark1 compareTo mark2)
        println(mark2 compareTo mark1)
        println(mark2)
        println(mark2.hashCode())
    }

private fun assertDifferentMarks(mark1: ComparableTimeMark, mark2: ComparableTimeMark, expectedCompare: Int) {
        assertNotEquals(Duration.ZERO, mark1 - mark2)
        assertNotEquals(Duration.ZERO, mark2 - mark1)
        println((mark1 compareTo mark2).sign)
        println((mark2 compareTo mark1).sign)
        assertNotEquals(mark1, mark2)
        // can't say anything about hash codes for non-equal marks
        // assertNotEquals(mark1.hashCode(), mark2.hashCode(), "hashCodes of: $mark1, $mark2")
    }

private class LongTimeSource(unit: DurationUnit) : AbstractLongTimeSource(unit) {
        var reading: Long = 0L
        override fun read(): Long = reading
    }

@OptIn(ExperimentalTime::class)
    @Suppress("DEPRECATION_ERROR")
    private class DoubleTimeSource(unit: DurationUnit) : AbstractDoubleTimeSource(unit) {
        var reading: Double = 0.0
        override fun read(): Double = reading
    }

fun main() {

        val timeSource = DoubleTimeSource(unit = DurationUnit.MILLISECONDS).apply { reading = -Double.MAX_VALUE }

        val mark1 = timeSource.markNow()
        timeSource.reading = 0.0
        val mark2 = timeSource.markNow() - Duration.INFINITE
        println(mark1.elapsedNow())
        println(mark2.elapsedNow())
        assertEqualMarks(mark1, mark2)
    
}
```

```text title="Output"
Infinity
Infinity
0s
0s
0
0
DoubleTimeMark(0.0ms + -Infinity, DoubleTimeSource@65b54208)
-2147483645
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/time/TimeMarkTest.kt#L282)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
