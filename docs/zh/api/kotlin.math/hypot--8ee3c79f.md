# hypot

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

计算`sqrt(x^2 + y^2)`,无溢出或溢出量。

特殊情况: - 如果任何参数是无限的,返回 `+Inf` - 如果任何参数是 `NaN` , 返回 `NaN` , 而其他参数不是无限的,返回 `NaN`

@sample 样本.math.MathSamples.Doubles.hypot

??? note "查看英文原文"

    Computes `sqrt(x^2 + y^2)` without intermediate overflow or underflow.
    
    Special cases:
      - returns `+Inf` if any of arguments is infinite
      - returns `NaN` if any of arguments is `NaN` and the other is not infinite
    
    @sample samples.math.MathSamples.Doubles.hypot

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun hypot(x: Double, y: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L193)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun hypot(x: Float, y: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L781)

计算`sqrt(x^2 + y^2)`,无溢出或溢出量。

特殊情况: - 如果任何参数是无限的,返回 `+Inf` - 如果任何参数是 `NaN` , 返回 `NaN` , 而其他参数不是无限的,返回 `NaN`

@sample 样本.math.MathSamples.花粉.hypoot

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    // sqrt(6 * 6 + 8 * 8) = sqrt(36 + 64) = sqrt(100) = 10
    println(hypot(6.0, 8.0))

    // special cases
    println(hypot(Double.NaN, 2.0))
    println(hypot(1.0, Double.NaN))
    println(hypot(Double.POSITIVE_INFINITY, 2.0))
    println(hypot(1.0, Double.NEGATIVE_INFINITY))
}
```

```text title="输出"
10.0
NaN
NaN
Infinity
Infinity
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L264)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    // sqrt(6 * 6 + 8 * 8) = sqrt(36 + 64) = sqrt(100) = 10
    println(hypot(6.0f, 8.0f))

    // special cases
    println(hypot(Float.NaN, 2.0f))
    println(hypot(1.0f, Float.NaN))
    println(hypot(Float.POSITIVE_INFINITY, 2.0f))
    println(hypot(1.0f, Float.NEGATIVE_INFINITY))
}
```

```text title="输出"
10.0
NaN
NaN
Infinity
Infinity
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L859)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
