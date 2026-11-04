# KMutableProperty1.set

`kotlin.reflect` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Modifies the value of the property.

@param receiver the receiver which is used to modify the value of the property.
                For example, it should be a class instance if this is a member property of that class,
                or an extension receiver if this is a top level extension property.
@param value the new value to be assigned to this property.

## Declarations and overloads

### 1. Common

```kotlin
public fun set(receiver: T, value: V)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/reflect/KProperty.kt#L75)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.reflect.KMutableProperty1
class Counter(var count: Int)
fun main() {
    val property: KMutableProperty1<Counter, Int> = Counter::count
    val counter = Counter(1)
    println(property.get(counter))
    property.set(counter, 42)
    println(counter.count)
}
```

```text title="Output"
1
42
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
