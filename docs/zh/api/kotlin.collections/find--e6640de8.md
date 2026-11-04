# find

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回第一个元素,如果找不到给定的 `predicate`, 则返回第一个元素, 或`null`。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、查找的样本

??? note "查看英文原文"

    Returns the first element matching the given `predicate`, or `null` if no such element was found.
    
    @sample samples.collections.Collections.Elements.find

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Array<out T>.find(predicate: (T) -> Boolean): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L944)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun ByteArray.find(predicate: (Byte) -> Boolean): Byte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L954)

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun ShortArray.find(predicate: (Short) -> Boolean): Short?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L964)

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun IntArray.find(predicate: (Int) -> Boolean): Int?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L974)

### 5. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun LongArray.find(predicate: (Long) -> Boolean): Long?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L984)

### 6. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun FloatArray.find(predicate: (Float) -> Boolean): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L994)

### 7. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun DoubleArray.find(predicate: (Double) -> Boolean): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1004)

### 8. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun BooleanArray.find(predicate: (Boolean) -> Boolean): Boolean?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1014)

### 9. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharArray.find(predicate: (Char) -> Boolean): Char?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1024)

### 10. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Iterable<T>.find(predicate: (T) -> Boolean): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L168)

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.find(predicate: (UInt) -> Boolean): UInt?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L467)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.find(predicate: (ULong) -> Boolean): ULong?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L479)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.find(predicate: (UByte) -> Boolean): UByte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L491)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.find(predicate: (UShort) -> Boolean): UShort?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L503)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val numbers = listOf(1, 2, 3, 4, 5, 6, 7)
    val firstOdd = numbers.find { it % 2 != 0 }
    val lastEven = numbers.findLast { it % 2 == 0 }

    println(firstOdd)
    println(lastEven)
}
```

```text title="输出"
1
6
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1335)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
