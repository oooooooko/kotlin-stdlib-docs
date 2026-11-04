# Regex.replaceFirst

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将指定的 `input` 字符串中此正则表达式的首次发生替换为指定的 `replacement` 表达式。

替换字符串中可能包含匹配中被捕获组的引用。 替换字符串中的 `${name}` 或 `$index` 的值将被替换为与指定名称或索引的被捕获组相对应的子序列。 在 `$index` 中, “ $” 之后的第一个数字总是作为群集参考的一部分处理。 只有当后继数字构成有效的群集引用时, 后继数字才被纳入 `index` 。 只有数字 '0'.\\ 9 才会被视为群集引用的潜在组成部分。 注意被捕获组的索引从1开始, 而有指数0的组是整个匹配。 在`${name}` 的情况下, `name` 可以是 latin 字母“ a. z” 和“ A.” 。 “ Z” 或数字“ 0” 。 。 第一个字符必须是字母 。

后斜线字符“\”可以用来将后斜线字符作为替换字符串中的字句包含在内,例如,`\$`或 `\\` .`Regex.escapeReplacement`。 如果必须将`replacement`作为字串处理,则可以使用 `Regex.escapeReplacement` 。

@param 输入字符序列以查找此正则表达式的匹配
@param 替换表达式以替换找到的匹配
@return 将`input`中此正则表达式首次发生的情况替换为对 `replacement` 表达式进行评价的结果
@throws 运行时间例外, 如果 `replacement` 表达式变形, 或捕获指定为 `name` 或 `index` 的组不存在, 则排除此例外

@sample 样本.text.regexps. regexpreserfirst

??? note "查看英文原文"

    Replaces the first occurrence of this regular expression in the specified `input` string with specified `replacement` expression.
    
    The replacement string may contain references to the captured groups during a match. Occurrences of `${name}` or `$index`
    in the replacement string will be substituted with the subsequences corresponding to the captured groups with the specified name or index.
    In case of `$index`, the first digit after '$' is always treated as a part of group reference. Subsequent digits are incorporated
    into `index` only if they would form a valid group reference. Only the digits '0'..'9' are considered as potential components
    of the group reference. Note that indexes of captured groups start from 1, and the group with index 0 is the whole match.
    In case of `${name}`, the `name` can consist of latin letters 'a'..'z' and 'A'..'Z', or digits '0'..'9'. The first character must be
    a letter.
    
    Backslash character '\' can be used to include the succeeding character as a literal in the replacement string, e.g, `\$` or `\\`.
    `Regex.escapeReplacement` can be used if `replacement` have to be treated as a literal string.
    
    @param input the char sequence to find a match of this regular expression in
    @param replacement the expression to replace the found match with
    @return the result of replacing the first occurrence of this regular expression in `input` with the result of evaluating the `replacement` expression
    @throws RuntimeException if `replacement` expression is malformed, or capturing group with specified `name` or `index` does not exist
    
    @sample samples.text.Regexps.replaceFirstWithExpression

## 声明与重载

### 1. Common

```kotlin
public fun replaceFirst(input: CharSequence, replacement: String): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L99)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.text.*

fun main() {
    val source = Regex("[a-z]+")
    val result = source.`replaceFirst`("AQID", "o")
    println(result)
}
```

```text title="输出"
AQID
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
