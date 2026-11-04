# exp

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

计算Euler的 `e` 号 提高到 `x` 的功率

特殊情况:
  - `exp(NaN)`是`NaN`
  - `exp(+Inf)`是`+Inf`
  - `exp(-Inf)`是`0.0`

@sample 样本 麻黄麻样本 豆类样本

??? note "查看英文原文"

    Computes Euler's number `e` raised to the power of the value `x`.
    
    Special cases:
      - `exp(NaN)` is `NaN`
      - `exp(+Inf)` is `+Inf`
      - `exp(-Inf)` is `0.0`
    
    @sample samples.math.MathSamples.Doubles.exp

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun exp(x: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L218)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun exp(x: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L806)

计算Euler的 `e` 号 提高到 `x` 的功率

特殊情况:
  - `exp(NaN)`是`NaN`
  - `exp(+Inf)`是`+Inf`
  - `exp(-Inf)`是`0.0`

@sample 样本 地图样本 花粉样本 样本

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    fun Double.firstFiveDigits(): String = toString().substring(0, 7)

    println(exp(1.0).firstFiveDigits())
    println(exp(2.0).firstFiveDigits())
    println(exp(-1.0).firstFiveDigits())

    // special cases
    println(exp(Double.NaN))
    println(exp(Double.POSITIVE_INFINITY))
    println(exp(Double.NEGATIVE_INFINITY))
}
```

```text title="输出"
2.71828
7.38905
0.36787
NaN
Infinity
0.0
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L309)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    fun Float.firstFiveDigits(): String = toString().substring(0, 7)

    println(exp(1.0f).firstFiveDigits())
    println(exp(2.0f).firstFiveDigits())
    println(exp(-1.0f).firstFiveDigits())

    // special cases
    println(exp(Float.NaN))
    println(exp(Float.POSITIVE_INFINITY))
    println(exp(Float.NEGATIVE_INFINITY))
}
```

```text title="输出"
2.71828
7.38905
0.36787
NaN
Infinity
0.0
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L904)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
