# ceil

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将给定值 `x` 的整数舍入为正无穷。

特殊情况: - `ceil(x)` 为 `x` ,其中`x`为`NaN`,或`+Inf`或`-Inf`,或已经是一个数学整数。

@return 最小的双倍值,大于或等于给定值`x`, 是一个数学整数。

@sample 样本. math. MathSamples. Doubles. ceil @sample 样本.mathSamples. Doubles.

??? note "查看英文原文"

    Rounds the given value `x` to an integer towards positive infinity.
    
    Special cases:
      - `ceil(x)` is `x` where `x` is `NaN` or `+Inf` or `-Inf` or already a mathematical integer.
    
    @return the smallest double value that is greater than or equal to the given value `x` and is a mathematical integer.
    
    @sample samples.math.MathSamples.Doubles.ceil
    @sample samples.math.MathSamples.Doubles.roundingModes

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun ceil(x: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L318)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun ceil(x: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L906)

将给定值 `x` 的整数舍入为正无穷。

特殊情况: - `ceil(x)` 为 `x` ,其中`x`为`NaN`,或`+Inf`或`-Inf`,或已经是一个数学整数。

@return 最小浮点数值,大于或等于给定值`x`,是一个数学整数。

@sample 样本. math. MathSamples. Floats. ceil @sample 样本.math.MathSamples.Floats.

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(ceil(3.14159))
    println(ceil(-1.1))
    // 10.0 is already an "integer", so no rounding will take place
    println(ceil(10.0))
    // Special cases
    println(ceil(Double.NaN))
    println(ceil(Double.POSITIVE_INFINITY))
    println(ceil(Double.NEGATIVE_INFINITY))
}
```

```text title="输出"
4.0
-1.0
10.0
NaN
Infinity
-Infinity
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L27)

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
    println(ceil(3.14159f))
    println(ceil(-1.1f))
    // 10.0 is already an "integer", so no rounding will take place
    println(ceil(10.0f))
    // Special cases
    println(ceil(Float.NaN))
    println(ceil(Float.POSITIVE_INFINITY))
    println(ceil(Float.NEGATIVE_INFINITY))
}
```

```text title="输出"
4.0
-1.0
10.0
NaN
Infinity
-Infinity
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L621)

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
