# round

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将给定值`x` 的整数舍入到最接近的整数,将连接四舍五入到整数。

特殊情况: - `round(x)` 为 `x` ,其中`x`为`NaN`,或`+Inf`或`-Inf`,或已经是一个数学整数。

@sample 样本. math. MathSamples. Doubles. 轮 @sample 样本. mathSamples.

??? note "查看英文原文"

    Rounds the given value `x` towards the closest integer with ties rounded towards even integer.
    
    Special cases:
      - `round(x)` is `x` where `x` is `NaN` or `+Inf` or `-Inf` or already a mathematical integer.
    
    @sample samples.math.MathSamples.Doubles.round
    @sample samples.math.MathSamples.Doubles.roundingModes

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun round(x: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L360)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun round(x: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L948)

将给定值`x` 的整数舍入到最接近的整数,将连接四舍五入到整数。

特殊情况: - `round(x)` 为 `x` ,其中`x`为`NaN`,或`+Inf`或`-Inf`,或已经是一个数学整数。

@sample 样本. math. MathSamples. Floats. 轮 @sample 样本. mathSamples. Floats.

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(round(3.49))
    println(round(3.51))
    // 3.5 is between 3.0 and 4.0, so it is rounded towards an even number 4.0
    println(round(3.5))
    // 2.5 is between 2.0 and 3.0, so it is rounded towards an even number 2.0
    println(round(2.5))
    // -10.0 is already an "integer", so no rounding will take place
    println(truncate(-10.0))
    // Special cases
    println(round(Double.NaN))
    println(round(Double.POSITIVE_INFINITY))
    println(round(Double.NEGATIVE_INFINITY))
}
```

```text title="输出"
3.0
4.0
4.0
2.0
-10.0
NaN
Infinity
-Infinity
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L51)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(floor(3.5))
    println(ceil(3.5))
    println(truncate(3.5))
    println(round(3.5))
    println(round(3.49))

    println(floor(-3.5))
    println(ceil(-3.5))
    println(truncate(-3.5))
    println(round(-3.5))
    println(round(-3.49))
}
```

```text title="输出"
3.0
4.0
3.0
4.0
3.0
-4.0
-3.0
-3.0
-4.0
-3.0
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L67)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(round(3.49f))
    println(round(3.51f))
    // 3.5 is between 3.0 and 4.0, so it is rounded towards an even number 4.0
    println(round(3.5f))
    // 2.5 is between 2.0 and 3.0, so it is rounded towards an even number 2.0
    println(round(2.5f))
    // -10.0 is already an "integer", so no rounding will take place
    println(truncate(-10.0f))
    // Special cases
    println(round(Float.NaN))
    println(round(Float.POSITIVE_INFINITY))
    println(round(Float.NEGATIVE_INFINITY))
}
```

```text title="输出"
3.0
4.0
4.0
2.0
-10.0
NaN
Infinity
-Infinity
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L645)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(floor(3.5f))
    println(ceil(3.5f))
    println(truncate(3.5f))
    println(round(3.5f))
    println(round(3.49f))

    println(floor(-3.5f))
    println(ceil(-3.5f))
    println(truncate(-3.5f))
    println(round(-3.5f))
    println(round(-3.49f))
}
```

```text title="输出"
3.0
4.0
3.0
4.0
3.0
-4.0
-3.0
-3.0
-4.0
-3.0
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L661)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
