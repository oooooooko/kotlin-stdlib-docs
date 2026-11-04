# thenBy

`kotlin.comparisons` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

在主比较国将数值确定为等值后,创建一个比较比较值的参照国。它使用该函数将数值转换为`Comparable`例,以进行比较。

@sample 样本.比较.比较.比较.然后

??? note "查看英文原文"

    Creates a comparator comparing values after the primary comparator defined them equal. It uses
    the function to transform value to a `Comparable` instance for comparison.
    
    @sample samples.comparisons.Comparisons.thenBy

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Comparator<T>.thenBy(crossinline selector: (T) -> Comparable<*>?): Comparator<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L134)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T, K> Comparator<T>.thenBy(comparator: Comparator<in K>, crossinline selector: (T) -> K): Comparator<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L147)

在主比较国对数值进行等值定义后,建立一个比较比较国,使用`selector`函数转换数值,然后与给定的`comparator`数值进行比较。

@sample 样本.比较.比较.比较.然后与比较者比较.

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf("aa", "b", "bb", "a")

    val lengthComparator = compareBy<String> { it.length }
    println(list.sortedWith(lengthComparator))

    val lengthThenString = lengthComparator.thenBy { it }
    println(list.sortedWith(lengthThenString))
}
```

```text title="输出"
[b, a, aa, bb]
[a, b, aa, bb]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L118)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf("A", "aa", "b", "bb", "a")

    val lengthComparator = compareBy<String> { it.length }
    println(list.sortedWith(lengthComparator))

    val lengthThenCaseInsensitive = lengthComparator
        .thenBy(String.CASE_INSENSITIVE_ORDER) { it }
    println(list.sortedWith(lengthThenCaseInsensitive))
}
```

```text title="输出"
[A, b, a, aa, bb]
[A, a, b, aa, bb]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L129)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
