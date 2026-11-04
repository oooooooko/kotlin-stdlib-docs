# flatMap

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回从 `transform` 函数结果中得出的所有元素的单列列表,这些函数在原始字符序列的每个字符序列中被引用。

@sample 样本、采集、采集、变形、平流图

??? note "查看英文原文"

    Returns a single list of all elements yielded from results of `transform` function being invoked on each character of original char sequence.
    
    @sample samples.collections.Collections.Transformations.flatMap

## 声明与重载

### 1. Common

```kotlin
public inline fun <R> CharSequence.flatMap(transform: (Char) -> Iterable<R>): List<R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L856)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = listOf("123", "45")
    println(list.flatMap { it.toList() })
}
```

```text title="输出"
[1, 2, 3, 4, 5]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L897)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
