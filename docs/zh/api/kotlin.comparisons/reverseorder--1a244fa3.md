# reverseOrder

`kotlin.comparisons` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个比较国,以逆向自然顺序比较`Comparable`物体。

自然顺序为`Comparable`, 系指以其`compareTo`功能确定的顺序。

@sample 样本.比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性第一次与比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性试验性试验性试验性第一次与比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性试验第一次与比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性试验

??? note "查看英文原文"

    Returns a comparator that compares `Comparable` objects in reversed natural order.
    
    The natural order of a `Comparable` type here means the order established by its `compareTo` function.
    
    @sample samples.comparisons.Comparisons.nullsFirstLastWithComparator

## 声明与重载

### 1. Common

```kotlin
public fun <T : Comparable<T>> reverseOrder(): Comparator<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L285)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf(4, null, 1, -2, 3)

    val nullsFirstList = list.sortedWith(nullsFirst(reverseOrder()))
    println(nullsFirstList)

    val nullsLastList = list.sortedWith(nullsLast(reverseOrder()))
    println(nullsLastList)
}
```

```text title="输出"
[null, 4, 3, 1, -2]
[4, 3, 1, -2, null]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L213)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
