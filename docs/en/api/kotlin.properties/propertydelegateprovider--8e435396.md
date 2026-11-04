# PropertyDelegateProvider

`kotlin.properties` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Base interface that can be used for implementing property delegate providers.

This is provided only for convenience; you don't have to extend this interface
as long as your delegate provider has a method with the same signature.

@param T the type of object which owns the delegated property.
@param D the type of property delegates this provider provides.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
public fun interface PropertyDelegateProvider<in T, out D>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/Interfaces.kt#L56)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.properties.PropertyDelegateProvider
import kotlin.properties.ReadOnlyProperty
fun main() {
    val provider = PropertyDelegateProvider<Any?, ReadOnlyProperty<Any?, String>> { _, property ->
        println("provide: ${property.name}")
        ReadOnlyProperty { _, _ -> "ready" }
    }
    val status by provider
    println(status)
}
```

```text title="Output"
provide: status
ready
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
