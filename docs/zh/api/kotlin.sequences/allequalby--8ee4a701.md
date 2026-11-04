# allEqualBy

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果序列中的所有元素产生与给定的`selector`函数产生的相同价值,则返回`true`。

返回`true`, 空序 。

`selector` 值按结构平等(`==`)顺序比较,如果第一个元素的`selector`值等于其后每个元素的`selector`值,则所有元素都以`selector`值等值。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

操作为 _flintinal_。

@sample 样本. 生成. 等同。 所有等同序列 样本. allEqualBy

??? note "查看英文原文"

    Returns `true` if all elements in the sequence yield the same value
    produced by the given `selector` function.
    
    Returns `true` for an empty sequence.
    
    The `selector` values are compared sequentially using structural equality (`==`),
    and all elements are considered equal by the `selector` value if the `selector`
    value of the first element equals the `selector` value of every subsequent element.
    
    For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
    and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.
    
    The operation is _terminal_.
    
    @sample samples.generated.allequal.AllEqualSequencesSamples.allEqualBy

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <T, K> Sequence<T>.allEqualBy(selector: (T) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1517)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(sequenceOf<String>().allEqualBy { it.length })
    println(sequenceOf("apple").allEqualBy { it.length })

    println(sequenceOf("apple", "mango", "peach").allEqualBy { it.length })
    println(sequenceOf("apple", "mango", "peach").allEqualBy { it })
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualSequencesSamples.kt#L28)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
