# StringBuilder.insert

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将指定的布尔 `value` 的字符串表示表示插入到指定的 `index` 的字符串构建器中,并返回此实例。

整体效果完全像 `value` 被`value.toString()` 方法转换成字符串, 然后在指定的 `index` 的字符串构建器中插入字符串。

@throws 指数外在值除以`index` 低于零或大于此字符串构建器长度的值。

??? note "查看英文原文"

    Inserts the string representation of the specified boolean `value` into this string builder at the specified `index` and returns this instance.
    
    The overall effect is exactly as if the `value` were converted to a string by the `value.toString()` method,
    and then that string was inserted into this string builder at the specified `index`.
    
    @throws IndexOutOfBoundsException if `index` is less than zero or greater than the length of this string builder.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
    @IgnorableReturnValue public fun insert(index: Int, value: Boolean): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L178)

### 2. Common

```kotlin
@SinceKotlin("1.9")
    @IgnorableReturnValue public fun insert(index: Int, value: Int): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L189)

将指定的 `value` 的字符串表示式插入到指定的 `index` 的字符串构建器中,并返回此实例。

整体效果完全像 `value` 被`value.toString()` 方法转换成字符串, 然后在指定的 `index` 的字符串构建器中插入字符串。

@throws 指数外在值除以`index` 低于零或大于此字符串构建器长度的值。

### 3. Common

```kotlin
@SinceKotlin("1.9")
    @IgnorableReturnValue public fun insert(index: Int, value: Long): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L200)

将指定的长 `value` 的字符串表示式插入到指定的 `index` 的字符串构建器中,并返回此实例。

整体效果完全像 `value` 被`value.toString()` 方法转换成字符串, 然后在指定的 `index` 的字符串构建器中插入字符串。

@throws 指数外在值除以`index` 低于零或大于此字符串构建器长度的值。

### 4. Common

```kotlin
@SinceKotlin("1.9")
    @IgnorableReturnValue public fun insert(index: Int, value: Float): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L211)

将指定的 `value` 浮标的字符串表示表示方式插入到指定的`index`的字符串构建器中,并返回此实例。

整体效果完全像 `value` 被`value.toString()` 方法转换成字符串, 然后在指定的 `index` 的字符串构建器中插入字符串。

@throws 指数外在值除以`index` 低于零或大于此字符串构建器长度的值。

### 5. Common

```kotlin
@SinceKotlin("1.9")
    @IgnorableReturnValue public fun insert(index: Int, value: Double): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L222)

将指定的双倍 `value` 的字符串表示式插入到指定的 `index` 的字符串构建器中,并返回此实例。

整体效果完全像 `value` 被`value.toString()` 方法转换成字符串, 然后在指定的 `index` 的字符串构建器中插入字符串。

@throws 指数外在值除以`index` 低于零或大于此字符串构建器长度的值。

### 6. Common

```kotlin
@SinceKotlin("1.4")
    @IgnorableReturnValue public fun insert(index: Int, value: Char): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L233)

在指定的 `index` 中插入指定的字符 `value` 插入到此字符串构建器中,并返回此实例。

@throws 指数外在值除以`index` 低于零或大于此字符串构建器长度的值。

### 7. Common

```kotlin
@SinceKotlin("1.4")
    @IgnorableReturnValue public fun insert(index: Int, value: CharArray): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L241)

在指定的 `index` 中将指定字符字符数组 `value` 中的字符插入到此字符串构建器中,并返回此实例。

插入字符的顺序与 `value` 字符阵列中的顺序相同,从 `index` 开始。

@throws 指数外在值除以`index` 低于零或大于此字符串构建器长度的值。

### 8. Common

```kotlin
@SinceKotlin("1.4")
    @IgnorableReturnValue public fun insert(index: Int, value: CharSequence?): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L251)

在指定的 `index` 中将字符插入到指定的字符序列序列 `value` 中,然后返回此实例。

插入字符的顺序与 `value` 字符序列中的顺序相同,从 `index` 开始。

@param 索引在此字符串构建器中插入的位置。
@param 值为插入字符的字符序列。 如果 `value` 是 `null`,则插入四个字符 `"null"`。

@throws 指数外在值除以`index` 低于零或大于此字符串构建器长度的值。

### 9. Common

```kotlin
@SinceKotlin("1.4")
    @IgnorableReturnValue public fun insert(index: Int, value: Any?): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L264)

将指定的对象 `value` 的字符串表示式插入到指定的 `index` 的字符串构建器中,并返回此实例。

整体效果完全像 `value` 被`value.toString()` 方法转换成字符串, 然后在指定的 `index` 的字符串构建器中插入字符串。

@throws 指数外在值除以`index` 低于零或大于此字符串构建器长度的值。

### 10. Common

```kotlin
@SinceKotlin("1.4")
    @IgnorableReturnValue public fun insert(index: Int, value: String?): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L275)

将字符串 `value` 插入到指定的 `index` 指定的字符串构建器中,并返回此实例。

如果 `value` 是 `null` ,那么插入四个字符 `"null"`。

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
    val result = source.`insert`(0, false)
    println(result)
}
```

```text title="输出"
falsekotlin
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
