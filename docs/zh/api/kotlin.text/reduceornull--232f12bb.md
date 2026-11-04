# reduceOrNull

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

积累值,从第一个字符开始,将 `operation` 从左向右应用到当前累积值和每个字符。

如果字符序列为空,则返回 `null` 。

@param `operation` 函数,它使用当前累积值和一个字符,计算下一个累积值。

@sample 样本、采集的样本、采集的采集物、分类、Ornull

??? note "查看英文原文"

    Accumulates value starting with the first character and applying `operation` from left to right
    to current accumulator value and each character.
    
    Returns `null` if the char sequence is empty.
    
    @param `operation` function that takes current accumulator value and a character,
    and calculates the next accumulator value.
    
    @sample samples.collections.Collections.Aggregates.reduceOrNull

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public inline fun CharSequence.reduceOrNull(operation: (acc: Char, Char) -> Char): Char?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L1967)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val strings = listOf("a", "b", "c", "d")
    println(strings.reduceOrNull { acc, string -> acc + string })
    println(strings.reduceIndexedOrNull { index, acc, string -> acc + string + index })

    println(emptyList<String>().reduceOrNull { _, _ -> "" })
}
```

```text title="输出"
abcd
ab1c2d3
null
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1255)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
