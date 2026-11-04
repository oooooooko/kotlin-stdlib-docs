# Instant.Companion.DISTANT_PAST

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

即时价值是过去最遥远的

`isDistantPast` 返回这个值和所有早期值的正数。

@sample 样本的采样时间。

??? note "查看英文原文"

    An instant value that is far in the past.
    
    `isDistantPast` returns true for this value and all earlier ones.
    
    @sample samples.time.Instants.isDistantPast

## 声明与重载

### 1. Common

```kotlin
public val DISTANT_PAST: Instant // -100001-12-31T23:59:59.999999999Z
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L417)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    // Checking if an instant is so far in the past that it's probably irrelevant.
    val tenThousandYearsBC = Instant.parse("-10000-01-01T00:00:00Z")
    println(tenThousandYearsBC.isDistantPast)

    // Instant.DISTANT_PAST is the latest instant that is considered far in the past.
    println(Instant.DISTANT_PAST)
    println(Instant.DISTANT_PAST.isDistantPast)

    // All instants earlier than Instant.DISTANT_PAST are considered to be far in the past.
    val earlierThanDistantPast = Instant.DISTANT_PAST - 1.nanoseconds
    println(earlierThanDistantPast)
    println(earlierThanDistantPast.isDistantPast)

    // All instants later than Instant.DISTANT_PAST are not considered to be far in the past.
    val laterThanDistantPast = Instant.DISTANT_PAST + 1.nanoseconds
    println(laterThanDistantPast)
    println(laterThanDistantPast.isDistantPast)
}
```

```text title="输出"
false
-100001-12-31T23:59:59.999999999Z
true
-100001-12-31T23:59:59.999999998Z
true
-100000-01-01T00:00:00Z
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L183)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
