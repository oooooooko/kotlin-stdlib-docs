# elementAtOrElse

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns an element at the given `index` or the result of calling the `defaultValue` function if the `index` is out of bounds of this array.

@sample samples.collections.Collections.Elements.elementAtOrElse

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Array<out T>.elementAtOrElse(index: Int, defaultValue: (Int) -> T): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L737)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun ByteArray.elementAtOrElse(index: Int, defaultValue: (Int) -> Byte): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L750)

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun ShortArray.elementAtOrElse(index: Int, defaultValue: (Int) -> Short): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L763)

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun IntArray.elementAtOrElse(index: Int, defaultValue: (Int) -> Int): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L776)

### 5. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun LongArray.elementAtOrElse(index: Int, defaultValue: (Int) -> Long): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L789)

### 6. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun FloatArray.elementAtOrElse(index: Int, defaultValue: (Int) -> Float): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L802)

### 7. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun DoubleArray.elementAtOrElse(index: Int, defaultValue: (Int) -> Double): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L815)

### 8. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun BooleanArray.elementAtOrElse(index: Int, defaultValue: (Int) -> Boolean): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L828)

### 9. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharArray.elementAtOrElse(index: Int, defaultValue: (Int) -> Char): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L841)

### 10. Common

```kotlin
public fun <T> Iterable<T>.elementAtOrElse(index: Int, defaultValue: (Int) -> T): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L102)

Returns an element at the given `index` or the result of calling the `defaultValue` function if the `index` is out of bounds of this collection.

@sample samples.collections.Collections.Elements.elementAtOrElse

### 11. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> List<T>.elementAtOrElse(index: Int, defaultValue: (Int) -> T): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L125)

Returns an element at the given `index` or the result of calling the `defaultValue` function if the `index` is out of bounds of this list.

@sample samples.collections.Collections.Elements.elementAtOrElse

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.elementAtOrElse(index: Int, defaultValue: (Int) -> UInt): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L359)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.elementAtOrElse(index: Int, defaultValue: (Int) -> ULong): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L374)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.elementAtOrElse(index: Int, defaultValue: (Int) -> UByte): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L389)

### 15. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.elementAtOrElse(index: Int, defaultValue: (Int) -> UShort): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L404)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = listOf(1, 2, 3)
    println(list.elementAtOrElse(0) { 42 })
    println(list.elementAtOrElse(2) { 42 })
    println(list.elementAtOrElse(3) { 42 })

    val emptyList = emptyList<Int>()
    println(emptyList.elementAtOrElse(0) { "no int" })
}
```

```text title="Output"
1
3
42
no int
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1324)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
