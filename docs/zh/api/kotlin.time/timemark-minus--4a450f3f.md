# TimeMark.minus

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回同一时间源的时值,此时间值后面的 `duration` 是指定的时间值。

返回的时间值在`duration`为正数时,则在较早时增加,在`duration`为负数时增加。

如果时间标记在过去或将来调整过远,它可能会饱和到一个无限遥远的时间标记。 如果这样,`elapsedNow`将会返回从如此遥远的标记中留下的无限时间。

@throws 非法辩护 除非执行可能丢弃,如果从遥远的未来时间标记中减去正数无限期限,或从遥远的过去时间标记中减去负数无限期限,则执行可能会丢弃。

??? note "查看英文原文"

    Returns a time mark on the same time source that is behind this time mark by the specified `duration`.
    
    The returned time mark is more _early_ when the `duration` is positive, and more _late_ when the `duration` is negative.
    
    If the time mark is adjusted too far in the past or in the future, it may saturate to an infinitely distant time mark.
    In that case, `elapsedNow` will return an infinite duration elapsed from such infinitely distant mark.
    
    @throws IllegalArgumentException an implementation may throw if a positive infinite duration is subtracted from an infinitely distant future time mark or
    a negative infinite duration is subtracted from an infinitely distant past time mark.

## 声明与重载

### 1. Common

```kotlin
public open operator fun minus(duration: Duration): TimeMark
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSource.kt#L166)

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
    val source = TimeSource.Monotonic.markNow()
    val result = source.`minus`(2.seconds)
    println(result)
}
```

```text title="输出"
ValueTimeMark(reading=-1999995208)
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
