# cos

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

计算以弧度表示的 `x` 角的余弦。

特殊情况: - `cos(NaN|+Inf|-Inf)` 为 `NaN`

@sample 样本.math.MathSamples.doubles.cos. 样本

??? note "查看英文原文"

    Computes the cosine of the angle `x` given in radians.
    
    Special cases:
     - `cos(NaN|+Inf|-Inf)` is `NaN`
    
    @sample samples.math.MathSamples.Doubles.cos

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun cos(x: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L36)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun cos(x: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L624)

计算以弧度表示的 `x` 角的余弦。

特殊情况: - `cos(NaN|+Inf|-Inf)` 为 `NaN`

@sample 样本.math.MathSamples.floats.cos

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val epsilon = 1e-10

    println(cos(0.0))
    // Results may not be exact, so we're only checking that they are within epsilon from the expected value
    // cos(π/2) = 0
    println(cos(PI / 2).absoluteValue < epsilon)
    println(cos(PI))

    // special cases
    println(cos(Double.NaN))
    println(cos(Double.POSITIVE_INFINITY))
    println(cos(Double.NEGATIVE_INFINITY))
}
```

```text title="输出"
1.0
true
-1.0
NaN
NaN
NaN
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L356)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val epsilon = 1e-6f

    println(cos(0.0f))
    // Results may not be exact, so we're only checking that they are within epsilon from the expected value
    // cos(π/2) = 0
    println(cos(PI.toFloat() / 2).absoluteValue < epsilon)
    println(cos(PI.toFloat()))

    // special cases
    println(cos(Float.NaN))
    println(cos(Float.POSITIVE_INFINITY))
    println(cos(Float.NEGATIVE_INFINITY))
}
```

```text title="输出"
1.0
true
-1.0
NaN
NaN
NaN
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L951)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
