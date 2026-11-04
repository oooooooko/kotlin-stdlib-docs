# count

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回此数组中元素的数量。

??? note "查看英文原文"

    Returns the number of elements in this array.

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Array<out T>.count(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15393)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun ByteArray.count(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15401)

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun ShortArray.count(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15409)

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun IntArray.count(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15417)

### 5. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun LongArray.count(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15425)

### 6. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun FloatArray.count(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15433)

### 7. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun DoubleArray.count(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15441)

### 8. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun BooleanArray.count(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15449)

### 9. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharArray.count(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15457)

### 10. Common

```kotlin
public inline fun <T> Array<out T>.count(predicate: (T) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15465)

返回与给定的 `predicate` 匹配的元素数。

### 11. Common

```kotlin
public inline fun ByteArray.count(predicate: (Byte) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15474)

返回与给定的 `predicate` 匹配的元素数。

### 12. Common

```kotlin
public inline fun ShortArray.count(predicate: (Short) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15483)

返回与给定的 `predicate` 匹配的元素数。

### 13. Common

```kotlin
public inline fun IntArray.count(predicate: (Int) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15492)

返回与给定的 `predicate` 匹配的元素数。

### 14. Common

```kotlin
public inline fun LongArray.count(predicate: (Long) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15501)

返回与给定的 `predicate` 匹配的元素数。

### 15. Common

```kotlin
public inline fun FloatArray.count(predicate: (Float) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15510)

返回与给定的 `predicate` 匹配的元素数。

### 16. Common

```kotlin
public inline fun DoubleArray.count(predicate: (Double) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15519)

返回与给定的 `predicate` 匹配的元素数。

### 17. Common

```kotlin
public inline fun BooleanArray.count(predicate: (Boolean) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15528)

返回与给定的 `predicate` 匹配的元素数。

### 18. Common

```kotlin
public inline fun CharArray.count(predicate: (Char) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15537)

返回与给定的 `predicate` 匹配的元素数。

### 19. Common

```kotlin
public fun <T> Iterable<T>.count(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2096)

返回此收藏中元素的数。

### 20. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Collection<T>.count(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2106)

返回此收藏中元素的数。

### 21. Common

```kotlin
public inline fun <T> Iterable<T>.count(predicate: (T) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2114)

返回与给定的 `predicate` 匹配的元素数。

### 22. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <K, V> Map<out K, V>.count(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L198)

返回此地图中条目的数目。

### 23. Common

```kotlin
public inline fun <K, V> Map<out K, V>.count(predicate: (Map.Entry<K, V>) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L206)

返回匹配给定 `predicate` 的条目数。

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.count(predicate: (UInt) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6571)

返回与给定的 `predicate` 匹配的元素数。

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.count(predicate: (ULong) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6583)

返回与给定的 `predicate` 匹配的元素数。

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.count(predicate: (UByte) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6595)

返回与给定的 `predicate` 匹配的元素数。

### 27. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.count(predicate: (UShort) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6607)

返回与给定的 `predicate` 匹配的元素数。

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
    val result = source.`count`()
    println(result)
}
```

```text title="输出"
3
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
