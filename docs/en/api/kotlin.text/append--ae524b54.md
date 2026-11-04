# append

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Appends all arguments to the given `Appendable`.

## Declarations and overloads

### 1. Common

```kotlin
@IgnorableReturnValue
public fun <T : Appendable> T.append(vararg value: CharSequence?): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Appendable.kt#L61)

### 2. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.append(value: Byte): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L327)

Appends the string representation of the specified byte `value` to this string builder and returns this instance.

The overall effect is exactly as if the `value` were converted to a string by the `value.toString()` method,
and then that string was appended to this string builder.

### 3. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.append(value: Short): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L336)

Appends the string representation of the specified short `value` to this string builder and returns this instance.

The overall effect is exactly as if the `value` were converted to a string by the `value.toString()` method,
and then that string was appended to this string builder.

### 4. Common

```kotlin
@Suppress("EXTENSION_SHADOWED_BY_MEMBER")
@Deprecated("Use append(value: Any?) instead", ReplaceWith("append(value = obj)"), DeprecationLevel.WARNING)
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun StringBuilder.append(obj: Any?): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L491)

### 5. Common

```kotlin
@IgnorableReturnValue public fun StringBuilder.append(vararg value: String?): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L518)

Appends all arguments to the given StringBuilder.

### 6. Common

```kotlin
@IgnorableReturnValue public fun StringBuilder.append(vararg value: Any?): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L527)

Appends all arguments to the given StringBuilder.

### 7. Common

```kotlin
// KT-52336
@Deprecated("Use appendRange instead.", ReplaceWith("this.appendRange(str, offset, offset + len)"), level = DeprecationLevel.ERROR)
@kotlin.internal.InlineOnly
@Suppress("UNUSED_PARAMETER")
@IgnorableReturnValue public inline fun StringBuilder.append(str: CharArray, offset: Int, len: Int): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L536)

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
    val result = source.`append`(2.toByte())
    println(result)
}
```

```text title="Output"
kotlin2
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
