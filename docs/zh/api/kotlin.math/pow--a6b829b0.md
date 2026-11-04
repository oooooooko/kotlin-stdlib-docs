# pow

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将这个值提高到 `x` 电。

特殊情况：
  - `b.pow(0.0)` 为 `1.0`。
  - `b.pow(1.0) == b`。
  - `b.pow(NaN)` 为 `NaN`。
  - `x != 0.0` 时，`NaN.pow(x)` 为 `NaN`。
  - `abs(b) == 1.0` 时，`b.pow(Inf)` 为 `NaN`。
  - `b < 0` 且 `x` 为有限的非整数时，`b.pow(x)` 为 `NaN`。

@sample 样本.math.MathSamples.doubles.powDouble

??? note "查看英文原文"

    Raises this value to the power `x`.
    
    Special cases:
      - `b.pow(0.0)` is `1.0`
      - `b.pow(1.0) == b`
      - `b.pow(NaN)` is `NaN`
      - `NaN.pow(x)` is `NaN` for `x != 0.0`
      - `b.pow(Inf)` is `NaN` for `abs(b) == 1.0`
      - `b.pow(x)` is `NaN` for `b < 0` and `x` is finite and not an integer
    
    @sample samples.math.MathSamples.Doubles.powDouble

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Double.pow(x: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L439)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Double.pow(n: Int): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L455)

将这个值提高到 `n` 的整数。

详情请见其他超载`pow`。

@sample 样本.math.MathSamples.doubles.powInt

### 3. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Float.pow(x: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1031)

将这个值提高到 `x` 电。

特殊情况：
  - `b.pow(0.0)` 为 `1.0`。
  - `b.pow(1.0) == b`。
  - `b.pow(NaN)` 为 `NaN`。
  - `x != 0.0` 时，`NaN.pow(x)` 为 `NaN`。
  - `abs(b) == 1.0` 时，`b.pow(Inf)` 为 `NaN`。
  - `b < 0` 且 `x` 为有限的非整数时，`b.pow(x)` 为 `NaN`。

@sample 样本.math.MathSamples.floats.powFloat

### 4. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Float.pow(n: Int): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1047)

将这个值提高到 `n` 的整数。

详情请见其他超载`pow`。

@sample 样本.math.MathSamples.floats.powInt

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(2.0.pow(2.0))
    println(3.0.pow(1.0))
    println(4.0.pow(0.0))
    println(2.0.pow(-2.0))
    println(4.0.pow(0.5))
    println((-2.0).pow(2.0))

    // special cases
    println(Double.NaN.pow(42.0))
    println(Double.NaN.pow(0.0))
    println(3.0.pow(Double.NaN))
    println((-2.0).pow(0.75))
    println(1.0.pow(Double.POSITIVE_INFINITY))
    println(1.0.pow(Double.NEGATIVE_INFINITY))
    println(2.0.pow(Double.POSITIVE_INFINITY))
    println(2.0.pow(Double.NEGATIVE_INFINITY))
}
```

```text title="输出"
4.0
3.0
1.0
0.25
2.0
4.0
NaN
1.0
NaN
NaN
NaN
NaN
Infinity
0.0
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L276)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(2.0.pow(2))
    println(3.0.pow(1))
    println(4.0.pow(0))
    println(2.0.pow(-2))
    println((-2.0).pow(2))

    // special cases
    println(Double.NaN.pow(42))
    println(Double.NaN.pow(0))
}
```

```text title="输出"
4.0
3.0
1.0
0.25
4.0
NaN
1.0
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L296)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(2.0f.pow(2.0f))
    println(3.0f.pow(1.0f))
    println(4.0f.pow(0.0f))
    println(2.0f.pow(-2.0f))
    println(4.0f.pow(0.5f))
    println((-2.0f).pow(2.0f))

    // special cases
    println(Float.NaN.pow(42.0f))
    println(Float.NaN.pow(0.0f))
    println(3.0f.pow(Float.NaN))
    println((-2.0f).pow(0.75f))
    println(1.0f.pow(Float.POSITIVE_INFINITY))
    println(1.0f.pow(Float.NEGATIVE_INFINITY))
    println(2.0f.pow(Float.POSITIVE_INFINITY))
    println(2.0f.pow(Float.NEGATIVE_INFINITY))
}
```

```text title="输出"
4.0
3.0
1.0
0.25
2.0
4.0
NaN
1.0
NaN
NaN
NaN
NaN
Infinity
0.0
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L871)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(2.0f.pow(2))
    println(3.0f.pow(1))
    println(4.0f.pow(0))
    println(2.0f.pow(-2))
    println((-2.0f).pow(2))

    // special cases
    println(Float.NaN.pow(42))
    println(Float.NaN.pow(0))
}
```

```text title="输出"
4.0
3.0
1.0
0.25
4.0
NaN
1.0
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L891)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
