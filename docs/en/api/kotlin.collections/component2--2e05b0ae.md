# component2

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns 2nd *element* from the array.

If the size of this array is less than 2, throws an `IndexOutOfBoundsException` except in Kotlin/JS
where the behavior is unspecified, and in Kotlin/Wasm where
a [trap](https://webassembly.github.io/spec/core/intro/overview.html#trap) will be raised instead,
unless `-Xwasm-enable-array-range-checks` compiler flag was specified when linking an executable.

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun <T> Array<out T>.component2(): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L139)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun ByteArray.component2(): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L152)

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun ShortArray.component2(): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L165)

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun IntArray.component2(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L178)

### 5. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun LongArray.component2(): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L191)

### 6. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun FloatArray.component2(): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L204)

### 7. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun DoubleArray.component2(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L217)

### 8. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun BooleanArray.component2(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L230)

### 9. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun CharArray.component2(): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L243)

### 10. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun <T> List<T>.component2(): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L32)

Returns 2nd *element* from the list.

Throws an `IndexOutOfBoundsException` if the size of this list is less than 2.

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline operator fun UIntArray.component2(): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L83)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline operator fun ULongArray.component2(): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L98)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline operator fun UByteArray.component2(): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L113)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline operator fun UShortArray.component2(): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L128)

### 15. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun <K, V> Map.Entry<K, V>.component2(): V
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L314)

Returns the value component of the map entry.

This method allows to use destructuring declarations when working with maps, for example:
```
for ((key, value) in map) {
    // do something with the key and the value
}
```

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
    val result = source.`component2`()
    println(result)
}
```

```text title="Output"
2
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
