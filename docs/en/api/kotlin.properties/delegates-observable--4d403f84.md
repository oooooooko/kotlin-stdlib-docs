# Delegates.observable

`kotlin.properties` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a property delegate for a read/write property that calls a specified callback function when changed.
@param initialValue the initial value of the property.
@param onChange the callback which is called after the change of the property is made. The value of the property
 has already been changed when this callback is invoked.

 @sample samples.properties.Delegates.observableDelegate

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <T> observable(initialValue: T, crossinline onChange: (property: KProperty<*>, oldValue: T, newValue: T) -> Unit):
            ReadWriteProperty<Any?, T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/Delegates.kt#L23)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.properties.Delegates



fun main() {
    var observed = false
    var max: Int by Delegates.observable(0) { property, oldValue, newValue ->
        observed = true
    }

    println(max)
    println(observed)

    max = 10
    println(max)
    println(observed)
}
```

```text title="Output"
0
false
10
true
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/properties/delegates.kt#L65)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
