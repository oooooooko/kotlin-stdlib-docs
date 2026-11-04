# splitToSequence

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将此字符序列分割为串序列, 围绕指定的 `delimiters` 的发生时间进行 。

由此而来序列的最后元素对应的是一个子序列,它从上次的分隔符发生(或者如果没有此字符发生,则从此字符序列的起始处开始)开始,到此字符序列结束。这意味着如果此字符序列不包含`delimiters`, 则该字符序列产生的序列将包含一个与整个字符序列相应的单个元素。它还意味着,对于以 `delimiters` 为结尾的字符序列, 其结果序列将用空字符串结束。

为了避免在`delimiters` 字符串中字符共的模糊结果, 这种方法从此字符串的开头到结尾, 在每个位置上都发现 `delimiters` 中的第一个元素与该字符串相同 。

@param 划界器 @param 指定一个或多个字符串用作划界器。 @param 忽略 Case `true` 匹配一个分隔器时忽略字符设置。 默认情况下 `false`。 @param 限制返回子字符串的最大数量。 默认为零意味着没有设定限制 。

@sample 样本.text.Strings.sblits. 与 Strings 序列的分隔符

??? note "查看英文原文"

    Splits this char sequence to a sequence of strings around occurrences of the specified `delimiters`.
    
    The last element of the resulting sequence corresponds to a subsequence starting right after the last
    delimiter occurrence (or at the beginning of this char sequence if there were no such occurrences)
    and ending at the end of this char sequence. That implies that if this char sequence does not
    contain `delimiters`, the resulting sequence will contain a single element corresponding to
    the whole char sequence. It also implies that for char sequences ending with one of `delimiters`,
    the resulting sequence will end with an empty string.
    
    To avoid ambiguous results when strings in `delimiters` have characters in common, this method proceeds from
    the beginning to the end of this string, and finds at each position the first element in `delimiters`
    that matches this string at that position.
    
    @param delimiters One or more strings to be used as delimiters.
    @param ignoreCase `true` to ignore character case when matching a delimiter. By default `false`.
    @param limit The maximum number of substrings to return. Zero by default means no limit is set.
    
    @sample samples.text.Strings.splitToSequenceWithStringDelimiters

## 声明与重载

### 1. Common

```kotlin
public fun CharSequence.splitToSequence(vararg delimiters: String, ignoreCase: Boolean = false, limit: Int = 0): Sequence<String>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1383)

### 2. Common

```kotlin
public fun CharSequence.splitToSequence(vararg delimiters: Char, ignoreCase: Boolean = false, limit: Int = 0): Sequence<String>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1437)

将此字符序列分割为串序列, 围绕指定的 `delimiters` 的发生时间进行 。

由此而来序列的最后元素对应的是一个子序列,它从上次的分隔符发生(或者如果没有此字符发生,则从此字符序列的起始处开始)开始,到此字符序列结束。这意味着如果此字符序列不包含`delimiters`, 则该字符序列产生的序列将包含一个与整个字符序列相应的单个元素。它还意味着,对于以 `delimiters` 为结尾的字符序列, 其结果序列将用空字符串结束。

@param 划界器 将使用一个或多个字符作为划界器 。 @param 忽略 Case `true` , 以忽略字符 。 默认情况下 , `false`. @param 限制 返回的子字符串的最大数量 。

@sample 样本.text.Strings.sblit 与Char Determinalers的序列

### 3. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
public inline fun CharSequence.splitToSequence(regex: Regex, limit: Int = 0): Sequence<String>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1535)

将此字符序列分割为字符串序列, 围绕给定正则表达式的匹配进行 。

生成序列的最后元素对应于上次 `regex` 匹配( 或此字符序列的起始时没有匹配) 之后开始的子序列, 并结束于此字符序列的结尾。 这意味着如果此字符序列中不包含与 `regex` 匹配的子序列, 则该生成序列中将包含一个与整个字符序列相对应的单个元素。 它还意味着对于以 `regex` 匹配结束的字符序列, 其结果序列将用空字符串结束 。

@param 限制 @param 限制 非负值 指定返回子字符串的最大数量 。 默认为零 表示没有设定限制 。 @sample 样本. text. strings. plit To Actuce

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    fun Sequence<String>.toPrettyString() = joinToString(", ", "[", "]")

    val multiCharDelimiter = "apple--banana--cherry".splitToSequence("--").toPrettyString()
    println(multiCharDelimiter)

    val multipleSplit = "apple->banana;;cherry:::orange".splitToSequence("->", ";;", ":::").toPrettyString()
    println(multipleSplit)

    val longerDelimiterFirst = "apple<-banana<--cherry".splitToSequence("<--", "<-").toPrettyString()
    println(longerDelimiterFirst)

    val shorterDelimiterFirst = "apple<-banana<--cherry".splitToSequence("<-", "<--").toPrettyString()
    println(shorterDelimiterFirst)

    val limitSplit = "a->b->c->d->e".splitToSequence("->", limit = 3).toPrettyString()
    println(limitSplit)

    val emptyInputResult = "".splitToSequence("sep").toList()
    println(emptyInputResult == listOf(""))

    val emptyDelimiterSplit = "abc".splitToSequence("").toPrettyString()
    println(emptyDelimiterSplit)

    val mixedCase = "abcXYZdef".splitToSequence("xyz").toPrettyString()
    println(mixedCase)  // No match with case sensitivity

    val mixedCaseIgnored = "abcXYZdef".splitToSequence("xyz", ignoreCase = true).toPrettyString()
    println(mixedCaseIgnored)  // Matches with case insensitivity

    val emptyResults = "##a##b##c##".splitToSequence("##").toPrettyString()
    println(emptyResults)

    val consecutiveSeparators = "a--b------c".splitToSequence("--").toPrettyString()
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

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L708)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    fun Sequence<String>.toPrettyString() = joinToString(", ", "[", "]")

    val commaSplit = "apple,banana,cherry".splitToSequence(',').toPrettyString()
    println(commaSplit)

    val charSplit = "apple,banana;cherry".splitToSequence(',', ';').toPrettyString()
    println(charSplit)

    val limitSplit = "a,b,c,d,e".splitToSequence(',', limit = 3).toPrettyString()
    println(limitSplit)

    val emptyInputResult = "".splitToSequence('|').toList()
    println(emptyInputResult == listOf(""))

    val mixedCase = "abcXdef".splitToSequence('x').toPrettyString()
    println(mixedCase)  // No match with case sensitivity

    val mixedCaseIgnored = "abcXdef".splitToSequence('x', ignoreCase = true).toPrettyString()
    println(mixedCaseIgnored)  // Matches with case insensitivity

    val emptyResults = ",a,b,c,".splitToSequence(',').toPrettyString()
    println(emptyResults)

    val consecutiveSeparators = "a,,b,,,c".splitToSequence(',').toPrettyString()
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

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L773)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val colors = "green, red , brown&blue, orange, pink&green"
    val regex = "[,\\s]+".toRegex()

    val mixedColor = colors.splitToSequence(regex)
        .onEach { println(it) }
        .firstOrNull { it.contains('&') }

    println(mixedColor)
}
```

```text title="输出"
green
red
brown&blue
brown&blue
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L660)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
