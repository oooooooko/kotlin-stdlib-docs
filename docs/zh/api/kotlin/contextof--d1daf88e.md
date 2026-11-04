# contextOf

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

获取上下文参数、扩展或发送接收器, 范围与给定类型相同。 汇编者确保至少存在一个这样的给定值。 如果找到多个, 则优先排序更多的嵌套范围, 否则, 编译者会提出模糊错误 。

您必须总是提供类型参数到 `contextOf` , 即使从上下文可以推断出该类型 。

@sample 样本. misc.ContextParaters.contextforforst TextParaters @sample 样本.misc.ContextParaters.contextforfusOn Receiver

??? note "查看英文原文"

    Retrieves the context argument, extension or dispatch receiver
    in scope with the given type.
    The compiler ensures that at least one such given value exists.
    If more than one is found, more nested scopes are prioritized,
    and otherwise an ambiguity error is raised by the compiler.
    
    You must always provide a type argument to `contextOf`,
    even if the type could be inferred from the context.
    
    @sample samples.misc.ContextParameters.contextOfWithContextParameter
    @sample samples.misc.ContextParameters.contextOfWithReceiver

## 声明与重载

### 1. Common

```kotlin
@InlineOnly
@SinceKotlin("2.2")
context(context: @NoInfer A)
public inline fun <A> contextOf(): @NoInfer A
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contextParameters/ContextOf.kt#L13)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    abstract class Logger { abstract fun log(message: String) }
    class ConsoleLogger : Logger() { override fun log(message: String) = println(message) }

    fun <A> withConsoleLogger(block: context(Logger) () -> A): A =
        context(ConsoleLogger()) { block() }

    withConsoleLogger {
        contextOf<Logger>().log("start")
        println("work")
        contextOf<Logger>().log("end")
    }
}
```

```text title="输出"
start
work
end
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/contextParameters.kt#L30)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    abstract class Logger { abstract fun log(message: String) }
    class ConsoleLogger : Logger() { override fun log(message: String) = println(message) }

    fun <A> withConsoleLogger(block: Logger.() -> A): A =
        with(ConsoleLogger()) { block() }

    withConsoleLogger {
        contextOf<Logger>().log("start")
        println("work")
        contextOf<Logger>().log("end")
    }
}
```

```text title="输出"
start
work
end
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/contextParameters.kt#L45)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
