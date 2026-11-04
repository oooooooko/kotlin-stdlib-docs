# replace

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回新字符串, 以 `newChar` 取代所有 `oldChar` 。

@sample 样本.text.Strings.replace

??? note "查看英文原文"

    Returns a new string with all occurrences of `oldChar` replaced with `newChar`.
    
    @sample samples.text.Strings.replace

## 声明与重载

### 1. Common

```kotlin
public expect fun String.replace(oldChar: Char, newChar: Char, ignoreCase: Boolean = false): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L414)

### 2. Common

```kotlin
public expect fun String.replace(oldValue: String, newValue: String, ignoreCase: Boolean = false): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L421)

返回新字符串, 以指定的 `newValue` 字符串替换此字符串中`oldValue` 子字符串的所有发生。

@sample 样本.text.Strings.replace

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharSequence.replace(regex: Regex, replacement: String): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L786)

将在此字符序列中指定的正则表达式 `regex` 的所有发生替换为指定的 `replacement` 表达式。

这是一个相当于 `regex.replace(this, replacement)` 的便利功能。 关于其行为和替代语法( `replacement` 表达式)的详细信息,请参见 `Regex.replace` 。

@sample 样本.text.Strings.replaced

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharSequence.replace(regex: Regex, noinline transform: (MatchResult) -> CharSequence): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L798)

返回新字符串, 替换此字符串序列的每个子字符串, 以匹配给定正则表达式和给定函数 `transform` 的结果, 需要 `MatchResult` , 返回要用来替换此字符串的字符串 。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val inputString0 = "Mississippi"
    val inputString1 = "Insufficient data for meaningful answer."

    println(inputString0.replace('s', 'z'))
    println(inputString1.replace("data", "information"))
}
```

```text title="输出"
Mizzizzippi
Insufficient information for meaningful answer.
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L612)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val text = "The events are on 15-09-2024 and 16-10-2024."
    // Regex to match dates in dd-mm-yyyy format
    val dateRegex = "(?<day>\\d{2})-(?<month>\\d{2})-(?<year>\\d{4})".toRegex()
    // Replacement expression that puts day, month and year values in the ISO 8601 recommended yyyy-mm-dd format
    val replacement = "\${year}-\${month}-\${day}"

    // Replacing all occurrences of dates from dd-mm-yyyy to yyyy-mm-dd format
    println(text.replace(dateRegex, replacement))

    // One can also reference the matched groups by index
    println(text.replace(dateRegex, "$3-$2-$1"))

    // Using a backslash to include the special character '$' as a literal in the result
    println(text.replace(dateRegex, "$3-\\$2-$1"))
}
```

```text title="输出"
The events are on 2024-09-15 and 2024-10-16.
The events are on 2024-09-15 and 2024-10-16.
The events are on 2024-$2-15 and 2024-$2-16.
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L925)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
