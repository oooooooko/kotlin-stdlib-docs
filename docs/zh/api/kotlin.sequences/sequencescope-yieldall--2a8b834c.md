# SequenceScope.yieldAll

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将从`iterator`到正在建造的`Iterator`的所有值都投入使用,并暂停使用,直到所有这些值都循环并请求下一个值。

给定迭代器返回的值序列可能无限。

@sample 样本、采集资料、序列、建筑、建立序列

??? note "查看英文原文"

    Yields all values from the `iterator` to the `Iterator` being built
    and suspends until all these values are iterated and the next one is requested.
    
    The sequence of values returned by the given iterator can be potentially infinite.
    
    @sample samples.collections.Sequences.Building.buildSequenceYieldAll

## 声明与重载

### 1. Common

```kotlin
public abstract suspend fun yieldAll(iterator: Iterator<T>)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/SequenceBuilder.kt#L99)

### 2. Common

```kotlin
public suspend fun yieldAll(elements: Iterable<T>)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/SequenceBuilder.kt#L109)

生成`Iterator`的数值集合, 并暂停, 直到所有这些值都迭接, 并请求下一个值 。

@sample 样本、采集资料、序列、建筑、建立序列

### 3. Common

```kotlin
public suspend fun yieldAll(sequence: Sequence<T>): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/SequenceBuilder.kt#L120)

可能使`Iterator`的数值序列无限,直到所有这些数值被迭接,下一个数值被请求,然后才能完成。

序列可能是无限的

@sample 样本、采集资料、序列、建筑、建立序列

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*



fun main() {

        val result = sequence<Int> {
            yieldAll(listOf())
        }
        println(result.toList())
    
}
```

```text title="输出"
[]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/coroutines/SequenceBuilderTest.kt#L220)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
