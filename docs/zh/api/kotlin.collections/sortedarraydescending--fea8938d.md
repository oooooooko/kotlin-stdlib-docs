# sortedArrayDescending

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个数组,其中包含该数组的所有元素,根据自然排序顺序排序递减。

如果您需要将结果列入列表, 请使用 `sortedDescending` 。

类型是 _stair_。 这意味着等元素在排序后保持彼此相对的顺序 。

??? note "查看英文原文"

    Returns an array with all elements of this array sorted descending according to their natural sort order.
    
    Use `sortedDescending` if you need to get the result in a list.
    
    The sort is _stable_. It means that equal elements preserve their order relative to each other after sorting.

## 声明与重载

### 1. Common

```kotlin
public fun <T : Comparable<T>> Array<T>.sortedArrayDescending(): Array<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7648)

### 2. Common

```kotlin
public fun ByteArray.sortedArrayDescending(): ByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7660)

返回一个数组,其中包含该数组的所有元素,根据自然排序顺序排序递减。

如果您需要将结果列入列表, 请使用 `sortedDescending` 。

### 3. Common

```kotlin
public fun ShortArray.sortedArrayDescending(): ShortArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7670)

返回一个数组,其中包含该数组的所有元素,根据自然排序顺序排序递减。

如果您需要将结果列入列表, 请使用 `sortedDescending` 。

### 4. Common

```kotlin
public fun IntArray.sortedArrayDescending(): IntArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7680)

返回一个数组,其中包含该数组的所有元素,根据自然排序顺序排序递减。

如果您需要将结果列入列表, 请使用 `sortedDescending` 。

### 5. Common

```kotlin
public fun LongArray.sortedArrayDescending(): LongArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7690)

返回一个数组,其中包含该数组的所有元素,根据自然排序顺序排序递减。

如果您需要将结果列入列表, 请使用 `sortedDescending` 。

### 6. Common

```kotlin
public fun FloatArray.sortedArrayDescending(): FloatArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7700)

返回一个数组,其中包含该数组的所有元素,根据自然排序顺序排序递减。

如果您需要将结果列入列表, 请使用 `sortedDescending` 。

### 7. Common

```kotlin
public fun DoubleArray.sortedArrayDescending(): DoubleArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7710)

返回一个数组,其中包含该数组的所有元素,根据自然排序顺序排序递减。

如果您需要将结果列入列表, 请使用 `sortedDescending` 。

### 8. Common

```kotlin
public fun CharArray.sortedArrayDescending(): CharArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7720)

返回一个数组,其中包含该数组的所有元素,根据自然排序顺序排序递减。

如果您需要将结果列入列表, 请使用 `sortedDescending` 。

### 9. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.sortedArrayDescending(): UIntArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3683)

返回一个数组,其中包含该数组的所有元素,根据自然排序顺序排序递减。

如果您需要将结果列入列表, 请使用 `sortedDescending` 。

### 10. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.sortedArrayDescending(): ULongArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3695)

返回一个数组,其中包含该数组的所有元素,根据自然排序顺序排序递减。

如果您需要将结果列入列表, 请使用 `sortedDescending` 。

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.sortedArrayDescending(): UByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3707)

返回一个数组,其中包含该数组的所有元素,根据自然排序顺序排序递减。

如果您需要将结果列入列表, 请使用 `sortedDescending` 。

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.sortedArrayDescending(): UShortArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3719)

返回一个数组,其中包含该数组的所有元素,根据自然排序顺序排序递减。

如果您需要将结果列入列表, 请使用 `sortedDescending` 。

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
    val result = source.`sortedArrayDescending`()
    println(result.contentToString())
}
```

```text title="输出"
[3, 2, 1]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
