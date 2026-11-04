# singleOrNull

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回单元素,如果数组为空或有多个元素,则返回 `null` 。

??? note "查看英文原文"

    Returns single element, or `null` if the array is empty or has more than one element.

## 声明与重载

### 1. Common

```kotlin
public fun <T> Array<out T>.singleOrNull(): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3212)

### 2. Common

```kotlin
public fun ByteArray.singleOrNull(): Byte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3219)

### 3. Common

```kotlin
public fun ShortArray.singleOrNull(): Short?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3226)

### 4. Common

```kotlin
public fun IntArray.singleOrNull(): Int?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3233)

### 5. Common

```kotlin
public fun LongArray.singleOrNull(): Long?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3240)

### 6. Common

```kotlin
public fun FloatArray.singleOrNull(): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3247)

### 7. Common

```kotlin
public fun DoubleArray.singleOrNull(): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3254)

### 8. Common

```kotlin
public fun BooleanArray.singleOrNull(): Boolean?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3261)

### 9. Common

```kotlin
public fun CharArray.singleOrNull(): Char?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3268)

### 10. Common

```kotlin
public inline fun <T> Array<out T>.singleOrNull(predicate: (T) -> Boolean): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3275)

返回与给定 `predicate` 匹配的单元素,如果找不到元素或发现不止一个元素,则返回`null`。

### 11. Common

```kotlin
public inline fun ByteArray.singleOrNull(predicate: (Byte) -> Boolean): Byte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3292)

返回与给定 `predicate` 匹配的单元素,如果找不到元素或发现不止一个元素,则返回`null`。

### 12. Common

```kotlin
public inline fun ShortArray.singleOrNull(predicate: (Short) -> Boolean): Short?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3309)

返回与给定 `predicate` 匹配的单元素,如果找不到元素或发现不止一个元素,则返回`null`。

### 13. Common

```kotlin
public inline fun IntArray.singleOrNull(predicate: (Int) -> Boolean): Int?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3326)

返回与给定 `predicate` 匹配的单元素,如果找不到元素或发现不止一个元素,则返回`null`。

### 14. Common

```kotlin
public inline fun LongArray.singleOrNull(predicate: (Long) -> Boolean): Long?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3343)

返回与给定 `predicate` 匹配的单元素,如果找不到元素或发现不止一个元素,则返回`null`。

### 15. Common

```kotlin
public inline fun FloatArray.singleOrNull(predicate: (Float) -> Boolean): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3360)

返回与给定 `predicate` 匹配的单元素,如果找不到元素或发现不止一个元素,则返回`null`。

### 16. Common

```kotlin
public inline fun DoubleArray.singleOrNull(predicate: (Double) -> Boolean): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3377)

返回与给定 `predicate` 匹配的单元素,如果找不到元素或发现不止一个元素,则返回`null`。

### 17. Common

```kotlin
public inline fun BooleanArray.singleOrNull(predicate: (Boolean) -> Boolean): Boolean?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3394)

返回与给定 `predicate` 匹配的单元素,如果找不到元素或发现不止一个元素,则返回`null`。

### 18. Common

```kotlin
public inline fun CharArray.singleOrNull(predicate: (Char) -> Boolean): Char?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3411)

返回与给定 `predicate` 匹配的单元素,如果找不到元素或发现不止一个元素,则返回`null`。

### 19. Common

```kotlin
public fun <T> Iterable<T>.singleOrNull(): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L643)

返回单元素,如果收藏为空或含有多个元素,则返回 `null` 。

### 20. Common

```kotlin
public fun <T> List<T>.singleOrNull(): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L661)

返回单元素,如果列表为空或含有多个元素,则返回 `null` 。

### 21. Common

```kotlin
public inline fun <T> Iterable<T>.singleOrNull(predicate: (T) -> Boolean): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L668)

返回与给定 `predicate` 匹配的单元素,如果找不到元素或发现不止一个元素,则返回`null`。

### 22. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.singleOrNull(): UInt?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1547)

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.singleOrNull(): ULong?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1556)

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.singleOrNull(): UByte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1565)

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.singleOrNull(): UShort?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1574)

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.singleOrNull(predicate: (UInt) -> Boolean): UInt?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1583)

返回与给定 `predicate` 匹配的单元素,如果找不到元素或发现不止一个元素,则返回`null`。

### 27. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.singleOrNull(predicate: (ULong) -> Boolean): ULong?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1603)

返回与给定 `predicate` 匹配的单元素,如果找不到元素或发现不止一个元素,则返回`null`。

### 28. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.singleOrNull(predicate: (UByte) -> Boolean): UByte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1623)

返回与给定 `predicate` 匹配的单元素,如果找不到元素或发现不止一个元素,则返回`null`。

### 29. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.singleOrNull(predicate: (UShort) -> Boolean): UShort?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1643)

返回与给定 `predicate` 匹配的单元素,如果找不到元素或发现不止一个元素,则返回`null`。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
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
    val result = source.`singleOrNull`()
    println(result)
}
```

```text title="输出"
null
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
