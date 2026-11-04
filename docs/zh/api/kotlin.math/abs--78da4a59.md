# abs

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回给定值`x`的绝对值。

特殊情况: - `abs(NaN)` 为 `NaN`

@see 绝对价值扩展财产,包括 `Double` @sample 样本。

??? note "查看英文原文"

    Returns the absolute value of the given value `x`.
    
    Special cases:
      - `abs(NaN)` is `NaN`
    
    @see absoluteValue extension property for `Double`
    @sample samples.math.MathSamples.Doubles.abs

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun abs(x: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L372)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun abs(x: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L961)

返回给定值`x`的绝对值。

特殊情况: - `abs(NaN)` 为 `NaN`

@see 绝对价值扩展财产,包括 `Float` @sample 样本。

### 3. Common

```kotlin
@SinceKotlin("1.2")
public expect fun abs(n: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1137)

返回给定值`n`的绝对值。

特殊情况: - `abs(Int.MIN_VALUE)` ,因溢出而为 `Int.MIN_VALUE`

@see 绝对价值扩展财产, `Int` @sample 样本。

### 4. Common

```kotlin
@SinceKotlin("1.2")
public expect fun abs(n: Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1190)

返回给定值`n`的绝对值。

特殊情况: - `abs(Long.MIN_VALUE)` ,因溢出而为 `Long.MIN_VALUE`

@see 绝对价值扩展财产, `Long` @sample 样本。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(abs(3.14))
    println(abs(-3.14))
    println(abs(-0.0))
    println(abs(Double.NEGATIVE_INFINITY))
    println(abs(Double.NaN))
}
```

```text title="输出"
3.14
3.14
0.0
Infinity
NaN
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L205)

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
    println(abs(42))
    println(abs(-42))
    // Special case: can't get the absolute value due to an overflow
    println(abs(Int.MIN_VALUE) == Int.MIN_VALUE)
}
```

```text title="输出"
42
42
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1245)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(abs(42L))
    println(abs(-42L))
    // Special case: can't get the absolute value due to an overflow
    println(abs(Long.MIN_VALUE) == Long.MIN_VALUE)
}
```

```text title="输出"
42
42
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1204)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
