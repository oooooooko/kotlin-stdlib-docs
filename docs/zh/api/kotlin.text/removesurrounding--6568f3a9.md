# removeSurrounding

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

当此字符序列从给定的 `prefix` 开始, 以给定的 `suffix` 结束时, 返回一个新字符序列, 并同时删除给定的 `prefix` 和 `suffix` 。 否则, 返回一个带有相同字符的新的字符序列 。

@sample 样本.text.Strings.remove 环绕前六六后六

??? note "查看英文原文"

    When this char sequence starts with the given `prefix` and ends with the given `suffix`,
    returns a new char sequence having both the given `prefix` and `suffix` removed.
    Otherwise, returns a new char sequence with the same characters.
    
    @sample samples.text.Strings.removeSurroundingPrefixSuffixCharSequence

## 声明与重载

### 1. Common

```kotlin
public fun CharSequence.removeSurrounding(prefix: CharSequence, suffix: CharSequence): CharSequence
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L664)

### 2. Common

```kotlin
public fun String.removeSurrounding(prefix: CharSequence, suffix: CharSequence): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L678)

从给定的 `prefix` 和 `suffix` 字符串中删除, 如果且只有以 `prefix` 开头, 并以 `suffix` 结尾。 否则, 返回此字符串, 不变 。

@sample 样本.text.Strings.remove 环绕前六六后六

### 3. Common

```kotlin
public fun CharSequence.removeSurrounding(delimiter: CharSequence): CharSequence
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L692)

当此字符序列以给定 `delimiter` 开始和结束时, 返回从开始和结束时删除的新的字符序列。 否则, 返回一个带有相同字符的新的字符序列 。

@sample 样本.text.Strings.remove 环绕环绕

### 4. Common

```kotlin
public fun String.removeSurrounding(delimiter: CharSequence): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L701)

如果且只有在 `delimiter` 以该字符串开头和结尾开始和结束时才从此字符串的开头和结尾中删除给定的 `delimiter` 字符串。 否则, 返回此字符串, 不变 。

@sample 样本.text.Strings.remove 环绕环绕

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val textCharSequence: CharSequence = StringBuilder("[content]")
    println(textCharSequence.removeSurrounding("[", "]"))
    // Does not start with prefix
    println(StringBuilder("content]").removeSurrounding("[", "]"))
    // Does not end with suffix
    println(StringBuilder("[content").removeSurrounding("[", "]"))
    // Does not start or end with prefix/suffix
    println(StringBuilder("content").removeSurrounding("[", "]"))
    // Empty content
    println(StringBuilder("[]").removeSurrounding("[", "]"))
    // Different delimiters
    println(StringBuilder("<content>").removeSurrounding("[", "]"))
}
```

```text title="输出"
content
content]
[content
content

<content>
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L1068)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val textString = "[content]"
    println(textString.removeSurrounding("[", "]"))
    // Does not start with prefix
    println("content]".removeSurrounding("[", "]"))
    // Does not end with suffix
    println("[content".removeSurrounding("[", "]"))
    // Does not start or end with prefix/suffix
    println("content".removeSurrounding("[", "]"))
    // Empty content
    println("[]".removeSurrounding("[", "]"))
    // Different delimiters
    println("<content>".removeSurrounding("[", "]"))
}
```

```text title="输出"
content
content]
[content
content

<content>
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L1052)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val textCharSequence: CharSequence = StringBuilder("***content***")
    println(textCharSequence.removeSurrounding("***"))
    // Does not end with delimiter
    println(StringBuilder("##content").removeSurrounding("##"))
    // Does not start with delimiter
    println(StringBuilder("content##").removeSurrounding("##"))
    // No delimiters
    println(StringBuilder("content").removeSurrounding("##"))
    // Empty content
    println(StringBuilder("****").removeSurrounding("**"))
    // Delimiter is single char, removes only one pair
    println(StringBuilder("!!!content!!!").removeSurrounding("!"))
}
```

```text title="输出"
content
##content
content##
content

!!content!!
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L1100)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val textString = "***content***"
    println(textString.removeSurrounding("***"))
    // Does not end with delimiter
    println("##content".removeSurrounding("##"))
    // Does not start with delimiter
    println("content##".removeSurrounding("##"))
    // No delimiters
    println("content".removeSurrounding("##"))
    // Empty content
    println("****".removeSurrounding("**"))
    // Delimiter is single char, removes only one pair
    println("!!!content!!!".removeSurrounding("!"))
}
```

```text title="输出"
content
##content
content##
content

!!content!!
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L1084)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
