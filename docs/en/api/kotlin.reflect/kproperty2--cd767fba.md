# KProperty2

`kotlin.reflect` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Represents a property, operations on which take two receivers as parameters,
such as an extension property declared in a class.

@param D the type of the first receiver. In case of the extension property in a class this is
       the type of the declaring class of the property, or any subclass of that class.
@param E the type of the second receiver. In case of the extension property in a class this is
       the type of the extension receiver.
@param V the type of the property value.

## Declarations and overloads

### 1. Common

```kotlin
public expect interface KProperty2<D, E, out V> : KProperty<V>, (D, E) -> V
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/reflect/KProperty.kt#L87)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.reflect.KMutableProperty2
import kotlin.reflect.full.memberExtensionProperties
class Labels(var prefix: String) {
    var Int.label: String
        get() = "$prefix$this"
        set(value) { prefix = value }
}
fun main() {
    @Suppress("UNCHECKED_CAST")
    val property = Labels::class.memberExtensionProperties.single() as KMutableProperty2<Labels, Int, String>
    val labels = Labels("item-")
    println(property.get(labels, 7))
    property.set(labels, 7, "new-")
    println(property.get(labels, 7))
}
```

```text title="Output"
item-7
new-7
```

This example requires `kotlin-reflect:2.4.21`.

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
