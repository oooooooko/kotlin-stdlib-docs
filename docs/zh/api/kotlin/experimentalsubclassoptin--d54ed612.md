# ExperimentalSubclassOptIn

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

此注释标志着语言特写 `SubclassOptInRequired` 的实验预览 。

> 注意该 API 处于预览状态, 将来有可能被更改。 如果您开发了一个图书馆, 则不要使用它, 因为您的图书馆可能会成为与 Kotlin 未来版本不兼容的来源 。

??? note "查看英文原文"

    This annotation marks the experimental preview of the language feature `SubclassOptInRequired`.
    
    > Note that this API is in a preview state and has a chance of being changed in the future.
    Do not use it if you develop a library since your library can become source incompatible
    with the future versions of Kotlin.

## 声明与重载

### 1. Common

```kotlin
@Target(CLASS)
@Retention(BINARY)
@SinceKotlin("1.8")
@RequiresOptIn
public annotation class ExperimentalSubclassOptIn
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotations/OptIn.kt#L140)

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
    val value = kotlin.ExperimentalSubclassOptIn()
    println(value)
}
```

```text title="输出"
@kotlin.ExperimentalSubclassOptIn()
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
