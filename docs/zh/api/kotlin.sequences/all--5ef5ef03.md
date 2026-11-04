# all

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果所有元素都与给定的`predicate`相符,则返回`true`。

请注意,如果序列中不含元素,函数返回 `true` , 因为其中没有元素_ 与前提匹配。 请在 [“ 虚伪的真理 ” (https://en.wikipedia.org/wiki/Vacuous_truth) 条) 中更详细地解释这一逻辑概念。

操作为 _flintinal_。

@sample 样本、采集的样本、采集的样本、采集的样本、分类的样本

??? note "查看英文原文"

    Returns `true` if all elements match the given `predicate`.
    
    Note that if the sequence contains no elements, the function returns `true`
    because there are no elements in it that _do not_ match the predicate.
    See a more detailed explanation of this logic concept in ["Vacuous truth"](https://en.wikipedia.org/wiki/Vacuous_truth) article.
    
    The operation is _terminal_.
    
    @sample samples.collections.Collections.Aggregates.all

## 声明与重载

### 1. Common

```kotlin
public inline fun <T> Sequence<T>.all(predicate: (T) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1410)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val isEven: (Int) -> Boolean = { it % 2 == 0 }
    val zeroToTen = 0..10
    println(zeroToTen.all { isEven(it) })
    println(zeroToTen.all(isEven))

    val evens = zeroToTen.map { it * 2 }
    println(evens.all { isEven(it) })

    val emptyList = emptyList<Int>()
    println(emptyList.all { false })
}
```

```text title="输出"
false
false
true
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L983)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
