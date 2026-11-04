# AbstractLongTimeSource.markNow

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 声明与重载

### 1. Common

```kotlin
override fun markNow(): ComparableTimeMark
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSources.kt#L87)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
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

```text title="输出"
-(177919d 23h 38m 48.09s)
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/time/TestTimeSourceTest.kt#L14)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
