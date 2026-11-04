# suspendCoroutine

`kotlin.coroutines` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

获得中止功能内目前持续运行的例数,并暂停目前运行的共同常规。

在此函数中,`Continuation.resume`和`Continuation.resumeWithException`两者都可以同步地用于执行暂停功能的同一堆叠框,或者在同一线条中不同步地后行,或者从另一线执行。随后援引任何恢复功能将产生`IllegalStateException`。

??? note "查看英文原文"

    Obtains the current continuation instance inside suspend functions and suspends
    the currently running coroutine.
    
    In this function both `Continuation.resume` and `Continuation.resumeWithException` can be used either synchronously in
    the same stack-frame where the suspension function is run or asynchronously later in the same thread or
    from a different thread of execution. Subsequent invocation of any resume function will produce an `IllegalStateException`.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
@InlineOnly
public suspend inline fun <T> suspendCoroutine(crossinline block: (Continuation<T>) -> Unit): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/Continuation.kt#L132)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.coroutines.*
class RequestId(val value: String) : AbstractCoroutineContextElement(Key) {
    companion object Key : CoroutineContext.Key<RequestId>
}
fun main() {
    val completion = object : Continuation<Int> {
        override val context: CoroutineContext = RequestId("request-42")
        override fun resumeWith(result: Result<Int>) { println("result=${result.getOrThrow()}") }
    }
    val work: suspend () -> Int = {
        println(coroutineContext[RequestId]?.value)
        suspendCoroutine { continuation -> continuation.resume(42) }
    }
    val created = work.createCoroutine(completion)
    println("created")
    created.resume(Unit)
    work.startCoroutine(completion)
}
```

```text title="输出"
created
request-42
result=42
request-42
result=42
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
