# any

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果序列至少有一个元素,则返回`true`。

操作为 _flintinal_。

@sample 样本、采集的样本、采集的样本、采集的样本、分类的样本、

??? note "查看英文原文"

    Returns `true` if sequence has at least one element.
    
    The operation is _terminal_.
    
    @sample samples.collections.Collections.Aggregates.any

## 声明与重载

### 1. Common

```kotlin
public fun <T> Sequence<T>.any(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1559)

### 2. Common

```kotlin
public inline fun <T> Sequence<T>.any(predicate: (T) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L1570)

如果至少有一个元素与给定的`predicate`值相符,则返回`true`。

操作为 _flintinal_。

@sample 样本、采集的样本、采集的采集资料、分类、任何

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val emptyList = emptyList<Int>()
    println(emptyList.any())

    val nonEmptyList = listOf(1, 2, 3)
    println(nonEmptyList.any())
}
```

```text title="输出"
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1020)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val isEven: (Int) -> Boolean = { it % 2 == 0 }
    val zeroToTen = 0..10
    println(zeroToTen.any { isEven(it) })
    println(zeroToTen.any(isEven))

    val odds = zeroToTen.map { it * 2 + 1 }
    println(odds.any { isEven(it) })

    val emptyList = emptyList<Int>()
    println(emptyList.any { true })
}
```

```text title="输出"
true
true
false
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1029)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
