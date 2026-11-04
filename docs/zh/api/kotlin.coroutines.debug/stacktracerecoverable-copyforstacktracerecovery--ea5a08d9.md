# StackTraceRecoverable.copyForStackTraceRecovery

`kotlin.coroutines.debug` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

创建 `this` 的复制件,用于恢复堆叠跟踪。

为了更好地调试,建议使用原例外情形,作为
所产生的`cause``Throwable.cause`ZZZZ 之一。
复制例外的堆叠踪迹将由
使用 `Throwable.setStackTrace` 呼叫的堆叠跟踪恢复机械 。

例外情形是,从此函数返回 `null` ,即可选择不复制。

原例外的禁止例外应当不加修正,以避免循环出现例外。

此函数可创建一个已修改的 `message`Z`Throwable.message` 复制件,
但请注意,该副本也可以在以后收回,
以便电文修改代码能够正确处理这种情况
(例如,同时存储原始电文并核对其)
产生人类可读的结果。

??? note "查看英文原文"

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

## 声明与重载

### 1. Common

```kotlin
public fun copyForStackTraceRecovery(): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/debug/StackTraceRecoverable.kt#L90)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
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

```text title="输出"
task failed
true
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
