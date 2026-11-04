# sortedArray

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns an array with all elements of this array sorted according to their natural sort order.

Use `sorted` if you need to get the result in a list.

The sort is _stable_. It means that equal elements preserve their order relative to each other after sorting.

## Declarations and overloads

### 1. Common

```kotlin
public fun <T : Comparable<T>> Array<T>.sortedArray(): Array<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7566)

### 2. Common

```kotlin
public fun ByteArray.sortedArray(): ByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7578)

Returns an array with all elements of this array sorted according to their natural sort order.

Use `sorted` if you need to get the result in a list.

### 3. Common

```kotlin
public fun ShortArray.sortedArray(): ShortArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7588)

Returns an array with all elements of this array sorted according to their natural sort order.

Use `sorted` if you need to get the result in a list.

### 4. Common

```kotlin
public fun IntArray.sortedArray(): IntArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7598)

Returns an array with all elements of this array sorted according to their natural sort order.

Use `sorted` if you need to get the result in a list.

### 5. Common

```kotlin
public fun LongArray.sortedArray(): LongArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7608)

Returns an array with all elements of this array sorted according to their natural sort order.

Use `sorted` if you need to get the result in a list.

### 6. Common

```kotlin
public fun FloatArray.sortedArray(): FloatArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7618)

Returns an array with all elements of this array sorted according to their natural sort order.

Use `sorted` if you need to get the result in a list.

### 7. Common

```kotlin
public fun DoubleArray.sortedArray(): DoubleArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7628)

Returns an array with all elements of this array sorted according to their natural sort order.

Use `sorted` if you need to get the result in a list.

### 8. Common

```kotlin
public fun CharArray.sortedArray(): CharArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7638)

Returns an array with all elements of this array sorted according to their natural sort order.

Use `sorted` if you need to get the result in a list.

### 9. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.sortedArray(): UIntArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3635)

Returns an array with all elements of this array sorted according to their natural sort order.

Use `sorted` if you need to get the result in a list.

### 10. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.sortedArray(): ULongArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3647)

Returns an array with all elements of this array sorted according to their natural sort order.

Use `sorted` if you need to get the result in a list.

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.sortedArray(): UByteArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3659)

Returns an array with all elements of this array sorted according to their natural sort order.

Use `sorted` if you need to get the result in a list.

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.sortedArray(): UShortArray
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3671)

Returns an array with all elements of this array sorted according to their natural sort order.

Use `sorted` if you need to get the result in a list.

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
    val result = source.`sortedArray`()
    println(result.contentToString())
}
```

```text title="Output"
[1, 2, 3]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
