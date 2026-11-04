# contentDeepEquals

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

检查两个指定的数组是否相等 * 深 * 。

如果两个阵列的大小相同,则认为它们十分相等,相应的指数中的要素则十分相等。
也就是说,如果两个相应的元素是嵌套阵列,它们也会得到深入的比较。
使用 `equals`Z`Any.equals`函数,其他类型要素的等同性比较。
对于浮动点数,这意味着`NaN`等于本身,而`-0.0`不等于`0.0`。

如果任何数组在任何嵌套级别都包含自己,则行为是未定义的。

@param 其它与此阵列进行深度比较的阵列。 @return `true`, 如果两个阵列的高度相等, 则 `false` 。

@sample 样本采集资料 阵列、实际操作、内部深赤道

??? note "查看英文原文"

    Checks if the two specified arrays are *deeply* equal to one another.
    
    Two arrays are considered deeply equal if they have the same size, and elements at corresponding indices are deeply equal.
    That is, if two corresponding elements are nested arrays, they are also compared deeply.
    Elements of other types are compared for equality using the `equals``Any.equals` function.
    For floating point numbers, this means `NaN` is equal to itself and `-0.0` is not equal to `0.0`.
    
    If any of the arrays contain themselves at any nesting level, the behavior is undefined.
    
    @param other the array to compare deeply with this array.
    @return `true` if the two arrays are deeply equal, `false` otherwise.
    
    @sample samples.collections.Arrays.ContentOperations.contentDeepEquals

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.LowPriorityInOverloadResolution
public expect infix fun <T> Array<out T>.contentDeepEquals(other: Array<out T>): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8144)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun <T> Array<out T>?.contentDeepEquals(other: Array<out T>?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8163)

检查两个指定的数组是否相等 * 深 * 。

如果两个阵列的大小相同,则认为它们十分相等,相应的指数中的要素则十分相等。
也就是说,如果两个相应的元素是嵌套阵列,它们也会得到深入的比较。
使用 `equals`Z`Any.equals`函数,其他类型要素的等同性比较。
对于浮动点数,这意味着`NaN`等于本身,而`-0.0`不等于`0.0`。

如果两个数组均为 `null` ,则也认为这些数组是十分平等的。

如果任何数组在任何嵌套级别都包含自己,则行为是未定义的。

@param 其它与此阵列进行深度比较的阵列。 @return `true`, 如果两个阵列的高度相等, 则 `false` 。

@sample 样本采集资料 阵列、实际操作、内部深赤道

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
    val result = source.`contentDeepEquals`(arrayOf(1, 2, 3))
    println(result)
}
```

```text title="输出"
true
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
