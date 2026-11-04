# filterIndexedTo

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将所有匹配给定的 `predicate` 的字符附加到给定的 `destination`. @param `predicate` 函数,该函数将字符本身的索引取下来,并返回字符的上游评价结果。

@sample 样本、采集的样本、采集的采集、采集的采集、过滤、过滤、过滤

??? note "查看英文原文"

    Appends all characters matching the given `predicate` to the given `destination`.
    @param `predicate` function that takes the index of a character and the character itself
    and returns the result of predicate evaluation on the character.
    
    @sample samples.collections.Collections.Filtering.filterIndexedTo

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
public inline fun <C : Appendable> CharSequence.filterIndexedTo(destination: C, predicate: (index: Int, Char) -> Boolean): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L466)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val numbers: List<Int> = listOf(0, 1, 2, 3, 4, 8, 6)
    val numbersOnSameIndexAsValue = mutableListOf<Int>()

    println(numbersOnSameIndexAsValue)

    numbers.filterIndexedTo(numbersOnSameIndexAsValue) { index, i -> index == i }

    println(numbersOnSameIndexAsValue)
}
```

```text title="输出"
[]
[0, 1, 2, 3, 4, 6]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1618)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
