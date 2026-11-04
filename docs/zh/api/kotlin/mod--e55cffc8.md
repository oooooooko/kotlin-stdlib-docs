# mod

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将此值( divided) 的下层分割的剩余值乘以其他值( diovisor) 。

结果为零或与 _divisor_ 具有相同的符号,绝对值低于 dvisor. @sample 样本的绝对值。 misc. ilutins.mod.

??? note "查看英文原文"

    Calculates the remainder of flooring division of this value (dividend) by the other value (divisor).
    
    The result is either zero or has the same sign as the _divisor_ and has the absolute value less than the absolute value of the divisor.
    @sample samples.misc.Builtins.mod

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Byte.mod(other: Byte): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L25)

### 2. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Byte.mod(other: Short): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L47)

### 3. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Byte.mod(other: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L69)

### 4. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Byte.mod(other: Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L91)

### 5. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Short.mod(other: Byte): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L113)

### 6. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Short.mod(other: Short): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L135)

### 7. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Short.mod(other: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L157)

### 8. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Short.mod(other: Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L179)

### 9. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Int.mod(other: Byte): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L201)

### 10. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Int.mod(other: Short): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L223)

### 11. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Int.mod(other: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L248)

### 12. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Int.mod(other: Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L272)

### 13. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Long.mod(other: Byte): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L294)

### 14. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Long.mod(other: Short): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L316)

### 15. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Long.mod(other: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L338)

### 16. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Long.mod(other: Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L363)

### 17. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Float.mod(other: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L377)

将此值( divided) 的下层分割的剩余值乘以其他值( diovisor) 。

结果为零或与 _divisor_ 具有相同的符号,绝对值小于断面的绝对值。

如果结果不能准确表示,则四舍五入到最接近的可代表数字。在这种情况下,结果的绝对值可能小于或等于_ divisor. @sample 样本的绝对值。 misc. Builtins.modFloat.modFloat

### 18. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Float.mod(other: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L393)

将此值( divided) 的下层分割的剩余值乘以其他值( diovisor) 。

结果为零或与 _divisor_ 具有相同的符号,绝对值小于断面的绝对值。

如果结果不能准确表示,则四舍五入到最接近的可代表数字。在这种情况下,结果的绝对值可能小于或等于_ divisor. @sample 样本的绝对值。 misc. Builtins.modFloat.modFloat

### 19. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Double.mod(other: Float): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L407)

将此值( divided) 的下层分割的剩余值乘以其他值( diovisor) 。

结果为零或与 _divisor_ 具有相同的符号,绝对值小于断面的绝对值。

如果结果不能准确表示,则四舍五入到最接近的可代表数字。在这种情况下,结果的绝对值可能小于或等于_ divisor. @sample 样本的绝对值。 misc. Builtins.modFloat.modFloat

### 20. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Double.mod(other: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/FloorDivMod.kt#L421)

将此值( divided) 的下层分割的剩余值乘以其他值( diovisor) 。

结果为零或与 _divisor_ 具有相同的符号,绝对值小于断面的绝对值。

如果结果不能准确表示,则四舍五入到最接近的可代表数字。在这种情况下,结果的绝对值可能小于或等于_ divisor. @sample 样本的绝对值。 misc. Builtins.modFloat.modFloat

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.assertFailsWith



fun main() {
    // Regular remainder (%) takes the sign of the dividend
    println((-7) % 3)
    // mod takes the sign of the divisor
    println((-7).mod(3))
    println(7.mod(3))
    println(7.mod(-3))

    // A zero divisor throws, just like the % operator
    assertFailsWith<ArithmeticException> { 1.mod(0) }
}
```

```text title="输出"
-1
2
1
-2
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/builtins.kt#L60)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.assertFailsWith



fun main() {
    // For finite arguments, the result has the same sign as the divisor
    println((-7.5).mod(3.0))
    println(7.5.mod(-3.0))

    // The divisor is not required to be an integer
    println(5.0.mod(1.1))

    // A negative-zero dividend keeps its sign
    println((-0.0).mod(3.0))

    // Unlike integer mod, a zero divisor produces NaN instead of throwing
    println(5.0.mod(0.0))

    // If either argument is NaN, or the dividend is infinite, the result is NaN
    println(Double.NaN.mod(3.0))
    println(Double.POSITIVE_INFINITY.mod(3.0))

    // If only the divisor is infinite, the result is the dividend when the
    // signs agree, and the infinite divisor otherwise
    println(3.0.mod(Double.POSITIVE_INFINITY))
    println((-3.0).mod(Double.POSITIVE_INFINITY))
}
```

```text title="输出"
1.5
-1.5
0.5999999999999996
-0.0
NaN
NaN
NaN
3.0
Infinity
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/builtins.kt#L73)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
