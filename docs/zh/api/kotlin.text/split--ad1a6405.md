# split

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将此字符序列分割为一个串列列表, 围绕指定的 `delimiters` 的发生时间进行 。

生成列表的最后元素对应的是一个子序列, 起始于上次的分隔符发生之后( 或此字符序列开始时没有发生) , 结束于此字符序列的结尾。 这意味着如果此字符序列不包含 `delimiters`, 则该生成列表将包含一个与整个字符序列相对应的元素。 它还意味着对于以 `delimiters` 结尾的字符序列序列, 其结果列表将用空字符串结束 。

为了避免在`delimiters`字符串中字符共用时产生模糊的结果,这种方法从此字符串的开头到结尾,并在每个位置匹配`delimiters`中的第一个元素,该元素相当于该位置的分隔符。

@param 划界器 @param 指定一个或多个字符串用作划界器。 @param 忽略 Case `true` 匹配一个分隔器时忽略字符设置。 默认情况下 `false`。 @param 限制返回子字符串的最大数量。 默认为零意味着没有设定限制 。

@sample 样本. 文本. 星环. 与星环相分割

??? note "查看英文原文"

    Splits this char sequence to a list of strings around occurrences of the specified `delimiters`.
    
    The last element of the resulting list corresponds to a subsequence starting right after the last
    delimiter occurrence (or at the beginning of this char sequence if there were no such occurrences)
    and ending at the end of this char sequence. That implies that if this char sequence does not
    contain `delimiters`, the resulting list will contain a single element corresponding to
    the whole char sequence. It also implies that for char sequences ending with one of `delimiters`,
    the resulting list will end with an empty string.
    
    To avoid ambiguous results when strings in `delimiters` have characters in common, this method proceeds from
    the beginning to the end of this string, and matches at each position the first element in `delimiters`
    that is equal to a delimiter in this instance at that position.
    
    @param delimiters One or more strings to be used as delimiters.
    @param ignoreCase `true` to ignore character case when matching a delimiter. By default `false`.
    @param limit The maximum number of substrings to return. Zero by default means no limit is set.
    
    @sample samples.text.Strings.splitWithStringDelimiters

## 声明与重载

### 1. Common

```kotlin
public fun CharSequence.split(vararg delimiters: String, ignoreCase: Boolean = false, limit: Int = 0): List<String>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1406)

### 2. Common

```kotlin
public fun CharSequence.split(vararg delimiters: Char, ignoreCase: Boolean = false, limit: Int = 0): List<String>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1456)

将此字符序列分割为一个串列列表, 围绕指定的 `delimiters` 的发生时间进行 。

生成列表的最后元素对应的是一个子序列, 起始于上次的分隔符发生之后( 或此字符序列开始时没有发生) , 结束于此字符序列的结尾。 这意味着如果此字符序列不包含 `delimiters`, 则该生成列表将包含一个与整个字符序列相对应的元素。 它还意味着对于以 `delimiters` 结尾的字符序列序列, 其结果列表将用空字符串结束 。

@param 划界器 将使用一个或多个字符作为划界器 。 @param 忽略 `true` 号 , 在匹配分隔器时忽略字符 。 默认情况下 `false`. @param 限制 子字符串的最大返回次数 。 @sample 样本. text. Strings.split withoutCharDescripters

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharSequence.split(regex: Regex, limit: Int = 0): List<String>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1517)

将此字符序列分割为一个字符串列表, 以匹配给定正则表达式的字符串列表 。

生成列表的最后元素对应于上次 `regex` 匹配( 或此字符序列的起始时没有匹配) 之后开始的子序列, 并在此字符序列的结尾处结束。 这意味着如果此字符序列中不包含匹配 `regex` 的子序列, 则该生成列表将包含一个与整个字符序列相对应的单个元素。 它还意味着对于以 `regex` 匹配结束的字符序列, 由此产生的列表将用空字符串结束 。

