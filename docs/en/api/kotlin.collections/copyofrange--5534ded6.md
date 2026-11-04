# copyOfRange

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a new array which is a copy of the specified range of the original array.

@param fromIndex the start of the range (inclusive) to copy.
@param toIndex the end of the range (exclusive) to copy.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

## Declarations and overloads

### 1. Common

```kotlin
public expect fun <T> Array<T>.copyOfRange(fromIndex: Int, toIndex: Int): Array<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9081)

### 2. Common

```kotlin
public expect fun ByteArray.copyOfRange(fromIndex: Int, toIndex: Int): ByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9092)

### 3. Common

```kotlin
public expect fun ShortArray.copyOfRange(fromIndex: Int, toIndex: Int): ShortArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9103)

### 4. Common

```kotlin
public expect fun IntArray.copyOfRange(fromIndex: Int, toIndex: Int): IntArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9114)

### 5. Common

```kotlin
public expect fun LongArray.copyOfRange(fromIndex: Int, toIndex: Int): LongArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9125)

### 6. Common

```kotlin
public expect fun FloatArray.copyOfRange(fromIndex: Int, toIndex: Int): FloatArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9136)

### 7. Common

```kotlin
public expect fun DoubleArray.copyOfRange(fromIndex: Int, toIndex: Int): DoubleArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9147)

### 8. Common

```kotlin
public expect fun BooleanArray.copyOfRange(fromIndex: Int, toIndex: Int): BooleanArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9158)

### 9. Common

```kotlin
public expect fun CharArray.copyOfRange(fromIndex: Int, toIndex: Int): CharArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9169)

### 10. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.copyOfRange(fromIndex: Int, toIndex: Int): UIntArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4359)

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.copyOfRange(fromIndex: Int, toIndex: Int): ULongArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4375)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.copyOfRange(fromIndex: Int, toIndex: Int): UByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4391)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.copyOfRange(fromIndex: Int, toIndex: Int): UShortArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4407)

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
    val result = source.`copyOfRange`(0, 2)
    println(result.contentToString())
}
```

```text title="Output"
[1, 2]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
