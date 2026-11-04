# eachCountTo

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将`Grouping`来源的元素按关键和数组组组成,每个元素组组成,然后绘制给定的`destination`地图。

如果`destination`地图已经具有与某些组的键相对应的值,则该值用作该组的柜台的初始值。

@return 将每个组的钥匙与组内各单元的数联系起来的`destination`地图。

@sample 样本、采集资料、分组、分组

??? note "查看英文原文"

    Groups elements from the `Grouping` source by key and counts elements in each group to the given `destination` map.
    
    If the `destination` map already has a value corresponding to the key of some group,
    that value is used as an initial value of the counter for that group.
    
    @return the `destination` map associating the key of each group with the count of elements in the group.
    
    @sample samples.collections.Grouping.groupingByEachCount

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.1")
public fun <T, K, M : MutableMap<in K, Int>> Grouping<T, K>.eachCountTo(destination: M): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Grouping.kt#L245)

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
