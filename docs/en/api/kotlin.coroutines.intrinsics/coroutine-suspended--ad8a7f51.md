# COROUTINE_SUSPENDED

`kotlin.coroutines.intrinsics` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

This value is used as a return value of `suspendCoroutineUninterceptedOrReturn` `block` argument to state that
the execution was suspended and will not return any result immediately.

**Note: this value should not be used in general code.** Using it outside of the context of
`suspendCoroutineUninterceptedOrReturn` function return value  (including, but not limited to,
storing this value in other properties, returning it from other functions, etc)
can lead to unspecified behavior of the code.

## Declarations and overloads

### 1. Common

```kotlin
// It is implemented as property with getter to avoid ProGuard <clinit> problem with multifile IntrinsicsKt class
@SinceKotlin("1.3")
public val COROUTINE_SUSPENDED: Any
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/intrinsics/Intrinsics.kt#L46)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.coroutines.intrinsics.*

fun main() {
    val result = `COROUTINE_SUSPENDED`
    println(result)
}
```

```text title="Output"
COROUTINE_SUSPENDED
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
