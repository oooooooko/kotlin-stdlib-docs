# count

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the number of elements in this array.

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Array<out T>.count(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15393)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun ByteArray.count(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15401)

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun ShortArray.count(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15409)

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun IntArray.count(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15417)

### 5. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun LongArray.count(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15425)

### 6. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun FloatArray.count(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15433)

### 7. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun DoubleArray.count(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15441)

### 8. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun BooleanArray.count(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15449)

### 9. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharArray.count(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15457)

### 10. Common

```kotlin
public inline fun <T> Array<out T>.count(predicate: (T) -> Boolean): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15465)

Returns the number of elements matching the given `predicate`.

### 11. Common

```kotlin
public inline fun ByteArray.count(predicate: (Byte) -> Boolean): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15474)

Returns the number of elements matching the given `predicate`.

### 12. Common

```kotlin
public inline fun ShortArray.count(predicate: (Short) -> Boolean): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15483)

Returns the number of elements matching the given `predicate`.

### 13. Common

```kotlin
public inline fun IntArray.count(predicate: (Int) -> Boolean): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15492)

Returns the number of elements matching the given `predicate`.

### 14. Common

```kotlin
public inline fun LongArray.count(predicate: (Long) -> Boolean): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15501)

Returns the number of elements matching the given `predicate`.

### 15. Common

```kotlin
public inline fun FloatArray.count(predicate: (Float) -> Boolean): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15510)

Returns the number of elements matching the given `predicate`.

### 16. Common

```kotlin
public inline fun DoubleArray.count(predicate: (Double) -> Boolean): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15519)

Returns the number of elements matching the given `predicate`.

### 17. Common

```kotlin
public inline fun BooleanArray.count(predicate: (Boolean) -> Boolean): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15528)

Returns the number of elements matching the given `predicate`.

### 18. Common

```kotlin
public inline fun CharArray.count(predicate: (Char) -> Boolean): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15537)

Returns the number of elements matching the given `predicate`.

### 19. Common

```kotlin
public fun <T> Iterable<T>.count(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2096)

Returns the number of elements in this collection.

### 20. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Collection<T>.count(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2106)

Returns the number of elements in this collection.

### 21. Common

```kotlin
public inline fun <T> Iterable<T>.count(predicate: (T) -> Boolean): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2114)

Returns the number of elements matching the given `predicate`.

### 22. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <K, V> Map<out K, V>.count(): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L198)

Returns the number of entries in this map.

### 23. Common

```kotlin
public inline fun <K, V> Map<out K, V>.count(predicate: (Map.Entry<K, V>) -> Boolean): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L206)

Returns the number of entries matching the given `predicate`.

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.count(predicate: (UInt) -> Boolean): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6571)

Returns the number of elements matching the given `predicate`.

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.count(predicate: (ULong) -> Boolean): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6583)

Returns the number of elements matching the given `predicate`.

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.count(predicate: (UByte) -> Boolean): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6595)

Returns the number of elements matching the given `predicate`.

### 27. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.count(predicate: (UShort) -> Boolean): Int
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6607)

Returns the number of elements matching the given `predicate`.

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
    val result = source.`count`()
    println(result)
}
```

```text title="Output"
3
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
