# isSortedDescending

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果序列中的每一元素根据其自然排序的顺序大于或等于下列元素,则返回`true`。

如果序列中元素少于两个,则返回`true`。

将按顺序用`Comparable.compareTo`对各元素进行比较,如果对每对相邻元素而言,前一元素不少于下一元素,则将按降序排序。

注意结果取决于序列的迭代顺序。 大约 `Sequence` 次执行的迭代顺序可能不稳定( 从一次援引改为下一次), 在这种情况下, 此函数可能会返回不一致的结果 。

对于浮动点类型(`Double`、 `Float` ),`NaN`被认为大于任何其他价值(包括正无限),`-0.0`被认为低于`0.0`,与`Double.compareTo`和`Float.compareTo`一致。

操作为 _flintinal_。

@sample 样本. 由. sssssssssss 排序序列样本。 issSorttedDescing

??? note "查看英文原文"

    Returns `true` if each element in the sequence is greater than or equal
    to the following element according to their natural sort order.
    
    Returns `true` if the sequence has fewer than two elements.
    
    The elements are compared sequentially using `Comparable.compareTo`,
    and the sequence is considered sorted in descending order if for each
    pair of adjacent elements the preceding element is not less than the following one.
    
    Note that the result depends on the iteration order of the sequence.
    The iteration order of some `Sequence` implementations may be unstable
    (change from one invocation to the next),
    in which case this function may return inconsistent results.
    
    For elements of floating-point types (`Double`, `Float`), `NaN` is considered greater
    than any other value (including positive infinity), and `-0.0` is considered less than `0.0`,
    consistent with `Double.compareTo` and `Float.compareTo`.
    
    The operation is _terminal_.
    
    @sample samples.generated.issorted.IsSortedSequencesSamples.isSortedDescending

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.4")
public fun <T : Comparable<T>> Sequence<T>.isSortedDescending(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L695)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(sequenceOf<String>().isSortedDescending())
    println(sequenceOf("cherry").isSortedDescending())

    val sorted = sequenceOf("cherry", "banana", "apple")
    println(sorted.isSortedDescending())

    val unsorted = sequenceOf("banana", "cherry", "apple")
    println(unsorted.isSortedDescending())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedSequencesSamples.kt#L30)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
