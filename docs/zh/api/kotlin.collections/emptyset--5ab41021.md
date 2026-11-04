# emptySet

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个只读的空集。 返回的集是可序列的( JVM) 。 @sample 样本. collects. Sets. srevenyRead OnlySet

??? note "查看英文原文"

    Returns an empty read-only set.  The returned set is serializable (JVM).
    @sample samples.collections.Collections.Sets.emptyReadOnlySet

## 声明与重载

### 1. Common

```kotlin
public fun <T> emptySet(): Set<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sets.kt#L32)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val set = setOf<String>()
    println(set.isEmpty())

    // another way to create an empty set,
    // type parameter is inferred from the expected type
    val other: Set<Int> = emptySet()

    println(set == other)
    println(set)
}
```

```text title="输出"
true
true
[]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L565)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
