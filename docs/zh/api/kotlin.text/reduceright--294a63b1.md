# reduceRight

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

积累值,从最后一个字符开始,对每个字符和当前累积值从右到左应用`operation`。

如果此字符序列为空, 则丢弃例外。 如果字符序列序列以预期方式为空, 请使用 `reduceRightOrNull` 来代替它。 当它接收器为空时, 它返回 `null` 。

@param `operation` 函数,它包含字符和当前累积值,并计算下一个累积值。

@sample 样本、采集的样本、采集的样本、采集的样本、分类的样本、减少的样本

??? note "查看英文原文"

    Accumulates value starting with the last character and applying `operation` from right to left
    to each character and current accumulator value.
    
    Throws an exception if this char sequence is empty. If the char sequence can be empty in an expected way,
    please use `reduceRightOrNull` instead. It returns `null` when its receiver is empty.
    
    @param `operation` function that takes a character and current accumulator value,
    and calculates the next accumulator value.
    
    @sample samples.collections.Collections.Aggregates.reduceRight

## 声明与重载

### 1. Common

```kotlin
public inline fun CharSequence.reduceRight(operation: (Char, acc: Char) -> Char): Char
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L1989)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val strings = listOf("a", "b", "c", "d")
    println(strings.reduceRight { string, acc -> acc + string })
    println(strings.reduceRightIndexed { index, string, acc -> acc + string + index })

    assertFails { emptyList<Int>().reduceRight { _, _ -> 0 } }
}
```

```text title="输出"
dcba
dc2b1a0
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1246)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
