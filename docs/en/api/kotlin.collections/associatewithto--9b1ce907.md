# associateWithTo

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Populates and returns the `destination` mutable map with key-value pairs for each element of the given array,
where key is the element itself and value is provided by the `valueSelector` function applied to that key.

If any two elements are equal, the last one overwrites the former value in the map.

@sample samples.collections.Collections.Transformations.associateWithTo

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> Array<out K>.associateWithTo(destination: M, valueSelector: (K) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11095)

### 2. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in Byte, in V>> ByteArray.associateWithTo(destination: M, valueSelector: (Byte) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11112)

### 3. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in Short, in V>> ShortArray.associateWithTo(destination: M, valueSelector: (Short) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11130)

### 4. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in Int, in V>> IntArray.associateWithTo(destination: M, valueSelector: (Int) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11148)

### 5. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in Long, in V>> LongArray.associateWithTo(destination: M, valueSelector: (Long) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11166)

### 6. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in Float, in V>> FloatArray.associateWithTo(destination: M, valueSelector: (Float) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11184)

### 7. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in Double, in V>> DoubleArray.associateWithTo(destination: M, valueSelector: (Double) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11202)

### 8. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in Boolean, in V>> BooleanArray.associateWithTo(destination: M, valueSelector: (Boolean) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11220)

### 9. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in Char, in V>> CharArray.associateWithTo(destination: M, valueSelector: (Char) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11238)

### 10. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> Iterable<K>.associateWithTo(destination: M, valueSelector: (K) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1463)

Populates and returns the `destination` mutable map with key-value pairs for each element of the given collection,
where key is the element itself and value is provided by the `valueSelector` function applied to that key.

If any two elements are equal, the last one overwrites the former value in the map.

@sample samples.collections.Collections.Transformations.associateWithTo

### 11. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in UInt, in V>> UIntArray.associateWithTo(destination: M, valueSelector: (UInt) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5091)

### 12. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in ULong, in V>> ULongArray.associateWithTo(destination: M, valueSelector: (ULong) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5110)

### 13. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in UByte, in V>> UByteArray.associateWithTo(destination: M, valueSelector: (UByte) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5129)

### 14. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in UShort, in V>> UShortArray.associateWithTo(destination: M, valueSelector: (UShort) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5148)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    data class Person(val firstName: String, val lastName: String) {
        override fun toString(): String = "$firstName $lastName"
    }

    val scientists = listOf(Person("Grace", "Hopper"), Person("Jacob", "Bernoulli"), Person("Jacob", "Bernoulli"))
    val withLengthOfNames = mutableMapOf<Person, Int>()
    println(withLengthOfNames.isEmpty())

    scientists.associateWithTo(withLengthOfNames) { it.firstName.length + it.lastName.length }

    println(withLengthOfNames.isNotEmpty())
    // Jacob Bernoulli only occurs once in the map because only the last pair with the same key gets added
    println(withLengthOfNames)
}
```

```text title="Output"
true
true
{Grace Hopper=11, Jacob Bernoulli=14}
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L802)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
