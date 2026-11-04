# ContinuationInterceptor.interceptContinuation

`kotlin.coroutines` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回继续, 以覆盖原始的 `continuation` , 从而拦截所有恢复。 必要时, 共路框架会引用此函数, 由此产生的连续函数会按原始的 `continuation` 的每例在内部隐藏 。

函数如果不想截断此特定延续, 只需返回原始 `continuation`即可。

最初的`continuation`框架完成后,共同规则框架援引`releaseInterceptedContinuation`,如果被拦截,则继续适用,也就是说,如果`interceptContinuation`以前又恢复了另一个继续适用的情况。

??? note "查看英文原文"

    Returns continuation that wraps the original `continuation`, thus intercepting all resumptions.
    This function is invoked by coroutines framework when needed and the resulting continuations are
    cached internally per each instance of the original `continuation`.
    
    This function may simply return original `continuation` if it does not want to intercept this particular continuation.
    
    When the original `continuation` completes, coroutine framework invokes `releaseInterceptedContinuation`
    with the resulting continuation if it was intercepted, that is if `interceptContinuation` had previously
    returned a different continuation instance.

## 声明与重载

### 1. Common

```kotlin
public fun <T> interceptContinuation(continuation: Continuation<T>): Continuation<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/ContinuationInterceptor.kt#L26)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.coroutines.*
class LoggingInterceptor : AbstractCoroutineContextElement(ContinuationInterceptor), ContinuationInterceptor {
    override fun <T> interceptContinuation(continuation: Continuation<T>): Continuation<T> =
        object : Continuation<T> {
            override val context = continuation.context
            override fun resumeWith(result: Result<T>) { println("intercept"); continuation.resumeWith(result) }
        }
    override fun releaseInterceptedContinuation(continuation: Continuation<*>) { println("released") }
}
fun main() {
    val interceptor = LoggingInterceptor()
    println(interceptor[ContinuationInterceptor] === interceptor)
    println(interceptor.minusKey(ContinuationInterceptor) === EmptyCoroutineContext)
    val work: suspend () -> Int = { 42 }
    work.startCoroutine(object : Continuation<Int> {
        override val context: CoroutineContext = interceptor
        override fun resumeWith(result: Result<Int>) { println(result.getOrThrow()) }
    })
}
```

```text title="输出"
true
true
intercept
released
42
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
