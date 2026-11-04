# CancellationException

`kotlin.coroutines.cancellation` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果在中止时共程被取消,则会被可变暂停功能扔弃。它表示共程取消 _正常_ 。

??? note "查看英文原文"

    Thrown by cancellable suspending functions if the coroutine is cancelled while it is suspended.
    It indicates _normal_ cancellation of a coroutine.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public expect open class CancellationException : IllegalStateException
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/cancellation/CancellationExceptionH.kt#L8)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public expect fun CancellationException(message: String?, cause: Throwable?): CancellationException
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/cancellation/CancellationExceptionH.kt#L18)

创建了 `CancellationException` 的例, 并给定 `message` 和 `cause` 。

### 3. Common

```kotlin
@SinceKotlin("1.4")
public expect fun CancellationException(cause: Throwable?): CancellationException
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/cancellation/CancellationExceptionH.kt#L24)

创建 `CancellationException` 实例, 并使用给定 `cause` 。

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
import kotlin.coroutines.cancellation.*

fun main() {
    val value = kotlin.coroutines.cancellation.CancellationException()
    println(value)
}
```

```text title="输出"
java.util.concurrent.CancellationException
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
