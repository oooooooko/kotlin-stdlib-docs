# zip

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个从 `this` 字符和 `other` 字符序列中构建的配对列表, 并具有相同的索引。 返回列表的长度为最短的字符序列 。

@sample 样本. 文本. Strings.zip

??? note "查看英文原文"

    Returns a list of pairs built from the characters of `this` and the `other` char sequences with the same index
    The returned list has length of the shortest char sequence.
    
    @sample samples.text.Strings.zip

## 声明与重载

### 1. Common

```kotlin
public infix fun CharSequence.zip(other: CharSequence): List<Pair<Char, Char>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L2515)

### 2. Common

```kotlin
public inline fun <V> CharSequence.zip(other: CharSequence, transform: (a: Char, b: Char) -> V): List<V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L2525)

返回从 `this` 字符和`other`字符序列中构建的数值列表,这些字符序列使用对每对字符适用的`transform`函数,与同一种索引。返回的列表长度为最短字符序列。

@sample 样本.text.Strings.zipOf Transform

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val stringA = "abcd"
    val stringB = "zyx"
    println(stringA zip stringB)
}
```

```text title="输出"
[(a, z), (b, y), (c, x)]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L174)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val stringA = "abcd"
    val stringB = "zyx"
    val result = stringA.zip(stringB) { a, b -> "$a$b" }
    println(result)
}
```

```text title="输出"
[az, by, cx]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L181)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
