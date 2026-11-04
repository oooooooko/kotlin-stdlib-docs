# acosh

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

计算值 `x` 的反双曲余弦。

返回值为正`y`, 即正`cosh(y) == x`。

特殊情况:
  - `acosh(NaN)`是`NaN`
- `acosh(x)`是`NaN` 当`x < 1`时
  - `acosh(+Inf)`是`+Inf`

??? note "查看英文原文"

    Computes the inverse hyperbolic cosine of the value `x`.
    
    The returned value is positive `y` such that `cosh(y) == x`.
    
    Special cases:
      - `acosh(NaN)` is `NaN`
      - `acosh(x)` is `NaN` when `x < 1`
      - `acosh(+Inf)` is `+Inf`

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun acosh(x: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L166)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun acosh(x: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L754)

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
import kotlin.math.*

fun main() {
    val result = `acosh`(2.0)
    println(result)
}
```

```text title="输出"
1.3169578969248166
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
