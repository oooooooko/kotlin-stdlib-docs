# PropertyDelegateProvider.provideDelegate

`kotlin.properties` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the delegate of the property for the given object.

This function can be used to extend the logic of creating the object (e.g. perform validation checks)
to which the property implementation is delegated.

@param thisRef the object for which property delegate is requested.
@param property the metadata for the property.
@return the property delegate.

## Declarations and overloads

### 1. Common

```kotlin
public operator fun provideDelegate(thisRef: T, property: KProperty<*>): D
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/Interfaces.kt#L67)

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
