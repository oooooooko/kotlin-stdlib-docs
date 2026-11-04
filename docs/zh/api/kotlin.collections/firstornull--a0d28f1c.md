# firstOrNull

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果数组为空,返回第一个元素,或 `null` 。

??? note "查看英文原文"

    Returns the first element, or `null` if the array is empty.

## 声明与重载

### 1. Common

```kotlin
public fun <T> Array<out T>.firstOrNull(): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1334)

### 2. Common

```kotlin
public fun ByteArray.firstOrNull(): Byte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1341)

### 3. Common

```kotlin
public fun ShortArray.firstOrNull(): Short?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1348)

### 4. Common

```kotlin
public fun IntArray.firstOrNull(): Int?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1355)

### 5. Common

```kotlin
public fun LongArray.firstOrNull(): Long?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1362)

### 6. Common

```kotlin
public fun FloatArray.firstOrNull(): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1369)

### 7. Common

```kotlin
public fun DoubleArray.firstOrNull(): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1376)

### 8. Common

```kotlin
public fun BooleanArray.firstOrNull(): Boolean?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1383)

### 9. Common

```kotlin
public fun CharArray.firstOrNull(): Char?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1390)

### 10. Common

```kotlin
public inline fun <T> Array<out T>.firstOrNull(predicate: (T) -> Boolean): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1397)

返回第一个元素,如果元素未找到,则返回与给定的 `predicate` 匹配的元素,或者`null`。

### 11. Common

```kotlin
public inline fun ByteArray.firstOrNull(predicate: (Byte) -> Boolean): Byte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1405)

返回第一个元素,如果元素未找到,则返回与给定的 `predicate` 匹配的元素,或者`null`。

### 12. Common

```kotlin
public inline fun ShortArray.firstOrNull(predicate: (Short) -> Boolean): Short?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1413)

返回第一个元素,如果元素未找到,则返回与给定的 `predicate` 匹配的元素,或者`null`。

### 13. Common

```kotlin
public inline fun IntArray.firstOrNull(predicate: (Int) -> Boolean): Int?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1421)

返回第一个元素,如果元素未找到,则返回与给定的 `predicate` 匹配的元素,或者`null`。

### 14. Common

```kotlin
public inline fun LongArray.firstOrNull(predicate: (Long) -> Boolean): Long?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1429)

返回第一个元素,如果元素未找到,则返回与给定的 `predicate` 匹配的元素,或者`null`。

### 15. Common

```kotlin
public inline fun FloatArray.firstOrNull(predicate: (Float) -> Boolean): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1437)

返回第一个元素,如果元素未找到,则返回与给定的 `predicate` 匹配的元素,或者`null`。

### 16. Common

```kotlin
public inline fun DoubleArray.firstOrNull(predicate: (Double) -> Boolean): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1445)

返回第一个元素,如果元素未找到,则返回与给定的 `predicate` 匹配的元素,或者`null`。

### 17. Common

```kotlin
public inline fun BooleanArray.firstOrNull(predicate: (Boolean) -> Boolean): Boolean?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1453)

返回第一个元素,如果元素未找到,则返回与给定的 `predicate` 匹配的元素,或者`null`。

### 18. Common

```kotlin
public inline fun CharArray.firstOrNull(predicate: (Char) -> Boolean): Char?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1461)

返回第一个元素,如果元素未找到,则返回与给定的 `predicate` 匹配的元素,或者`null`。

### 19. Common

```kotlin
public fun <T> Iterable<T>.firstOrNull(): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L265)

如果收藏为空,返回第一个元素,或 `null` 。

### 20. Common

```kotlin
public fun <T> List<T>.firstOrNull(): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L285)

如果列表为空,返回第一个元素,或 `null` 。

### 21. Common

```kotlin
public inline fun <T> Iterable<T>.firstOrNull(predicate: (T) -> Boolean): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L292)

返回第一个元素,如果元素未找到,则返回与给定的 `predicate` 匹配的元素,或者`null`。

### 22. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.firstOrNull(): UInt?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L659)

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.firstOrNull(): ULong?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L668)

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.firstOrNull(): UByte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L677)

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.firstOrNull(): UShort?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L686)

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.firstOrNull(predicate: (UInt) -> Boolean): UInt?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L695)

返回第一个元素,如果元素未找到,则返回与给定的 `predicate` 匹配的元素,或者`null`。

### 27. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.firstOrNull(predicate: (ULong) -> Boolean): ULong?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L706)

返回第一个元素,如果元素未找到,则返回与给定的 `predicate` 匹配的元素,或者`null`。

### 28. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.firstOrNull(predicate: (UByte) -> Boolean): UByte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L717)

返回第一个元素,如果元素未找到,则返回与给定的 `predicate` 匹配的元素,或者`null`。

### 29. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.firstOrNull(predicate: (UShort) -> Boolean): UShort?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L728)

返回第一个元素,如果元素未找到,则返回与给定的 `predicate` 匹配的元素,或者`null`。

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
    val result = source.`firstOrNull`()
    println(result)
}
```

```text title="输出"
1
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
