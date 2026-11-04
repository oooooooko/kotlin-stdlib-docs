# context

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Runs the specified `block` with the given value in context scope.

As opposed to `with`, `context` only makes the value available for
context parameter resolution, but not as implicit receiver.

@sample samples.misc.ContextParameters.useContext

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
@SinceKotlin("2.2")
public inline fun <T, R> context(with: T, block: context(T) () -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contextParameters/Context.kt#L14)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
@SinceKotlin("2.2")
public inline fun <A, B, R> context(a: A, b: B, block: context(A, B) () -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contextParameters/Context.kt#L32)

Runs the specified `block` with the given values in context scope.

As opposed to `with`, `context` only makes the values available for
context parameter resolution, but not as implicit receivers.

@sample samples.misc.ContextParameters.useContext

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
@SinceKotlin("2.2")
public inline fun <A, B, C, R> context(a: A, b: B, c: C, block: context(A, B, C) () -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contextParameters/Context.kt#L50)

Runs the specified `block` with the given values in context scope.

As opposed to `with`, `context` only makes the values available for
context parameter resolution, but not as implicit receivers.

@sample samples.misc.ContextParameters.useContext

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
@SinceKotlin("2.2")
public inline fun <A, B, C, D, R> context(a: A, b: B, c: C, d: D, block: context(A, B, C, D) () -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contextParameters/Context.kt#L68)

Runs the specified `block` with the given values in context scope.

As opposed to `with`, `context` only makes the values available for
context parameter resolution, but not as implicit receivers.

@sample samples.misc.ContextParameters.useContext

### 5. Common

```kotlin
@kotlin.internal.InlineOnly
@SinceKotlin("2.2")
public inline fun <A, B, C, D, E, R> context(a: A, b: B, c: C, d: D, e: E, block: context(A, B, C, D, E) () -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contextParameters/Context.kt#L86)

Runs the specified `block` with the given values in context scope.

As opposed to `with`, `context` only makes the values available for
context parameter resolution, but not as implicit receivers.

@sample samples.misc.ContextParameters.useContext

### 6. Common

```kotlin
@kotlin.internal.InlineOnly
@SinceKotlin("2.2")
public inline fun <A, B, C, D, E, F, R> context(a: A, b: B, c: C, d: D, e: E, f: F, block: context(A, B, C, D, E, F) () -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contextParameters/Context.kt#L104)

Runs the specified `block` with the given values in context scope.

As opposed to `with`, `context` only makes the values available for
context parameter resolution, but not as implicit receivers.

@sample samples.misc.ContextParameters.useContext

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
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

```text title="Output"

```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/contextParameters.kt#L12)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
