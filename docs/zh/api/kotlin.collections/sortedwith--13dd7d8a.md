# sortedWith

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回根据指定的 `comparator` 排序的所有元素的列表 。

如果您需要将结果以数组形式显示, 请使用 `sortedArrayWith` 。

类型是 _stair_。 这意味着等元素在排序后保持彼此相对的顺序 。

??? note "查看英文原文"

    Returns a list of all elements sorted according to the specified `comparator`.
    
    Use `sortedArrayWith` if you need to get the result in an array.
    
    The sort is _stable_. It means that equal elements preserve their order relative to each other after sorting.

## 声明与重载

### 1. Common

```kotlin
public fun <T> Array<out T>.sortedWith(comparator: Comparator<in T>): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8032)

### 2. Common

```kotlin
public fun ByteArray.sortedWith(comparator: Comparator<in Byte>): List<Byte>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8043)

返回根据指定的 `comparator` 排序的所有元素的列表 。

### 3. Common

```kotlin
public fun ShortArray.sortedWith(comparator: Comparator<in Short>): List<Short>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8050)

返回根据指定的 `comparator` 排序的所有元素的列表 。

### 4. Common

```kotlin
public fun IntArray.sortedWith(comparator: Comparator<in Int>): List<Int>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8057)

返回根据指定的 `comparator` 排序的所有元素的列表 。

### 5. Common

```kotlin
public fun LongArray.sortedWith(comparator: Comparator<in Long>): List<Long>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8064)

返回根据指定的 `comparator` 排序的所有元素的列表 。

### 6. Common

```kotlin
public fun FloatArray.sortedWith(comparator: Comparator<in Float>): List<Float>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8071)

返回根据指定的 `comparator` 排序的所有元素的列表 。

### 7. Common

```kotlin
public fun DoubleArray.sortedWith(comparator: Comparator<in Double>): List<Double>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8078)

返回根据指定的 `comparator` 排序的所有元素的列表 。

### 8. Common

```kotlin
public fun BooleanArray.sortedWith(comparator: Comparator<in Boolean>): List<Boolean>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8085)

返回根据指定的 `comparator` 排序的所有元素的列表 。

### 9. Common

```kotlin
public fun CharArray.sortedWith(comparator: Comparator<in Char>): List<Char>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8092)

返回根据指定的 `comparator` 排序的所有元素的列表 。

### 10. Common

```kotlin
public fun <T> Iterable<T>.sortedWith(comparator: Comparator<in T>): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1251)

返回根据指定的 `comparator` 排序的所有元素的列表 。

类型是 _stair_。 这意味着等元素在排序后保持彼此相对的顺序 。

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
    val result = source.`sortedWith`(naturalOrder())
    println(result)
}
```

```text title="输出"
[1, 2, 3]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
