# step

`kotlin.ranges` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a progression that goes over the same range with the given step.

@sample samples.ranges.Ranges.stepInt

## Declarations and overloads

### 1. Common

```kotlin
public infix fun IntProgression.step(step: Int): IntProgression
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L992)

### 2. Common

```kotlin
public infix fun LongProgression.step(step: Long): LongProgression
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1002)

Returns a progression that goes over the same range with the given step.

@sample samples.ranges.Ranges.stepLong

### 3. Common

```kotlin
public infix fun CharProgression.step(step: Int): CharProgression
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1012)

Returns a progression that goes over the same range with the given step.

@sample samples.ranges.Ranges.stepChar

### 4. Common

```kotlin
@SinceKotlin("1.5")
public infix fun UIntProgression.step(step: Int): UIntProgression
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L334)

Returns a progression that goes over the same range with the given step.

@sample samples.ranges.Ranges.stepUInt

### 5. Common

```kotlin
@SinceKotlin("1.5")
public infix fun ULongProgression.step(step: Long): ULongProgression
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L345)

Returns a progression that goes over the same range with the given step.

@sample samples.ranges.Ranges.stepULong

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val ascendingProgression = 1..6 step 2
    val descendingProgression = 6 downTo 1 step 2
    println(ascendingProgression.toList())
    println(descendingProgression.toList())
}
```

```text title="Output"
[1, 3, 5]
[6, 4, 2]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L86)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val ascendingProgression = 1L..6L step 2L
    val descendingProgression = 6L downTo 1L step 2L
    println(ascendingProgression.toList())
    println(descendingProgression.toList())
}
```

```text title="Output"
[1, 3, 5]
[6, 4, 2]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L102)

### Example 3 · JVM

```kotlin title="Example 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val ascendingProgression = 'a'..'f' step 2
    val descendingProgression = 'f' downTo 'a' step 2
    println(ascendingProgression.toList())
    println(descendingProgression.toList())
}
```

```text title="Output"
[a, c, e]
[f, d, b]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L118)

### Example 4 · JVM

```kotlin title="Example 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val ascendingProgression = 1u..6u step 2
    val descendingProgression = 6u downTo 1u step 2
    println(ascendingProgression.toList())
    println(descendingProgression.toList())
}
```

```text title="Output"
[1, 3, 5]
[6, 4, 2]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L94)

### Example 5 · JVM

```kotlin title="Example 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val ascendingProgression = 1UL..6UL step 2L
    val descendingProgression = 6UL downTo 1UL step 2L
    println(ascendingProgression.toList())
    println(descendingProgression.toList())
}
```

```text title="Output"
[1, 3, 5]
[6, 4, 2]
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L110)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
