# Duration

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

表示时间的时数,一个时数与另一个时数的时数。

如果第二个瞬间早于第一个时段,则可能出现负时段。

型号可以以纳米第二精度存储146年的 +146 年,以毫秒精确度存储1.46亿年。如果在 `kotlin.time` 中提供的周期返回操作产生一个不与上述范围相容的周期值,则返回的`Duration` 是无限的。

无限期限值 `Duration.INFINITE` 可用于表示无限超时。

建造一个期限,使用扩展功能 `toDuration` ,或扩展属性 `hours` 、 `minutes` 、 `seconds` 等,可使用`Int`、`Long`和`Double`数字类型。

要获得在特定的 `duration units`Z`DurationUnit` 中表达的这一持续时间值
函数 `toInt`、`toLong`和`toDouble`
或`inWholeHours`、`inWholeMinutes`、`inWholeSeconds`、`inWholeNanoseconds`等属性。

??? note "查看英文原文"

    Represents the amount of time one instant of time is away from another instant.
    
    A negative duration is possible in a situation when the second instant is earlier than the first one.
    
    The type can store duration values up to ±146 years with nanosecond precision,
    and up to ±146 million years with millisecond precision.
    If a duration-returning operation provided in `kotlin.time` produces a duration value that doesn't fit into the above range,
    the returned `Duration` is infinite.
    
    An infinite duration value `Duration.INFINITE` can be used to represent infinite timeouts.
    
    To construct a duration use either the extension function `toDuration`,
    or the extension properties `hours`, `minutes`, `seconds`, and so on,
    available on `Int`, `Long`, and `Double` numeric types.
    
    To get the value of this duration expressed in a particular `duration units``DurationUnit`
    use the functions `toInt`, `toLong`, and `toDouble`
    or the properties `inWholeHours`, `inWholeMinutes`, `inWholeSeconds`, `inWholeNanoseconds`, and so on.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.6")
@JvmInline
public value class Duration
// A temporary workaround for KT-81995, the constructor has to be private once the issue is resolved.
@Deprecated("Don't call this constructor directly.", level = DeprecationLevel.ERROR)
internal constructor(private val rawValue: Long) :
    Comparable<Duration>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L12)

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
    val value = 2.seconds
    println(value)
}
```

```text title="输出"
2s
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
