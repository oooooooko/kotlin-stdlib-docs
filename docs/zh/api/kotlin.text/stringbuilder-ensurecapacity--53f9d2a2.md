# StringBuilder.ensureCapacity

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

确保该字符串构建器的能力至少等于指定的 `minimumCapacity` 。

如果现有容量低于`minimumCapacity`,则用更大的容量分配新的后备储存,否则,这种方法不采取行动,而只是返回。

??? note "查看英文原文"

    Ensures that the capacity of this string builder is at least equal to the specified `minimumCapacity`.
    
    If the current capacity is less than the `minimumCapacity`, a new backing storage is allocated with greater capacity.
    Otherwise, this method takes no action and simply returns.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
    public fun ensureCapacity(minimumCapacity: Int)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L134)

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
import kotlin.text.*

fun main() {
    val source = StringBuilder("kotlin")
    val result = source.`ensureCapacity`(2)
    println(result)
}
```

```text title="输出"
kotlin.Unit
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
