# atan

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

计算值 `x` 的正正切值;返回值是一个角度,在`-PI/2`至`PI/2`弧度之间。

特殊情况: - `atan(NaN)` 为 `NaN`

@sample 样本. math. 马斯抽样.

??? note "查看英文原文"

    Computes the arc tangent of the value `x`;
    the returned value is an angle in the range from `-PI/2` to `PI/2` radians.
    
    Special cases:
      - `atan(NaN)` is `NaN`
    
    @sample samples.math.MathSamples.Doubles.atan

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun atan(x: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L82)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun atan(x: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L670)

计算值 `x` 的正正切值;返回值是一个角度,在`-PI/2`至`PI/2`弧度之间。

特殊情况: - `atan(NaN)` 为 `NaN`

@sample 样本.math.MathSamples.Floats.atan。 地图样本

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val epsilon = 1e-10

    println(atan(0.0))
    // Results may not be exact, so we're only checking that they are within epsilon from the expected value
    // atan(1.0) = π/4
    println((atan(1.0) - PI / 4).absoluteValue < epsilon)
    // atan(-1.0) = -π/4
    println((atan(-1.0) - (-PI / 4)).absoluteValue < epsilon)
    // atan(tan(x)) = x
    println((atan(tan(0.123)) - 0.123).absoluteValue < epsilon)

    // special cases
    println(atan(Double.NaN))
}
```

```text title="输出"
0.0
true
true
true
NaN
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L427)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val epsilon = 1e-6f

    println(atan(0.0f))
    // Results may not be exact, so we're only checking that they are within epsilon from the expected value
    // atan(1.0) = π/4
    println((atan(1.0f) - PI.toFloat() / 4).absoluteValue < epsilon)
    // atan(-1.0) = -π/4
    println((atan(-1.0f) - (-PI.toFloat() / 4)).absoluteValue < epsilon)
    // atan(tan(x)) = x
    println((atan(tan(0.25f)) - 0.25f).absoluteValue < epsilon)

    // special cases
    println(atan(Float.NaN))
}
```

```text title="输出"
0.0
true
true
true
NaN
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1022)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
