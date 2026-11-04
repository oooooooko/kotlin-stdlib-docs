# insert

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将指定的 `value` 字节的字符串表示式插入到指定的 `index` 的字符串构建器中,并返回此实例。

整体效果完全像 `value` 被`value.toString()` 方法转换成字符串, 然后在指定的 `index` 的字符串构建器中插入字符串。

@throws 指数外在值除以`index` 低于零或大于此字符串构建器长度的值。

??? note "查看英文原文"

    Inserts the string representation of the specified byte `value` into this string builder at the specified `index` and returns this instance.
    
    The overall effect is exactly as if the `value` were converted to a string by the `value.toString()` method,
    and then that string was inserted into this string builder at the specified `index`.
    
    @throws IndexOutOfBoundsException if `index` is less than zero or greater than the length of this string builder.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.insert(index: Int, value: Byte): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L345)

### 2. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.insert(index: Int, value: Short): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L356)

将指定的 `value` 短字符串的字符串表示式插入到指定的 `index` 的字符串构建器中,并返回此实例。

整体效果完全像 `value` 被`value.toString()` 方法转换成字符串, 然后在指定的 `index` 的字符串构建器中插入字符串。

@throws 指数外在值除以`index` 低于零或大于此字符串构建器长度的值。

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
    val result = source.`insert`(0, 2.toByte())
    println(result)
}
```

```text title="输出"
2kotlin
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
