# suspend

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

功能型构建器,确保给定的 `block` 有`suspend`修饰机,并用作暂停功能。

默认情况下,功能型声明不以`suspend`推定,不能作为下列声明使用:

```
suspend fun yield() {}

// Inferred type: '() -> Unit'
val regularBlock = { yield() } // Does not compile, `yield` requires to be in the suspend context
// Inferred type: 'suspend () -> Unit'
val suspendBlock = suspend { yield() } // Compiles as expected
```

??? note "查看英文原文"

    A functional type builder that ensures the given `block` has a `suspend` modifier and can be
    used as a suspend function.
    
    By default, functional type declarations are not inferred as `suspend` and cannot be used as such:
    
    ```
    suspend fun yield() {}
    
    // Inferred type: '() -> Unit'
    val regularBlock = { yield() } // Does not compile, `yield` requires to be in the suspend context
    // Inferred type: 'suspend () -> Unit'
    val suspendBlock = suspend { yield() } // Compiles as expected
    ```

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
@SinceKotlin("1.2")
@Suppress("INVISIBLE_MEMBER", "INVISIBLE_REFERENCE")
public inline fun <R> suspend(noinline block: suspend () -> R): suspend () -> R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Suspend.kt#L9)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.coroutines.*
fun main() {
    val work = suspend { 42 }
    work.startCoroutine(object : Continuation<Int> {
        override val context = EmptyCoroutineContext
        override fun resumeWith(result: Result<Int>) { println(result.getOrThrow()) }
    })
}
```

```text title="输出"
42
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
