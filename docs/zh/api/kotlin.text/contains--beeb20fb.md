# contains

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果此字符序列包含指定的 `other` 字符序列作为子字符串,则返回 `true` 。

@param 忽略Case `true` 来比较字符串时忽略字符 。 默认为 `false`。
@sample 样本. text. strings. contains

??? note "查看英文原文"

    Returns `true` if this char sequence contains the specified `other` sequence of characters as a substring.
    
    @param ignoreCase `true` to ignore character case when comparing strings. By default `false`.
    @sample samples.text.Strings.contains

## 声明与重载

### 1. Common

```kotlin
@Suppress("INAPPLICABLE_OPERATOR_MODIFIER")
public operator fun CharSequence.contains(other: CharSequence, ignoreCase: Boolean = false): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1183)

### 2. Common

```kotlin
@Suppress("INAPPLICABLE_OPERATOR_MODIFIER")
public operator fun CharSequence.contains(char: Char, ignoreCase: Boolean = false): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1198)

如果字符序列包含指定的字符 `char` , 则返回 `true` 。

@param 忽略Case `true` 来忽略字符 。 默认为 `false`。
@sample样本. text. strings. containsChar

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun CharSequence.contains(regex: Regex): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1208)

如果此字符序列含有至少一个符合指定的正则表达式 `regex` 的值,则返回 `true` 。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val string = "Kotlin 2.2.0"
    println("K" in string)

    // The string only contains capital K
    println("k" in string)
    // However, it will be located if the case is ignored
    println(string.contains("k", ignoreCase = true))

    // Every string contains an empty string
    println("" in string)
    // The string contains itself ...
    println(string in string)
    // ... even if it is empty
    println("" in "")

    // String's prefix is shorter than a string, so it can't contain it
    println(string in "Kotlin")
}
```

```text title="输出"
true
false
true
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L561)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val text = "kotlin"

    // The string contains lowercase 'k'
    println('k' in text)

    // The string does not contain uppercase 'K' (case-sensitive check)
    println('K' in text)

    // However, it will be located if the case is ignored
    println(text.contains('K', ignoreCase = true))

    // The string does not contain 'z'
    println('z' in text)
}
```

```text title="输出"
true
false
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L582)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
