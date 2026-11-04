# Instant.toString

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将此转换为 ISO 8601 字符串表示式, 例如 `2023-01-02T23:40:57.120Z` 。

表示法使用UTC- SLS 时间比UTC 的时间比UTC 。 在实践中, 这意味着跳跃第二处理不会被调整为 UTC 。 跳跃秒不会被添加或跳过, 因此无法获取一个字符串, 组件的秒数为60 秒, 并且随时可以观察到 23: 59: 59 。

@see 分析
@sample样本.时间. Instrants.to stringSample

??? note "查看英文原文"

    Converts this instant to the ISO 8601 string representation, for example, `2023-01-02T23:40:57.120Z`.
    
    The representation uses the UTC-SLS time scale instead of UTC.
    In practice, this means that leap second handling will not be readjusted to the UTC.
    Leap seconds will not be added or skipped, so it is impossible to acquire a string
    where the component for seconds is 60, and for any day, it's possible to observe 23:59:59.
    
    @see parse
    @sample samples.time.Instants.toStringSample

## 声明与重载

### 1. Common

```kotlin
public override fun toString(): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L256)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    // The string representation of the current instant in ISO 8601 format.
    val currentInstant = Clock.System.now()
    println(currentInstant.toString())
    // The string representation of the Unix epoch.
    val unixEpochInstant = Instant.fromEpochSeconds(0)
    println(unixEpochInstant.toString())
    // The string representation of an instant.
    val instant = Instant.fromEpochMilliseconds(1_000_000_000_123)
    println(instant.toString())
}
```

```text title="输出"
2026-11-04T02:16:16.622229Z
1970-01-01T00:00:00Z
2001-09-09T01:46:40.123Z
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L103)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
