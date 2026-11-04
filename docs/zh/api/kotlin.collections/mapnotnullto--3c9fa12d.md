# mapNotNullTo

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

对原始数组中的每个元素应用给定的 `transform` 函数,并将非nnull 结果附加到给定的 `destination` 。

??? note "查看英文原文"

    Applies the given `transform` function to each element in the original array
    and appends only the non-null results to the given `destination`.

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, R : Any, C : MutableCollection<in R>> Array<out T>.mapNotNullTo(destination: C, transform: (T) -> R?): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13181)

### 2. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, R : Any, C : MutableCollection<in R>> Iterable<T>.mapNotNullTo(destination: C, transform: (T) -> R?): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1804)

对原始收藏中的每个元素应用给定的 `transform` 函数,仅将非nnull 结果附加到给定的 `destination` 。

### 3. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, R : Any, C : MutableCollection<in R>> Map<out K, V>.mapNotNullTo(destination: C, transform: (Map.Entry<K, V>) -> R?): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L142)

对原始地图中的每个条目应用给定的 `transform` 函数,并将非nnull 结果附加到给定的 `destination` 。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() {
    println(listOf(1, 2).flatMapTo(mutableListOf<Int>()) { listOf(it, -it) })
    println(listOf(1, 2).flatMapIndexedTo(mutableListOf<Int>()) { index, value -> listOf(index, value) })
    println(listOf(1, 2).mapTo(mutableListOf<String>()) { "v$it" })
    println(listOf(1, 2).mapIndexedTo(mutableListOf<String>()) { index, value -> "$index:$value" })
    println(listOf(1, 2).mapNotNullTo(mutableListOf<Int>()) { it.takeIf { n -> n > 1 } })
    println(listOf(1, 2).mapIndexedNotNullTo(mutableListOf<Int>()) { index, value -> value.takeIf { index > 0 } })
    val values = linkedMapOf("a" to 1, "b" to 2)
    println(values.mapKeysTo(linkedMapOf<String, Int>()) { it.key.uppercase() })
    println(values.mapValues { it.value * 10 })
    println(values.mapValuesTo(linkedMapOf<String, Int>()) { it.value * 10 })
}
```

```text title="输出"
[1, -1, 2, -2]
[0, 1, 1, 2]
[v1, v2]
[0:1, 1:2]
[2]
[2]
{A=1, B=2}
{a=10, b=20}
{a=10, b=20}
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
