# KotlinVersion.compareTo

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Declarations and overloads

### 1. Common

```kotlin
override fun compareTo(other: KotlinVersion): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/KotlinVersion.kt#L45)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.random.Random
import kotlin.test.*



fun main() {

        println(KotlinVersion.CURRENT.isAtLeast(1, 1))
        println(KotlinVersion.CURRENT.isAtLeast(1, 1, 0))
        println(KotlinVersion.CURRENT >= KotlinVersion(1, 1))
        println(KotlinVersion(1, 1) <= KotlinVersion.CURRENT)

        val anotherCurrent = KotlinVersion.CURRENT.run { KotlinVersion(major, minor, patch) }
        println(anotherCurrent)
        println(anotherCurrent.hashCode())
        println(KotlinVersion.CURRENT compareTo anotherCurrent)
    
}
```

```text title="Output"
true
true
true
true
2.4.21
132117
0
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/utils/KotlinVersionTest.kt#L14)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
