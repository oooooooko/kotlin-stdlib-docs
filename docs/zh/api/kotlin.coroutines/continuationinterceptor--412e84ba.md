# ContinuationInterceptor

`kotlin.coroutines` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

共路框架使用 `ContinuationInterceptor.Key` 来取回拦截器,并用`interceptContinuation`次引用来拦截所有共路延续。

`ContinuationInterceptor`行为举止像`polymorphic element``AbstractCoroutineContextKey`,意思是
代表执行《公约》的代表`get``CoroutineContext.Element.get`和`minusKey``CoroutineContext.Element.minusKey`
分别对`getPolymorphicElement`和`minusPolymorphicKey`分别适用。
`ContinuationInterceptor` 子类型可以使用 任何`ContinuationInterceptor.Key` 从共律上下文中提取
如果扩展 `AbstractCoroutineContextKey`,则使用子类型键。

??? note "查看英文原文"

    Marks coroutine context element that intercepts coroutine continuations.
    The coroutines framework uses `ContinuationInterceptor.Key` to retrieve the interceptor and
    intercepts all coroutine continuations with `interceptContinuation` invocations.
    
    `ContinuationInterceptor` behaves like a `polymorphic element``AbstractCoroutineContextKey`, meaning that
    its implementation delegates `get``CoroutineContext.Element.get` and `minusKey``CoroutineContext.Element.minusKey`
    to `getPolymorphicElement` and `minusPolymorphicKey` respectively.
    `ContinuationInterceptor` subtypes can be extracted from the coroutine context using either `ContinuationInterceptor.Key`
    or subtype key if it extends `AbstractCoroutineContextKey`.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
public interface ContinuationInterceptor : CoroutineContext.Element
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/ContinuationInterceptor.kt#L8)

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
