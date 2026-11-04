# sorted

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回所有元素的列表, 并按自然排序顺序排序 。

如果您需要将结果以数组形式显示, 请使用 `sortedArray` 。

类型是 _stair_。 这意味着等元素在排序后保持彼此相对的顺序 。

??? note "查看英文原文"

    Returns a list of all elements sorted according to their natural sort order.
    
    Use `sortedArray` if you need to get the result in an array.
    
    The sort is _stable_. It means that equal elements preserve their order relative to each other after sorting.

## 声明与重载

### 1. Common

```kotlin
public fun <T : Comparable<T>> Array<out T>.sorted(): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7492)

### 2. Common

```kotlin
public fun ByteArray.sorted(): List<Byte>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7503)

返回所有元素的列表, 并按自然排序顺序排序 。

如果您需要将结果以数组形式显示, 请使用 `sortedArray` 。

### 3. Common

```kotlin
public fun ShortArray.sorted(): List<Short>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7512)

返回所有元素的列表, 并按自然排序顺序排序 。

如果您需要将结果以数组形式显示, 请使用 `sortedArray` 。

### 4. Common

```kotlin
public fun IntArray.sorted(): List<Int>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7521)

返回所有元素的列表, 并按自然排序顺序排序 。

如果您需要将结果以数组形式显示, 请使用 `sortedArray` 。

### 5. Common

```kotlin
public fun LongArray.sorted(): List<Long>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7530)

返回所有元素的列表, 并按自然排序顺序排序 。

如果您需要将结果以数组形式显示, 请使用 `sortedArray` 。

### 6. Common

```kotlin
public fun FloatArray.sorted(): List<Float>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7539)

返回所有元素的列表, 并按自然排序顺序排序 。

如果您需要将结果以数组形式显示, 请使用 `sortedArray` 。

### 7. Common

```kotlin
public fun DoubleArray.sorted(): List<Double>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7548)

返回所有元素的列表, 并按自然排序顺序排序 。

如果您需要将结果以数组形式显示, 请使用 `sortedArray` 。

### 8. Common

```kotlin
public fun CharArray.sorted(): List<Char>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7557)

返回所有元素的列表, 并按自然排序顺序排序 。

如果您需要将结果以数组形式显示, 请使用 `sortedArray` 。

### 9. Common

```kotlin
public fun <T : Comparable<T>> Iterable<T>.sorted(): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1204)

返回所有元素的列表, 并按自然排序顺序排序 。

类型是 _stair_。 这意味着等元素在排序后保持彼此相对的顺序 。

### 10. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.sorted(): List<UInt>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3591)

返回所有元素的列表, 并按自然排序顺序排序 。

如果您需要将结果以数组形式显示, 请使用 `sortedArray` 。

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.sorted(): List<ULong>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3602)

返回所有元素的列表, 并按自然排序顺序排序 。

如果您需要将结果以数组形式显示, 请使用 `sortedArray` 。

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.sorted(): List<UByte>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3613)

返回所有元素的列表, 并按自然排序顺序排序 。

如果您需要将结果以数组形式显示, 请使用 `sortedArray` 。

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.sorted(): List<UShort>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3624)

返回所有元素的列表, 并按自然排序顺序排序 。

如果您需要将结果以数组形式显示, 请使用 `sortedArray` 。

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
    val result = source.`sorted`()
    println(result)
}
```

```text title="输出"
[1, 2, 3]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
