# filterIsInstanceTo

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Appends all elements that are instances of specified type parameter R to the given `destination`.

@sample samples.collections.Collections.Filtering.filterIsInstanceTo

## Declarations and overloads

### 1. Common

```kotlin
@IgnorableReturnValue
public inline fun <reified R, C : MutableCollection<in R>> Array<*>.filterIsInstanceTo(destination: C): C
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4256)

### 2. Common

```kotlin
@IgnorableReturnValue
public inline fun <reified R, C : MutableCollection<in R>> Iterable<*>.filterIsInstanceTo(destination: C): C
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L815)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    open class Animal(val name: String) {
        override fun toString(): String {
            return name
        }
    }
    class Dog(name: String): Animal(name)
    class Cat(name: String): Animal(name)

    val animals: List<Animal> = listOf(Cat("Scratchy"), Dog("Poochie"))
    val cats = mutableListOf<Cat>()

    println(cats)

    animals.filterIsInstanceTo<Cat, MutableList<Cat>>(cats)

    println(cats)
}
```

```text title="Output"
[]
[Scratchy]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1662)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
