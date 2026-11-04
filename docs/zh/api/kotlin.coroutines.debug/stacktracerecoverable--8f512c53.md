# StackTraceRecoverable

`kotlin.coroutines.debug` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

了解堆积轨迹恢复情况并明确支持复制程序的A`Throwable`号。

当一个例外对象在同时计算中创建,存储在某种共享内存中,然后由另一个同时计算中访问并重新发射时,则该例外的堆叠跟踪中将没有重放计算中的堆叠跟踪。

为了围绕这一点开展工作,非同步框架可订立一项公约,规定从不同同时计算中得到的例外首先获得*copied*,副本与打电话者的堆叠跟踪相连接,然后才重新发射。

在`kotlinx.coroutines`年,在JVM上有一个这样的公约,作为选入者,称为“回收垃圾跟踪”,默认情况下,所有例外类别中拥有下列建造者之一的,即 - `(String, Throwable?)` - `(String)` - `(Throwable?)` - `(Throwable?)` - 一个没有参数的建造者,都可以使用。

在`Throwable`亚级中实施`StackTraceRecoverable`,这样,当一个无同步框架找不到合适的建筑工时,就可以复制其实例,以便进行堆叠追踪回收。

另一种办法是,即使一个非同步框架可以绕过复制程序,也可以使用这一接口选择退出堆叠追踪回收。 为此,`copyForStackTraceRecovery`需要返回 `null` 。

`kotlinx.coroutines`年,只有联合核查团可以使用复制机制,但所有目标都可使用这一接口,这样,共同编码中实施的例外情况也能支持联合核查团的堆叠追踪器回收。

执行 `StackTraceRecoverable`

考虑这一类:

```
class BadResponseCodeException(val responseCode: Int): Exception()
```

因为它只有一台`kotlinx.coroutines`不承认的建筑机 其堆积痕迹将不留痕迹

在联合核查团方面,执行`StackTraceRecoverable`只要求增加一种约束型,并采用新方法:

```
class BadResponseCodeException(
    val responseCode: Int
): Exception(), StackTraceRecoverable<BadResponseCodeException> {
    override fun copyForStackTraceRecovery(): BadResponseCodeException {
        val result = BadResponseCodeException(responseCode)
        result.initCause(this)
        return result
    }
}
```

在多平台代码中,没有`initCause`,因此更难实现将原来的例外保留为 `cause` `Throwable.cause`的建议模式。

```
class BadResponseCodeException private constructor(
    val responseCode: Int,
    cause: Throwable?
) : Exception(cause), StackTraceRecoverable<BadResponseCodeException> {

    // The original public constructor
    constructor(responseCode: Int): this(responseCode, null)

    override fun copyForStackTraceRecovery(): BadResponseCodeException =
        BadResponseCodeException(responseCode, this)
}
```

??? note "查看英文原文"

    A `Throwable` that is aware of stacktrace recovery and explicitly supports
    a procedure for copying it.
    
    Whenever an exception object is created in one concurrent computation,
    stored in some shared memory, and then accessed by and rethrown in another
    concurrent computation, the stacktrace of rethrowing computation is going
    to be absent from the exception's stacktrace.
    
    To work around this, asynchronous frameworks may establish a convention where
    an exception received from a different concurrent computation is getting
    *copied* first, with the copy getting populated with the stacktrace of the
    caller and only then rethrown.
    
    In `kotlinx.coroutines`, there is such a convention available on the JVM as
    an opt-in, called "stacktrace recovery".
    It is available by default to all exception classes that have one of the
    following constructors:
    - `(String, Throwable?)`
    - `(String)`
    - `(Throwable?)`
    - a constructor with no parameters.
    
    Implementing `StackTraceRecoverable` in a `Throwable` subclass allows
    its instances to be copied for stacktrace recovery when an asynchronous
    framework can not find a suitable constructor.
    
    Alternatively, this interface can be used to opt out
    from stacktrace recovery even in scenarios when an asynchronous framework
    can heuristically find a copying procedure.
    To that end, `copyForStackTraceRecovery` needs to return `null`.
    
    In `kotlinx.coroutines`, the copying mechanism is only available on the JVM,
    but this interface is available on all targets so that exceptions
    implemented in common code can also support stacktrace recovery on the JVM.
    
    ### Implementing `StackTraceRecoverable`
    
    Consider this class:
    
    ```
    class BadResponseCodeException(val responseCode: Int): Exception()
    ```
    
    Since it only has a constructor that isn't recognized by `kotlinx.coroutines`,
    its stack traces will be left untouched.
    
    On the JVM, implementing `StackTraceRecoverable` only requires adding a type bound and
    implementing the new method:
    
    ```
    class BadResponseCodeException(
        val responseCode: Int
    ): Exception(), StackTraceRecoverable<BadResponseCodeException> {
        override fun copyForStackTraceRecovery(): BadResponseCodeException {
            val result = BadResponseCodeException(responseCode)
            result.initCause(this)
            return result
        }
    }
    ```
    
    In multiplatform code, `initCause` is not available, so it is more diffcult
    to fulfill the recommended pattern of keeping the original exception
    as the `cause``Throwable.cause`.
    A separate private constructor is required to achieve that:
    
    ```
    class BadResponseCodeException private constructor(
        val responseCode: Int,
        cause: Throwable?
    ) : Exception(cause), StackTraceRecoverable<BadResponseCodeException> {
    
        // The original public constructor
        constructor(responseCode: Int): this(responseCode, null)
    
        override fun copyForStackTraceRecovery(): BadResponseCodeException =
            BadResponseCodeException(responseCode, this)
    }
    ```

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibCoroutineSupportApi
public interface StackTraceRecoverable<T>
where T: Throwable, T: StackTraceRecoverable<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/debug/StackTraceRecoverable.kt#L5)

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
