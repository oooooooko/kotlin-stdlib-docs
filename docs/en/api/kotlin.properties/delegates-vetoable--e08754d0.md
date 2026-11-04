# Delegates.vetoable

`kotlin.properties` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a property delegate for a read/write property that calls a specified callback function when changed,
allowing the callback to veto the modification.
@param initialValue the initial value of the property.
@param onChange the callback which is called before a change to the property value is attempted.
 The value of the property hasn't been changed yet, when this callback is invoked.
 If the callback returns `true` the value of the property is being set to the new value,
 and if the callback returns `false` the new value is discarded and the property remains its old value.

 @sample samples.properties.Delegates.vetoableDelegate
 @sample samples.properties.Delegates.throwVetoableDelegate

## Declarations and overloads

### 1. Common

```kotlin
public inline fun <T> vetoable(initialValue: T, crossinline onChange: (property: KProperty<*>, oldValue: T, newValue: T) -> Boolean):
            ReadWriteProperty<Any?, T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/Delegates.kt#L37)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.properties.Delegates



fun main() {
    var max: Int by Delegates.vetoable(0) { property, oldValue, newValue ->
        newValue > oldValue
    }

    println(max)

    max = 10
    println(max)

    max = 5
    println(max)
}
```

```text title="Output"
0
10
10
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/properties/delegates.kt#L26)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.properties.Delegates
import kotlin.test.*



fun main() {
    var max: Int by Delegates.vetoable(0) { property, oldValue, newValue ->
        if (newValue > oldValue) true else throw IllegalArgumentException("New value must be larger than old value.")
    }

    println(max)

    max = 10
    println(max)

    assertFailsWith<IllegalArgumentException> { max = 5 }
}
```

```text title="Output"
0
10
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/properties/delegates.kt#L41)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
