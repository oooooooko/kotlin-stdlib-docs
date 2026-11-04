# component5

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns 5th *element* from the array.

If the size of this array is less than 5, throws an `IndexOutOfBoundsException` except in Kotlin/JS
where the behavior is unspecified, and in Kotlin/Wasm where
a [trap](https://webassembly.github.io/spec/core/intro/overview.html#trap) will be raised instead,
unless `-Xwasm-enable-array-range-checks` compiler flag was specified when linking an executable.

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun <T> Array<out T>.component5(): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L490)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun ByteArray.component5(): Byte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L503)

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun ShortArray.component5(): Short
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L516)

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun IntArray.component5(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L529)

### 5. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun LongArray.component5(): Long
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L542)

### 6. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun FloatArray.component5(): Float
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L555)

### 7. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun DoubleArray.component5(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L568)

### 8. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun BooleanArray.component5(): Boolean
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L581)

### 9. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun CharArray.component5(): Char
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L594)

### 10. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun <T> List<T>.component5(): T
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L62)

Returns 5th *element* from the list.

Throws an `IndexOutOfBoundsException` if the size of this list is less than 5.

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline operator fun UIntArray.component5(): UInt
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L263)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline operator fun ULongArray.component5(): ULong
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L278)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline operator fun UByteArray.component5(): UByte
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L293)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline operator fun UShortArray.component5(): UShort
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L308)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import java.math.BigInteger
import java.math.BigDecimal
import kotlin.test.*
import java.math.MathContext
import java.math.RoundingMode



fun main() {

        val (d1, d2, d3, d4, d5) = (1..5).map { BigDecimal(it.toString()) }
        val d7 = BigDecimal("7")

        println(d2 / d3)
        println(d3 / d2)
        println(d5 / d2)
        println(d7 / d2)
        println(d7 / d5)
    
}
```

```text title="Output"
1
2
2
4
1
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/jvm/test/numbers/BigNumbersTest.kt#L128)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
