# indexOf

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回指定字符首出现时,从指定的 `startIndex` 开始,在此字符串中的索引。

@param 忽略 `true` 号Case `true` , 以忽略字符在匹配字符时的字符。 默认为 `false`. @return 。 首发事件`char` 或 - 1 的索引, 如果找不到的话 。

??? note "查看英文原文"

    Returns the index within this string of the first occurrence of the specified character, starting from the specified `startIndex`.
    
    @param ignoreCase `true` to ignore character case when matching a character. By default `false`.
    @return An index of the first occurrence of `char` or -1 if none is found.

## 声明与重载

### 1. Common

```kotlin
public fun CharSequence.indexOf(char: Char, startIndex: Int = 0, ignoreCase: Boolean = false): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1124)

### 2. Common

```kotlin
public fun CharSequence.indexOf(string: String, startIndex: Int = 0, ignoreCase: Boolean = false): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1137)

返回指定 `string` 首次出现的字符序列中的索引,从指定的 `startIndex` 开始。

@param 忽略 `true` 号Case `true` , 以忽略字符串匹配字符串时的字符特例。 默认为 `false`. @return 。 默认为 @return 。 首发的 `string` 或 `-1` 的索引, 如果找不到的话 。 @sample 样本. text. strings. indexof

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    fun matchDetails(inputString: String, whatToFind: String, startIndex: Int = 0): String {
        val matchIndex = inputString.indexOf(whatToFind, startIndex)
        return "Searching for '$whatToFind' in '$inputString' starting at position $startIndex: " +
                if (matchIndex >= 0) "Found at $matchIndex" else "Not found"
    }

    val inputString = "Never ever give up"
    val toFind = "ever"

    println(matchDetails(inputString, toFind))
    println(matchDetails(inputString, toFind, 2))
    println(matchDetails(inputString, toFind, 10))
}
```

```text title="输出"
Searching for 'ever' in 'Never ever give up' starting at position 0: Found at 1
Searching for 'ever' in 'Never ever give up' starting at position 2: Found at 6
Searching for 'ever' in 'Never ever give up' starting at position 10: Not found
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L529)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
