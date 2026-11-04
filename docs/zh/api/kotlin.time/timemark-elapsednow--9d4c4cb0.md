# TimeMark.elapsedNow

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回从此标记中传送的时间, 计算该标记的时间源。

请注意,此函数返回的值在随后的援引中可能发生变化。

此函数返回的值可能无限大(以`Duration.isInfinite`计算)。

取决于 `TimeMark` 的 `TimeSource` 的单音保证,后继电话可以返回不增加的(甚至负)`Duration`的值,如果有一份有关`TimeSource`执行文件,了解关于单声保证的更多细节,则可以查阅。

@throws 非法辩护 除非执行可能丢弃,如果计算所花时间涉及在遥远的过去时间标记上增加一个正数无限的时段,或将一个无限的负数持续时间加到遥远的未来时间标记上,则执行可能会丢弃。

??? note "查看英文原文"

    Returns the amount of time passed from this mark measured with the time source from which this mark was taken.
    
    Note that the value returned by this function can change on subsequent invocations.
    
    The value returned by this function may be infinitely large (in terms of `Duration.isInfinite`).
    
    Depending on monotonicity guarantees of a `TimeSource` from which a `TimeMark` was obtained,
    subsequence calls may return non-increasing (or even negative) `Duration` values.
    Consult with a documentation of a particular `TimeSource` implementation for more details about
    monotonicity guarantees.
    
    @throws IllegalArgumentException an implementation may throw if calculating the elapsed time involves
    adding a positive infinite duration to an infinitely distant past time mark or
    a negative infinite duration to an infinitely distant future time mark.

## 声明与重载

### 1. Common

```kotlin
public abstract fun elapsedNow(): Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSource.kt#L135)

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
    val result = source.`elapsedNow`()
    println(result)
}
```

```text title="输出"
231.916us
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
