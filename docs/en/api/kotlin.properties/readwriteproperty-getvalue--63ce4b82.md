# ReadWriteProperty.getValue

`kotlin.properties` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the value of the property for the given object.
@param thisRef the object for which the value is requested.
@param property the metadata for the property.
@return the property value.

## Declarations and overloads

### 1. Common

```kotlin
public override operator fun getValue(thisRef: T, property: KProperty<*>): V
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/Interfaces.kt#L39)

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

val demoProperty = 42
var demoMutable = 42
fun demoFunction(value: Int): Int = value + 1

fun main() {
    val source = object : kotlin.properties.ReadWriteProperty<Any?, Int> { private var data = 42; override fun getValue(thisRef: Any?, property: kotlin.reflect.KProperty<*>) = data; override fun setValue(thisRef: Any?, property: kotlin.reflect.KProperty<*>, value: Int) { data = value } }
    val result = source.`getValue`(1, ::demoProperty)
    println(result)
}
```

```text title="Output"
42
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
