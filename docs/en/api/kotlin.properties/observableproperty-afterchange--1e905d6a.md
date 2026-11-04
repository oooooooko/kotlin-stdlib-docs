# ObservableProperty.afterChange

`kotlin.properties` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

The callback which is called after the change of the property is made. The value of the property
has already been changed when this callback is invoked.

## Declarations and overloads

### 1. Common

```kotlin
protected open fun afterChange(property: KProperty<*>, oldValue: V, newValue: V): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/ObservableProperty.kt#L25)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.properties.ObservableProperty
import kotlin.reflect.KProperty
class NonNegative(initial: Int) : ObservableProperty<Int>(initial) {
    override fun beforeChange(property: KProperty<*>, oldValue: Int, newValue: Int): Boolean = newValue >= 0
    override fun afterChange(property: KProperty<*>, oldValue: Int, newValue: Int) {
        println("${property.name}: $oldValue -> $newValue")
    }
}
fun main() {
    val delegate = NonNegative(1)
    var count by delegate
    println(count)
    count = 2
    count = -1
    println(count)
    println(delegate.toString())
}
```

```text title="Output"
1
count: 1 -> 2
2
ObservableProperty(value=2)
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
