# contains

`kotlin.ranges` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果此范围包含指定的 `element` , 则返回 `true` 。

如果 `element` 是 `null`, 则总是返回 `false` 。

??? note "查看英文原文"

    Returns `true` if this range contains the specified `element`.
    
    Always returns `false` if the `element` is `null`.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
@kotlin.internal.InlineOnly
public inline operator fun IntRange.contains(element: Int?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L284)

### 2. Common

```kotlin
@SinceKotlin("1.3")
@kotlin.internal.InlineOnly
public inline operator fun LongRange.contains(element: Long?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L295)

### 3. Common

```kotlin
@SinceKotlin("1.3")
@kotlin.internal.InlineOnly
public inline operator fun CharRange.contains(element: Char?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L306)

### 4. Common

```kotlin
@kotlin.jvm.JvmName("intRangeContains")
public operator fun ClosedRange<Int>.contains(value: Byte): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L317)

检查指定的 `value` 是否属于此范围。

### 5. Common

```kotlin
@kotlin.jvm.JvmName("longRangeContains")
public operator fun ClosedRange<Long>.contains(value: Byte): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L325)

检查指定的 `value` 是否属于此范围。

### 6. Common

```kotlin
@kotlin.jvm.JvmName("shortRangeContains")
public operator fun ClosedRange<Short>.contains(value: Byte): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L333)

检查指定的 `value` 是否属于此范围。

### 7. Common

```kotlin
@kotlin.jvm.JvmName("intRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Int>.contains(value: Byte): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L361)

检查指定的 `value` 是否属于此范围。

### 8. Common

```kotlin
@kotlin.jvm.JvmName("longRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Long>.contains(value: Byte): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L371)

检查指定的 `value` 是否属于此范围。

### 9. Common

```kotlin
@kotlin.jvm.JvmName("shortRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Short>.contains(value: Byte): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L381)

检查指定的 `value` 是否属于此范围。

### 10. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun IntRange.contains(value: Byte): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L391)

检查指定的 `value` 是否属于此范围。

### 11. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun LongRange.contains(value: Byte): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L399)

检查指定的 `value` 是否属于此范围。

### 12. Common

```kotlin
@kotlin.jvm.JvmName("floatRangeContains")
public operator fun ClosedRange<Float>.contains(value: Double): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L447)

检查指定的 `value` 是否属于此范围。

### 13. Common

```kotlin
@kotlin.jvm.JvmName("doubleRangeContains")
public operator fun ClosedRange<Double>.contains(value: Float): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L495)

检查指定的 `value` 是否属于此范围。

### 14. Common

```kotlin
@kotlin.jvm.JvmName("doubleRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Double>.contains(value: Float): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L503)

检查指定的 `value` 是否属于此范围。

### 15. Common

```kotlin
@kotlin.jvm.JvmName("longRangeContains")
public operator fun ClosedRange<Long>.contains(value: Int): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L513)

检查指定的 `value` 是否属于此范围。

### 16. Common

```kotlin
@kotlin.jvm.JvmName("byteRangeContains")
public operator fun ClosedRange<Byte>.contains(value: Int): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L521)

检查指定的 `value` 是否属于此范围。

### 17. Common

```kotlin
@kotlin.jvm.JvmName("shortRangeContains")
public operator fun ClosedRange<Short>.contains(value: Int): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L529)

检查指定的 `value` 是否属于此范围。

### 18. Common

```kotlin
@kotlin.jvm.JvmName("longRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Long>.contains(value: Int): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L557)

检查指定的 `value` 是否属于此范围。

### 19. Common

```kotlin
@kotlin.jvm.JvmName("byteRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Byte>.contains(value: Int): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L567)

检查指定的 `value` 是否属于此范围。

### 20. Common

```kotlin
@kotlin.jvm.JvmName("shortRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Short>.contains(value: Int): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L577)

检查指定的 `value` 是否属于此范围。

### 21. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun LongRange.contains(value: Int): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L587)

检查指定的 `value` 是否属于此范围。

### 22. Common

```kotlin
@kotlin.jvm.JvmName("intRangeContains")
public operator fun ClosedRange<Int>.contains(value: Long): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L595)

检查指定的 `value` 是否属于此范围。

### 23. Common

```kotlin
@kotlin.jvm.JvmName("byteRangeContains")
public operator fun ClosedRange<Byte>.contains(value: Long): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L603)

检查指定的 `value` 是否属于此范围。

### 24. Common

```kotlin
@kotlin.jvm.JvmName("shortRangeContains")
public operator fun ClosedRange<Short>.contains(value: Long): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L611)

