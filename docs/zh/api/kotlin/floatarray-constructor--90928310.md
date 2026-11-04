# FloatArray.constructor

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

创建指定 `size` 的新数组, 以调用指定的 `init` 函数计算每个元素 。

函数 `init` 由第一个数组元素依次对每个数组元素调用。 它应该返回一个数组元素的值, 并给定其索引 。

@throws 运行时间例外,如果指定的 `size` 是负值 。

??? note "查看英文原文"

    Creates a new array of the specified `size`, where each element is calculated by calling the specified
    `init` function.
    
    The function `init` is called for each array element sequentially starting from the first one.
    It should return the value for an array element given its index.
    
    @throws RuntimeException if the specified `size` is negative.

## 声明与重载

### 1. Common

```kotlin
public constructor(size: Int)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Arrays.kt#L333)

### 2. Common

```kotlin
@Suppress("WRONG_MODIFIER_TARGET")
    public inline constructor(size: Int, init: (Int) -> Float)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Arrays.kt#L334)

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
import kotlin.*

fun main() {
    val value = floatArrayOf(1f, 2f, 3f)
    println(value)
}
```

```text title="输出"
[F@7ad041f3
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
