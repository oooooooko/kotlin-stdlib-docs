# recoverCatching

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回给定 `transform` 函数的封装结果,该函数适用于封装`Throwable`的例外,如果此实例代表 `failure` `Result.isFailure`,则返回封装结果,如果是 `success` `Result.isSuccess`,则返回原封装值。

此函数捕获 `Throwable` 个例外, 由 `transform` 函数投出, 并封装为失败。 重投例外的替代方法请参见 `recover` 。

??? note "查看英文原文"

    Returns the encapsulated result of the given `transform` function applied to the encapsulated `Throwable` exception
    if this instance represents `failure``Result.isFailure` or the
    original encapsulated value if it is `success``Result.isSuccess`.
    
    This function catches any `Throwable` exception thrown by `transform` function and encapsulates it as a failure.
    See `recover` for an alternative that rethrows exceptions.

## 声明与重载

### 1. Common

```kotlin
@InlineOnly
@SinceKotlin("1.3")
public inline fun <R, T : R> Result<T>.recoverCatching(transform: (exception: Throwable) -> R): Result<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Result.kt#L292)

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
    val result = source.`recoverCatching`({ it.toString() })
    println(result)
}
```

```text title="输出"
Success(42)
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
