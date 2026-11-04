# toTypedArray

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a *typed* object array containing all of the elements of this primitive array.

## Declarations and overloads

### 1. Common

```kotlin
public expect fun ByteArray.toTypedArray(): Array<Byte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10057)

### 2. Common

```kotlin
public expect fun ShortArray.toTypedArray(): Array<Short>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10062)

### 3. Common

```kotlin
public expect fun IntArray.toTypedArray(): Array<Int>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10067)

### 4. Common

```kotlin
public expect fun LongArray.toTypedArray(): Array<Long>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10072)

### 5. Common

```kotlin
public expect fun FloatArray.toTypedArray(): Array<Float>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10077)

### 6. Common

```kotlin
public expect fun DoubleArray.toTypedArray(): Array<Double>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10082)

### 7. Common

```kotlin
public expect fun BooleanArray.toTypedArray(): Array<Boolean>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10087)

### 8. Common

```kotlin
public expect fun CharArray.toTypedArray(): Array<Char>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10092)

### 9. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.toTypedArray(): Array<UInt>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4903)

### 10. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.toTypedArray(): Array<ULong>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4912)

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.toTypedArray(): Array<UByte>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4921)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.toTypedArray(): Array<UShort>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4930)

### 13. Common

```kotlin
public expect inline fun <reified T> Collection<T>.toTypedArray(): Array<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/CollectionsH.kt#L19)

Returns a *typed* array containing all the elements of this collection.

Allocates an array of runtime type `T` having its size equal to the size of this collection
and populates the array with the elements of this collection.
@sample samples.collections.Collections.Collections.collectionToTypedArray

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val collection = listOf(1, 2, 3)
    val array = collection.toTypedArray()
    println(array.contentToString())
}
```

```text title="Output"
[1, 2, 3]
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L81)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
