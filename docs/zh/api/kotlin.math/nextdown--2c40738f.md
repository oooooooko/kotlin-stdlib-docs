# nextDown

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回接近此值的 `Double` 值,向负无穷方向返回。

特殊情况: - `NaN.nextDown() is ` N` - `Double.NEGATIVE_INFINITY.nextDown() is ` -无穷 ' - `0.0.nextDown()` 为 `-Double.MIN_VALUE`

@see 下一个 @see 下一个 @see lib @sample 样本 地图样本 地图样本 下个 @sample 样本 地图样本 地图样本 杜布斯 分层谷

??? note "查看英文原文"

    Returns the `Double` value nearest to this value in a direction of negative infinity.
    
    Special cases:
      - `NaN.nextDown() is `NaN`
      - `Double.NEGATIVE_INFINITY.nextDown() is `-Infinity`
      - `0.0.nextDown()` is `-Double.MIN_VALUE`
    
    @see nextUp
    @see nextTowards
    @see ulp
    @sample samples.math.MathSamples.Doubles.nextDown
    @sample samples.math.MathSamples.Doubles.discreteValues

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Double.nextDown(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L546)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    // Floating point numbers have discrete representation,
    // so depending on the value's magnitude, the step towards
    // the previous representable value will be different
    println(10000.0.nextDown())
    println(100000.0.nextDown())

    // Infinity is any value large enough to no longer fit Double,
    // so the previous value towards 0.0 is Double.MAX_VALUE
    println(Double.POSITIVE_INFINITY.nextDown() == Double.MAX_VALUE)

    // For 0.0, the previous value is the -Double.MIN_VALUE, the smallest representable Double value
    println(0.0.nextDown() == -Double.MIN_VALUE)

    // special cases
    println(Double.NaN.nextDown())
    println(Double.NEGATIVE_INFINITY.nextDown())
}
```

```text title="输出"
9999.999999999998
99999.99999999999
true
true
NaN
-Infinity
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L550)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    // Unlike true real numbers, Double can only represent a fixed set of discrete values.
    // According to IEEE-754, Double uses a single bit for a sign, 11 bits for the exponent, and 52 for the fraction.
    // The bigger the integer part of the floating point value, the less space remains for "fitting" fractional part.
    // As a result, starting from 2⁵² and until 2⁵³-1 Double values are incremented by 1.0
    // (meaning that there are no in-between values), values from 2⁵³ until 2⁵⁴-1 are incremented by 2.0,
    // but values in between 2⁵¹ and 2⁵²-1 are incremented by 0.5.
    //
    // The "distance" between a current value and the next one (the "increment" mentioned above) is dynamic,
    // it depends on the magnitude of the current value, and it could be checked using Double.ulp.
    val v2_52_53 = 4503599627370498.0 // value in range [2⁵², 2⁵³-1]
    println(v2_52_53.ulp)

    val v2_53_54 = 9007199254740998.0 // value in range [2⁵³, 2⁵⁴-1]
    println(v2_53_54.ulp)

    val v2_51_52 = 4503599627370490.0 // value in range [2⁵¹, 2⁵²-1]
    println(v2_51_52.ulp)

    // Instead of using ulp, you can also check the next and previous values representable with a Double
    // using Double.nextUp and Double.nextDown correspondingly.
    println(9007199254740998.0.nextUp() - 9007199254740998.0)
    println(9007199254740998.0 - 9007199254740998.0.nextDown())

    // As a more flexible alternative to nextUp/nextDown, one may use nextTowards, which accepts a value
    // that works as a direction to increase/decrease a given value towards.
    println(4503599627370496.0.nextTowards(Double.POSITIVE_INFINITY) - 4503599627370496.0)
    println(4503599627370496.0 - 4503599627370496.0.nextTowards(Double.NEGATIVE_INFINITY))
}
```

```text title="输出"
1.0
2.0
0.5
2.0
2.0
1.0
0.5
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L499)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
