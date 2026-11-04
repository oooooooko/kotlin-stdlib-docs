# appendLine

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Appends a line feed character (`\n`) to this Appendable.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun Appendable.appendLine(): Appendable
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Appendable.kt#L71)

### 2. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun Appendable.appendLine(value: CharSequence?): Appendable
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Appendable.kt#L77)

Appends value to the given Appendable and a line feed character (`\n`) after it.

### 3. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun Appendable.appendLine(value: Char): Appendable
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Appendable.kt#L83)

Appends value to the given Appendable and a line feed character (`\n`) after it.

### 4. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue public inline fun StringBuilder.appendLine(): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L542)

Appends a line feed character (`\n`) to this StringBuilder.

### 5. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue public inline fun StringBuilder.appendLine(value: CharSequence?): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L547)

Appends `value` to this `StringBuilder`, followed by a line feed character (`\n`).

### 6. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue public inline fun StringBuilder.appendLine(value: String?): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L552)

Appends `value` to this `StringBuilder`, followed by a line feed character (`\n`).

### 7. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue public inline fun StringBuilder.appendLine(value: Any?): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L557)

Appends `value` to this `StringBuilder`, followed by a line feed character (`\n`).

### 8. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue public inline fun StringBuilder.appendLine(value: CharArray): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L562)

Appends `value` to this `StringBuilder`, followed by a line feed character (`\n`).

### 9. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue public inline fun StringBuilder.appendLine(value: Char): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L567)

Appends `value` to this `StringBuilder`, followed by a line feed character (`\n`).

### 10. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue public inline fun StringBuilder.appendLine(value: Boolean): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L572)

Appends `value` to this `StringBuilder`, followed by a line feed character (`\n`).

### 11. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.appendLine(value: Byte): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L577)

Appends `value` to this `StringBuilder`, followed by a line feed character (`\n`).

### 12. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.appendLine(value: Short): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L581)

Appends `value` to this `StringBuilder`, followed by a line feed character (`\n`).

### 13. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.appendLine(value: Int): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L585)

Appends `value` to this `StringBuilder`, followed by a line feed character (`\n`).

### 14. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.appendLine(value: Long): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L589)

Appends `value` to this `StringBuilder`, followed by a line feed character (`\n`).

### 15. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.appendLine(value: Float): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L593)

Appends `value` to this `StringBuilder`, followed by a line feed character (`\n`).

### 16. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.appendLine(value: Double): StringBuilder
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L597)

Appends `value` to this `StringBuilder`, followed by a line feed character (`\n`).

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.random.Random
import kotlin.test.*
import kotlin.text.*



fun main() {

        val stringBuilder = StringBuilder()
        stringBuilder.appendLine('c')
        stringBuilder.appendLine("string")
        stringBuilder.appendLine(true)
        stringBuilder.appendLine(charArrayOf('a', 'r', 'r', 'a', 'y'))
        stringBuilder.appendLine()
        stringBuilder.appendLine("char sequence" as CharSequence)
        stringBuilder.appendLine(null as Any?)
        stringBuilder.appendLine("nonnull" as Any?)
        stringBuilder.appendLine(null as String?)
        stringBuilder.appendLine(null as CharSequence?)

        val expected =
            """
            c
            string
            true
            array
            
            char sequence
            null
            nonnull
            null
            null
            
            """.trimIndent()

        println(stringBuilder.toString())
    
}
```

```text title="Output"
c
string
true
array

char sequence
null
nonnull
null
null
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/text/StringBuilderTest.kt#L551)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
