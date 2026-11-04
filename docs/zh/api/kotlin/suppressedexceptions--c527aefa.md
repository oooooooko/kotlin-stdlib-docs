# suppressedExceptions

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回所有被抑制的例外清单,以便提供这一例外。

列表可以是空的: - 如果没有排除例外; - 如果平台不支持被抑制的例外; - 如果这个 `Throwable` 例禁用了抑制 。

??? note "查看英文原文"

    Returns a list of all exceptions that were suppressed in order to deliver this exception.
    
    The list can be empty:
    - if no exceptions were suppressed;
    - if the platform doesn't support suppressed exceptions;
    - if this `Throwable` instance has disabled the suppression.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public expect val Throwable.suppressedExceptions: List<Throwable>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/ExceptionsH.kt#L153)

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
import kotlin.*

fun main() {
    val source = IllegalArgumentException("example")
    val result = source.`suppressedExceptions`
    println(result)
}
```

```text title="输出"
[]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
