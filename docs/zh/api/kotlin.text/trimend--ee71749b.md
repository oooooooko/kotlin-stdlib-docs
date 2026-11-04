# trimEnd

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回此字符序列的子序列, 其尾部字符与`predicate` 的删除相匹配 。

??? note "查看英文原文"

    Returns a subsequence of this char sequence having trailing characters matching the `predicate` removed.

## 声明与重载

### 1. Common

```kotlin
public inline fun CharSequence.trimEnd(predicate: (Char) -> Boolean): CharSequence
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L125)

### 2. Common

```kotlin
public inline fun String.trimEnd(predicate: (Char) -> Boolean): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L136)

返回一个字符串,其尾部字符与`predicate` 的删除字符匹配。

### 3. Common

```kotlin
public fun CharSequence.trimEnd(vararg chars: Char): CharSequence
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L162)

返回从`chars` 矩阵中移除的后端字符的字符序列的子序列。

### 4. Common

```kotlin
public fun String.trimEnd(vararg chars: Char): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L167)

返回从`chars` 矩阵中移除的有尾行字符的字符串。

### 5. Common

```kotlin
public fun CharSequence.trimEnd(): CharSequence
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L194)

返回此字符序列的子序列, 后继空白已删除 。

### 6. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun String.trimEnd(): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L199)

返回一个字符串, 后行空格已删除 。

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
    val result = source.`trimEnd`({ it.toString().length > 0 })
    println(result)
}
```

```text title="输出"

```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
