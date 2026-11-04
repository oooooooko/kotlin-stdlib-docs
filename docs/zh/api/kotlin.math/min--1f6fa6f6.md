# min

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回两个值中较小部分。

如果其中任何一个值为 `NaN` ,结果为`NaN`。

@sample 样本.math.MathSamples.Doubles.min. 毛图样本。

??? note "查看英文原文"

    Returns the smaller of two values.
    
    If either value is `NaN`, then the result is `NaN`.
    
    @sample samples.math.MathSamples.Doubles.min

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun min(a: Double, b: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L400)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun min(a: Float, b: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L990)

返回两个值中较小部分。

如果其中任何一个值为 `NaN` ,结果为`NaN`。

@sample 样本.math.MathSamples.Floats.min. 地图样本

### 3. Common

```kotlin
@SinceKotlin("1.2")
public expect fun min(a: Int, b: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1149)

返回两个值中较小部分。

@sample 样本.math.MathSamples.Intsmin

### 4. Common

```kotlin
@SinceKotlin("1.2")
public expect fun min(a: Long, b: Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1202)

返回两个值中较小部分。

@sample 样本.math.MathSamples.Longs.min.

### 5. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun min(a: UInt, b: UInt): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UMath.kt#L8)

返回两个值中较小部分。

### 6. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun min(a: ULong, b: ULong): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UMath.kt#L17)

返回两个值中较小部分。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(min(-1.0, 1.0))
    println(min(1.0, -1.0))
    println(min(-3.0, -1.0))
    println(min(-0.0, 0.0))

    // special cases
    println(min(Double.NaN, 0.0))
    println(min(-9000.0, Double.NaN))
    // Note that MIN_VALUE has a different meaning compared to Long.MIN_VALUE or Int.MIN_VALUE
    println(min(Double.MIN_VALUE, 0.0))
    println(min(Double.POSITIVE_INFINITY, Double.MAX_VALUE) == Double.MAX_VALUE)
}
```

```text title="输出"
-1.0
-1.0
-3.0
-0.0
NaN
NaN
0.0
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L469)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(min(-1.0f, 1.0f))
    println(min(1.0f, -1.0f))
    println(min(-3.0f, -1.0f))
    println(min(-0.0f, 0.0f))

    // special cases
    println(min(Float.NaN, 0.0f))
    println(min(-9000.0f, Float.NaN))
    // Note that MIN_VALUE has a different meaning compared to Long.MIN_VALUE or Int.MIN_VALUE
    println(min(Float.MIN_VALUE, 0.0f))
    println(min(Float.POSITIVE_INFINITY, Float.MAX_VALUE) == Float.MAX_VALUE)
}
```

```text title="输出"
-1.0
-1.0
-3.0
-0.0
NaN
NaN
0.0
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1064)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(min(-1, 1))
    println(min(1, -1))
    println(min(-3, -1))
}
```

```text title="输出"
-1
-1
-3
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1270)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(min(-1L, 1L))
    println(min(1L, -1L))
    println(min(-3L, -1L))
}
```

```text title="输出"
-1
-1
-3
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1229)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
