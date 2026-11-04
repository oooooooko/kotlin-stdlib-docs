# average

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns an average value of elements in the array.

## Declarations and overloads

### 1. Common

```kotlin
@kotlin.jvm.JvmName("averageOfByte")
public fun Array<out Byte>.average(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27702)

### 2. Common

```kotlin
@kotlin.jvm.JvmName("averageOfShort")
public fun Array<out Short>.average(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27716)

### 3. Common

```kotlin
@kotlin.jvm.JvmName("averageOfInt")
public fun Array<out Int>.average(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27730)

### 4. Common

```kotlin
@kotlin.jvm.JvmName("averageOfLong")
public fun Array<out Long>.average(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27744)

### 5. Common

```kotlin
@kotlin.jvm.JvmName("averageOfFloat")
public fun Array<out Float>.average(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27758)

### 6. Common

```kotlin
@kotlin.jvm.JvmName("averageOfDouble")
public fun Array<out Double>.average(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27772)

### 7. Common

```kotlin
public fun ByteArray.average(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27786)

### 8. Common

```kotlin
public fun ShortArray.average(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27799)

### 9. Common

```kotlin
public fun IntArray.average(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27812)

### 10. Common

```kotlin
public fun LongArray.average(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27825)

### 11. Common

```kotlin
public fun FloatArray.average(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27838)

### 12. Common

```kotlin
public fun DoubleArray.average(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27851)

### 13. Common

```kotlin
@kotlin.jvm.JvmName("averageOfByte")
public fun Iterable<Byte>.average(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3975)

Returns an average value of elements in the collection.

### 14. Common

```kotlin
@kotlin.jvm.JvmName("averageOfShort")
public fun Iterable<Short>.average(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3989)

Returns an average value of elements in the collection.

### 15. Common

```kotlin
@kotlin.jvm.JvmName("averageOfInt")
public fun Iterable<Int>.average(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L4003)

Returns an average value of elements in the collection.

### 16. Common

```kotlin
@kotlin.jvm.JvmName("averageOfLong")
public fun Iterable<Long>.average(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L4017)

Returns an average value of elements in the collection.

### 17. Common

```kotlin
@kotlin.jvm.JvmName("averageOfFloat")
public fun Iterable<Float>.average(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L4031)

Returns an average value of elements in the collection.

### 18. Common

```kotlin
@kotlin.jvm.JvmName("averageOfDouble")
public fun Iterable<Double>.average(): Double
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L4045)

Returns an average value of elements in the collection.

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
    val result = source.`average`()
    println(result)
}
```

```text title="Output"
2.0
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
