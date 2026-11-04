# contentToString

`kotlin.collections` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns a string representation of the contents of the specified array as if it is `List`.

@sample samples.collections.Arrays.ContentOperations.contentToString

## Declarations and overloads

### 1. Common

```kotlin
@SinceKotlin("1.4")
public expect fun <T> Array<out T>?.contentToString(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8424)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public expect fun ByteArray?.contentToString(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8432)

### 3. Common

```kotlin
@SinceKotlin("1.4")
public expect fun ShortArray?.contentToString(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8440)

### 4. Common

```kotlin
@SinceKotlin("1.4")
public expect fun IntArray?.contentToString(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8448)

### 5. Common

```kotlin
@SinceKotlin("1.4")
public expect fun LongArray?.contentToString(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8456)

### 6. Common

```kotlin
@SinceKotlin("1.4")
public expect fun FloatArray?.contentToString(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8464)

### 7. Common

```kotlin
@SinceKotlin("1.4")
public expect fun DoubleArray?.contentToString(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8472)

### 8. Common

```kotlin
@SinceKotlin("1.4")
public expect fun BooleanArray?.contentToString(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8480)

### 9. Common

```kotlin
@SinceKotlin("1.4")
public expect fun CharArray?.contentToString(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8488)

### 10. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UIntArray?.contentToString(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3999)

### 11. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun ULongArray?.contentToString(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4010)

### 12. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UByteArray?.contentToString(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4021)

### 13. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UShortArray?.contentToString(): String
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4032)

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
    val result = source.`contentToString`()
    println(result)
}
```

```text title="Output"
[1, 2, 3]
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
