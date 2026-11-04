# until

`kotlin.ranges` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a range from this value up to but excluding the specified `to` value.

If the `to` value is less than or equal to `this` value, then the returned range is empty.

## Declarations and overloads

### 1. Common

```kotlin
public infix fun Int.until(to: Byte): IntRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1078)

### 2. Common

```kotlin
public infix fun Long.until(to: Byte): LongRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1087)

### 3. Common

```kotlin
public infix fun Byte.until(to: Byte): IntRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1096)

### 4. Common

```kotlin
public infix fun Short.until(to: Byte): IntRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1105)

### 5. Common

```kotlin
public infix fun Char.until(to: Char): CharRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1114)

### 6. Common

```kotlin
public infix fun Int.until(to: Int): IntRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1124)

### 7. Common

```kotlin
public infix fun Long.until(to: Int): LongRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1134)

### 8. Common

```kotlin
public infix fun Byte.until(to: Int): IntRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1143)

### 9. Common

```kotlin
public infix fun Short.until(to: Int): IntRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1153)

### 10. Common

```kotlin
public infix fun Int.until(to: Long): LongRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1163)

### 11. Common

```kotlin
public infix fun Long.until(to: Long): LongRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1173)

### 12. Common

```kotlin
public infix fun Byte.until(to: Long): LongRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1183)

### 13. Common

```kotlin
public infix fun Short.until(to: Long): LongRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1193)

### 14. Common

```kotlin
public infix fun Int.until(to: Short): IntRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1203)

### 15. Common

```kotlin
public infix fun Long.until(to: Short): LongRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1212)

### 16. Common

```kotlin
public infix fun Byte.until(to: Short): IntRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1221)

### 17. Common

```kotlin
public infix fun Short.until(to: Short): IntRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1230)

### 18. Common

```kotlin
@SinceKotlin("1.5")
public infix fun UByte.until(to: UByte): UIntRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L356)

### 19. Common

```kotlin
@SinceKotlin("1.5")
public infix fun UInt.until(to: UInt): UIntRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L367)

### 20. Common

```kotlin
@SinceKotlin("1.5")
public infix fun ULong.until(to: ULong): ULongRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L378)

### 21. Common

```kotlin
@SinceKotlin("1.5")
public infix fun UShort.until(to: UShort): UIntRange
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L389)

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
import kotlin.ranges.*

fun main() {
    val source = 5
    val result = source.`until`(2.toByte())
    println(result)
}
```

```text title="Output"
5..1
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
