# AutoCloseable

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

一种可以关闭或释放的资源。

??? note "查看英文原文"

    A resource that can be closed or released.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.0")
@WasExperimental(ExperimentalStdlibApi::class)
public expect interface AutoCloseable
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/AutoCloseable.kt#L11)

### 2. Common

```kotlin
@SinceKotlin("2.0")
@kotlin.internal.InlineOnly
public expect inline fun AutoCloseable(crossinline closeAction: () -> Unit): AutoCloseable
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/AutoCloseable.kt#L34)

返回 `AutoCloseable` 实例, 用于在援引“ 关闭 () ” 时执行指定的 `closeAction` 。```AutoCloseable.close` function.

This function allows specifying custom cleanup actions for resources.

Note that each invocation of the `close()` function on the returned `AutoCloseable` instance executes the `closeAction`.
Therefore, implementers are strongly recommended to make the `closeAction` idempotent, or to prevent multiple invocations.

Example:

```Kotlin val Val 自动关闭 = 自动关闭 {// 清理动作, 例如关闭文件或释放网络连接 Logger. log ("释放网络连接") 网络连接 。 release () }

/ 现在您可以将自动关闭的自动传送到函数上或直接使用它。 自动关闭 。 use {/ 使用连接, 它将在此范围完成时自动发布 。 val 内容 = 网络连接 。 readContent () Logger. log (“ 网络连接内容: $content ”) }

@See 自动封闭。

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
    val value = AutoCloseable { println("closed") }
    println(value)
}
```

```text title="输出"
ExampleKt$$Lambda$1/0x000000e001000a08@7344699f
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
