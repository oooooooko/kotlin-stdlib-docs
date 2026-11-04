# Enum.compareTo

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 声明与重载

### 1. Common

```kotlin
public final override fun compareTo(other: E): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Enum.kt#L29)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
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

        for (unit in units) {
            val timeSource = LongTimeSource(unit).apply {
                markNow() // fix zero reading
                reading = Long.MIN_VALUE + 1
            }

            val mark1 = timeSource.markNow()
            timeSource.reading = 0
            val mark2 = timeSource.markNow() - Duration.INFINITE
            if (unit >= DurationUnit.MILLISECONDS) {
                println(mark1.elapsedNow())
            }
            println(mark2.elapsedNow())
            assertDifferentMarks(mark1, mark2, 1)

            val mark3 = mark1 + Duration.INFINITE
            println(mark3.elapsedNow())
            val mark4 = timeSource.markNow() + Duration.INFINITE
            println(mark4.elapsedNow())
            assertEqualMarks(mark3, mark4) // different readings, same infinite offset
        }
    
}
```

```text title="输出"
Infinity
1
-1
-Infinity
-Infinity
0s
0s
0
0
LongTimeMark(9223372036854775807ns + 0s, LongTimeSource@9807454)
-2147483648
Infinity
1
-1
-Infinity
-Infinity
0s
0s
0
0
LongTimeMark(9223372036854775807us + 0s, LongTimeSource@3d494fbf)
-2147483648
Infinity
Infinity
1
-1
-Infinity
-Infinity
0s
0s
0
0
LongTimeMark(9223372036854775807ms + 0s, LongTimeSource@66a29884)
-2147483648
Infinity
Infinity
1
-1
-Infinity
-Infinity
0s
0s
0
0
LongTimeMark(9223372036854775807s + 0s, LongTimeSource@4769b07b)
-2147483648
Infinity
Infinity
1
-1
-Infinity
-Infinity
0s
0s
0
0
LongTimeMark(9223372036854775807m + 0s, LongTimeSource@cc34f4d)
-2147483648
Infinity
Infinity
1
-1
-Infinity
-Infinity
0s
0s
0
0
LongTimeMark(9223372036854775807h + 0s, LongTimeSource@17a7cec2)
-2147483648
Infinity
Infinity
1
-1
-Infinity
-Infinity
0s
0s
0
0
LongTimeMark(9223372036854775807d + 0s, LongTimeSource@65b3120a)
-2147483648
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/time/TimeMarkTest.kt#L257)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
