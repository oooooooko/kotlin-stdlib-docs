# lastOrNull

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果数组为空,则返回最后一个元素,即 `null` 。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、最后元素

??? note "查看英文原文"

    Returns the last element, or `null` if the array is empty.
    
    @sample samples.collections.Collections.Elements.last

## 声明与重载

### 1. Common

```kotlin
public fun <T> Array<out T>.lastOrNull(): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2375)

### 2. Common

```kotlin
public fun ByteArray.lastOrNull(): Byte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2384)

### 3. Common

```kotlin
public fun ShortArray.lastOrNull(): Short?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2393)

### 4. Common

```kotlin
public fun IntArray.lastOrNull(): Int?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2402)

### 5. Common

```kotlin
public fun LongArray.lastOrNull(): Long?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2411)

### 6. Common

```kotlin
public fun FloatArray.lastOrNull(): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2420)

### 7. Common

```kotlin
public fun DoubleArray.lastOrNull(): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2429)

### 8. Common

```kotlin
public fun BooleanArray.lastOrNull(): Boolean?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2438)

### 9. Common

```kotlin
public fun CharArray.lastOrNull(): Char?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2447)

### 10. Common

```kotlin
public inline fun <T> Array<out T>.lastOrNull(predicate: (T) -> Boolean): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2456)

返回与给定 `predicate` 匹配的最后元素,如果没有找到此元素,则返回 `null`。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、最后元素

### 11. Common

```kotlin
public inline fun ByteArray.lastOrNull(predicate: (Byte) -> Boolean): Byte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2469)

返回与给定 `predicate` 匹配的最后元素,如果没有找到此元素,则返回 `null`。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、最后元素

### 12. Common

```kotlin
public inline fun ShortArray.lastOrNull(predicate: (Short) -> Boolean): Short?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2482)

返回与给定 `predicate` 匹配的最后元素,如果没有找到此元素,则返回 `null`。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、最后元素

### 13. Common

```kotlin
public inline fun IntArray.lastOrNull(predicate: (Int) -> Boolean): Int?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2495)

返回与给定 `predicate` 匹配的最后元素,如果没有找到此元素,则返回 `null`。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、最后元素

### 14. Common

```kotlin
public inline fun LongArray.lastOrNull(predicate: (Long) -> Boolean): Long?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2508)

返回与给定 `predicate` 匹配的最后元素,如果没有找到此元素,则返回 `null`。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、最后元素

### 15. Common

```kotlin
public inline fun FloatArray.lastOrNull(predicate: (Float) -> Boolean): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2521)

返回与给定 `predicate` 匹配的最后元素,如果没有找到此元素,则返回 `null`。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、最后元素

### 16. Common

```kotlin
public inline fun DoubleArray.lastOrNull(predicate: (Double) -> Boolean): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2534)

返回与给定 `predicate` 匹配的最后元素,如果没有找到此元素,则返回 `null`。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、最后元素

### 17. Common

```kotlin
public inline fun BooleanArray.lastOrNull(predicate: (Boolean) -> Boolean): Boolean?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2547)

返回与给定 `predicate` 匹配的最后元素,如果没有找到此元素,则返回 `null`。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、最后元素

### 18. Common

```kotlin
public inline fun CharArray.lastOrNull(predicate: (Char) -> Boolean): Char?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L2560)

返回与给定 `predicate` 匹配的最后元素,如果没有找到此元素,则返回 `null`。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、最后元素

### 19. Common

```kotlin
public fun <T> Iterable<T>.lastOrNull(): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L496)

如果收藏为空,返回最后一个元素,或 `null` 。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、最后元素

### 20. Common

```kotlin
public fun <T> List<T>.lastOrNull(): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L516)

如果列表为空,则返回最后一个元素,即 `null` 。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、最后元素

### 21. Common

```kotlin
public inline fun <T> Iterable<T>.lastOrNull(predicate: (T) -> Boolean): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L525)

返回与给定 `predicate` 匹配的最后元素,如果没有找到此元素,则返回 `null`。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、最后元素

### 22. Common

```kotlin
public inline fun <T> List<T>.lastOrNull(predicate: (T) -> Boolean): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L540)

返回与给定 `predicate` 匹配的最后元素,如果没有找到此元素,则返回 `null`。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、最后元素

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.lastOrNull(): UInt?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1131)

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.lastOrNull(): ULong?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1142)

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.lastOrNull(): UByte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1153)

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.lastOrNull(): UShort?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1164)

### 27. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.lastOrNull(predicate: (UInt) -> Boolean): UInt?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1175)

返回与给定 `predicate` 匹配的最后元素,如果没有找到此元素,则返回 `null`。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、最后元素

### 28. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.lastOrNull(predicate: (ULong) -> Boolean): ULong?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1191)

返回与给定 `predicate` 匹配的最后元素,如果没有找到此元素,则返回 `null`。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、最后元素

### 29. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.lastOrNull(predicate: (UByte) -> Boolean): UByte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1207)

返回与给定 `predicate` 匹配的最后元素,如果没有找到此元素,则返回 `null`。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、最后元素

### 30. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.lastOrNull(predicate: (UShort) -> Boolean): UShort?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1223)

返回与给定 `predicate` 匹配的最后元素,如果没有找到此元素,则返回 `null`。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、最后元素

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val list = listOf(1, 2, 3, 4)
    println(list.last())
    println(list.last { it % 2 == 1 })
    println(list.lastOrNull { it < 0 })
    assertFails { list.last { it < 0 } }

    val emptyList = emptyList<Int>()
    println(emptyList.lastOrNull())
    assertFails { emptyList.last() }
}
```

```text title="输出"
4
3
null
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1368)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
