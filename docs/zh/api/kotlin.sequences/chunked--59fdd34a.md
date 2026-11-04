# chunked

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将此序列分割成一个序列, 列表的顺序各不超过给定的 `size` 。

所产生序列的最后列表中可能比给定的`size`的元素更少。

每一清单中要包含的元素数量必须为正数,且大于此序列中元素的数量,但大小为@param。

操作是 _ 中间线 _ 和 _ tateful_ 。

@sample 样本、采集物、采集物、变形物、沉没

??? note "查看英文原文"

    Splits this sequence into a sequence of lists each not exceeding the given `size`.
    
    The last list in the resulting sequence may have fewer elements than the given `size`.
    
    @param size the number of elements to take in each list, must be positive and can be greater than the number of elements in this sequence.
    
    The operation is _intermediate_ and _stateful_.
    
    @sample samples.collections.Collections.Transformations.chunked

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public fun <T> Sequence<T>.chunked(size: Int): Sequence<List<T>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3008)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public fun <T, R> Sequence<T>.chunked(size: Int, transform: (List<T>) -> R): Sequence<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3024)

将这个序列分成若干个清单,每个清单不超过给定的 `size` ,并对每个序列适用给定的`transform`函数。

`transform` 结果的@return序列适用于每个清单。

请注意, 列表传递到 `transform` 函数时长, 并且仅在该函数中有效。 您不应该保存它, 也不应该允许它以某种方式逃脱, 除非您对它做了一个快照。 最后列表中的内容可能少于给定的 `size` 。

每一清单中要包含的元素数量必须为正数,且大于此序列中元素的数量,但大小为@param。

操作是 _ 中间线 _ 和 _ tateful_ 。

@sample 样本.text. strings.chnuked 变形

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val words = "one two three four five six seven eight nine ten".split(' ')
    val chunks = words.chunked(3)

    println(chunks)
}
```

```text title="输出"
[[one, two, three], [four, five, six], [seven, eight, nine], [ten]]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L929)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val codonTable = mapOf("ATT" to "Isoleucine", "CAA" to "Glutamine", "CGC" to "Arginine", "GGC" to "Glycine")
    val dnaFragment = "ATTCGCGGCCGCCAA"

    val proteins = dnaFragment.chunked(3) { codon: CharSequence -> codonTable[codon.toString()] ?: error("Unknown codon") }

    println(proteins)
}
```

```text title="输出"
[Isoleucine, Arginine, Glycine, Arginine, Glutamine]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L82)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
