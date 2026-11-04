# createCoroutineUnintercepted

`kotlin.coroutines.intrinsics` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

These are coroutine implementation primitives. A synchronous result does not invoke completion. A suspended operation must return `COROUTINE_SUSPENDED` and resume exactly once.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.3")
public expect fun <T> (suspend () -> T).createCoroutineUnintercepted(
    completion: Continuation<T>
): Continuation<Unit>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/CoroutinesIntrinsicsH.kt#L54)

### 2. Common

```kotlin
@SinceKotlin("1.3")
public expect fun <R, T> (suspend R.() -> T).createCoroutineUnintercepted(
    receiver: R,
    completion: Continuation<T>
): Continuation<Unit>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/CoroutinesIntrinsicsH.kt#L59)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
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

```text title="Output"
true
completed=42
immediate=42
false
```

## Version and sources

This page's explanation and examples have been separately prepared. Declarations are pinned to `v2.4.21`; examples were verified on the JVM with Kotlin / stdlib 2.4.21.
