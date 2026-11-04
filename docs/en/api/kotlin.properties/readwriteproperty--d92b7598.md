# ReadWriteProperty

`kotlin.properties` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Base interface that can be used for implementing property delegates of read-write properties.

This is provided only for convenience; you don't have to extend this interface
as long as your property delegate has methods with the same signatures.

@param T the type of object which owns the delegated property.
@param V the type of the property value.

## Declarations and overloads

### 1. Common

```kotlin
public interface ReadWriteProperty<in T, V> : ReadOnlyProperty<T, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/Interfaces.kt#L29)

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
import kotlin.properties.*

fun main() {
    val value = object : kotlin.properties.ReadWriteProperty<Any?, Int> { private var data = 42; override fun getValue(thisRef: Any?, property: kotlin.reflect.KProperty<*>) = data; override fun setValue(thisRef: Any?, property: kotlin.reflect.KProperty<*>, value: Int) { data = value } }
    println(value)
}
```

```text title="Output"
ExampleKt$main$value$1@6d06d69c
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
