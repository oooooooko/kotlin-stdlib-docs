# Long.rem

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将此值的短差分割( divid) 的剩余部分乘以其他值( diovisor) 。

结果为零或与 _dividend_具有相同的符号,绝对值小于断面的绝对值。

??? note "查看英文原文"

    Calculates the remainder of truncating division of this value (dividend) by the other value (divisor).
    
    The result is either zero or has the same sign as the _dividend_ and has the absolute value less than the absolute value of the divisor.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.1")
    @kotlin.internal.IntrinsicConstEvaluation
    public operator fun rem(other: Byte): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L1334)

### 2. Common

```kotlin
@SinceKotlin("1.1")
    @kotlin.internal.IntrinsicConstEvaluation
    public operator fun rem(other: Short): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L1343)

### 3. Common

```kotlin
@SinceKotlin("1.1")
    @kotlin.internal.IntrinsicConstEvaluation
    public operator fun rem(other: Int): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L1352)

### 4. Common

```kotlin
@SinceKotlin("1.1")
    @kotlin.internal.IntrinsicConstEvaluation
    public operator fun rem(other: Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L1361)

### 5. Common

```kotlin
@SinceKotlin("1.1")
    @kotlin.internal.IntrinsicConstEvaluation
    public operator fun rem(other: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L1370)

### 6. Common

```kotlin
@SinceKotlin("1.1")
    @kotlin.internal.IntrinsicConstEvaluation
    public operator fun rem(other: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L1379)

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
    val source = 5L
    val result = source.`rem`(2.toByte())
    println(result)
}
```

```text title="输出"
1
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
