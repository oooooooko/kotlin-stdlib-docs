# fill

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Fills this array or its subrange with the specified `element` value.

@param fromIndex the start of the range (inclusive) to fill, 0 by default.
@param toIndex the end of the range (exclusive) to fill, size of this array by default.

@throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
@throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.3")
public expect fun <T> Array<T>.fill(element: T, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9180)

### 2. Common

```kotlin
@SinceKotlin("1.3")
public expect fun ByteArray.fill(element: Byte, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9192)

### 3. Common

```kotlin
@SinceKotlin("1.3")
public expect fun ShortArray.fill(element: Short, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9204)

### 4. Common

```kotlin
@SinceKotlin("1.3")
public expect fun IntArray.fill(element: Int, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9216)

### 5. Common

```kotlin
@SinceKotlin("1.3")
public expect fun LongArray.fill(element: Long, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9228)

### 6. Common

```kotlin
@SinceKotlin("1.3")
public expect fun FloatArray.fill(element: Float, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9240)

### 7. Common

```kotlin
@SinceKotlin("1.3")
public expect fun DoubleArray.fill(element: Double, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9252)

### 8. Common

```kotlin
@SinceKotlin("1.3")
public expect fun BooleanArray.fill(element: Boolean, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9264)

### 9. Common

```kotlin
@SinceKotlin("1.3")
public expect fun CharArray.fill(element: Char, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9276)

### 10. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.fill(element: UInt, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4423)

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.fill(element: ULong, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4438)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.fill(element: UByte, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4453)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.fill(element: UShort, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4468)

### 14. Common

```kotlin
@SinceKotlin("1.2")
public expect fun <T> MutableList<T>.fill(value: T): Unit
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/CollectionsH.kt#L28)

Fills the list with the provided `value`.

Each element in the list gets replaced with the `value`.

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
    val result = source.`fill`(1)
    println(result)
}
```

```text title="Output"
kotlin.Unit
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
