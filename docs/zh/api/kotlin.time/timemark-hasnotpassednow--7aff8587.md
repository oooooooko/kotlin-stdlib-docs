# TimeMark.hasNotPassedNow

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果此时间标记未按照使用此时间标记的时间源通过, 返回错误 。

请注意,此函数返回的值在随后的引用中可以改变。如果时间源是单调的,它只能从 `true` 变为 `false` ,即当时间标记在时间源当前点之后。

??? note "查看英文原文"

    Returns false if this time mark has not passed according to the time source from which this mark was taken.
    
    Note that the value returned by this function can change on subsequent invocations.
    If the time source is monotonic, it can change only from `true` to `false`, namely, when the time mark becomes behind the current point of the time source.

## 声明与重载

### 1. Common

```kotlin
public fun hasNotPassedNow(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSource.kt#L188)

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
import kotlin.time.*

fun main() {
    val source = TimeSource.Monotonic.markNow()
    val result = source.`hasNotPassedNow`()
    println(result)
}
```

```text title="输出"
false
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
