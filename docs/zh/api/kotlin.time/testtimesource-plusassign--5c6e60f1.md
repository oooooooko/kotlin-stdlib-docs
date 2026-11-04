# TestTimeSource.plusAssign

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将当前此时间源的读数值提高为指定的 `duration` 。

`duration` 值转换为`Long` 纳米秒时,会四舍五入为零。例如,如果添加的长度为`0.6.nanoseconds`,读数不会进步,因为时间值四舍五入为零纳米秒。

@throws 非法居留除外,因为这次行动导致读数溢出。

??? note "查看英文原文"

    Advances the current reading value of this time source by the specified `duration`.
    
    `duration` value is rounded down towards zero when converting it to a `Long` number of nanoseconds.
    For example, if the duration being added is `0.6.nanoseconds`, the reading doesn't advance because
    the duration value is rounded to zero nanoseconds.
    
    @throws IllegalStateException when the reading value overflows as the result of this operation.

## 声明与重载

### 1. Common

```kotlin
public operator fun plusAssign(duration: Duration)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSources.kt#L173)

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
    val source = kotlin.time.TestTimeSource()
    val result = source.`plusAssign`(2.seconds)
    println(result)
}
```

```text title="输出"
kotlin.Unit
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
