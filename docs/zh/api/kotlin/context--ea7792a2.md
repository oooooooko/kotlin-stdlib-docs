# context

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

运行指定的 `block` ,并使用上下文范围中的给定值。

相对于 `with` ,`context`仅提供上下文参数分辨率的值,但不能作为隐性接收器。

@sample 样本.misc.contextParaters. 使用Context

??? note "查看英文原文"

    Runs the specified `block` with the given value in context scope.
    
    As opposed to `with`, `context` only makes the value available for
    context parameter resolution, but not as implicit receiver.
    
    @sample samples.misc.ContextParameters.useContext

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
@SinceKotlin("2.2")
public inline fun <T, R> context(with: T, block: context(T) () -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contextParameters/Context.kt#L14)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
@SinceKotlin("2.2")
public inline fun <A, B, R> context(a: A, b: B, block: context(A, B) () -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contextParameters/Context.kt#L32)

运行指定的`block`, 并使用上下文范围内的给定值。

相对于 `with` ,`context`仅提供上下文参数分辨率的数值,而不是作为隐含接收器。

@sample 样本.misc.contextParaters. 使用Context

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
@SinceKotlin("2.2")
public inline fun <A, B, C, R> context(a: A, b: B, c: C, block: context(A, B, C) () -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contextParameters/Context.kt#L50)

运行指定的`block`, 并使用上下文范围内的给定值。

相对于 `with` ,`context`仅提供上下文参数分辨率的数值,而不是作为隐含接收器。

@sample 样本.misc.contextParaters. 使用Context

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
@SinceKotlin("2.2")
public inline fun <A, B, C, D, R> context(a: A, b: B, c: C, d: D, block: context(A, B, C, D) () -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contextParameters/Context.kt#L68)

运行指定的`block`, 并使用上下文范围内的给定值。

相对于 `with` ,`context`仅提供上下文参数分辨率的数值,而不是作为隐含接收器。

@sample 样本.misc.contextParaters. 使用Context

### 5. Common

```kotlin
@kotlin.internal.InlineOnly
@SinceKotlin("2.2")
public inline fun <A, B, C, D, E, R> context(a: A, b: B, c: C, d: D, e: E, block: context(A, B, C, D, E) () -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contextParameters/Context.kt#L86)

运行指定的`block`, 并使用上下文范围内的给定值。

相对于 `with` ,`context`仅提供上下文参数分辨率的数值,而不是作为隐含接收器。

@sample 样本.misc.contextParaters. 使用Context

### 6. Common

```kotlin
@kotlin.internal.InlineOnly
@SinceKotlin("2.2")
public inline fun <A, B, C, D, E, F, R> context(a: A, b: B, c: C, d: D, e: E, f: F, block: context(A, B, C, D, E, F) () -> R): R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contextParameters/Context.kt#L104)

运行指定的`block`, 并使用上下文范围内的给定值。

相对于 `with` ,`context`仅提供上下文参数分辨率的数值,而不是作为隐含接收器。

@sample 样本.misc.contextParaters. 使用Context

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    abstract class Logger { abstract fun log(message: String) }
    class ConsoleLogger : Logger() { override fun log(message: String) = println(message) }

    context(logger: Logger) fun doSomething() {
        logger.log("hello")
        // do something
        logger.log("bye")
    }

    fun example() {
        context(ConsoleLogger()) {
            doSomething()
        }
    }
}
```

```text title="输出"

```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/contextParameters.kt#L12)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
