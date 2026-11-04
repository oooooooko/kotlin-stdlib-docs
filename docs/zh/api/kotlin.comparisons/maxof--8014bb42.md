# maxOf

`kotlin.comparisons` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回两个值的最大值。

如果数值相等,则返回第一个数值。

??? note "查看英文原文"

    Returns the greater of two values.
    
    If values are equal, returns the first one.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.1")
public expect fun <T : Comparable<T>> maxOf(a: T, b: T): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L20)

### 2. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun maxOf(a: Byte, b: Byte): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L28)

返回两个值的最大值。

### 3. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun maxOf(a: Short, b: Short): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L34)

返回两个值的最大值。

### 4. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun maxOf(a: Int, b: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L40)

返回两个值的最大值。

### 5. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun maxOf(a: Long, b: Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L46)

返回两个值的最大值。

### 6. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun maxOf(a: Float, b: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L52)

返回两个值的最大值。

如果其中任何一个值为 `NaN` ,则返回 `NaN` 。

### 7. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun maxOf(a: Double, b: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L60)

返回两个值的最大值。

如果其中任何一个值为 `NaN` ,则返回 `NaN` 。

### 8. Common

```kotlin
@SinceKotlin("1.1")
public expect fun <T : Comparable<T>> maxOf(a: T, b: T, c: T): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L68)

返回三个值的最大值。

如果存在多重等同的最大化值,则返回第一个值。

### 9. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun maxOf(a: Byte, b: Byte, c: Byte): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L76)

返回三个值的最大值。

### 10. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun maxOf(a: Short, b: Short, c: Short): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L83)

返回三个值的最大值。

### 11. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun maxOf(a: Int, b: Int, c: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L90)

返回三个值的最大值。

### 12. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun maxOf(a: Long, b: Long, c: Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L97)

返回三个值的最大值。

### 13. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun maxOf(a: Float, b: Float, c: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L104)

返回三个值的最大值。

如果值为 `NaN` ,则返回 `NaN` 。

### 14. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public expect inline fun maxOf(a: Double, b: Double, c: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L113)

返回三个值的最大值。

如果值为 `NaN` ,则返回 `NaN` 。

### 15. Common

```kotlin
@SinceKotlin("1.1")
public fun <T> maxOf(a: T, b: T, c: T, comparator: Comparator<in T>): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L122)

返回给定的 `comparator` 指定的顺序,以三个数值的较大值为准。

如果存在多重等同的最大化值,则返回第一个值。

### 16. Common

```kotlin
@SinceKotlin("1.1")
public fun <T> maxOf(a: T, b: T, comparator: Comparator<in T>): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L132)

返回给定的 `comparator` 指定的顺序中两个数值的最大值。

如果数值相等,则返回第一个数值。

### 17. Common

```kotlin
@SinceKotlin("1.4")
public expect fun <T : Comparable<T>> maxOf(a: T, vararg other: T): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L142)

返回给定值的最大值。

如果存在多重等同的最大化值,则返回第一个值。

### 18. Common

```kotlin
@SinceKotlin("1.4")
public expect fun maxOf(a: Byte, vararg other: Byte): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L150)

返回给定值的最大值。

### 19. Common

```kotlin
@SinceKotlin("1.4")
public expect fun maxOf(a: Short, vararg other: Short): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L156)

返回给定值的最大值。

### 20. Common

```kotlin
@SinceKotlin("1.4")
public expect fun maxOf(a: Int, vararg other: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L162)

返回给定值的最大值。

### 21. Common

```kotlin
@SinceKotlin("1.4")
public expect fun maxOf(a: Long, vararg other: Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L168)

返回给定值的最大值。

### 22. Common

```kotlin
@SinceKotlin("1.4")
public expect fun maxOf(a: Float, vararg other: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L174)

返回给定值的最大值。

如果值为 `NaN` ,则返回 `NaN` 。

### 23. Common

```kotlin
@SinceKotlin("1.4")
public expect fun maxOf(a: Double, vararg other: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L182)

返回给定值的最大值。

如果值为 `NaN` ,则返回 `NaN` 。

### 24. Common

```kotlin
@SinceKotlin("1.4")
public fun <T> maxOf(a: T, vararg other: T, comparator: Comparator<in T>): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Comparisons.kt#L190)

根据给定的 `comparator` 指定的顺序返回给定值的最大值。

如果存在多重等同的最大化值,则返回第一个值。

### 25. Common

```kotlin
@SinceKotlin("1.5")
public fun maxOf(a: UInt, b: UInt): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L20)

返回两个值的最大值。

### 26. Common

```kotlin
@SinceKotlin("1.5")
public fun maxOf(a: ULong, b: ULong): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L28)

返回两个值的最大值。

### 27. Common

```kotlin
@SinceKotlin("1.5")
public fun maxOf(a: UByte, b: UByte): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L36)

返回两个值的最大值。

### 28. Common

```kotlin
@SinceKotlin("1.5")
public fun maxOf(a: UShort, b: UShort): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L44)

返回两个值的最大值。

### 29. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun maxOf(a: UInt, b: UInt, c: UInt): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L52)

返回三个值的最大值。

### 30. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun maxOf(a: ULong, b: ULong, c: ULong): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L61)

返回三个值的最大值。

### 31. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun maxOf(a: UByte, b: UByte, c: UByte): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L70)

返回三个值的最大值。

### 32. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline fun maxOf(a: UShort, b: UShort, c: UShort): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L79)

返回三个值的最大值。

### 33. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun maxOf(a: UInt, vararg other: UInt): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L88)

返回给定值的最大值。

### 34. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun maxOf(a: ULong, vararg other: ULong): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L99)

返回给定值的最大值。

### 35. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun maxOf(a: UByte, vararg other: UByte): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L110)

返回给定值的最大值。

### 36. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun maxOf(a: UShort, vararg other: UShort): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UComparisons.kt#L121)

返回给定值的最大值。

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
    val result = `maxOf`(1, 1)
    println(result)
}
```

```text title="输出"
1
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
