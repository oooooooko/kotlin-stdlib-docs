# StringBuilder.insert

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Inserts the string representation of the specified boolean `value` into this string builder at the specified `index` and returns this instance.

The overall effect is exactly as if the `value` were converted to a string by the `value.toString()` method,
and then that string was inserted into this string builder at the specified `index`.

@throws IndexOutOfBoundsException if `index` is less than zero or greater than the length of this string builder.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
    @IgnorableReturnValue public fun insert(index: Int, value: Boolean): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L178)

### 2. Common

```kotlin
@SinceKotlin("1.9")
    @IgnorableReturnValue public fun insert(index: Int, value: Int): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L189)

Inserts the string representation of the specified int `value` into this string builder at the specified `index` and returns this instance.

The overall effect is exactly as if the `value` were converted to a string by the `value.toString()` method,
and then that string was inserted into this string builder at the specified `index`.

@throws IndexOutOfBoundsException if `index` is less than zero or greater than the length of this string builder.

### 3. Common

```kotlin
@SinceKotlin("1.9")
    @IgnorableReturnValue public fun insert(index: Int, value: Long): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L200)

Inserts the string representation of the specified long `value` into this string builder at the specified `index` and returns this instance.

The overall effect is exactly as if the `value` were converted to a string by the `value.toString()` method,
and then that string was inserted into this string builder at the specified `index`.

@throws IndexOutOfBoundsException if `index` is less than zero or greater than the length of this string builder.

### 4. Common

```kotlin
@SinceKotlin("1.9")
    @IgnorableReturnValue public fun insert(index: Int, value: Float): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L211)

Inserts the string representation of the specified float `value` into this string builder at the specified `index` and returns this instance.

The overall effect is exactly as if the `value` were converted to a string by the `value.toString()` method,
and then that string was inserted into this string builder at the specified `index`.

@throws IndexOutOfBoundsException if `index` is less than zero or greater than the length of this string builder.

### 5. Common

```kotlin
@SinceKotlin("1.9")
    @IgnorableReturnValue public fun insert(index: Int, value: Double): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L222)

Inserts the string representation of the specified double `value` into this string builder at the specified `index` and returns this instance.

The overall effect is exactly as if the `value` were converted to a string by the `value.toString()` method,
and then that string was inserted into this string builder at the specified `index`.

@throws IndexOutOfBoundsException if `index` is less than zero or greater than the length of this string builder.

### 6. Common

```kotlin
@SinceKotlin("1.4")
    @IgnorableReturnValue public fun insert(index: Int, value: Char): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L233)

Inserts the specified character `value` into this string builder at the specified `index` and returns this instance.

@throws IndexOutOfBoundsException if `index` is less than zero or greater than the length of this string builder.

### 7. Common

```kotlin
@SinceKotlin("1.4")
    @IgnorableReturnValue public fun insert(index: Int, value: CharArray): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L241)

Inserts characters in the specified character array `value` into this string builder at the specified `index` and returns this instance.

The inserted characters go in same order as in the `value` character array, starting at `index`.

@throws IndexOutOfBoundsException if `index` is less than zero or greater than the length of this string builder.

### 8. Common

```kotlin
@SinceKotlin("1.4")
    @IgnorableReturnValue public fun insert(index: Int, value: CharSequence?): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L251)

Inserts characters in the specified character sequence `value` into this string builder at the specified `index` and returns this instance.

The inserted characters go in the same order as in the `value` character sequence, starting at `index`.

@param index the position in this string builder to insert at.
@param value the character sequence from which characters are inserted. If `value` is `null`, then the four characters `"null"` are inserted.

@throws IndexOutOfBoundsException if `index` is less than zero or greater than the length of this string builder.

### 9. Common

```kotlin
@SinceKotlin("1.4")
    @IgnorableReturnValue public fun insert(index: Int, value: Any?): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L264)

Inserts the string representation of the specified object `value` into this string builder at the specified `index` and returns this instance.

The overall effect is exactly as if the `value` were converted to a string by the `value.toString()` method,
and then that string was inserted into this string builder at the specified `index`.

@throws IndexOutOfBoundsException if `index` is less than zero or greater than the length of this string builder.

### 10. Common

```kotlin
@SinceKotlin("1.4")
    @IgnorableReturnValue public fun insert(index: Int, value: String?): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L275)

Inserts the string `value` into this string builder at the specified `index` and returns this instance.

If `value` is `null`, then the four characters `"null"` are inserted.

@throws IndexOutOfBoundsException if `index` is less than zero or greater than the length of this string builder.

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
    val source = StringBuilder("kotlin")
    val result = source.`insert`(0, false)
    println(result)
}
```

```text title="Output"
falsekotlin
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
