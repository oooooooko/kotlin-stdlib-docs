# MatchGroupCollection

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Represents a collection of captured groups in a single match of a regular expression.

This collection has size of `groupCount + 1` where `groupCount` is the count of groups in the regular expression.
Groups are indexed from 1 to `groupCount` and group with the index 0 corresponds to the entire match.

An element of the collection at the particular index can be `null`,
if the corresponding group in the regular expression is optional and
there was no match captured by that group.

## Declarations and overloads

### 1. Common

```kotlin
public interface MatchGroupCollection : Collection<MatchGroup?>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/regex/MatchResult.kt#L8)

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
import kotlin.text.*

fun main() {
    val value = Regex("([a-z]+)").find("hello")!!.groups
    println(value)
}
```

```text title="Output"
[MatchGroup(value=hello, range=0..4), MatchGroup(value=hello, range=0..4)]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
