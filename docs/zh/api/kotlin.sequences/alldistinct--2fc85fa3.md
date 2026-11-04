# allDistinct

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果序列中的所有元素彼此不同,即没有两个元素是相等的,则返回`true`。

返回`true`, 空序 。

使用结构平等( `==` )对这些元素进行比较,一旦发现重复元素,操作就会返回 `false` 。

对于浮动点类型( `Double` , `Float` ),`NaN` 的值为 `NaN` ,`-0.0`的值为`Double.equals`和`Float.equals`,不等于`0.0`。

操作为 _flintinal_。

@sample 样本, 生成. 全部 。 所有 Distincet 序列样本, 全部 Distinct

??? note "查看英文原文"

    Returns `true` if all elements in the sequence are distinct from each other,
    that is, no two elements are equal.
    
    Returns `true` for an empty sequence.
    
    The elements are compared using structural equality (`==`).
    The operation returns `false` as soon as a duplicate element is found.
    
    For elements of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
    and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.
    
    The operation is _terminal_.
    
    @sample samples.generated.alldistinct.AllDistinctSequencesSamples.allDistinct

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public fun <T> Sequence<T>.allDistinct(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1426)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(sequenceOf<String>().allDistinct())
    println(sequenceOf("apple").allDistinct())

    println(sequenceOf("apple", "mango", "peach").allDistinct())

    println(sequenceOf("apple", "mango", "apple").allDistinct())
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctSequencesSamples.kt#L18)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
