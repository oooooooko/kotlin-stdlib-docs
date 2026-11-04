# getOrElse

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果此实例代表 `success`Z`Result.isSuccess` 或
产生结果`onFailure`封装的`Throwable`例外(如果例外)`failure``Result.isFailure`.

注意, 此函数重新播放 `Throwable` 函数所投出的任何`onFailure` 的例外 。

此函数是 `fold(onSuccess = { it }, onFailure = onFailure)` 的简称(见 `fold` )。

??? note "查看英文原文"

    Returns the encapsulated value if this instance represents `success``Result.isSuccess` or the
    result of `onFailure` function for the encapsulated `Throwable` exception if it is `failure``Result.isFailure`.
    
    Note, that this function rethrows any `Throwable` exception thrown by `onFailure` function.
    
    This function is a shorthand for `fold(onSuccess = { it }, onFailure = onFailure)` (see `fold`).

## 声明与重载

### 1. Common

```kotlin
@InlineOnly
@SinceKotlin("1.3")
public inline fun <R, T : R> Result<T>.getOrElse(onFailure: (exception: Throwable) -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Result.kt#L178)

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
    val source = Result.success(42)
    val result = source.`getOrElse`({ it })
    println(result)
}
```

```text title="输出"
42
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
