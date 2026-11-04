# use

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Executes the given `block` function on this resource and then closes it down correctly whether an exception
is thrown or not.

In case if the resource is being closed due to an exception occurred in `block`, and the closing also fails with an exception,
the latter is added to the `suppressed``Throwable.addSuppressed` exceptions of the former.

@param block a function to process this `AutoCloseable` resource.
@return the result of `block` function invoked on this resource.

## Declarations and overloads

### 1. Common

```kotlin
@Suppress("EXPECTED_DECLARATION_WITH_BODY", "WRONG_INVOCATION_KIND")
@SinceKotlin("2.0")
@WasExperimental(ExperimentalStdlibApi::class)
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public expect inline fun <T : AutoCloseable?, R> T.use(block: (T) -> R): R
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/AutoCloseable.kt#L66)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*

class ResourceCloseException : Exception()

fun main() {

        var isClosed = false
        val resource = AutoCloseable(closeAction = { isClosed = true })
        val result = resource.use { "ok" }
        println(result)
        println(isClosed)
    
}
```

```text title="Output"
ok
true
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/autoCloseable/AutoCloseableConstructorFunctionTest.kt#L13)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
