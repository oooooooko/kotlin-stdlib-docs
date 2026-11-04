# commonPrefixWith

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回最长的字符串 `prefix` , 使此字符串序列和 `other` 字符序列都以此前缀开始, 注意不要分割代理配对。 如果此字符串和 `other` 没有共同的前缀, 请返回空字符串 。

@param 忽略Case `true` 以忽略匹配字符的字符大小写 。 默认为 `false`。
@sample 样本. text. strings. 普通 Prefix

??? note "查看英文原文"

    Returns the longest string `prefix` such that this char sequence and `other` char sequence both start with this prefix,
    taking care not to split surrogate pairs.
    If this and `other` have no common prefix, returns the empty string.
    
    @param ignoreCase `true` to ignore character case when matching a character. By default `false`.
    @sample samples.text.Strings.commonPrefixWith

## 声明与重载

### 1. Common

```kotlin
public fun CharSequence.commonPrefixWith(other: CharSequence, ignoreCase: Boolean = false): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L921)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println("Hot_Coffee".commonPrefixWith("Hot_cocoa"))
    println("Hot_Coffee".commonPrefixWith("Hot_cocoa", true))
    println("Hot_Coffee".commonPrefixWith("Iced_Coffee"))
}
```

```text title="输出"
Hot_
Hot_Co
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L432)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
