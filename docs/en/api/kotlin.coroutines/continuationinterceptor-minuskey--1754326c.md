# ContinuationInterceptor.minusKey

`kotlin.coroutines` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Declarations and overloads

### 1. Common

```kotlin
public override fun minusKey(key: CoroutineContext.Key<*>): CoroutineContext
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/ContinuationInterceptor.kt#L64)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
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

```text title="Output"
true
true
intercept
released
42
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
