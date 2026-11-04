# associateByTo

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Populates and returns the `destination` mutable map with key-value pairs,
where key is provided by the `keySelector` function applied to each element of the given array
and value is the element itself.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByTo

## Declarations and overloads

### 1. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, K, M : MutableMap<in K, in T>> Array<out T>.associateByTo(destination: M, keySelector: (T) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10493)

### 2. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, in Byte>> ByteArray.associateByTo(destination: M, keySelector: (Byte) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10510)

### 3. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, in Short>> ShortArray.associateByTo(destination: M, keySelector: (Short) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10527)

### 4. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, in Int>> IntArray.associateByTo(destination: M, keySelector: (Int) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10544)

### 5. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, in Long>> LongArray.associateByTo(destination: M, keySelector: (Long) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10561)

### 6. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, in Float>> FloatArray.associateByTo(destination: M, keySelector: (Float) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10578)

### 7. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, in Double>> DoubleArray.associateByTo(destination: M, keySelector: (Double) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10595)

### 8. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, in Boolean>> BooleanArray.associateByTo(destination: M, keySelector: (Boolean) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10612)

### 9. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, in Char>> CharArray.associateByTo(destination: M, keySelector: (Char) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10629)

### 10. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, K, V, M : MutableMap<in K, in V>> Array<out T>.associateByTo(destination: M, keySelector: (T) -> K, valueTransform: (T) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10646)

Populates and returns the `destination` mutable map with key-value pairs,
where key is provided by the `keySelector` function and
and value is provided by the `valueTransform` function applied to elements of the given array.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByToWithValueTransform

### 11. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> ByteArray.associateByTo(destination: M, keySelector: (Byte) -> K, valueTransform: (Byte) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10663)

Populates and returns the `destination` mutable map with key-value pairs,
where key is provided by the `keySelector` function and
and value is provided by the `valueTransform` function applied to elements of the given array.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByToWithValueTransform

### 12. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> ShortArray.associateByTo(destination: M, keySelector: (Short) -> K, valueTransform: (Short) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10680)

Populates and returns the `destination` mutable map with key-value pairs,
where key is provided by the `keySelector` function and
and value is provided by the `valueTransform` function applied to elements of the given array.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByToWithValueTransform

### 13. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> IntArray.associateByTo(destination: M, keySelector: (Int) -> K, valueTransform: (Int) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10697)

Populates and returns the `destination` mutable map with key-value pairs,
where key is provided by the `keySelector` function and
and value is provided by the `valueTransform` function applied to elements of the given array.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByToWithValueTransform

### 14. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> LongArray.associateByTo(destination: M, keySelector: (Long) -> K, valueTransform: (Long) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10714)

Populates and returns the `destination` mutable map with key-value pairs,
where key is provided by the `keySelector` function and
and value is provided by the `valueTransform` function applied to elements of the given array.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByToWithValueTransform

### 15. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> FloatArray.associateByTo(destination: M, keySelector: (Float) -> K, valueTransform: (Float) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10731)

Populates and returns the `destination` mutable map with key-value pairs,
where key is provided by the `keySelector` function and
and value is provided by the `valueTransform` function applied to elements of the given array.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByToWithValueTransform

### 16. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> DoubleArray.associateByTo(destination: M, keySelector: (Double) -> K, valueTransform: (Double) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10748)

Populates and returns the `destination` mutable map with key-value pairs,
where key is provided by the `keySelector` function and
and value is provided by the `valueTransform` function applied to elements of the given array.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByToWithValueTransform

### 17. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> BooleanArray.associateByTo(destination: M, keySelector: (Boolean) -> K, valueTransform: (Boolean) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10765)

Populates and returns the `destination` mutable map with key-value pairs,
where key is provided by the `keySelector` function and
and value is provided by the `valueTransform` function applied to elements of the given array.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByToWithValueTransform

### 18. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> CharArray.associateByTo(destination: M, keySelector: (Char) -> K, valueTransform: (Char) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10782)

Populates and returns the `destination` mutable map with key-value pairs,
where key is provided by the `keySelector` function and
and value is provided by the `valueTransform` function applied to elements of the given array.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

@sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByToWithValueTransform

### 19. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, K, M : MutableMap<in K, in T>> Iterable<T>.associateByTo(destination: M, keySelector: (T) -> K): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1397)

Populates and returns the `destination` mutable map with key-value pairs,
where key is provided by the `keySelector` function applied to each element of the given collection
and value is the element itself.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

@sample samples.collections.Collections.Transformations.associateByTo

### 20. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, K, V, M : MutableMap<in K, in V>> Iterable<T>.associateByTo(destination: M, keySelector: (T) -> K, valueTransform: (T) -> V): M
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1414)

Populates and returns the `destination` mutable map with key-value pairs,
where key is provided by the `keySelector` function and
and value is provided by the `valueTransform` function applied to elements of the given collection.

If any two elements would have the same key returned by `keySelector` the last one gets added to the map.

@sample samples.collections.Collections.Transformations.associateByToWithValueTransform

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    data class Person(val firstName: String, val lastName: String) {
        override fun toString(): String = "$firstName $lastName"
    }

    val scientists = listOf(Person("Grace", "Hopper"), Person("Jacob", "Bernoulli"), Person("Johann", "Bernoulli"))

    val byLastName = mutableMapOf<String, Person>()
    println(byLastName.isEmpty())

    scientists.associateByTo(byLastName) { it.lastName }

    println(byLastName.isNotEmpty())
    // Jacob Bernoulli does not occur in the map because only the last pair with the same key gets added
    println(byLastName)
}
```

```text title="Output"
true
true
{Hopper=Grace Hopper, Bernoulli=Johann Bernoulli}
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L744)

### Example 2 · JVM

```kotlin title="Example 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    data class Person(val firstName: String, val lastName: String)

    val scientists = listOf(Person("Grace", "Hopper"), Person("Jacob", "Bernoulli"), Person("Johann", "Bernoulli"))

    val byLastName = mutableMapOf<String, String>()
    println(byLastName.isEmpty())

    scientists.associateByTo(byLastName, { it.lastName }, { it.firstName} )

    println(byLastName.isNotEmpty())
    // Jacob Bernoulli does not occur in the map because only the last pair with the same key gets added
    println(byLastName)
}
```

```text title="Output"
true
true
{Hopper=Grace, Bernoulli=Johann}
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L762)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
