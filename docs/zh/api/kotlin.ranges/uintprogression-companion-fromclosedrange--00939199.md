# UIntProgression.Companion.fromClosedRange

`kotlin.ranges` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

在封闭范围指定范围内创建 UInt 进步。

递进从 `rangeStart` 值开始,然后向`rangeEnd`值(不包括它)走,并加上指定的 `step` 。要向后退, `step` 必须是负的。

`step`必须大于`Int.MIN_VALUE`, 而不是等于零。

??? note "查看英文原文"

    Creates UIntProgression within the specified bounds of a closed range.
    
    The progression starts with the `rangeStart` value and goes toward the `rangeEnd` value not excluding it, with the specified `step`.
    In order to go backwards the `step` must be negative.
    
    `step` must be greater than `Int.MIN_VALUE` and not equal to zero.

## 声明与重载

### 1. Common

```kotlin
public fun fromClosedRange(rangeStart: UInt, rangeEnd: UInt, step: Int): UIntProgression
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UIntRange.kt#L106)

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
import kotlin.ranges.*

fun main() {
    val source = kotlin.ranges.UIntProgression.Companion
    val result = source.`fromClosedRange`(2u, 2u, 2)
    println(result)
}
```

```text title="输出"
2..2 step 2
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
