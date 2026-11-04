# allDistinctBy

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果对序列中元素应用给定的 `selector` 函数产生的全部数值彼此不同,则返回 `true`。

返回`true`, 空序 。

`selector` 值是使用结构平等( `==` )进行比较的,一旦发现 `false` 的值重复值,该操作将返回 `false` 。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

操作为 _flintinal_。

@sample 样本, 生成. 全部 。 所有 Distincet 序列样本, 全部 DistinctBy

??? note "查看英文原文"

    Returns `true` if all values produced by applying the given `selector` function to the
    elements in the sequence are distinct from each other.
    
    Returns `true` for an empty sequence.
    
    The `selector` values are compared using structural equality (`==`).
    The operation returns `false` as soon as a duplicate `selector` value is found.
    
    For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
    and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.
    
    The operation is _terminal_.
    
    @sample samples.generated.alldistinct.AllDistinctSequencesSamples.allDistinctBy

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <T, K> Sequence<T>.allDistinctBy(selector: (T) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1457)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(sequenceOf<String>().allDistinctBy { it.length })
    println(sequenceOf("apple").allDistinctBy { it.length })

    println(sequenceOf("apple", "mango", "peach").allDistinctBy { it.length })
    println(sequenceOf("apple", "mango", "peach").allDistinctBy { it })
}
```

```text title="输出"
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctSequencesSamples.kt#L28)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
