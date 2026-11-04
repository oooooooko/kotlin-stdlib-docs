# Continuation.resumeWith

`kotlin.coroutines` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

这里使用普通回调对象分别展示三个入口。由协程创建的一次性 continuation 只能恢复一次，不能按此例连续恢复同一真实挂起点。

??? note "查看英文原文"

    Resumes the execution of the corresponding coroutine passing a successful or failed `result` as the
    return value of the last suspension point.

## 声明与重载

### 1. Common

```kotlin
public fun resumeWith(result: Result<T>)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/Continuation.kt#L22)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.coroutines.*
fun main() {
    val completion = object : Continuation<Int> {
        override val context: CoroutineContext = EmptyCoroutineContext
        override fun resumeWith(result: Result<Int>) {
            println(result.fold({ "value=$it" }, { "error=${it.message}" }))
        }
    }
    println(completion.context === EmptyCoroutineContext)
    completion.resumeWith(Result.success(1))
    completion.resume(42)
    completion.resumeWithException(IllegalStateException("failed"))
}
```

```text title="输出"
true
value=1
value=42
error=failed
```

## 版本与来源

本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。
