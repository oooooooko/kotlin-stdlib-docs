# toCollection

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将所有元素附加到给定的 `destination` 收藏中。

操作为 _flintinal_。

??? note "查看英文原文"

    Appends all elements to the given `destination` collection.
    
    The operation is _terminal_.

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
public fun <T, C : MutableCollection<in T>> Sequence<T>.toCollection(destination: C): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L968)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*
import java.io.File
import java.io.Reader
import java.io.StringReader
import java.net.URL
import java.util.ArrayList

private fun sample(): Reader = StringReader("Hello\nWorld");

fun main() {

        // TODO we should maybe zap the useLines approach as it encourages
        // use of iterators which don't close the underlying stream
        val list1 = sample().useLines { it.toList() }
        val list2 = sample().useLines<ArrayList<String>>{ it.toCollection(arrayListOf()) }

        println(list1)
        println(list2)
    
}
```

```text title="输出"
[Hello, World]
[Hello, World]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/jvm/test/io/ReadWrite.kt#L153)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
