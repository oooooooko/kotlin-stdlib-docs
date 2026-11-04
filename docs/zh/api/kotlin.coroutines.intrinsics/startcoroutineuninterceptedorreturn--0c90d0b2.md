# startCoroutineUninterceptedOrReturn

`kotlin.coroutines.intrinsics` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

这是协程实现者使用的底层 API。同步返回值时不会再调用 completion；真正挂起时必须返回 `COROUTINE_SUSPENDED` 并确保只恢复一次。

??? note "查看英文原文"

    Starts an unintercepted coroutine without a receiver and with result type `T` and executes it until its first suspension.
    Returns the result of the coroutine or throws its exception if it does not suspend or `COROUTINE_SUSPENDED` if it suspends.
    In the latter case, the `completion` continuation is invoked when the coroutine completes with a result or an exception.
    
    The coroutine is started directly in the invoker's thread without going through the `ContinuationInterceptor` that might
    be present in the completion's `CoroutineContext`. It is the invoker's responsibility to ensure that a proper invocation
    context is established.
    
    This function is designed to be used from inside of `suspendCoroutineUninterceptedOrReturn` to resume the execution of the suspended
    coroutine using a reference to the suspending function.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
public expect inline fun <T> (suspend () -> T).startCoroutineUninterceptedOrReturn(
    completion: Continuation<T>
): Any?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/CoroutinesIntrinsicsH.kt#L12)

### 2. Common

```kotlin
@SinceKotlin("1.3")
public expect inline fun <R, T> (suspend R.() -> T).startCoroutineUninterceptedOrReturn(
    receiver: R,
    completion: Continuation<T>
): Any?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/CoroutinesIntrinsicsH.kt#L29)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.coroutines.*
import kotlin.coroutines.intrinsics.*
fun main() {
    val completion = object : Continuation<Int> {
        override val context: CoroutineContext = EmptyCoroutineContext
        override fun resumeWith(result: Result<Int>) { println("completed=${result.getOrThrow()}") }
    }
    val work: suspend () -> Int = { suspendCoroutineUninterceptedOrReturn<Int> { 42 } }
    val created = work.createCoroutineUnintercepted(completion)
    println(created.intercepted() === created)
    created.resume(Unit)
    val immediate = work.startCoroutineUninterceptedOrReturn(completion)
    println("immediate=$immediate")
    println(immediate === COROUTINE_SUSPENDED)
}
```

```text title="输出"
true
completed=42
immediate=42
false
```

## 版本与来源

本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。
