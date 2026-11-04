# reduce

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

积累值,从第一个元素开始,从左向右应用 `operation` ,到目前的累积值和每个元素。

如果此数组为空, 则丢弃例外。 如果数组可以以预期方式为空, 请使用 `reduceOrNull` 来代替。 当收件人为空时, 它返回 `null` 。

@param `operation` 函数,它使用当前累积值和元素,计算下一个累积值。

@sample 样本、采集的样本、采集的采集量、聚合的样本、

??? note "查看英文原文"

    Accumulates value starting with the first element and applying `operation` from left to right
    to current accumulator value and each element.
    
    Throws an exception if this array is empty. If the array can be empty in an expected way,
    please use `reduceOrNull` instead. It returns `null` when its receiver is empty.
    
    @param `operation` function that takes current accumulator value and an element,
    and calculates the next accumulator value.
    
    @sample samples.collections.Collections.Aggregates.reduce

## 声明与重载

### 1. Common

```kotlin
public inline fun <S, T : S> Array<out T>.reduce(operation: (acc: S, T) -> S): S
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22597)

### 2. Common

```kotlin
public inline fun ByteArray.reduce(operation: (acc: Byte, Byte) -> Byte): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22619)

### 3. Common

```kotlin
public inline fun ShortArray.reduce(operation: (acc: Short, Short) -> Short): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22641)

### 4. Common

```kotlin
public inline fun IntArray.reduce(operation: (acc: Int, Int) -> Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22663)

### 5. Common

```kotlin
public inline fun LongArray.reduce(operation: (acc: Long, Long) -> Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22685)

### 6. Common

```kotlin
public inline fun FloatArray.reduce(operation: (acc: Float, Float) -> Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22707)

### 7. Common

```kotlin
public inline fun DoubleArray.reduce(operation: (acc: Double, Double) -> Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22729)

### 8. Common

```kotlin
public inline fun BooleanArray.reduce(operation: (acc: Boolean, Boolean) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22751)

### 9. Common

```kotlin
public inline fun CharArray.reduce(operation: (acc: Char, Char) -> Char): Char
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L22773)

### 10. Common

```kotlin
public inline fun <S, T : S> Iterable<T>.reduce(operation: (acc: S, T) -> S): S
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3100)

积累值,从第一个元素开始,从左向右应用 `operation` ,到目前的累积值和每个元素。

如果收藏为空, 丢弃例外。 如果收藏可以以预期方式为空, 请使用 `reduceOrNull` 来代替它。 当它接收器为空时, 它返回 `null` 。

@param `operation` 函数,它使用当前累积值和元素,计算下一个累积值。

@sample 样本、采集的样本、采集的采集量、聚合的样本、

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.reduce(operation: (acc: UInt, UInt) -> UInt): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9935)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.reduce(operation: (acc: ULong, ULong) -> ULong): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9960)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.reduce(operation: (acc: UByte, UByte) -> UByte): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L9985)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.reduce(operation: (acc: UShort, UShort) -> UShort): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L10010)

### 15. Common

```kotlin
@SinceKotlin("1.1")
public inline fun <S, T : S, K> Grouping<T, K>.reduce(
    operation: (key: K, accumulator: S, element: T) -> S
): Map<K, S>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Grouping.kt#L192)

`Grouping` 源的元素按键分组,对从该组的第二个元素开始的每个组的元素按顺序递转`operation`,将先前的累计值和当前元素作为参数,并将结果存储在新地图中。组的第一个元素是集合器的初始值。

@param运行一个函数,该函数在组内随后每个元素上援引,参数如下: - `key`:该元素所属的组的钥匙; - `accumulator`:该组的积累者的现值; - `element`:源的累积要素。

@return a `Map` 将每一组的关键与组元素积累的结果联系起来。 @sample 样本. 收集。 分组. dudeByMaxVowels

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val strings = listOf("a", "b", "c", "d")
    println(strings.reduce { acc, string -> acc + string })
    println(strings.reduceIndexed { index, acc, string -> acc + string + index })

    assertFails { emptyList<Int>().reduce { _, _ -> 0 } }
}
```

```text title="输出"
abcd
ab1c2d3
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1237)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val animals = listOf("raccoon", "reindeer", "cow", "camel", "giraffe", "goat")

    // grouping by first char and collect only max of contains vowels
    val compareByVowelCount = compareBy { s: String -> s.count { it in "aeiou" } }

    val maxVowels = animals.groupingBy { it.first() }.reduce { _, a, b -> maxOf(a, b, compareByVowelCount) }

    println(maxVowels)
}
```

```text title="输出"
{r=reindeer, c=camel, g=giraffe}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/grouping.kt#L111)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
