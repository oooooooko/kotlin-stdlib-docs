# expm1

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

计算 `exp(x) - 1` 。

此函数可以用于为接近零的`x`产生更精确的结果。

特殊情况:
  - `expm1(NaN)`是`NaN`
  - `expm1(+Inf)`是`+Inf`
  - `expm1(-Inf)`是`-1.0`

@see `exp` 函数。 @see `ln1p` 函数。 @sample 样本.math.MathSamples.Doubles.Expm1

??? note "查看英文原文"

    Computes `exp(x) - 1`.
    
    This function can be implemented to produce more precise result for `x` near zero.
    
    Special cases:
      - `expm1(NaN)` is `NaN`
      - `expm1(+Inf)` is `+Inf`
      - `expm1(-Inf)` is `-1.0`
    
    @see `exp` function.
    @see `ln1p` function.
    @sample samples.math.MathSamples.Doubles.expm1

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun expm1(x: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L231)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun expm1(x: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L819)

计算 `exp(x) - 1` 。

此函数可以用于为接近零的`x`产生更精确的结果。

特殊情况:
  - `expm1(NaN)`是`NaN`
  - `expm1(+Inf)`是`+Inf`
  - `expm1(-Inf)`是`-1.0`

@see `exp` 函数。 @see `ln1p` 函数。 @sample 样本.math.MathSamples.Floats.expm1

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    fun Double.firstFiveDigits(): String = toString().substring(0, 7)

    println(expm1(1.0).firstFiveDigits())
    // While it does not really matter for relatively large x values (like 1.0),
    // the difference is getting more pronounced when x is getting closer to 0.0
    println(exp(1e-17) - 1.0)
    println(expm1(1e-17))

    // special cases
    println(expm1(Double.NaN))
    println(expm1(Double.POSITIVE_INFINITY))
    println(expm1(Double.NEGATIVE_INFINITY))
}
```

```text title="输出"
1.71828
0.0
1.0E-17
NaN
Infinity
-1.0
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L323)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    fun Float.firstFiveDigits(): String = toString().substring(0, 7)

    println(expm1(1.0f).firstFiveDigits())
    // While it does not really matter for relatively large x values (like 1.0),
    // the difference is getting more pronounced when x is getting closer to 0.0
    println(exp(1e-17f) - 1.0f)
    println(expm1(1e-17f))

    // special cases
    println(expm1(Float.NaN))
    println(expm1(Float.POSITIVE_INFINITY))
    println(expm1(Float.NEGATIVE_INFINITY))
}
```

```text title="输出"
1.71828
0.0
1.0E-17
NaN
Infinity
-1.0
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L918)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
