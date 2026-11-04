# cbrt

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回 `x` 的立方根。 对于任何 `x`, `cbrt(-x) == -cbrt(x)`; 负值的立方根是该数值大小的立方根的负值 。

特殊情形: - 如果争论为 `NaN` ,结果为 `NaN` 。 - 如果争论是无限的,结果与争论的符号相同。 - 如果争论为零,结果为零,结果与争论的符号相同。

@sample 样本.math.MathSamples.doubles.cbrt

??? note "查看英文原文"

    Returns the cube root of `x`. For any `x`, `cbrt(-x) == -cbrt(x)`;
    that is, the cube root of a negative value is the negative of the cube root
    of that value's magnitude.
    
    Special cases:
      - If the argument is `NaN`, then the result is `NaN`.
      - If the argument is infinite, then the result is an infinity with the same sign as the argument.
      - If the argument is zero, then the result is a zero with the same sign as the argument.
    
    @sample samples.math.MathSamples.Doubles.cbrt

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.8")
public expect fun cbrt(x: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L421)

### 2. Common

```kotlin
@SinceKotlin("1.8")
@WasExperimental(ExperimentalStdlibApi::class)
public expect fun cbrt(x: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1011)

返回 `x` 的立方根。 对于任何 `x`, `cbrt(-x) == -cbrt(x)`; 负值的立方根是该数值大小的立方根的负值 。

特殊情形: - 如果争论为 `NaN` ,结果为 `NaN` 。 - 如果争论是无限的,结果与争论的符号相同。 - 如果争论为零,结果为零,结果与争论的符号相同。

@sample 样本.math.MathSamples.cbrt

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(cbrt(8.0))
    println(cbrt(-8.0))

    // special cases
    println(cbrt(Double.NaN))
    println(cbrt(Double.POSITIVE_INFINITY))
    println(cbrt(Double.NEGATIVE_INFINITY))
    println(cbrt(-0.0))
}
```

```text title="输出"
2.0
-2.0
NaN
Infinity
-Infinity
-0.0
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L241)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(cbrt(8.0f))
    println(cbrt(-8.0f))

    // special cases
    println(cbrt(Float.NaN))
    println(cbrt(Float.POSITIVE_INFINITY))
    println(cbrt(Float.NEGATIVE_INFINITY))
    println(cbrt(-0.0f))
}
```

```text title="输出"
2.0
-2.0
NaN
Infinity
-Infinity
-0.0
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L835)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
