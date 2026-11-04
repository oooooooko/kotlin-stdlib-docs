# contextOf

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Retrieves the context argument, extension or dispatch receiver
in scope with the given type.
The compiler ensures that at least one such given value exists.
If more than one is found, more nested scopes are prioritized,
and otherwise an ambiguity error is raised by the compiler.

You must always provide a type argument to `contextOf`,
even if the type could be inferred from the context.

@sample samples.misc.ContextParameters.contextOfWithContextParameter
@sample samples.misc.ContextParameters.contextOfWithReceiver

## Declarations and overloads

### 1. Common

```kotlin
@InlineOnly
@SinceKotlin("2.2")
context(context: @NoInfer A)
public inline fun <A> contextOf(): @NoInfer A
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contextParameters/ContextOf.kt#L13)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
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

```text title="Output"
start
work
end
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/contextParameters.kt#L30)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
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

```text title="Output"
start
work
end
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/contextParameters.kt#L45)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
