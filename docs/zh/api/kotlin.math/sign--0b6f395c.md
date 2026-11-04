# sign

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回给定值 `x`: - `-1.0` 的符号。如果值为负值,返回 `x` 的 - `-1.0` ;如果值为负值,返回 0 返回 零 返回 ;如果值为正值,返回 `1.0`

特殊情况:
  - `sign(NaN)`是`NaN`
  - `sign(-0.0)`是`-0.0`

@sample 样本.math.MathSamples.Doubles.ignignFun

??? note "查看英文原文"

    Returns the sign of the given value `x`:
      - `-1.0` if the value is negative,
      - zero if the value is zero,
      - `1.0` if the value is positive
    
    Special cases:
      - `sign(NaN)` is `NaN`
      - `sign(-0.0)` is `-0.0`
    
    @sample samples.math.MathSamples.Doubles.signFun

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun sign(x: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L384)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect val Double.sign: Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L477)

返回此值的符号: - `-1.0` ,如果值为负值,返回 `-1.0` ;如果值为负值,返回0,返回0;如果值为正值,返回 `1.0`

特殊情况:
  - `NaN.sign`是`NaN`
  - `(-0.0).sign`是`-0.0`

@sample 样本.math.MathSamples.Doubles.sign. 签名

### 3. Common

```kotlin
@SinceKotlin("1.2")
public expect fun sign(x: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L973)

返回给定值 `x`: - `-1.0` 的符号。如果值为负值,返回 `x` 的 - `-1.0` ;如果值为负值,返回 0 返回 零 返回 ;如果值为正值,返回 `1.0`

特殊情况:
  - `sign(NaN)`是`NaN`
  - `sign(-0.0)`是`-0.0`

@sample 样本.math.MathSamples.Floats.ignign Fun

### 4. Common

```kotlin
@SinceKotlin("1.2")
public expect val Float.sign: Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1069)

返回此值的符号: - `-1.0` ,如果值为负值,返回 `-1.0` ;如果值为负值,返回0,返回0;如果值为正值,返回 `1.0`

特殊情况:
  - `NaN.sign`是`NaN`
  - `(-0.0).sign`是`-0.0`

@sample 样本.math.MathSamples.Floats.sign.ign. 样本

### 5. Common

```kotlin
@SinceKotlin("1.2")
public expect val Int.sign: Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1177)

返回此值的符号: - `-1` ,如果值为负值,返回 - `-1` ;如果值为负值,返回 - `0` ,如果值为零,返回 - `1` ;如果值为正值,返回 - `1`

@sample 样本.math.MathSamples.Ints.int.

### 6. Common

```kotlin
@SinceKotlin("1.2")
public expect val Long.sign: Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1230)

返回此值的符号: - `-1` ,如果值为负值,返回 - `-1` ;如果值为负值,返回 - `0` ,如果值为零,返回 - `1` ;如果值为正值,返回 - `1`

@sample 样本.math.MathSamples.Longs.sign.ign

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(sign(3.14))
    println(sign(-3.14))
    println(sign(0.0))
    println(sign(Double.POSITIVE_INFINITY))
    println(sign(Double.NEGATIVE_INFINITY))

    // Special cases
    println(sign(Double.NaN))
    println(sign(-0.0))
}
```

```text title="输出"
1.0
-1.0
0.0
1.0
-1.0
NaN
-0.0
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L123)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(3.14.sign)
    println((-3.14).sign)
    println(0.0.sign)
    println(Double.POSITIVE_INFINITY.sign)
    println(Double.NEGATIVE_INFINITY.sign)

    // Special cases
    println(Double.NaN.sign)
    println((-0.0).sign)
}
```

```text title="输出"
1.0
-1.0
0.0
1.0
-1.0
NaN
-0.0
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L110)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(sign(3.14f))
    println(sign(-3.14f))
    println(sign(0.0f))
    println(sign(Float.POSITIVE_INFINITY))
    println(sign(Float.NEGATIVE_INFINITY))

    // Special cases
    println(sign(Float.NaN))
    println(sign(-0.0f))
}
```

```text title="输出"
1.0
-1.0
0.0
1.0
-1.0
NaN
-0.0
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L717)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(3.14f.sign)
    println((-3.14f).sign)
    println(0.0f.sign)
    println(Float.POSITIVE_INFINITY.sign)
    println(Float.NEGATIVE_INFINITY.sign)

    // Special cases
    println(Float.NaN.sign)
    println((-0.0f).sign)
}
```

```text title="输出"
1.0
-1.0
0.0
1.0
-1.0
NaN
-0.0
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L704)

### 示例 5 · JVM

```kotlin title="示例 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(0.sign)
    println(9000.sign)
    println((-9000).sign)
    println(Int.MAX_VALUE.sign)
    println(Int.MIN_VALUE.sign)
}
```

```text title="输出"
0
1
-1
1
-1
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1261)

### 示例 6 · JVM

```kotlin title="示例 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(0L.sign)
    println(9000L.sign)
    println((-9000L).sign)
    println(Long.MAX_VALUE.sign)
    println(Long.MIN_VALUE.sign)
}
```

```text title="输出"
0
1
-1
1
-1
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1220)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
