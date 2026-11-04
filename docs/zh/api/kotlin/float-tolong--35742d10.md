# Float.toLong

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将这个`Float`值转换为 `Long` 。

如果有的话, 分部分会四舍五入为零。 如果 `Float` 值为`NaN`, `Long.MIN_VALUE`, 如果低于`Long.MIN_VALUE`, 则返回为零 。 如果大于`Long.MAX_VALUE`, 则返回为 `Long.MAX_VALUE` 。

??? note "查看英文原文"

    Converts this `Float` value to `Long`.
    
    The fractional part, if any, is rounded down towards zero.
    Returns zero if this `Float` value is `NaN`, `Long.MIN_VALUE` if it's less than `Long.MIN_VALUE`,
    `Long.MAX_VALUE` if it's bigger than `Long.MAX_VALUE`.

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.IntrinsicConstEvaluation
    public override fun toLong(): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L1882)

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
    val source = 5.5f
    val result = source.`toLong`()
    println(result)
}
```

```text title="输出"
5
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