检查指定的 `value` 是否属于此范围。

### 25. Common

```kotlin
@kotlin.jvm.JvmName("intRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Int>.contains(value: Long): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L639)

检查指定的 `value` 是否属于此范围。

### 26. Common

```kotlin
@kotlin.jvm.JvmName("byteRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Byte>.contains(value: Long): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L649)

检查指定的 `value` 是否属于此范围。

### 27. Common

```kotlin
@kotlin.jvm.JvmName("shortRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Short>.contains(value: Long): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L659)

检查指定的 `value` 是否属于此范围。

### 28. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun IntRange.contains(value: Long): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L669)

检查指定的 `value` 是否属于此范围。

### 29. Common

```kotlin
@kotlin.jvm.JvmName("intRangeContains")
public operator fun ClosedRange<Int>.contains(value: Short): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L677)

检查指定的 `value` 是否属于此范围。

### 30. Common

```kotlin
@kotlin.jvm.JvmName("longRangeContains")
public operator fun ClosedRange<Long>.contains(value: Short): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L685)

检查指定的 `value` 是否属于此范围。

### 31. Common

```kotlin
@kotlin.jvm.JvmName("byteRangeContains")
public operator fun ClosedRange<Byte>.contains(value: Short): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L693)

检查指定的 `value` 是否属于此范围。

### 32. Common

```kotlin
@kotlin.jvm.JvmName("intRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Int>.contains(value: Short): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L721)

检查指定的 `value` 是否属于此范围。

### 33. Common

```kotlin
@kotlin.jvm.JvmName("longRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Long>.contains(value: Short): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L731)

检查指定的 `value` 是否属于此范围。

### 34. Common

```kotlin
@kotlin.jvm.JvmName("byteRangeContains")
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun OpenEndRange<Byte>.contains(value: Short): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L741)

检查指定的 `value` 是否属于此范围。

### 35. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun IntRange.contains(value: Short): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L751)

检查指定的 `value` 是否属于此范围。

### 36. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun LongRange.contains(value: Short): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L759)

检查指定的 `value` 是否属于此范围。

### 37. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline operator fun UIntRange.contains(element: UInt?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L196)

### 38. Common

```kotlin
@SinceKotlin("1.5")
@kotlin.internal.InlineOnly
public inline operator fun ULongRange.contains(element: ULong?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L207)

### 39. Common

```kotlin
@SinceKotlin("1.5")
public operator fun UIntRange.contains(value: UByte): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L218)

检查指定的 `value` 是否属于此范围。

### 40. Common

```kotlin
@SinceKotlin("1.5")
public operator fun ULongRange.contains(value: UByte): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L226)

检查指定的 `value` 是否属于此范围。

### 41. Common

```kotlin
@SinceKotlin("1.5")
public operator fun ULongRange.contains(value: UInt): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L234)

检查指定的 `value` 是否属于此范围。

### 42. Common

```kotlin
@SinceKotlin("1.5")
public operator fun UIntRange.contains(value: ULong): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L242)

检查指定的 `value` 是否属于此范围。

### 43. Common

```kotlin
@SinceKotlin("1.5")
public operator fun UIntRange.contains(value: UShort): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L250)

检查指定的 `value` 是否属于此范围。

### 44. Common

```kotlin
@SinceKotlin("1.5")
public operator fun ULongRange.contains(value: UShort): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L258)

检查指定的 `value` 是否属于此范围。

### 45. Common

```kotlin
@SinceKotlin("2.3")
@kotlin.internal.InlineOnly
public inline operator fun <T, R> R.contains(element: T?): Boolean where T : Comparable<T>, R : ClosedRange<T>, R : Iterable<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ranges/Ranges.kt#L260)

如果此可扩展范围包含指定的 `element` ,则返回 `true` 。

如果 `element` 是 `null`, 则总是返回 `false` 。

### 46. Common

```kotlin
@SinceKotlin("2.3")
@WasExperimental(ExperimentalStdlibApi::class)
@kotlin.internal.InlineOnly
public inline operator fun <T, R> R.contains(element: T?): Boolean where T : Comparable<T>, R : OpenEndRange<T>, R : Iterable<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ranges/Ranges.kt#L286)

如果此可扩展范围包含指定的 `element` ,则返回 `true` 。

如果 `element` 是 `null`, 则总是返回 `false` 。

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
import kotlin.ranges.*

fun main() {
    val source = 1..3
    val result = source.`contains`(2)
    println(result)
}
```

```text title="输出"
true
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
