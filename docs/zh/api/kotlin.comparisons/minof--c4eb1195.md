# minOf

`kotlin.comparisons` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回两个值中较小部分。

如果数值相等,则返回第一个数值。

??? note "查看英文原文"

    Returns the smaller of two values.
    
    If values are equal, returns the first one.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.1")
public expect fun <T : Comparable<T>> minOf(a: T, b: T): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L202)

### 2. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun minOf(a: Byte, b: Byte): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L210)

返回两个值中较小部分。

### 3. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun minOf(a: Short, b: Short): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L216)

返回两个值中较小部分。

### 4. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun minOf(a: Int, b: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L222)

返回两个值中较小部分。

### 5. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun minOf(a: Long, b: Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L228)

返回两个值中较小部分。

### 6. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun minOf(a: Float, b: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L234)

返回两个值中较小部分。

如果其中任何一个值为 `NaN` ,则返回 `NaN` 。

### 7. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun minOf(a: Double, b: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L242)

返回两个值中较小部分。

如果其中任何一个值为 `NaN` ,则返回 `NaN` 。

### 8. Common

```kotlin
@SinceKotlin("1.1")
public expect fun <T : Comparable<T>> minOf(a: T, b: T, c: T): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L250)

返回三个数值中较小的数值。

如果有多个等值最低值,则返回第一个值。

### 9. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun minOf(a: Byte, b: Byte, c: Byte): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L258)

返回三个数值中较小的数值。

### 10. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun minOf(a: Short, b: Short, c: Short): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L265)

返回三个数值中较小的数值。

### 11. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun minOf(a: Int, b: Int, c: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L272)

返回三个数值中较小的数值。

### 12. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun minOf(a: Long, b: Long, c: Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L279)

返回三个数值中较小的数值。

### 13. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun minOf(a: Float, b: Float, c: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L286)

返回三个数值中较小的数值。

如果值为 `NaN` ,则返回 `NaN` 。

### 14. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun minOf(a: Double, b: Double, c: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L295)

返回三个数值中较小的数值。

如果值为 `NaN` ,则返回 `NaN` 。

### 15. Common

```kotlin
@SinceKotlin("1.1")
public fun <T> minOf(a: T, b: T, c: T, comparator: Comparator<in T>): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L304)

返回给定 `comparator` 指定的顺序,以三个数值中较小的数值返回。

如果有多个等值最低值,则返回第一个值。

### 16. Common

```kotlin
@SinceKotlin("1.1")
public fun <T> minOf(a: T, b: T, comparator: Comparator<in T>): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L314)

返回给定的 `comparator` 指定的顺序,以两个数值中较小的两个值返回。

如果数值相等,则返回第一个数值。

### 17. Common

```kotlin
@SinceKotlin("1.4")
public expect fun <T : Comparable<T>> minOf(a: T, vararg other: T): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L324)

返回给定值中较小部分。

如果有多个等值最低值,则返回第一个值。

### 18. Common

```kotlin
@SinceKotlin("1.4")
public expect fun minOf(a: Byte, vararg other: Byte): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L332)

返回给定值中较小部分。

### 19. Common

```kotlin
@SinceKotlin("1.4")
public expect fun minOf(a: Short, vararg other: Short): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L338)

返回给定值中较小部分。

### 20. Common

```kotlin
@SinceKotlin("1.4")
public expect fun minOf(a: Int, vararg other: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L344)

返回给定值中较小部分。

### 21. Common

```kotlin
@SinceKotlin("1.4")
public expect fun minOf(a: Long, vararg other: Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L350)

返回给定值中较小部分。

### 22. Common

```kotlin
@SinceKotlin("1.4")
public expect fun minOf(a: Float, vararg other: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L356)

返回给定值中较小部分。

如果值为 `NaN` ,则返回 `NaN` 。

### 23. Common

```kotlin
@SinceKotlin("1.4")
public expect fun minOf(a: Double, vararg other: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L364)

返回给定值中较小部分。

如果值为 `NaN` ,则返回 `NaN` 。

### 24. Common

```kotlin
@SinceKotlin("1.4")
public fun <T> minOf(a: T, vararg other: T, comparator: Comparator<in T>): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L372)

返回给定值的较小值,根据给定的 `comparator` 指定的顺序返回。

如果有多个等值最低值,则返回第一个值。

### 25. Common

```kotlin
@SinceKotlin("1.5")
public fun minOf(a: UInt, b: UInt): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L132)

返回两个值中较小部分。

### 26. Common

```kotlin
@SinceKotlin("1.5")
public fun minOf(a: ULong, b: ULong): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L140)

返回两个值中较小部分。

### 27. Common

```kotlin
@SinceKotlin("1.5")
public fun minOf(a: UByte, b: UByte): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L148)

返回两个值中较小部分。

### 28. Common

```kotlin
@SinceKotlin("1.5")
public fun minOf(a: UShort, b: UShort): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L156)

返回两个值中较小部分。

### 29. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun minOf(a: UInt, b: UInt, c: UInt): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L164)

返回三个数值中较小的数值。

### 30. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun minOf(a: ULong, b: ULong, c: ULong): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L173)

返回三个数值中较小的数值。

### 31. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun minOf(a: UByte, b: UByte, c: UByte): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L182)

返回三个数值中较小的数值。

### 32. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun minOf(a: UShort, b: UShort, c: UShort): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L191)

返回三个数值中较小的数值。

### 33. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun minOf(a: UInt, vararg other: UInt): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L200)

返回给定值中较小部分。

### 34. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun minOf(a: ULong, vararg other: ULong): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L211)

返回给定值中较小部分。

### 35. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun minOf(a: UByte, vararg other: UByte): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L222)

返回给定值中较小部分。

### 36. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun minOf(a: UShort, vararg other: UShort): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L233)

返回给定值中较小部分。

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
import kotlin.comparisons.*

fun main() {
    val result = `minOf`(1, 1)
    println(result)
}
```

```text title="输出"
1
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
