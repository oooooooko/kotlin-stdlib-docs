# lastIndex

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the last valid index for the array.

## Declarations and overloads

### 1. Common

```kotlin
public val <T> Array<out T>.lastIndex: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9486)

### 2. Common

```kotlin
public val ByteArray.lastIndex: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9492)

### 3. Common

```kotlin
public val ShortArray.lastIndex: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9498)

### 4. Common

```kotlin
public val IntArray.lastIndex: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9504)

### 5. Common

```kotlin
public val LongArray.lastIndex: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9510)

### 6. Common

```kotlin
public val FloatArray.lastIndex: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9516)

### 7. Common

```kotlin
public val DoubleArray.lastIndex: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9522)

### 8. Common

```kotlin
public val BooleanArray.lastIndex: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9528)

### 9. Common

```kotlin
public val CharArray.lastIndex: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9534)

### 10. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public inline val UIntArray.lastIndex: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4515)

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public inline val ULongArray.lastIndex: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4523)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public inline val UByteArray.lastIndex: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4531)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public inline val UShortArray.lastIndex: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4539)

### 14. Common

```kotlin
public val <T> List<T>.lastIndex: Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L231)

Returns the index of the last item in the list or -1 if the list is empty.

@sample samples.collections.Collections.Lists.lastIndexOfList

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    println(emptyList<Any>().lastIndex)
    val list = listOf("a", "x", "y")
    println(list.lastIndex)
    println(list[list.lastIndex])
}
```

```text title="Output"
-1
2
y
```

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L242)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
