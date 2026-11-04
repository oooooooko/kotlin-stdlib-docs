# toUShort

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将这个`Byte`值转换为 `UShort` 。

如果这个值为正值,则得出的 `UShort` 值与这个`Byte`值的数值相同。

所得出的`UShort` 值中最小的8位数与这个`Byte` 值的8位数相同,而最重要的8位数则填充这个值的符号位。

??? note "查看英文原文"

    Converts this `Byte` value to `UShort`.
    
    If this value is positive, the resulting `UShort` value represents the same numerical value as this `Byte`.
    
    The least significant 8 bits of the resulting `UShort` value are the same as the bits of this `Byte` value,
    whereas the most significant 8 bits are filled with the sign bit of this value.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Byte.toUShort(): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UShort.kt#L413)

### 2. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Short.toUShort(): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UShort.kt#L425)

将这个`Short`值转换为 `UShort` 。

如果这个值为正值,则得出的 `UShort` 值与这个`Short`值的数值相同。

所产生的`UShort`值与这个`Short`值具有相同的二进制表示。

### 3. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Int.toUShort(): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UShort.kt#L436)

将这个`Int`值转换为 `UShort` 。

如果这个值为正值,且小于或等于 `UShort.MAX_VALUE` ,则由此得出的`UShort`值与这个`Int`值具有相同的数值。

由此得出的`UShort`值代表的值为`Int`值中最小的16位数。

### 4. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
@kotlin.internal.IntrinsicConstEvaluation
public inline fun Long.toUShort(): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UShort.kt#L448)

将这个`Long`值转换为 `UShort` 。

如果这个值为正值,且小于或等于 `UShort.MAX_VALUE` ,则由此得出的`UShort`值与这个`Long`值具有相同的数值。

由此得出的`UShort`值代表的值为`Long`值中最小的16位数。

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
    val result = source.`toUShort`()
    println(result)
}
```

```text title="输出"
5
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
