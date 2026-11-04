# max

`kotlin.math` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回两个值的最大值。

如果其中任何一个值为 `NaN` ,结果为`NaN`。

@sample 样本.math.MathSamples. Doubles.max

??? note "查看英文原文"

    Returns the greater of two values.
    
    If either value is `NaN`, then the result is `NaN`.
    
    @sample samples.math.MathSamples.Doubles.max

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun max(a: Double, b: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L410)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun max(a: Float, b: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1000)

返回两个值的最大值。

如果其中任何一个值为 `NaN` ,结果为`NaN`。

@sample 样本.math.MathSamples.

### 3. Common

```kotlin
@SinceKotlin("1.2")
public expect fun max(a: Int, b: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1157)

返回两个值的最大值。

@sample 样本.math.MathSamples. Ints.max

### 4. Common

```kotlin
@SinceKotlin("1.2")
public expect fun max(a: Long, b: Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/MathH.kt#L1210)

返回两个值的最大值。

@sample 样本.math.MathSamples.Longs.max

### 5. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun max(a: UInt, b: UInt): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UMath.kt#L26)

返回两个值的最大值。

### 6. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun max(a: ULong, b: ULong): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UMath.kt#L35)

返回两个值的最大值。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(max(-1.0, 1.0))
    println(max(1.0, -1.0))
    println(max(-3.0, -1.0))
    println(max(-0.0, 0.0))

    // special cases
    println(max(Double.NaN, 0.0))
    println(max(-9000.0, Double.NaN))
    // Note that MIN_VALUE has a different meaning compared to Long.MIN_VALUE or Int.MIN_VALUE
    println(max(Double.MIN_VALUE, 0.0) == Double.MIN_VALUE)
    println(max(Double.POSITIVE_INFINITY, Double.MAX_VALUE))
}
```

```text title="输出"
1.0
1.0
-1.0
0.0
NaN
NaN
true
Infinity
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L484)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(max(-1.0f, 1.0f))
    println(max(1.0f, -1.0f))
    println(max(-3.0f, -1.0f))
    println(max(-0.0f, 0.0f))

    // special cases
    println(max(Float.NaN, 0.0f))
    println(max(-9000.0f, Float.NaN))
    // Note that MIN_VALUE has a different meaning compared to Long.MIN_VALUE or Int.MIN_VALUE
    println(max(Float.MIN_VALUE, 0.0f) == Float.MIN_VALUE)
    println(max(Float.POSITIVE_INFINITY, Float.MAX_VALUE))
}
```

```text title="输出"
1.0
1.0
-1.0
0.0
NaN
NaN
true
Infinity
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1079)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(max(-1, 1))
    println(max(1, -1))
    println(max(-3, -1))
}
```

```text title="输出"
1
1
-1
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1277)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(max(-1L, 1L))
    println(max(1L, -1L))
    println(max(-3L, -1L))
}
```

```text title="输出"
1
1
-1
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/math/MathSamples.kt#L1236)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
