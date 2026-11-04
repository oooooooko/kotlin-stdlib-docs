# nullsLast

`kotlin.comparisons` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将给定的`comparator`非无效值扩大到无效值的参照方,即`null`值大于任何其他值。

@sample 样本.比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性第一次与比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性试验性试验性试验性第一次与比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性试验第一次与比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性试验

??? note "查看英文原文"

    Extends the given `comparator` of non-nullable values to a comparator of nullable values
    considering `null` value greater than any other value.
    Non-null values are compared with the provided `comparator`.
    
    @sample samples.comparisons.Comparisons.nullsFirstLastWithComparator

## 声明与重载

### 1. Common

```kotlin
public fun <T : Any> nullsLast(comparator: Comparator<in T>): Comparator<T?>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L250)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T : Comparable<T>> nullsLast(): Comparator<T?>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L266)

提供了无效的 `Comparable` 值的参照,计算值为`null`值大于任何其他值。非null值按其 `natural order` `naturalOrder`值进行比较。

@sample 样本.比较性比较性比较性比较性比较性比较性比较性比较性比较性第一次比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性比较性

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

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf(4, null, -1, 1)

    val nullsFirstList = list.sortedWith(nullsFirst())
    println(nullsFirstList)

    val nullsLastList = list.sortedWith(nullsLast())
    println(nullsLastList)
}
```

```text title="输出"
[null, -1, 1, 4]
[-1, 1, 4, null]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L202)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
