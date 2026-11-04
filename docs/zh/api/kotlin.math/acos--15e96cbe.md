# acos

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

计算值 `x` 的弧余弦;返回值是一个角,在`0.0`至`PI`弧度之间。

特殊情况: - `acos(x)` 为 `NaN` ,而`abs(x) > 1`或x为 `NaN` 。

@sample 样本.math.MathSamples.doubles.acos

??? note "查看英文原文"

    Computes the arc cosine of the value `x`;
    the returned value is an angle in the range from `0.0` to `PI` radians.
    
    Special cases:
      - `acos(x)` is `NaN`, when `abs(x) > 1` or x is `NaN`
    
    @sample samples.math.MathSamples.Doubles.acos

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun acos(x: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L70)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun acos(x: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L658)

计算值 `x` 的弧余弦;返回值是一个角,在`0.0`至`PI`弧度之间。

特殊情况: - `acos(x)` 为 `NaN` ,而`abs(x) > 1`或x为 `NaN` 。

@sample 样本.math.MathSamples.floats.acos

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val epsilon = 1e-10

    println(acos(1.0))
    // Results may not be exact, so we're only checking that they are within epsilon from the expected value
    // acos(0.0) = π/2
    println((acos(0.0) - PI / 2).absoluteValue < epsilon)
    // acos(-1.0) = π
    println((acos(-1.0) - PI).absoluteValue < epsilon)
    // acos(cos(x)) = x
    println((acos(cos(0.123)) - 0.123).absoluteValue < epsilon)

    // special cases
    println(acos(Double.NaN))
    println(acos(1.1))
    println(acos(-2.0))
}
```

```text title="输出"
0.0
true
true
true
NaN
NaN
NaN
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L408)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val epsilon = 1e-6f

    println(acos(1.0f))
    // Results may not be exact, so we're only checking that they are within epsilon from the expected value
    // acos(0.0) = π/2
    println((acos(0.0f) - PI.toFloat() / 2).absoluteValue < epsilon)
    // acos(-1.0) = π
    println((acos(-1.0f) - PI.toFloat()).absoluteValue < epsilon)
    // acos(cos(x)) = x
    println((acos(cos(0.25f)) - 0.25f).absoluteValue < epsilon)

    // special cases
    println(acos(Float.NaN))
    println(acos(1.1f))
    println(acos(-2.0f))
}
```

```text title="输出"
0.0
true
true
true
NaN
NaN
NaN
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1003)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
