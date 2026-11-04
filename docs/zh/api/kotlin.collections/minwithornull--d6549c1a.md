# minWithOrNull

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回第一个最小值元素,如果没有元素,则根据 `comparator` 或`null`提供最小值。

??? note "查看英文原文"

    Returns the first element having the smallest value according to the provided `comparator` or `null` if there are no elements.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public fun <T> Array<out T>.minWithOrNull(comparator: Comparator<in T>): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22111)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public fun ByteArray.minWithOrNull(comparator: Comparator<in Byte>): Byte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22125)

### 3. Common

```kotlin
@SinceKotlin("1.4")
public fun ShortArray.minWithOrNull(comparator: Comparator<in Short>): Short?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22139)

### 4. Common

```kotlin
@SinceKotlin("1.4")
public fun IntArray.minWithOrNull(comparator: Comparator<in Int>): Int?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22153)

### 5. Common

```kotlin
@SinceKotlin("1.4")
public fun LongArray.minWithOrNull(comparator: Comparator<in Long>): Long?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22167)

### 6. Common

```kotlin
@SinceKotlin("1.4")
public fun FloatArray.minWithOrNull(comparator: Comparator<in Float>): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22181)

### 7. Common

```kotlin
@SinceKotlin("1.4")
public fun DoubleArray.minWithOrNull(comparator: Comparator<in Double>): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22195)

### 8. Common

```kotlin
@SinceKotlin("1.4")
public fun BooleanArray.minWithOrNull(comparator: Comparator<in Boolean>): Boolean?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22209)

### 9. Common

```kotlin
@SinceKotlin("1.4")
public fun CharArray.minWithOrNull(comparator: Comparator<in Char>): Char?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22223)

### 10. Common

```kotlin
@SinceKotlin("1.4")
public fun <T> Iterable<T>.minWithOrNull(comparator: Comparator<in T>): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3045)

### 11. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline fun <K, V> Map<out K, V>.minWithOrNull(comparator: Comparator<in Map.Entry<K, V>>): Map.Entry<K, V>?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L611)

返回第一个条目,其最小值根据提供的 `comparator` 或 `null` 来计算,如果没有输入的话。

### 12. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UIntArray.minWithOrNull(comparator: Comparator<in UInt>): UInt?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9683)

### 13. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun ULongArray.minWithOrNull(comparator: Comparator<in ULong>): ULong?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9698)

### 14. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UByteArray.minWithOrNull(comparator: Comparator<in UByte>): UByte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9713)

### 15. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UShortArray.minWithOrNull(comparator: Comparator<in UShort>): UShort?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9728)

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
    val result = source.`minWithOrNull`(naturalOrder())
    println(result)
}
```

```text title="输出"
1
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
