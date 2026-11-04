# ArrayDeque

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

恢复数据结构脱钩的全程实施。

名字缩略语为“ 两端队列” , 通常会用“ 甲板” 来表示 。

收集为方便地进入两端提供了方法,还安装了 `MutableList` 接口,支持按指数进行高效的获取/设置操作。

??? note "查看英文原文"

    Resizable-array implementation of the deque data structure.
    
    The name deque is short for "double ended queue" and is usually pronounced "deck".
    
    The collection provide methods for convenient access to the both ends.
    It also implements `MutableList` interface and supports efficient get/set operations by index.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public class ArrayDeque<E> : AbstractMutableList<E>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/ArrayDeque.kt#L8)

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
    val value = ArrayDeque(listOf(1, 2, 3))
    println(value)
}
```

```text title="输出"
[1, 2, 3]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
