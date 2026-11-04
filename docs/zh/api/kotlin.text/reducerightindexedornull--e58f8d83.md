# reduceRightIndexedOrNull

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

积累值,从最后一个字符开始,从右到左对每个字符应用 `operation` ,并按其原有字符序列和当前累积值的索引,对每个字符应用`operation`。

如果字符序列为空,则返回 `null` 。

@param `operation` 函数,该函数采用字符索引、字符本身和当前累积值,并计算下一个累积值。

@sample 样本、采集的样本、采集的采集物、分类、 分选的RiightOrnull

??? note "查看英文原文"

    Accumulates value starting with the last character and applying `operation` from right to left
    to each character with its index in the original char sequence and current accumulator value.
    
    Returns `null` if the char sequence is empty.
    
    @param `operation` function that takes the index of a character, the character itself and current accumulator value,
    and calculates the next accumulator value.
    
    @sample samples.collections.Collections.Aggregates.reduceRightOrNull

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public inline fun CharSequence.reduceRightIndexedOrNull(operation: (index: Int, Char, acc: Char) -> Char): Char?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L2034)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val strings = listOf("a", "b", "c", "d")
    println(strings.reduceRightOrNull { string, acc -> acc + string })
    println(strings.reduceRightIndexedOrNull { index, string, acc -> acc + string + index })

    println(emptyList<String>().reduceRightOrNull { _, _ -> "" })
}
```

```text title="输出"
dcba
dc2b1a0
null
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1264)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
