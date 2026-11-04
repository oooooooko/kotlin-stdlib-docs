# createCoroutine

`kotlin.coroutines` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

创建没有接收器、结果类型为`T`的共例。此函数每次引用时,都创建一个新的可中止计算的新实例。

开始执行创建的共生律例,在返回的 `Continuation` 例中援引 `resume(Unit)` 。当共生律例最终或例外完成时,则援引`completion`的继续。随后在继续后援引任何恢复功能将产生 `IllegalStateException` 。

??? note "查看英文原文"

    Creates a coroutine without a receiver and with result type `T`.
    This function creates a new, fresh instance of suspendable computation every time it is invoked.
    
    To start executing the created coroutine, invoke `resume(Unit)` on the returned `Continuation` instance.
    The `completion` continuation is invoked when the coroutine completes with a result or an exception.
    Subsequent invocation of any resume function on the resulting continuation will produce an `IllegalStateException`.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
@Suppress("UNCHECKED_CAST")
public fun <T> (suspend () -> T).createCoroutine(
    completion: Continuation<T>
): Continuation<Unit>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/Continuation.kt#L74)

### 2. Common

```kotlin
@SinceKotlin("1.3")
@Suppress("UNCHECKED_CAST")
public fun <R, T> (suspend R.() -> T).createCoroutine(
    receiver: R,
    completion: Continuation<T>
): Continuation<Unit>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/Continuation.kt#L89)

创建具有 `R` 型接收器和结果型号 `T` 的共程。此函数每次引用时,将产生一个新的可中止计算的新实例。

开始执行创建的共生律例,在返回的 `Continuation` 例中援引 `resume(Unit)` 。当共生律例最终或例外完成时,则援引`completion`的继续。随后在继续后援引任何恢复功能将产生 `IllegalStateException` 。

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
