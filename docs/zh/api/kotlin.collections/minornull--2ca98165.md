# minOrNull

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果数组为空,则返回最小元素或`null`。

如果元素中的任何元素为 `NaN` ,此函数返回 `NaN` 。

@sample 样本、采集的样本、采集的采集量、聚合的样本、最大MinFloction

??? note "查看英文原文"

    Returns the smallest element or `null` if the array is empty.
    
    If any of elements is `NaN`, this function returns `NaN`.
    
    @sample samples.collections.Collections.Aggregates.maxMinFloating

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public fun Array<out Double>.minOrNull(): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21779)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public fun Array<out Float>.minOrNull(): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21797)

### 3. Common

```kotlin
@SinceKotlin("1.4")
public fun <T : Comparable<T>> Array<out T>.minOrNull(): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21815)

如果数组为空,则返回最小元素或`null`。

如果有多个等同最小元素,此函数返回其中的第一个元素。

@sample 样本、采集的样本、采集的采集。

### 4. Common

```kotlin
@SinceKotlin("1.4")
public fun ByteArray.minOrNull(): Byte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21833)

如果数组为空,则返回最小元素或`null`。

@sample 样本、采集的样本、采集的采集。

### 5. Common

```kotlin
@SinceKotlin("1.4")
public fun ShortArray.minOrNull(): Short?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21849)

如果数组为空,则返回最小元素或`null`。

@sample 样本、采集的样本、采集的采集。

### 6. Common

```kotlin
@SinceKotlin("1.4")
public fun IntArray.minOrNull(): Int?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21865)

如果数组为空,则返回最小元素或`null`。

@sample 样本、采集的样本、采集的采集。

### 7. Common

```kotlin
@SinceKotlin("1.4")
public fun LongArray.minOrNull(): Long?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21881)

如果数组为空,则返回最小元素或`null`。

@sample 样本、采集的样本、采集的采集。

### 8. Common

```kotlin
@SinceKotlin("1.4")
public fun FloatArray.minOrNull(): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21897)

### 9. Common

```kotlin
@SinceKotlin("1.4")
public fun DoubleArray.minOrNull(): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21915)

### 10. Common

```kotlin
@SinceKotlin("1.4")
public fun CharArray.minOrNull(): Char?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L21933)

如果数组为空,则返回最小元素或`null`。

@sample 样本、采集的样本、采集的采集。

### 11. Common

```kotlin
@SinceKotlin("1.4")
public fun Iterable<Double>.minOrNull(): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2969)

如果收藏为空,返回最小元素或`null`。

如果元素中的任何元素为 `NaN` ,此函数返回 `NaN` 。

@sample 样本、采集的样本、采集的采集量、聚合的样本、最大MinFloction

### 12. Common

```kotlin
@SinceKotlin("1.4")
public fun Iterable<Float>.minOrNull(): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2988)

如果收藏为空,返回最小元素或`null`。

如果元素中的任何元素为 `NaN` ,此函数返回 `NaN` 。

@sample 样本、采集的样本、采集的采集量、聚合的样本、最大MinFloction

### 13. Common

```kotlin
@SinceKotlin("1.4")
public fun <T : Comparable<T>> Iterable<T>.minOrNull(): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3007)

如果收藏为空,返回最小元素或`null`。

如果有多个等同最小元素,此函数返回其中的第一个元素。

@sample 样本、采集的样本、采集的采集。

### 14. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UIntArray.minOrNull(): UInt?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9539)

如果数组为空,则返回最小元素或`null`。

@sample 样本、采集的样本、采集的采集。

### 15. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun ULongArray.minOrNull(): ULong?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9556)

如果数组为空,则返回最小元素或`null`。

@sample 样本、采集的样本、采集的采集。

### 16. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UByteArray.minOrNull(): UByte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9573)

如果数组为空,则返回最小元素或`null`。

@sample 样本、采集的样本、采集的采集。

### 17. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UShortArray.minOrNull(): UShort?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9590)

如果数组为空,则返回最小元素或`null`。

@sample 样本、采集的样本、采集的采集。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    // The largest and smallest elements in the array
    val numbers = doubleArrayOf(3.0, 7.2, 2.4, 6.5)
    println(numbers.max())
    println(numbers.min())

    // max() and min() return `NaN` if any of elements is `NaN`
    val numbersWithNaN = doubleArrayOf(3.0, Double.NaN, 7.2, 2.4, 6.5)
    println(numbersWithNaN.max())
    println(numbersWithNaN.min())

    val emptyArray = doubleArrayOf()

    // max() and min() throw if the array is empty
    assertFailsWith<NoSuchElementException> { emptyArray.max() }
    assertFailsWith<NoSuchElementException> { emptyArray.min() }

    // maxOrNull() and minOrNull() return null if the array is empty
    println(emptyArray.maxOrNull())
    println(emptyArray.minOrNull())
}
```

```text title="输出"
7.2
2.4
NaN
NaN
null
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1061)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    // The largest and smallest elements according to String.compareTo
    val names = listOf("Alice", "Bob", "Carol")
    println(names.max())
    println(names.min())

    val emptyList = emptyList<Int>()

    // max() and min() throw if the collection is empty
    assertFailsWith<NoSuchElementException> { emptyList.max() }
    assertFailsWith<NoSuchElementException> { emptyList.min() }

    // maxOrNull() and minOrNull() return null if the collection is empty
    println(emptyList.maxOrNull())
    println(emptyList.minOrNull())
}
```

```text title="输出"
Carol
Alice
null
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1084)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    // The largest and smallest elements in the array
    val numbers = intArrayOf(3, 7, 2, 6)
    println(numbers.max())
    println(numbers.min())

    val emptyArray = intArrayOf()

    // max() and min() throw if the array is empty
    assertFailsWith<NoSuchElementException> { emptyArray.max() }
    assertFailsWith<NoSuchElementException> { emptyArray.min() }

    // maxOrNull() and minOrNull() return null if the array is empty
    println(emptyArray.maxOrNull())
    println(emptyArray.minOrNull())
}
```

```text title="输出"
7
2
null
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1043)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
