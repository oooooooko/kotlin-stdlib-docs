# Instant.Companion.fromEpochMilliseconds

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回`Instant`, 也就是`epochMilliseconds` 毫秒数 从`1970-01-01T00:00:00Z`号时钟返回

保证 `epochMilliseconds` 的每笔价值都可被作为`Instant`的标值。

请注意, `Instant` 还支持通过`fromEpochSeconds`支持纳米二精度。

@see 立即到Epoch- Militos @sample 样本. time. Instants. from Epoch- Militos.

??? note "查看英文原文"

    Returns an `Instant` that is `epochMilliseconds` number of milliseconds from the epoch instant `1970-01-01T00:00:00Z`.
    
    Every value of `epochMilliseconds` is guaranteed to be representable as an `Instant`.
    
    Note that `Instant` also supports nanosecond precision via `fromEpochSeconds`.
    
    @see Instant.toEpochMilliseconds
    @sample samples.time.Instants.fromEpochMilliseconds

## 声明与重载

### 1. Common

```kotlin
public fun fromEpochMilliseconds(epochMilliseconds: Long): Instant
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L277)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    // Creating an Instant representing the Unix epoch.
    val instant1 = Instant.fromEpochMilliseconds(0)
    // Creating an Instant from a specific number of milliseconds since the Unix epoch.
    val instant2 = Instant.fromEpochMilliseconds(1_000_000_000_123)

    // toEpochMilliseconds returns the exact millisecond value provided during construction.
    println(instant1.toEpochMilliseconds())
    println(instant2.toEpochMilliseconds())

    // The string representation of the constructed instants.
    println(instant1)
    println(instant2)
}
```

```text title="输出"
0
1000000000123
1970-01-01T00:00:00Z
2001-09-09T01:46:40.123Z
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L116)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
