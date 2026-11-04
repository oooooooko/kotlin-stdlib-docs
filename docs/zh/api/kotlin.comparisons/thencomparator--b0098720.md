# thenComparator

`kotlin.comparisons` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

利用主要参照国和功能,建立一个比较国,以计算比较结果。

@sample 样本.比较.比较.比较.比较.然后比较

??? note "查看英文原文"

    Creates a comparator using the primary comparator and function to calculate a result of comparison.
    
    @sample samples.comparisons.Comparisons.thenComparator

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Comparator<T>.thenComparator(crossinline comparison: (a: T, b: T) -> Int): Comparator<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L187)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf("c" to 1, "b" to 2, "a" to 1, "d" to 0, null to 0)

    val valueComparator = compareBy<Pair<String?, Int>> { it.second }
    val map1 = list.sortedWith(valueComparator).toMap()
    println(map1)

    val valueThenKeyComparator = valueComparator
        .thenComparator({ a, b -> compareValues(a.first, b.first) })
    val map2 = list.sortedWith(valueThenKeyComparator).toMap()
    println(map2)
}
```

```text title="输出"
{d=0, null=0, c=1, a=1, b=2}
{null=0, d=0, a=1, c=1, b=2}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L164)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
