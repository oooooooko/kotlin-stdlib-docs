# roundToInt

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

圆形值为 `Double` ,折成最接近的整数,然后将结果转换为 `Int` 。 将带四舍五入为正无穷。

特殊情况: - `x.roundToInt() == Int.MAX_VALUE` , `x > Int.MAX_VALUE` - `x.roundToInt() == Int.MIN_VALUE` , `x < Int.MIN_VALUE`

@throws 非法设备除外,如果值为 `NaN` @sample 样本.math.MathSamples.Doubles.jour ToInt 。

??? note "查看英文原文"

    Rounds this `Double` value to the nearest integer and converts the result to `Int`.
    Ties are rounded towards positive infinity.
    
    Special cases:
      - `x.roundToInt() == Int.MAX_VALUE` when `x > Int.MAX_VALUE`
      - `x.roundToInt() == Int.MIN_VALUE` when `x < Int.MIN_VALUE`
    
    @throws IllegalArgumentException when this value is `NaN`
    @sample samples.math.MathSamples.Doubles.roundToInt

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Double.roundToInt(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L579)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Float.roundToInt(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1103)

圆形值为 `Float` ,折成最接近的整数,然后将结果转换为 `Int` 。 将带四舍五入为正无穷。

特殊情况: - `x.roundToInt() == Int.MAX_VALUE` , `x > Int.MAX_VALUE` - `x.roundToInt() == Int.MIN_VALUE` , `x < Int.MIN_VALUE`

@throws 非法证据排除值为 `NaN` @sample 样本.math.MathSamples.Floats.foundToInt 的这一值的例外。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    println(3.14159.roundToInt())
    println((-10.0).roundToInt())
    // Values greater than Int.MAX_VALUE are rounded to Int.MAX_VALUE
    println((Int.MAX_VALUE.toDouble() + 1.0).roundToInt() == Int.MAX_VALUE)
    println(Double.POSITIVE_INFINITY.roundToInt() == Int.MAX_VALUE)
    // Values smaller than Int.MIN_VALUE are rounded to Int.MIN_VALUE
    println((Int.MIN_VALUE.toDouble() - 1.0).roundToInt() == Int.MIN_VALUE)
    println(Double.NEGATIVE_INFINITY.roundToInt() == Int.MIN_VALUE)
    // NaN could not be rounded to Int
    assertFailsWith<IllegalArgumentException> { Double.NaN.roundToInt() }
}
```

```text title="输出"
3
-10
true
true
true
true
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L82)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    println(3.14159f.roundToInt())
    println((-10.0f).roundToInt())
    // Values greater than Int.MAX_VALUE are rounded to Int.MAX_VALUE
    println((Int.MAX_VALUE.toFloat() * 2.0f).roundToInt() == Int.MAX_VALUE)
    println(Float.POSITIVE_INFINITY.roundToInt() == Int.MAX_VALUE)
    // Values smaller than Int.MIN_VALUE are rounded to Int.MIN_VALUE
    println((Int.MIN_VALUE.toFloat() * 2.0f).roundToInt() == Int.MIN_VALUE)
    println(Float.NEGATIVE_INFINITY.roundToInt() == Int.MIN_VALUE)
    // NaN could not be rounded to Int
    assertFailsWith<IllegalArgumentException> { Float.NaN.roundToInt() }
}
```

```text title="输出"
3
-10
true
true
true
true
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L676)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
