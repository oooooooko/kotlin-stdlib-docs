# eachCount

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

`Grouping`来源的元素组,按关键和每个组的元素计数。

@return a `Map` 将每个组的钥匙与该组的分子数目联系起来。

@sample 样本、采集资料、分组、分组

??? note "查看英文原文"

    Groups elements from the `Grouping` source by key and counts elements in each group.
    
    @return a `Map` associating the key of each group with the count of elements in the group.
    
    @sample samples.collections.Grouping.groupingByEachCount

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.1")
public expect fun <T, K> Grouping<T, K>.eachCount(): Map<K, Int>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/CollectionsH.kt#L71)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val words = "one two three four five six seven eight nine ten".split(' ')
    val frequenciesByFirstChar = words.groupingBy { it.first() }.eachCount()
    println("Counting first letters:")
    println(frequenciesByFirstChar)

    val moreWords = "eleven twelve".split(' ')
    val moreFrequencies = moreWords.groupingBy { it.first() }.eachCountTo(frequenciesByFirstChar.toMutableMap())
    println(moreFrequencies)
}
```

```text title="输出"
Counting first letters:
{o=1, t=3, f=2, s=2, e=1, n=1}
{o=1, t=4, f=2, s=2, e=2, n=1}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/grouping.kt#L12)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
