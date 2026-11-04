# appendRange

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将指定的字符序列 `value` 的子序列附加到此附加文件并返回此实例。

@param 值作为子序列的附件的字符序列。 @param 开头为 Index 后继的开头(包括) 后继的开头(包括) 后继的开头(包括) 。 @param 结尾为 Index 后继的结尾(不包括) 。

@throws 指数外向值或 `IllegalArgumentException` ,当 `startIndex` 或 `endIndex` 不在`value`字符序列指数范围或`startIndex > endIndex`时,则 `IllegalArgumentException` 。

??? note "查看英文原文"

    Appends a subsequence of the specified character sequence `value` to this Appendable and returns this instance.
    
    @param value the character sequence from which a subsequence is appended.
    @param startIndex the beginning (inclusive) of the subsequence to append.
    @param endIndex the end (exclusive) of the subsequence to append.
    
    @throws IndexOutOfBoundsException or `IllegalArgumentException` when `startIndex` or `endIndex` is out of range of the `value` character sequence indices or when `startIndex > endIndex`.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
public fun <T : Appendable> T.appendRange(value: CharSequence, startIndex: Int, endIndex: Int): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Appendable.kt#L45)

### 2. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue public expect fun StringBuilder.appendRange(value: CharArray, startIndex: Int, endIndex: Int): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L433)

将指定字符数组 `value` 的子组中的字符附加到此字符串构建器中, 并返回此实例 。

字符按顺序附后,从指定的 `startIndex` 开始。

@param 值,以图添加字符的数组。 @param 开头 INdex 以图附件@param 结尾 INdex 的开头(包括) 以图附件。 @param 结尾 内德克斯 以图附件的子组结尾(不包括) 。

@throws参数外出指数`IllegalArgumentException`何时`startIndex`或`endIndex`超出该值范围`value`矩阵索引或当`startIndex > endIndex`.

### 3. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue public expect fun StringBuilder.appendRange(value: CharSequence, startIndex: Int, endIndex: Int): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L447)

将指定的字符序列`value`的子序列附加到此字符串构建器并返回此实例。

@param 值作为子序列的附件的字符序列。 @param 开头为 Index 后继的开头(包括) 后继的开头(包括) 后继的开头(包括) 。 @param 结尾为 Index 后继的结尾(不包括) 。

@throws 指数外向值或 `IllegalArgumentException` ,当 `startIndex` 或 `endIndex` 不在`value`字符序列指数范围或`startIndex > endIndex`时,则 `IllegalArgumentException` 。

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
    val source = StringBuilder("kotlin")
    val result = source.`appendRange`(charArrayOf('a', 'b', 'c'), 0, 2)
    println(result)
}
```

```text title="输出"
kotlinab
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
