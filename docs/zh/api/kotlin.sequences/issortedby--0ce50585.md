# isSortedBy

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果序列中的每一元素的值为`selector`,则返回`true`,如果根据选择值的自然排序,每元素的值低于或等于以下元素的`selector`,则返回`true`。

如果序列中元素少于两个,则返回`true`。

相邻元素的`selector`值按顺序使用`compareValues`进行比较,如果对相邻元素的每一对的上一个元素的`selector`值不大于下一个元素的`selector`值,则该序列被视为分拣。

如果`selector`返回`null`,则`null`值作为低于任何非核值处理。

注意结果取决于序列的迭代顺序。 大约 `Sequence` 次执行的迭代顺序可能不稳定( 从一次援引改为下一次), 在这种情况下, 此函数可能会返回不一致的结果 。

操作为 _flintinal_。

@sample 样本. 生成. issored.  Iss 类序列样本. is SortedBy

??? note "查看英文原文"

    Returns `true` if each element in the sequence yields a `selector` value
    that is less than or equal to the `selector` value of the following element
    according to the natural sort order of the selector values.
    
    Returns `true` if the sequence has fewer than two elements.
    
    The `selector` values of adjacent elements are compared sequentially using `compareValues`,
    and the sequence is considered sorted if for each pair of adjacent elements
    the `selector` value of the preceding element is not greater than that of the following one.
    
    If the `selector` returns `null` for an element, the `null` value is treated as less than any non-null value.
    
    Note that the result depends on the iteration order of the sequence.
    The iteration order of some `Sequence` implementations may be unstable
    (change from one invocation to the next),
    in which case this function may return inconsistent results.
    
    The operation is _terminal_.
    
    @sample samples.generated.issorted.IsSortedSequencesSamples.isSortedBy

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.4")
public inline fun <T, R : Comparable<R>> Sequence<T>.isSortedBy(selector: (T) -> R?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L614)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(sequenceOf<String>().isSortedBy { it.length })
    println(sequenceOf("c").isSortedBy { it.length })

    println(sequenceOf("c", "bb", "aaa").isSortedBy { it.length })
    println(sequenceOf("c", "bb", "aaa").isSortedBy { it })
    println(sequenceOf("a", "b").isSortedBy { if (it == "a") null else it })
    println(sequenceOf(null, "a", "b").isSortedBy { it })
    println(sequenceOf(null, "c", "bb").isSortedBy { it?.length })
}
```

```text title="输出"
true
true
true
false
true
true
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/issorted/IsSortedSequencesSamples.kt#L58)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
