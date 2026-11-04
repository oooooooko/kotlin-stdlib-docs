# TestTimeSource

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

具有方案上上上上下高的读数的时间源,作为测试时间的可预测来源,很有用。

当前读数值可以按规定的长度,由操作员`plusAssign` 来推算:

```
val timeSource = TestTimeSource()
timeSource += 10.seconds
```

返回此时间源的时间标记可以与从同一时间源获得的其他时间标记的差别比较。

执行注释:当前读数以`Long`纳米秒储存,因此它能够代表大约292年的时间范围。如果由于`plusAssign`操作而出现读数溢出,则会投出`IllegalStateException`。

@sample 样本. 时间. 计量时间. ExclectimeTimeSimes 样本 : @sample 样本. 时间. mecureTimeTimes. ExclusureTimeTimes

??? note "查看英文原文"

    A time source that has programmatically updatable readings. It is useful as a predictable source of time in tests.
    
    The current reading value can be advanced by the specified duration amount with the operator `plusAssign`:
    
    ```
    val timeSource = TestTimeSource()
    timeSource += 10.seconds
    ```
    
    Time marks returned by this time source can be compared for difference with other time marks
    obtained from the same time source.
    
    Implementation note: the current reading value is stored as a `Long` number of nanoseconds,
    thus it's capable to represent a time range of approximately ±292 years.
    Should the reading value overflow as the result of `plusAssign` operation, an `IllegalStateException` is thrown.
    
    @sample samples.time.MeasureTime.explicitMeasureTimeSample
    @sample samples.time.MeasureTime.explicitMeasureTimedValueSample

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.9")
@WasExperimental(ExperimentalTime::class)
public class TestTimeSource : AbstractLongTimeSource(unit = DurationUnit.NANOSECONDS)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSources.kt#L142)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.time.*

fun main() {
    val value = kotlin.time.TestTimeSource()
    println(value)
}
```

```text title="输出"
kotlin.time.TestTimeSource@452b3a41
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
