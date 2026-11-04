# regionMatches

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回 `true`, 如果此字符序列中的指定区域与其它字符序列中指定区域相等的话。 @param 此折叠设置子字符串此字符串序列中的起始偏移, 以比较 。 @param 其它字符串则返回 `true`。 @param 其它字符串则返回 。 将子字符串中其他字符串序列中的起始偏移进行对比 。 @param 的长度与子字符串的长度进行比较 。

??? note "查看英文原文"

    Returns `true` if the specified range in this char sequence is equal to the specified range in another char sequence.
    @param thisOffset the start offset in this char sequence of the substring to compare.
    @param other the string against a substring of which the comparison is performed.
    @param otherOffset the start offset in the other char sequence of the substring to compare.
    @param length the length of the substring to compare.

## 声明与重载

### 1. Common

```kotlin
public expect fun CharSequence.regionMatches(
    thisOffset: Int,
    other: CharSequence,
    otherOffset: Int,
    length: Int,
    ignoreCase: Boolean = false
): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L501)

### 2. Common

```kotlin
@SinceKotlin("1.9")
public expect fun String.regionMatches(
    thisOffset: Int,
    other: String,
    otherOffset: Int,
    length: Int,
    ignoreCase: Boolean = false
): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L516)

返回 `true`,如果此字符串中指定的区域等于其它字符串中指定的区域。 @param 此折叠设置子字符串中的起始偏移以比较。 @param 其它字符串则相对于进行比较的子字符串。 @param 其它折叠设置子字符串中的其他起始偏移以比较的子字符串中的其他起始偏移。 @param 长度为要比较的子字符串长度 。

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
    val source = "kotlin"
    val result = source.`regionMatches`(0, "o", 0, 2)
    println(result)
}
```

```text title="输出"
false
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
