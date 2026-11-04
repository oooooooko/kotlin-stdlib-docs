# Duration.times

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个值为此持续期值乘以给定`scale`号的长度。

@throws 非法辩护除外,如果操作结果给给定参数带来未定义的值,例如,将无限持续时间乘以零。

??? note "查看英文原文"

    Returns a duration whose value is this duration value multiplied by the given `scale` number.
    
    @throws IllegalArgumentException if the operation results in an undefined value for the given arguments,
    e.g. when multiplying an infinite duration by zero.

## 声明与重载

### 1. Common

```kotlin
public operator fun times(scale: Int): Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L397)

### 2. Common

```kotlin
public operator fun times(scale: Double): Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L443)

返回一个值为此持续期值乘以给定`scale`号的长度。

当结果不能精确代表`Double`的号码时,操作可能涉及四舍五入。

@throws 非法辩护除外,如果操作结果给给定参数带来未定义的值,例如,将无限持续时间乘以零。

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
    val source = 2.seconds
    val result = source.`times`(2)
    println(result)
}
```

```text title="输出"
4s
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
