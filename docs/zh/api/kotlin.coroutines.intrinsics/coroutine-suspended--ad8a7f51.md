# COROUTINE_SUSPENDED

`kotlin.coroutines.intrinsics` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

此值用作 `suspendCoroutineUninterceptedOrReturn` `block` 的返回值,以说明执行暂停,不会立即返回任何结果。

** 这一数值不应用于普通代码。 ** 在`suspendCoroutineUninterceptedOrReturn`函数返回值(包括但不限于将这一值储存在其他属性中,从其他函数中返回,等等)的上下文之外使用该数值可能导致代码出现未指明的行为。

??? note "查看英文原文"

    This value is used as a return value of `suspendCoroutineUninterceptedOrReturn` `block` argument to state that
    the execution was suspended and will not return any result immediately.
    
    **Note: this value should not be used in general code.** Using it outside of the context of
    `suspendCoroutineUninterceptedOrReturn` function return value  (including, but not limited to,
    storing this value in other properties, returning it from other functions, etc)
    can lead to unspecified behavior of the code.

## 声明与重载

### 1. Common

```kotlin
// It is implemented as property with getter to avoid ProGuard <clinit> problem with multifile IntrinsicsKt class
@SinceKotlin("1.3")
public val COROUTINE_SUSPENDED: Any
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/intrinsics/Intrinsics.kt#L46)

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
import kotlin.coroutines.intrinsics.*

fun main() {
    val result = `COROUTINE_SUSPENDED`
    println(result)
}
```

```text title="输出"
COROUTINE_SUSPENDED
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
