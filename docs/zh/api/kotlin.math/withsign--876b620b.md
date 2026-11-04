# withSign

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回此值,符号位数与`sign`值相同。

如果 `sign` 是`NaN`,结果的符号是未定义的。

@sample 样本.math.MathSamples.Doubles,带有SignDouble的样本

??? note "查看英文原文"

    Returns this value with the sign bit same as of the `sign` value.
    
    If `sign` is `NaN` the sign of the result is undefined.
    
    @sample samples.math.MathSamples.Doubles.withSignDouble

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Double.withSign(sign: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L492)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Double.withSign(sign: Int): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L502)

返回此值,符号位数与`sign`值相同。

@sample 样本.math.MathSamples.Doubles.

### 3. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Float.withSign(sign: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1084)

返回此值,符号位数与`sign`值相同。

如果 `sign` 是`NaN`,结果的符号是未定义的。

@sample 样本.math.MathSamples.Floats,带有SignFloat的样本

### 4. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Float.withSign(sign: Int): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1094)

返回此值,符号位数与`sign`值相同。

@sample 样本.math.MathSamples.有Signint的花样

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(3.14.withSign(3.14))
    println(3.14.withSign(-3.14))
    println((-3.14).withSign(-3.14))
    println((-3.14).withSign(0.0))
    println(Double.NaN.withSign(-1.0))
}
```

```text title="输出"
3.14
-3.14
-3.14
3.14
NaN
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L223)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(3.14.withSign(100))
    println(3.14.withSign(-100))
    println((-3.14).withSign(-100))
    println((-3.14).withSign(0))
    println(Double.NaN.withSign(-1))
}
```

```text title="输出"
3.14
-3.14
-3.14
3.14
NaN
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L232)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(3.14f.withSign(3.14f))
    println(3.14f.withSign(-3.14f))
    println((-3.14f).withSign(-3.14f))
    println((-3.14f).withSign(0.0f))
    println(Float.NaN.withSign(-1.0f))
}
```

```text title="输出"
3.14
-3.14
-3.14
3.14
NaN
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L817)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(3.14f.withSign(100))
    println(3.14f.withSign(-100))
    println((-3.14f).withSign(-100))
    println((-3.14f).withSign(0))
    println(Float.NaN.withSign(-1))
}
```

```text title="输出"
3.14
-3.14
-3.14
3.14
NaN
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L826)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
