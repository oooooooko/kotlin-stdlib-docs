# TimeSource.markNow

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

标记此时间源的时间点 。

返回的 `TimeMark` 实例包嵌了所捕捉的时间点,并允许从该点询问`elapsed``TimeMark.elapsedNow`的时间间隔。

??? note "查看英文原文"

    Marks a point in time on this time source.
    
    The returned `TimeMark` instance encapsulates the captured time point and allows querying
    the duration of time interval `elapsed``TimeMark.elapsedNow` from that point.

## 声明与重载

### 1. Common

```kotlin
public fun markNow(): TimeMark
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSource.kt#L25)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*
import kotlin.time.*
import kotlin.time.Duration.Companion.nanoseconds



fun main() {

        val baseMark = TimeSource.Monotonic.markNow()
        val longDuration = Long.MAX_VALUE.nanoseconds

        val pastMark = baseMark - longDuration
        val infiniteFutureMark1 = pastMark + longDuration * 3

        println(infiniteFutureMark1.elapsedNow())
    
}
```

```text title="输出"
-Infinity
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/jvm/test/time/TimeMarkJVMTest.kt#L19)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
