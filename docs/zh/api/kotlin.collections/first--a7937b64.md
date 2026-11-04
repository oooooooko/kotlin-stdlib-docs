# first

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回第一个元素。

@throws 无效元素,如果数组为空,则例外。

??? note "查看英文原文"

    Returns the first element.
    
    @throws NoSuchElementException if the array is empty.

## 声明与重载

### 1. Common

```kotlin
public fun <T> Array<out T>.first(): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1124)

### 2. Common

```kotlin
public fun ByteArray.first(): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1135)

### 3. Common

```kotlin
public fun ShortArray.first(): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1146)

### 4. Common

```kotlin
public fun IntArray.first(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1157)

### 5. Common

```kotlin
public fun LongArray.first(): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1168)

### 6. Common

```kotlin
public fun FloatArray.first(): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1179)

### 7. Common

```kotlin
public fun DoubleArray.first(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1190)

### 8. Common

```kotlin
public fun BooleanArray.first(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1201)

### 9. Common

```kotlin
public fun CharArray.first(): Char
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1212)

### 10. Common

```kotlin
public inline fun <T> Array<out T>.first(predicate: (T) -> Boolean): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1223)

如果没有找到此元素, 返回第一个匹配给定 `predicate` 的元素 。 @throws `NoSuchElementException` 。

### 11. Common

```kotlin
public inline fun ByteArray.first(predicate: (Byte) -> Boolean): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1232)

如果没有找到此元素, 返回第一个匹配给定 `predicate` 的元素 。 @throws `NoSuchElementException` 。

### 12. Common

```kotlin
public inline fun ShortArray.first(predicate: (Short) -> Boolean): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1241)

如果没有找到此元素, 返回第一个匹配给定 `predicate` 的元素 。 @throws `NoSuchElementException` 。

### 13. Common

```kotlin
public inline fun IntArray.first(predicate: (Int) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1250)

如果没有找到此元素, 返回第一个匹配给定 `predicate` 的元素 。 @throws `NoSuchElementException` 。

### 14. Common

```kotlin
public inline fun LongArray.first(predicate: (Long) -> Boolean): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1259)

如果没有找到此元素, 返回第一个匹配给定 `predicate` 的元素 。 @throws `NoSuchElementException` 。

### 15. Common

```kotlin
public inline fun FloatArray.first(predicate: (Float) -> Boolean): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1268)

如果没有找到此元素, 返回第一个匹配给定 `predicate` 的元素 。 @throws `NoSuchElementException` 。

### 16. Common

```kotlin
public inline fun DoubleArray.first(predicate: (Double) -> Boolean): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1277)

如果没有找到此元素, 返回第一个匹配给定 `predicate` 的元素 。 @throws `NoSuchElementException` 。

### 17. Common

```kotlin
public inline fun BooleanArray.first(predicate: (Boolean) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1286)

如果没有找到此元素, 返回第一个匹配给定 `predicate` 的元素 。 @throws `NoSuchElementException` 。

### 18. Common

```kotlin
public inline fun CharArray.first(predicate: (Char) -> Boolean): Char
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1295)

如果没有找到此元素, 返回第一个匹配给定 `predicate` 的元素 。 @throws `NoSuchElementException` 。

### 19. Common

```kotlin
public fun <T> Iterable<T>.first(): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L198)

返回第一个元素。

@throws 否 元素 , 收藏为空时除外 。

### 20. Common

```kotlin
public fun <T> List<T>.first(): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L215)

返回第一个元素。

@throws 无效元素, 列表为空时除外 。

### 21. Common

```kotlin
public inline fun <T> Iterable<T>.first(predicate: (T) -> Boolean): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L226)

如果没有找到此元素, 返回第一个匹配给定 `predicate` 的元素 。 @throws `NoSuchElementException` 。

### 22. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.first(): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L563)

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.first(): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L575)

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.first(): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L587)

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.first(): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L599)

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.first(predicate: (UInt) -> Boolean): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L611)

如果没有找到此元素, 返回第一个匹配给定 `predicate` 的元素 。 @throws `NoSuchElementException` 。

### 27. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.first(predicate: (ULong) -> Boolean): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L623)

如果没有找到此元素, 返回第一个匹配给定 `predicate` 的元素 。 @throws `NoSuchElementException` 。

### 28. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.first(predicate: (UByte) -> Boolean): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L635)

如果没有找到此元素, 返回第一个匹配给定 `predicate` 的元素 。 @throws `NoSuchElementException` 。

### 29. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.first(predicate: (UShort) -> Boolean): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L647)

如果没有找到此元素, 返回第一个匹配给定 `predicate` 的元素 。 @throws `NoSuchElementException` 。

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
import kotlin.collections.*

fun main() {
    val source = arrayOf(1, 2, 3)
    val result = source.`first`()
    println(result)
}
```

```text title="输出"
1
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
