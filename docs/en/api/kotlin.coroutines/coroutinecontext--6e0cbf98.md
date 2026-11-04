# coroutineContext

`kotlin.coroutines` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the context of the current coroutine.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.3")
@Suppress("WRONG_MODIFIER_TARGET")
@InlineOnly
public suspend inline val coroutineContext: CoroutineContext
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/Continuation.kt#L151)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
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

```text title="Output"
created
request-42
result=42
request-42
result=42
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
