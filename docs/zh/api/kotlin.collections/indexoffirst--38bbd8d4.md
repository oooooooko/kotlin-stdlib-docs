# indexOfFirst

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回匹配给定 `predicate`的第一个元素的索引,如果数组不包含该元素,则返回 - 1。

??? note "查看英文原文"

    Returns index of the first element matching the given `predicate`, or -1 if the array does not contain such element.

## 声明与重载

### 1. Common

```kotlin
public inline fun <T> Array<out T>.indexOfFirst(predicate: (T) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1787)

### 2. Common

```kotlin
public inline fun ByteArray.indexOfFirst(predicate: (Byte) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1799)

### 3. Common

```kotlin
public inline fun ShortArray.indexOfFirst(predicate: (Short) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1811)

### 4. Common

```kotlin
public inline fun IntArray.indexOfFirst(predicate: (Int) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1823)

### 5. Common

```kotlin
public inline fun LongArray.indexOfFirst(predicate: (Long) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1835)

### 6. Common

```kotlin
public inline fun FloatArray.indexOfFirst(predicate: (Float) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1847)

### 7. Common

```kotlin
public inline fun DoubleArray.indexOfFirst(predicate: (Double) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1859)

### 8. Common

```kotlin
public inline fun BooleanArray.indexOfFirst(predicate: (Boolean) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1871)

### 9. Common

```kotlin
public inline fun CharArray.indexOfFirst(predicate: (Char) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1883)

### 10. Common

```kotlin
public inline fun <T> Iterable<T>.indexOfFirst(predicate: (T) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L345)

返回第一个元素的索引,该元素与给定的 `predicate` 匹配,如果收藏中不含该元素,则返回 - 1 。

### 11. Common

```kotlin
public inline fun <T> List<T>.indexOfFirst(predicate: (T) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L359)

返回第一个元素的索引,该元素与给定的 `predicate` 匹配,如果列表中没有包含 - 1 ,则返回该元素的索引。

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.indexOfFirst(predicate: (UInt) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L883)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.indexOfFirst(predicate: (ULong) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L893)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.indexOfFirst(predicate: (UByte) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L903)

### 15. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.indexOfFirst(predicate: (UShort) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L913)

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
    val result = source.`indexOfFirst`({ it.toString().length > 0 })
    println(result)
}
```

```text title="输出"
0
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
