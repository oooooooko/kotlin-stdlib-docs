# chunkedSequence

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将此字符序列分割成字符串序列,每字符串不超过给定的`size`。

生成序列中最后一个字符串的字符数可能少于给定的 `size` 。

@param 大小, 以每字符串中要包含的元素数量为单位, 必须是正数, 并且可以大于此字符序列中元素的数量 。

@sample 样本.text.Strings.chunkenched 序列

??? note "查看英文原文"

    Splits this char sequence into a sequence of strings each not exceeding the given `size`.
    
    The last string in the resulting sequence may have fewer characters than the given `size`.
    
    @param size the number of elements to take in each string, must be positive and can be greater than the number of elements in this char sequence.
    
    @sample samples.text.Strings.chunkedSequence

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public fun CharSequence.chunkedSequence(size: Int): Sequence<String>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L2341)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public fun <R> CharSequence.chunkedSequence(size: Int, transform: (CharSequence) -> R): Sequence<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L2355)

将此字符序列分割成数个字符序列,每个字符序列不超过给定的 `size` ,并将给定的`transform`函数应用于每个字符。

`transform` 结果的@return序列适用于每个字符序列。

请注意, 传给 `transform` 函数的字符序列是短时间的, 并且只在该函数中有效。 您不应该保存它, 或者允许它以某种方式逃跑, 除非您对它做了一个快照。 最后字符序列的字符数可能少于给定的 `size` 。

@param 大小, 每一字符序列中要包含的元素数量, 必须是正数, 并且可以大于此字符序列中元素的数量 。

@sample 样本.text.Strings.chnocked 变形序列

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val dnaFragment = "ATTCGCCAAXXX"
    val knownAcids = setOf("ATT", "CGC", "CAA") // XXX would cause error if processed
    val codons = dnaFragment.chunkedSequence(3).onEach { check(it in knownAcids) }
    val firstTwo = codons.take(2).toList()

    println(firstTwo)
}
```

```text title="输出"
[ATT, CGC]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L72)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val codonTable = mapOf("ATT" to "Isoleucine", "CAA" to "Glutamine", "CGC" to "Arginine", "GGC" to "Glycine")
    val dnaFragment = "ATTCGCGGCCGCCAACGG"

    val proteins = dnaFragment.chunkedSequence(3) { codon: CharSequence -> codonTable[codon.toString()] ?: error("Unknown codon") }

    // sequence is evaluated lazily, so that unknown codon is not reached
    println(proteins.take(5).toList())
}
```

```text title="输出"
[Isoleucine, Arginine, Glycine, Arginine, Glutamine]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L92)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
