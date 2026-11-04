# SequenceScope.yield

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将正在建造的`Iterator`的值进行成数值,并暂停到下一个值要求时。

@sample 样本、采集量、序列、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、建筑、

??? note "查看英文原文"

    Yields a value to the `Iterator` being built and suspends
    until the next value is requested.
    
    @sample samples.collections.Sequences.Building.buildSequenceYieldAll
    @sample samples.collections.Sequences.Building.buildFibonacciSequence

## 声明与重载

### 1. Common

```kotlin
public abstract suspend fun yield(value: T)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/SequenceBuilder.kt#L90)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*



fun main() {

        val result = sequence {
            yieldAll(listOf(1, 2, 3))
            yield(4)
        }
        println(result.toList())
    
}
```

```text title="输出"
[1, 2, 3, 4]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/coroutines/SequenceBuilderTest.kt#L186)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
