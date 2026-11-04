# absoluteValue

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回此值的绝对值。

特殊情况: - `NaN.absoluteValue` 为 `NaN`

@see abs 函数
@sample样本.math.MathSamples.doubles.absolute Value

??? note "查看英文原文"

    Returns the absolute value of this value.
    
    Special cases:
      - `NaN.absoluteValue` is `NaN`
    
    @see abs function
    @sample samples.math.MathSamples.Doubles.absoluteValue

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect val Double.absoluteValue: Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L465)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect val Float.absoluteValue: Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1057)

返回此值的绝对值。

特殊情况: - `NaN.absoluteValue` 为 `NaN`

@see abs 函数
@sample样本.math.MathSamples.floats.absolute Value

### 3. Common

```kotlin
@SinceKotlin("1.2")
public expect val Int.absoluteValue: Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1165)

返回此值的绝对值。

特殊情况: - `Int.MIN_VALUE.absoluteValue` ,因溢出而为 `Int.MIN_VALUE`

@see abs 函数
@sample样本.math.MathSamples.ints.absolute Value

### 4. Common

```kotlin
@SinceKotlin("1.2")
public expect val Long.absoluteValue: Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1218)

返回此值的绝对值。

特殊情况: - `Long.MIN_VALUE.absoluteValue` ,因溢出而为 `Long.MIN_VALUE`

@see abs 函数
@sample样本.math.MathSamples.Longs.absolute Value

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(3.14.absoluteValue)
    println((-3.14).absoluteValue)
    println((-0.0).absoluteValue)
    println(Double.NEGATIVE_INFINITY.absoluteValue)
    println(Double.NaN.absoluteValue)
}
```

```text title="输出"
3.14
3.14
0.0
Infinity
NaN
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L214)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(3.14f.absoluteValue)
    println((-3.14f).absoluteValue)
    println((-0.0f).absoluteValue)
    println(Float.NEGATIVE_INFINITY.absoluteValue)
    println(Float.NaN.absoluteValue)
}
```

```text title="输出"
3.14
3.14
0.0
Infinity
NaN
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L808)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(42.absoluteValue)
    println((-42).absoluteValue)
    // Special case: can't get the absolute value due to an overflow
    println(Int.MIN_VALUE.absoluteValue == Int.MIN_VALUE)
}
```

```text title="输出"
42
42
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1253)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(42L.absoluteValue)
    println((-42L).absoluteValue)
    // Special case: can't get the absolute value due to an overflow
    println(Long.MIN_VALUE.absoluteValue == Long.MIN_VALUE)
}
```

```text title="输出"
42
42
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1212)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
