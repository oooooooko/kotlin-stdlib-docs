# sqrt

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

计算值 `x` 的正方根。

特殊情况:
  - `sqrt(NaN)`是`NaN`
  - `sqrt(-0.0)`是`-0.0`
- `sqrt(x)`是`NaN` 当`x < 0`时

@sample 样本.math.MathSamples.doubles.sqrt

??? note "查看英文原文"

    Computes the positive square root of the value `x`.
    
    Special cases:
      - `sqrt(NaN)` is `NaN`
      - `sqrt(-0.0)` is `-0.0`
      - `sqrt(x)` is `NaN` when `x < 0`
    
    @sample samples.math.MathSamples.Doubles.sqrt

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun sqrt(x: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L205)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun sqrt(x: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L793)

计算值 `x` 的正方根。

特殊情况:
  - `sqrt(NaN)`是`NaN`
  - `sqrt(-0.0)`是`-0.0`
- `sqrt(x)`是`NaN` 当`x < 0`时

@sample 样本.math.MathSamples.floatsqrt

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(sqrt(9.0))
    println(sqrt(5.76))
    // special cases
    println(sqrt(-0.0))
    println(sqrt(-4.0))
    println(sqrt(Double.NaN))
    println(sqrt(Double.POSITIVE_INFINITY))
}
```

```text title="输出"
3.0
2.4
-0.0
NaN
NaN
Infinity
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L253)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(sqrt(9.0f))
    println(sqrt(5.76f))

    // special cases
    println(sqrt(-0.0f))
    println(sqrt(-4.0f))
    println(sqrt(Float.NaN))
    println(sqrt(Float.POSITIVE_INFINITY))
}
```

```text title="输出"
3.0
2.4
-0.0
NaN
NaN
Infinity
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L847)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
