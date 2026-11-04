# toULong

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将这个`Byte`值转换为 `ULong` 。

如果这个值为正值,则得出的 `ULong` 值与这个`Byte`值的数值相同。

所得出的`ULong` 值中最小的8位数与这个`Byte` 值的8位数相同,而最重要的56位数则以这个值的符号位填充。

??? note "查看英文原文"

    Converts this `Byte` value to `ULong`.
    
    If this value is positive, the resulting `ULong` value represents the same numerical value as this `Byte`.
    
    The least significant 8 bits of the resulting `ULong` value are the same as the bits of this `Byte` value,
    whereas the most significant 56 bits are filled with the sign bit of this value.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Byte.toULong(): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/ULong.kt#L439)

### 2. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Short.toULong(): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/ULong.kt#L451)

将这个`Short`值转换为 `ULong` 。

如果这个值为正值,则得出的 `ULong` 值与这个`Short`值的数值相同。

由此得出的`ULong` 值中最小的16位数与这个`Short` 值的16位数相同,而最重要的48位数则以这个值的符号位填充。

### 3. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Int.toULong(): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/ULong.kt#L463)

将这个`Int`值转换为 `ULong` 。

如果这个值为正值,则得出的 `ULong` 值与这个`Int`值的数值相同。

由此得出的`ULong` 值中最小的32位数与这个`Int` 值的3位数相同,而最重要的32位数则以这个值的符号位填充。

### 4. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Long.toULong(): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/ULong.kt#L475)

将这个`Long`值转换为 `ULong` 。

如果这个值为正值,则得出的 `ULong` 值与这个`Long`值的数值相同。

所产生的`ULong`值与这个`Long`值具有相同的二进制表示。

### 5. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Float.toULong(): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/ULong.kt#L487)

将这个`Float`值转换为 `ULong` 。

如果有分部分,则四舍五入为零。
如果返回为零,则返回为零`Float`负值或`NaN`, `ULong.MAX_VALUE`如果大于`ULong.MAX_VALUE`.

### 6. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Double.toULong(): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/ULong.kt#L497)

将这个`Double`值转换为 `ULong` 。

如果有分部分,则四舍五入为零。
如果返回为零,则返回为零`Double`负值或`NaN`, `ULong.MAX_VALUE`如果大于`ULong.MAX_VALUE`.

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.*

fun main() {
    val source = 5.toByte()
    val result = source.`toULong`()
    println(result)
}
```

```text title="输出"
5
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