@param 限制 @param 非负值 指定返回子字符串的最大数量 。 默认为零 表示没有设定限制 。 @sample 样本. text. strings. plit withRegex

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val multiCharDelimiter = "apple--banana--cherry".split("--")
    println(multiCharDelimiter)

    val multipleSplit = "apple->banana;;cherry:::orange".split("->", ";;", ":::")
    println(multipleSplit)

    val longerDelimiterFirst = "apple<-banana<--cherry".split("<--", "<-")
    println(longerDelimiterFirst)

    val shorterDelimiterFirst = "apple<-banana<--cherry".split("<-", "<--")
    println(shorterDelimiterFirst)

    val limitSplit = "a->b->c->d->e".split("->", limit = 3)
    println(limitSplit)

    val emptyInputResult = "".split("sep")
    println(emptyInputResult == listOf(""))

    val emptyDelimiterSplit = "abc".split("")
    println(emptyDelimiterSplit)

    val mixedCase = "abcXYZdef".split("xyz")
    println(mixedCase)  // No match with case sensitivity

    val mixedCaseIgnored = "abcXYZdef".split("xyz", ignoreCase = true)
    println(mixedCaseIgnored)  // Matches with case insensitivity

    val emptyResults = "##a##b##c##".split("##")
    println(emptyResults)

    val consecutiveSeparators = "a--b------c".split("--")
    println(consecutiveSeparators)
}
```

```text title="输出"
[apple, banana, cherry]
[apple, banana, cherry, orange]
[apple, banana, cherry]
[apple, banana, -cherry]
[a, b, c->d->e]
true
[, a, b, c, ]
[abcXYZdef]
[abc, def]
[, a, b, c, ]
[a, b, , , c]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L672)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val commaSplit = "apple,banana,cherry".split(',')
    println(commaSplit)

    val charSplit = "apple,banana;cherry".split(',', ';')
    println(charSplit)

    val limitSplit = "a,b,c,d,e".split(',', limit = 3)
    println(limitSplit)

    val emptyInputResult = "".split('|')
    println(emptyInputResult == listOf(""))

    val mixedCase = "abcXdef".split('x')
    println(mixedCase)  // No match with case sensitivity

    val mixedCaseIgnored = "abcXdef".split('x', ignoreCase = true)
    println(mixedCaseIgnored)  // Matches with case insensitivity

    val emptyResults = ",a,b,c,".split(',')
    println(emptyResults)

    val consecutiveSeparators = "a,,b,,,c".split(',')
    println(consecutiveSeparators)
}
```

```text title="输出"
[apple, banana, cherry]
[apple, banana, cherry]
[a, b, c,d,e]
true
[abcXdef]
[abc, def]
[, a, b, c, ]
[a, , b, , , c]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L746)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val digitSplit = "apple123banana456cherry".split(Regex("\\d+"))
    println(digitSplit)

    val wordBoundarySplit = "The quick brown fox".split(Regex("\\s+"))
    println(wordBoundarySplit)

    val limitSplit = "a,b,c,d,e".split(Regex(","), limit = 3)
    println(limitSplit)

    val patternGroups = "abc-123def_456ghi".split(Regex("[\\-_]\\d+"))
    println(patternGroups)

    val caseInsensitiveSplit = "Apple123Banana45CHERRY".split(Regex("[a-z]+", RegexOption.IGNORE_CASE))
    println(caseInsensitiveSplit)

    val emptyInputResult = "".split(Regex("sep"))
    println(emptyInputResult == listOf(""))

    val emptyDelimiterSplit = "abc".split(Regex(""))
    println(emptyDelimiterSplit)

    val splitByMultipleSpaces = "a  b    c".split(Regex("\\s+"))
    println(splitByMultipleSpaces)

    val splitBySingleSpace = "a  b    c".split(Regex("\\s"))
    println(splitBySingleSpace)
}
```

```text title="输出"
[apple, banana, cherry]
[The, quick, brown, fox]
[a, b, c,d,e]
[abc, def, ghi]
[, 123, 45, ]
true
[, a, b, c, ]
[a, b, c]
[a, , b, , , , c]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L802)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
