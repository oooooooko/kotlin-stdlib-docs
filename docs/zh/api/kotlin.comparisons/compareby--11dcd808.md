# compareBy

`kotlin.comparisons` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

创建参照方,使用函数序列来计算比较结果。函数顺序命名,接收给定值 `a` 和 `b` ,并返回`Comparable`对象。当`Comparable` 参数被函数返回,返回值为 8,0000005和 `b` 时,当`a` 和 `b` 值的数值不以等值比较时,比较结果从 `Comparator` 返回。

@sample 样本.比较.比较.比较.比较.比较.比较.与选择者比较

??? note "查看英文原文"

    Creates a comparator using the sequence of functions to calculate a result of comparison.
    The functions are called sequentially, receive the given values `a` and `b` and return `Comparable`
    objects. As soon as the `Comparable` instances returned by a function for `a` and `b` values do not
    compare as equal, the result of that comparison is returned from the `Comparator`.
    
    @sample samples.comparisons.Comparisons.compareByWithSelectors

## 声明与重载

### 1. Common

```kotlin
public fun <T> compareBy(vararg selectors: (T) -> Comparable<*>?): Comparator<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L80)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> compareBy(crossinline selector: (T) -> Comparable<*>?): Comparator<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L94)

创建参照方,使用该函数将值转换为`Comparable`实例,以进行比较。

@sample 样本.比较.比较.比较.比较.比较.比较.比较.与单一选择器比

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T, K> compareBy(comparator: Comparator<in K>, crossinline selector: (T) -> K): Comparator<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L103)

创建参照方,使用 `selector` 函数来转换要比较的值,然后应用指定的 `comparator` 来比较已变的值。

@sample 样本.比较.比较.比较.比较.比较.比较.比较.与比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较. 比较.比较.比较.比较. 比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较.比较. 比较.比较.比较.比较. 比较.比较. 比较.比较. 比较. 比较.比较. 比较. 比较. 比较. 比较.比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 与比较. 与比较. 比较. 与比较. 比较. 比较. 比较. 比较. 比较. 与比较. 比较. 比较. 比较. 比较. 比较. 与比较. 与比较. 比较. 与比较.

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf("aa", "b", "bb", "a")

    val sorted = list.sortedWith(compareBy(
        { it.length },
        { it }
    ))

    println(sorted)
}
```

```text title="输出"
[a, b, aa, bb]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L75)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf("aa", "b", "bb", "a")

    val sorted = list.sortedWith(compareBy { it.length })

    println(sorted)
}
```

```text title="输出"
[b, a, aa, bb]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L66)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf('B', 'a', 'A', 'b')

    val sorted = list.sortedWith(
        compareBy(String.CASE_INSENSITIVE_ORDER) { v -> v.toString() }
    )

    println(sorted)
}
```

```text title="输出"
[a, A, B, b]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L87)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
