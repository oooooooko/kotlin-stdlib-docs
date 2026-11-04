# suspendCoroutineUninterceptedOrReturn

`kotlin.coroutines.intrinsics` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

这是协程实现者使用的底层 API。同步返回值时不会再调用 completion；真正挂起时必须返回 `COROUTINE_SUSPENDED` 并确保只恢复一次。

??? note "查看英文原文"

    Obtains the current continuation instance inside suspend functions and either suspends
    currently running coroutine or returns result immediately without suspension.
    
    If the `block` returns the special `COROUTINE_SUSPENDED` value, it means that suspend function did suspend the execution and will
    not return any result immediately. In this case, the `Continuation` provided to the `block` shall be
    resumed by invoking `Continuation.resumeWith` at some moment in the
    future when the result becomes available to resume the computation.
    
    Otherwise, the return value of the `block` must have a type assignable to `T` and represents the result of this suspend function.
    It means that the execution was not suspended and the `Continuation` provided to the `block` shall not be invoked.
    As the result type of the `block` is declared as `Any?` and cannot be correctly type-checked,
    its proper return type remains on the conscience of the suspend function's author.
    
    Invocation of `Continuation.resumeWith` resumes coroutine directly in the invoker's thread without going through the
    `ContinuationInterceptor` that might be present in the coroutine's `CoroutineContext`.
    It is the invoker's responsibility to ensure that a proper invocation context is established.
    `Continuation.intercepted` can be used to acquire the intercepted continuation.
    
    Note that it is not recommended to call either `Continuation.resume` nor `Continuation.resumeWithException` functions synchronously
    in the same stackframe where suspension function is run. Use `suspendCoroutine` as a safer way to obtain current
    continuation instance.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
@InlineOnly
@Suppress("WRONG_INVOCATION_KIND", "UNUSED_PARAMETER", "RedundantSuspendModifier")
public suspend inline fun <T> suspendCoroutineUninterceptedOrReturn(crossinline block: (Continuation<T>) -> Any?): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/intrinsics/Intrinsics.kt#L15)

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
