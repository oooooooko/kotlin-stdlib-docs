# joinToString

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

创建从所有元素中分离的字符串,使用 `separator` 和 如果提供, 则使用给定的 `prefix` 和 `postfix` 。

如果收藏没有元素,结果只包含 `prefix` ,然后是 `postfix` (默认为空)。

如果收藏量巨大, 您可以指定一个非负值为 `limit` , 这样, 首个`limit`元素将被附加, 之后是 `truncated` 字符串( 默认为 "... " )。

操作为 _flintinal_。

@sample 样本、采集、采集、转化、加入String

??? note "查看英文原文"

    Creates a string from all the elements separated using `separator` and using the given `prefix` and `postfix` if supplied.
    
    If the collection has no elements, the result consists of only `prefix` followed by `postfix` (both are empty by default).
    
    If the collection is huge, you can specify a non-negative value of `limit`, in which case only the first `limit`
    elements will be appended, followed by the `truncated` string (which defaults to "...").
    
    The operation is _terminal_.
    
    @sample samples.collections.Collections.Transformations.joinToString

## 声明与重载

### 1. Common

```kotlin
public fun <T> Sequence<T>.joinToString(separator: CharSequence = ", ", prefix: CharSequence = "", postfix: CharSequence = "", limit: Int = -1, truncated: CharSequence = "...", transform: ((T) -> CharSequence)? = null): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3337)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val numbers = listOf(1, 2, 3, 4, 5, 6)
    println(numbers.joinToString())
    println(numbers.joinToString(prefix = "[", postfix = "]"))
    println(numbers.joinToString(prefix = "<", postfix = ">", separator = "•"))

    val chars = charArrayOf('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q')
    println(chars.joinToString(limit = 5, truncated = "...!") { it.uppercaseChar().toString() })

    // If the receiver is empty, the result only contains prefix and postfix
    println(emptyList<Int>().joinToString().isEmpty())
    println(emptyList<Int>().joinToString(prefix = "[", postfix = "]"))
}
```

```text title="输出"
1, 2, 3, 4, 5, 6
[1, 2, 3, 4, 5, 6]
<1•2•3•4•5•6>
A, B, C, D, E, ...!
true
[]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L867)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
