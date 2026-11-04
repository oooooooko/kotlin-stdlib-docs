# trimEnd

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a subsequence of this char sequence having trailing characters matching the `predicate` removed.

## Declarations and overloads

### 1. Common

```kotlin
public inline fun CharSequence.trimEnd(predicate: (Char) -> Boolean): CharSequence
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L125)

### 2. Common

```kotlin
public inline fun String.trimEnd(predicate: (Char) -> Boolean): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L136)

Returns a string having trailing characters matching the `predicate` removed.

### 3. Common

```kotlin
public fun CharSequence.trimEnd(vararg chars: Char): CharSequence
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L162)

Returns a subsequence of this char sequence having trailing characters from the `chars` array removed.

### 4. Common

```kotlin
public fun String.trimEnd(vararg chars: Char): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L167)

Returns a string having trailing characters from the `chars` array removed.

### 5. Common

```kotlin
public fun CharSequence.trimEnd(): CharSequence
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L194)

Returns a subsequence of this char sequence having trailing whitespace removed.

### 6. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun String.trimEnd(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L199)

Returns a string having trailing whitespace removed.

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
    val source = "kotlin"
    val result = source.`trimEnd`({ it.toString().length > 0 })
    println(result)
}
```

```text title="Output"

```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
