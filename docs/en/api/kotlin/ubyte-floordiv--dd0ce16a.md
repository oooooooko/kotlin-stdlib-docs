# UByte.floorDiv

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Divides this value by the other value, flooring the result to an integer that is closer to negative infinity.

For unsigned types, the results of flooring division and truncating division are the same.
@sample samples.misc.Builtins.floorDivUnsigned

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
    @kotlin.internal.IntrinsicConstEvaluation
    public inline fun floorDiv(other: UByte): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UByte.kt#L178)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
    @kotlin.internal.IntrinsicConstEvaluation
    public inline fun floorDiv(other: UShort): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UByte.kt#L187)

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
    @kotlin.internal.IntrinsicConstEvaluation
    public inline fun floorDiv(other: UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UByte.kt#L196)

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
    @kotlin.internal.IntrinsicConstEvaluation
    public inline fun floorDiv(other: ULong): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UByte.kt#L205)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.assertFailsWith



fun main() {
    // Unsigned types have no negative values, so floorDiv produces the
    // same result as the / operator
    println(7u.floorDiv(3u))
    println(7u / 3u)

    // Dividing by zero throws
    assertFailsWith<ArithmeticException> { 1u.floorDiv(0u) }
}
```

```text title="Output"
2
2
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/builtins.kt#L98)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
