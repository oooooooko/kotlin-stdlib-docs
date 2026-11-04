# ExperimentalContextParameters

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

标记与 Kotlin [ 参数] (https://github.com/Kotlin/KEEP/blob/context-parameters/proposals/context-parameters.md)) 实验特性有关的 API 。

标记的 API 取决于该特性的设计, 并随着开发的继续可以更改或删除, 因此它没有提供任何兼容性保证 。

??? note "查看英文原文"

    Marks an API related to the Kotlin's [context parameters](https://github.com/Kotlin/KEEP/blob/context-parameters/proposals/context-parameters.md)
    experimental feature.
    
    Marked API depends on the design of this feature, and can be changed or removed as development continues.
    Therefore, it does not provide any compatibility guarantees.

## 声明与重载

### 1. Common

```kotlin
@RequiresOptIn(
    "The API is related to the experimental feature \"context parameters\" (see KEEP-367) and may be changed or removed in any future release.",
    RequiresOptIn.Level.ERROR
)
@Retention(AnnotationRetention.BINARY)
@MustBeDocumented
@SinceKotlin("2.2")
public annotation class ExperimentalContextParameters
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contextParameters/ExperimentalContextParameters.kt#L8)

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
    val value = kotlin.ExperimentalContextParameters()
    println(value)
}
```

```text title="输出"
@kotlin.ExperimentalContextParameters()
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
