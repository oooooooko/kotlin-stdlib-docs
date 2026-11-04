# minWith

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回第一个根据`comparator`提供的最小值的元素。

@throws 无效元素,如果数组为空,则例外。

??? note "查看英文原文"

    Returns the first element having the smallest value according to the provided `comparator`.
    
    @throws NoSuchElementException if the array is empty.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun <T> Array<out T>.minWith(comparator: Comparator<in T>): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21949)

### 2. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun ByteArray.minWith(comparator: Comparator<in Byte>): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21967)

### 3. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun ShortArray.minWith(comparator: Comparator<in Short>): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21985)

### 4. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun IntArray.minWith(comparator: Comparator<in Int>): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22003)

### 5. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun LongArray.minWith(comparator: Comparator<in Long>): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22021)

### 6. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun FloatArray.minWith(comparator: Comparator<in Float>): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22039)

### 7. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun DoubleArray.minWith(comparator: Comparator<in Double>): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22057)

### 8. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun BooleanArray.minWith(comparator: Comparator<in Boolean>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22075)

### 9. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun CharArray.minWith(comparator: Comparator<in Char>): Char
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22093)

### 10. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun <T> Iterable<T>.minWith(comparator: Comparator<in T>): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3026)

返回第一个根据`comparator`提供的最小值的元素。

@throws 否 元素 , 收藏为空时除外 。

### 11. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow")
@kotlin.internal.InlineOnly
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <K, V> Map<out K, V>.minWith(comparator: Comparator<in Map.Entry<K, V>>): Map.Entry<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L598)

返回第一个条目,其最小值根据所提供的 `comparator` 值计算。

@throws 否 元素, 如果地图为空则例外 。

### 12. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow-U")
@ExperimentalUnsignedTypes
@Suppress("CONFLICTING_OVERLOADS")
public fun UIntArray.minWith(comparator: Comparator<in UInt>): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9607)

### 13. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow-U")
@ExperimentalUnsignedTypes
@Suppress("CONFLICTING_OVERLOADS")
public fun ULongArray.minWith(comparator: Comparator<in ULong>): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9626)

### 14. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow-U")
@ExperimentalUnsignedTypes
@Suppress("CONFLICTING_OVERLOADS")
public fun UByteArray.minWith(comparator: Comparator<in UByte>): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9645)

### 15. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("minWithOrThrow-U")
@ExperimentalUnsignedTypes
@Suppress("CONFLICTING_OVERLOADS")
public fun UShortArray.minWith(comparator: Comparator<in UShort>): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9664)

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
    val result = source.`minWith`(naturalOrder())
    println(result)
}
```

```text title="输出"
1
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
