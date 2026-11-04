# append

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将所有参数附加到给定的 `Appendable` 。

??? note "查看英文原文"

    Appends all arguments to the given `Appendable`.

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
public fun <T : Appendable> T.append(vararg value: CharSequence?): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Appendable.kt#L61)

### 2. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.append(value: Byte): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L327)

将指定的 $ `value` 字节的字符串表示式附加到此字符串构建器, 并返回此实例 。

整体效果完全像 `value` 被`value.toString()` 方法转换成字符串, 然后字符串被附加到这个字符串构建器上。

### 3. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.append(value: Short): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L336)

将指定的短 `value` 的字符串表示方式附加到此字符串构建器,并返回此实例。

整体效果完全像 `value` 被`value.toString()` 方法转换成字符串, 然后字符串被附加到这个字符串构建器上。

### 4. Common

```kotlin
@Suppress("EXTENSION_SHADOWED_BY_MEMBER")
@Deprecated("Use append(value: Any?) instead", ReplaceWith("append(value = obj)"), DeprecationLevel.WARNING)
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun StringBuilder.append(obj: Any?): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L491)

### 5. Common

```kotlin
@IgnorableReturnValue public fun StringBuilder.append(vararg value: String?): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L518)

将所有参数附加到给定的字符串构建器 。

### 6. Common

```kotlin
@IgnorableReturnValue public fun StringBuilder.append(vararg value: Any?): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L527)

将所有参数附加到给定的字符串构建器 。

### 7. Common

```kotlin
// KT-52336
@Deprecated("Use appendRange instead.", ReplaceWith("this.appendRange(str, offset, offset + len)"), level = DeprecationLevel.ERROR)
@kotlin.internal.InlineOnly
@Suppress("UNUSED_PARAMETER")
@IgnorableReturnValue public inline fun StringBuilder.append(str: CharArray, offset: Int, len: Int): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L536)

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
    val result = source.`append`(2.toByte())
    println(result)
}
```

```text title="输出"
kotlin2
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
