# contentDeepEquals

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Checks if the two specified arrays are *deeply* equal to one another.

Two arrays are considered deeply equal if they have the same size, and elements at corresponding indices are deeply equal.
That is, if two corresponding elements are nested arrays, they are also compared deeply.
Elements of other types are compared for equality using the `equals``Any.equals` function.
For floating point numbers, this means `NaN` is equal to itself and `-0.0` is not equal to `0.0`.

If any of the arrays contain themselves at any nesting level, the behavior is undefined.

@param other the array to compare deeply with this array.
@return `true` if the two arrays are deeply equal, `false` otherwise.

@sample samples.collections.Arrays.ContentOperations.contentDeepEquals

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.LowPriorityInOverloadResolution
public expect infix fun <T> Array<out T>.contentDeepEquals(other: Array<out T>): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8144)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun <T> Array<out T>?.contentDeepEquals(other: Array<out T>?): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8163)

Checks if the two specified arrays are *deeply* equal to one another.

Two arrays are considered deeply equal if they have the same size, and elements at corresponding indices are deeply equal.
That is, if two corresponding elements are nested arrays, they are also compared deeply.
Elements of other types are compared for equality using the `equals``Any.equals` function.
For floating point numbers, this means `NaN` is equal to itself and `-0.0` is not equal to `0.0`.

The arrays are also considered deeply equal if both are `null`.

If any of the arrays contain themselves at any nesting level, the behavior is undefined.

@param other the array to compare deeply with this array.
@return `true` if the two arrays are deeply equal, `false` otherwise.

@sample samples.collections.Arrays.ContentOperations.contentDeepEquals

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
import kotlin.collections.*

fun main() {
    val source = arrayOf(1, 2, 3)
    val result = source.`contentDeepEquals`(arrayOf(1, 2, 3))
    println(result)
}
```

```text title="Output"
true
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
