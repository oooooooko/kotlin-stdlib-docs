# sumBy

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the sum of all values produced by `selector` function applied to each element in the array.

## Declarations and overloads

### 1. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun <T> Array<out T>.sumBy(selector: (T) -> Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L25342)

### 2. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun ByteArray.sumBy(selector: (Byte) -> Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L25355)

### 3. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun ShortArray.sumBy(selector: (Short) -> Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L25368)

### 4. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun IntArray.sumBy(selector: (Int) -> Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L25381)

### 5. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun LongArray.sumBy(selector: (Long) -> Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L25394)

### 6. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun FloatArray.sumBy(selector: (Float) -> Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L25407)

### 7. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun DoubleArray.sumBy(selector: (Double) -> Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L25420)

### 8. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun BooleanArray.sumBy(selector: (Boolean) -> Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L25433)

### 9. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun CharArray.sumBy(selector: (Char) -> Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L25446)

### 10. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public inline fun <T> Iterable<T>.sumBy(selector: (T) -> Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3417)

Returns the sum of all values produced by `selector` function applied to each element in the collection.

### 11. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.sumBy(selector: (UInt) -> UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11283)

### 12. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.sumBy(selector: (ULong) -> UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11299)

### 13. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.sumBy(selector: (UByte) -> UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11315)

### 14. Common

```kotlin
@Deprecated("Use sumOf instead.", ReplaceWith("this.sumOf(selector)"))
@DeprecatedSinceKotlin(warningSince = "1.5")
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.sumBy(selector: (UShort) -> UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L11331)

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
    val result = source.`sumBy`({ it.toString().length })
    println(result)
}
```

```text title="Output"
3
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
