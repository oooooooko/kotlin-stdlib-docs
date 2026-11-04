# withDefault

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a wrapper of this read-only map, having the implicit default value provided with the specified function `defaultValue`.

This implicit default value is used when the original map doesn't contain a value for the key specified
and a value is obtained with `Map.getValue` function, for example when properties are delegated to the map.

When this map already has an implicit default value provided with a former call to `withDefault`, it is being replaced by this call.

@sample samples.collections.Maps.Usage.getValueWithDefault
@sample samples.collections.Maps.Usage.getValueWithReplacedDefault

## Declarations and overloads

### 1. Common

```kotlin
public fun <K, V> Map<K, V>.withDefault(defaultValue: (key: K) -> V): Map<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MapWithDefault.kt#L28)

### 2. Common

```kotlin
@kotlin.jvm.JvmName("withDefaultMutable")
public fun <K, V> MutableMap<K, V>.withDefault(defaultValue: (key: K) -> V): MutableMap<K, V>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MapWithDefault.kt#L45)

Returns a wrapper of this mutable map, having the implicit default value provided with the specified function `defaultValue`.

This implicit default value is used when the original map doesn't contain a value for the key specified
and a value is obtained with `Map.getValue` function, for example when properties are delegated to the map.

When this map already has an implicit default value provided with a former call to `withDefault`, it is being replaced by this call.

@sample samples.collections.Maps.Usage.getValueWithDefault
@sample samples.collections.Maps.Usage.getValueWithReplacedDefault
@sample samples.collections.Maps.Usage.changesToMutableMapWithDefaultPropagateToUnderlyingMap

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*

val map = hashMapOf<String, Any?>("a" to "all", "b" to null, "c" to 1, "xProperty" to 1.0)

val map2: MutableMap<String, CharSequence> = hashMapOf("a2" to "all")

var a: String by map

var b: Any? by map

var c: Int by map

var d: String? by map

var a2: String by map2.withDefault { "empty" }

fun main() {

        println(a)
        println(b)
        println(c)
        c = 2
        println(c)
        println(map["c"])

        println(a2)
        map2.remove("a2")
        println(a2)

        assertFailsWith<NoSuchElementException> { d }
        map["d"] = null
        println(d)
    
}
```

```text title="Output"
all
null
1
2
2
all
empty
null
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/properties/delegation/MapAccessorsTest.kt#L55)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
