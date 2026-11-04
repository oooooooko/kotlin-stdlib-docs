# Duration.div

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个长度,其值是此持续时间值除以给定的 `scale` 号。

@throws 非法辩护除外,如果操作结果给给定参数带来未定义的值,例如,将零时间除以零。

??? note "查看英文原文"

    Returns a duration whose value is this duration value divided by the given `scale` number.
    
    @throws IllegalArgumentException if the operation results in an undefined value for the given arguments,
    e.g. when dividing zero duration by zero.

## 声明与重载

### 1. Common

```kotlin
public operator fun div(scale: Int): Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L462)

### 2. Common

```kotlin
public operator fun div(scale: Double): Duration
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L492)

返回一个长度,其值是此持续时间值除以给定的 `scale` 号。

@throws 非法辩护除外,如果操作结果给给定参数带来未定义的值,例如,将无限期限除以无限或零期限除以零。

### 3. Common

```kotlin
public operator fun div(other: Duration): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Duration.kt#L509)

返回一个数字,即此值与 `other` 年持续时间值之比。

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
    val result = source.`div`(2)
    println(result)
}
```

```text title="输出"
1s
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
