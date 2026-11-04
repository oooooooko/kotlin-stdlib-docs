# compareValuesBy

`kotlin.comparisons` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

比较两个值, 使用指定的函数 `selectors` 来计算比较结果。 函数顺序调用, 接收给定值 `a` 和 `b` , 并返回 `Comparable` 对象。 当 `a` 和 `b` 等值函数返回 `Comparable` 时, 比较结果将被返回 。

@sample 样本.比较.比较.比较.比较.比较.比较.比较与选择者比较

??? note "查看英文原文"

    Compares two values using the specified functions `selectors` to calculate the result of the comparison.
    The functions are called sequentially, receive the given values `a` and `b` and return `Comparable`
    objects. As soon as the `Comparable` instances returned by a function for `a` and `b` values do not
    compare as equal, the result of that comparison is returned.
    
    @sample samples.comparisons.Comparisons.compareValuesByWithSelectors

## 声明与重载

### 1. Common

```kotlin
public fun <T> compareValuesBy(a: T, b: T, vararg selectors: (T) -> Comparable<*>?): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L10)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> compareValuesBy(a: T, b: T, selector: (T) -> Comparable<*>?): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L33)

比较两个值, 使用指定的 `selector` 函数计算比较结果。 该函数应用到给定值 `a` 和 `b` , 并返回 `Comparable` 对象。 返回了这些 8,0000005 实例的比较结果 。

@sample 样本.比较.比较.比较.比较.比较.比较.比较.比较 与单一选择器比较

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T, K> compareValuesBy(a: T, b: T, comparator: Comparator<in K>, selector: (T) -> K): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L45)

比较两个值, 使用指定的 `selector` 函数计算比较结果。 该函数应用到给定值 `a` 和 `b` , 然后返回 K 类型的对象, 然后将对象与给定的 `comparator` 比较 。

@sample 样本.比较.比较.比较.比较.比较.比较.比较.比较.比较.估价. 与比较比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较.比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较. 比较.

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    fun compareLengthThenString(a: String, b: String): Int =
        compareValuesBy(a, b, { it.length }, { it })

    println(compareLengthThenString("b", "aa") < 0)

    println(compareLengthThenString("a", "b") < 0)
    println(compareLengthThenString("b", "a") > 0)
    println(compareLengthThenString("a", "a") == 0)
}
```

```text title="输出"
true
true
true
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L33)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    fun compareLength(a: String, b: String): Int =
        compareValuesBy(a, b) { it.length }

    println(compareLength("a", "b") == 0)
    println(compareLength("bb", "a") > 0)
    println(compareLength("a", "bb") < 0)
}
```

```text title="输出"
true
true
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L23)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    fun compareInsensitiveOrder(a: Char, b: Char): Int =
        compareValuesBy(a, b, String.CASE_INSENSITIVE_ORDER, { c -> c.toString() })

    println(compareInsensitiveOrder('a', 'a') == 0)
    println(compareInsensitiveOrder('a', 'A') == 0)

    println(compareInsensitiveOrder('a', 'b') < 0)
    println(compareInsensitiveOrder('A', 'b') < 0)
    println(compareInsensitiveOrder('b', 'a') > 0)
}
```

```text title="输出"
true
true
true
true
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L45)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
