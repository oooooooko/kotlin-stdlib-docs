# StackTraceRecoverable.copyForStackTraceRecovery

`kotlin.coroutines.debug` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Creates a copy of `this` for stacktrace recovery.

For better debuggability, it is recommended to use original exception as
the `cause``Throwable.cause` of the resulting one.
The stack trace of the copied exception will be overwritten by
stacktrace recovery machinery using the `Throwable.setStackTrace` call.

An exception can opt-out of copying by returning `null` from this function.

Suppressed exceptions of the original exception should be left uncopied,
to avoid circular exceptions.

This function may create a copy with a modified `message``Throwable.message`,
but note that the copy can be later recovered as well,
so the message modification code should handle this situation correctly
(e.g. by also storing the original message and checking it)
to produce a human-readable result.

## Declarations and overloads

### 1. Common

```kotlin
public fun copyForStackTraceRecovery(): T?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/debug/StackTraceRecoverable.kt#L90)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.coroutines.debug.StackTraceRecoverable
class TaskFailure(message: String, cause: Throwable? = null) : Exception(message, cause), StackTraceRecoverable<TaskFailure> {
    override fun copyForStackTraceRecovery(): TaskFailure = TaskFailure(message ?: "", this)
}
fun main() {
    val original = TaskFailure("task failed")
    val copy = original.copyForStackTraceRecovery()
    println(copy.message)
    println(copy.cause === original)
}
```

```text title="Output"
task failed
true
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
