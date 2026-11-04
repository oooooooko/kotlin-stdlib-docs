# StringBuilder.append

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Appends the string representation of the specified object `value` to this string builder and returns this instance.

The overall effect is exactly as if the `value` were converted to a string by the `value.toString()` method,
and then that string was appended to this string builder.

## Declarations and overloads

### 1. Common

```kotlin
@IgnorableReturnValue override fun append(value: Char): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L40)

### 2. Common

```kotlin
@IgnorableReturnValue override fun append(value: CharSequence?): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L41)

### 3. Common

```kotlin
@IgnorableReturnValue override fun append(value: CharSequence?, startIndex: Int, endIndex: Int): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L42)

### 4. Common

```kotlin
@IgnorableReturnValue public fun append(value: Any?): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L55)

### 5. Common

```kotlin
@SinceKotlin("1.3")
    @IgnorableReturnValue public fun append(value: Boolean): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L63)

Appends the string representation of the specified boolean `value` to this string builder and returns this instance.

The overall effect is exactly as if the `value` were converted to a string by the `value.toString()` method,
and then that string was appended to this string builder.

### 6. Common

```kotlin
@SinceKotlin("1.9")
    @IgnorableReturnValue public fun append(value: Int): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L72)

Appends the string representation of the specified int `value` to this string builder and returns this instance.

The overall effect is exactly as if the `value` were converted to a string by the `value.toString()` method,
and then that string was appended to this string builder.

### 7. Common

```kotlin
@SinceKotlin("1.9")
    @IgnorableReturnValue public fun append(value: Long): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L81)

Appends the string representation of the specified long `value` to this string builder and returns this instance.

The overall effect is exactly as if the `value` were converted to a string by the `value.toString()` method,
and then that string was appended to this string builder.

### 8. Common

```kotlin
@SinceKotlin("1.9")
    @IgnorableReturnValue public fun append(value: Float): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L90)

Appends the string representation of the specified float `value` to this string builder and returns this instance.

The overall effect is exactly as if the `value` were converted to a string by the `value.toString()` method,
and then that string was appended to this string builder.

### 9. Common

```kotlin
@SinceKotlin("1.9")
    @IgnorableReturnValue public fun append(value: Double): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L99)

Appends the string representation of the specified double `value` to this string builder and returns this instance.

The overall effect is exactly as if the `value` were converted to a string by the `value.toString()` method,
and then that string was appended to this string builder.

### 10. Common

```kotlin
@SinceKotlin("1.4")
    @IgnorableReturnValue public fun append(value: CharArray): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L108)

Appends characters in the specified character array `value` to this string builder and returns this instance.

Characters are appended in order, starting at the index 0.

### 11. Common

```kotlin
@SinceKotlin("1.3")
    @IgnorableReturnValue public fun append(value: String?): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L116)

Appends the specified string `value` to this string builder and returns this instance.

If `value` is `null`, then the four characters `"null"` are appended.

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
    val result = source.`append`('o')
    println(result)
}
```

```text title="Output"
kotlino
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
