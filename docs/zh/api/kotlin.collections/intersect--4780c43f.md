# intersect

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回包含此数组元素的一组元素,这些元素也包含在指定的 `other` 数组中。

返回的集保留原始数组的元素迭代顺序。

返回的集利用结构平等(`==`)来区分元素,这意味着不会有两个
结构上平等,但其中各部分不同。

获得一套包含至少包含在其中一个收藏中的所有元素的集合,使用 `union` 。

??? note "查看英文原文"

    Returns a set containing elements of this array that are also contained in the specified `other` array.
    
    The returned set preserves the element iteration order of the original array.
    
    The returned set uses structural equality (`==`) to distinguish elements, meaning there will be no two
    structurally equal, but otherwise different elements in it.
    
    To get a set containing all elements that are contained at least in one of these collections use `union`.

## 声明与重载

### 1. Common

```kotlin
public infix fun <T> Array<out T>.intersect(other: Iterable<T>): Set<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13634)

### 2. Common

```kotlin
public infix fun ByteArray.intersect(other: Iterable<Byte>): Set<Byte>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13655)

### 3. Common

```kotlin
public infix fun ShortArray.intersect(other: Iterable<Short>): Set<Short>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13671)

### 4. Common

```kotlin
public infix fun IntArray.intersect(other: Iterable<Int>): Set<Int>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13687)

### 5. Common

```kotlin
public infix fun LongArray.intersect(other: Iterable<Long>): Set<Long>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13703)

### 6. Common

```kotlin
public infix fun FloatArray.intersect(other: Iterable<Float>): Set<Float>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13719)

### 7. Common

```kotlin
public infix fun DoubleArray.intersect(other: Iterable<Double>): Set<Double>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13735)

### 8. Common

```kotlin
public infix fun BooleanArray.intersect(other: Iterable<Boolean>): Set<Boolean>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13751)

### 9. Common

```kotlin
public infix fun CharArray.intersect(other: Iterable<Char>): Set<Char>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13767)

### 10. Common

```kotlin
public infix fun <T> Iterable<T>.intersect(other: Iterable<T>): Set<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1865)

返回包含此收藏元素的一组元素,这些元素也包含在指定的 `other` 收藏中。

返回的集保存原始收藏的元素迭代顺序。

返回的集利用结构平等(`==`)来区分元素,这意味着不会有两个
结构上平等,但其中各部分不同。

获得一套包含至少包含在其中一个收藏中的所有元素的集合,使用 `union` 。

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
    val result = source.`intersect`(listOf(1, 2, 3))
    println(result)
}
```

```text title="输出"
[1, 2, 3]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
