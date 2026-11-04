# AbstractList.equals

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

检查两个指定的列表是否 * 结构 * 等同。

两个清单如果规模相同,则被视为结构上相等,相应的指数各要素相同。
使用 `equals`Z`Any.equals` 函数对元素进行平等比较。
对于浮动点数,这意味着`NaN`等于本身,而`-0.0`不等于`0.0`。

@param 其它列表, 与此列表比较 。
如果`other`是一个`List`,则@return`true`在结构上等于该清单,否则`false`。

??? note "查看英文原文"

    Checks if the two specified lists are *structurally* equal to one another.
    
    Two lists are considered structurally equal if they have the same size, and elements at corresponding indices are equal.
    Elements are compared for equality using the `equals``Any.equals` function.
    For floating point numbers, this means `NaN` is equal to itself and `-0.0` is not equal to `0.0`.
    
    @param other the list to compare with this list.
    @return `true` if `other` is a `List` that is structurally equal to this list, `false` otherwise.

## 声明与重载

### 1. Common

```kotlin
override fun equals(other: Any?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/AbstractList.kt#L59)

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
    val source = object : AbstractList<Int>() { override val size = 3; override fun get(index: Int) = index + 1 }
    val result = source.`equals`(1)
    println(result)
}
```

```text title="输出"
false
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
