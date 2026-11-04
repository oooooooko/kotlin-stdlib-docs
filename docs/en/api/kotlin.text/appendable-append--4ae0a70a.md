# Appendable.append

`kotlin.text` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Appends the specified character `value` to this Appendable and returns this instance.

@param value the character to append.

## Declarations and overloads

### 1. Common

```kotlin
@IgnorableReturnValue
    public fun append(value: Char): Appendable
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Appendable.kt#L15)

### 2. Common

```kotlin
@IgnorableReturnValue
    public fun append(value: CharSequence?): Appendable
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Appendable.kt#L23)

Appends the specified character sequence `value` to this Appendable and returns this instance.

@param value the character sequence to append. If `value` is `null`, then the four characters `"null"` are appended to this Appendable.

### 3. Common

```kotlin
@IgnorableReturnValue
    public fun append(value: CharSequence?, startIndex: Int, endIndex: Int): Appendable
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Appendable.kt#L31)

Appends a subsequence of the specified character sequence `value` to this Appendable and returns this instance.

@param value the character sequence from which a subsequence is appended. If `value` is `null`,
 then characters are appended as if `value` contained the four characters `"null"`.
@param startIndex the beginning (inclusive) of the subsequence to append.
@param endIndex the end (exclusive) of the subsequence to append.

@throws IndexOutOfBoundsException or `IllegalArgumentException` when `startIndex` or `endIndex` is out of range of the `value` character sequence indices or when `startIndex > endIndex`.

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.random.Random
import kotlin.test.*
import kotlin.text.*



fun main() {

        StringBuilder("my trimToSize test").let { sb ->
            println(sb.length)
//            assertTrue(sb.capacity() >= sb.length)
            sb.append('1')
            sb.trimToSize()
            println(sb.length)
//            assertTrue(sb.capacity() >= sb.length)
        }
    
}
```

```text title="Output"
18
19
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/text/StringBuilderTest.kt#L482)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
