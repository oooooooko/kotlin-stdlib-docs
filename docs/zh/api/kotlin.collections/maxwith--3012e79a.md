# maxWith

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回根据`comparator`提供的数值最大的第一个元素。

@throws 无效元素,如果数组为空,则例外。

??? note "查看英文原文"

    Returns the first element having the largest value according to the provided `comparator`.
    
    @throws NoSuchElementException if the array is empty.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun <T> Array<out T>.maxWith(comparator: Comparator<in T>): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18977)

### 2. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun ByteArray.maxWith(comparator: Comparator<in Byte>): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L18995)

### 3. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun ShortArray.maxWith(comparator: Comparator<in Short>): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19013)

### 4. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun IntArray.maxWith(comparator: Comparator<in Int>): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19031)

### 5. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun LongArray.maxWith(comparator: Comparator<in Long>): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19049)

### 6. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun FloatArray.maxWith(comparator: Comparator<in Float>): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19067)

### 7. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun DoubleArray.maxWith(comparator: Comparator<in Double>): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19085)

### 8. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun BooleanArray.maxWith(comparator: Comparator<in Boolean>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19103)

### 9. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun CharArray.maxWith(comparator: Comparator<in Char>): Char
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L19121)

### 10. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@Suppress("CONFLICTING_OVERLOADS")
public fun <T> Iterable<T>.maxWith(comparator: Comparator<in T>): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2602)

返回根据`comparator`提供的数值最大的第一个元素。

@throws 否 元素 , 收藏为空时除外 。

### 11. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow")
@kotlin.internal.InlineOnly
@Suppress("CONFLICTING_OVERLOADS")
public inline fun <K, V> Map<out K, V>.maxWith(comparator: Comparator<in Map.Entry<K, V>>): Map.Entry<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L400)

返回根据`comparator`提供的数值最大的第一个条目。

@throws 否 元素, 如果地图为空则例外 。

### 12. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow-U")
@ExperimentalUnsignedTypes
@Suppress("CONFLICTING_OVERLOADS")
public fun UIntArray.maxWith(comparator: Comparator<in UInt>): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8247)

### 13. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow-U")
@ExperimentalUnsignedTypes
@Suppress("CONFLICTING_OVERLOADS")
public fun ULongArray.maxWith(comparator: Comparator<in ULong>): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8266)

### 14. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow-U")
@ExperimentalUnsignedTypes
@Suppress("CONFLICTING_OVERLOADS")
public fun UByteArray.maxWith(comparator: Comparator<in UByte>): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8285)

### 15. Common

```kotlin
@SinceKotlin("1.7")
@kotlin.jvm.JvmName("maxWithOrThrow-U")
@ExperimentalUnsignedTypes
@Suppress("CONFLICTING_OVERLOADS")
public fun UShortArray.maxWith(comparator: Comparator<in UShort>): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L8304)

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
    val result = source.`maxWith`(naturalOrder())
    println(result)
}
```

```text title="输出"
3
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
