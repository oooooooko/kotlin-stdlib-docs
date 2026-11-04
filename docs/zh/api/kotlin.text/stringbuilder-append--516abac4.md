# StringBuilder.append

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将指定的对象 `value` 的字符串表示方式附加到此字符串构建器,并返回此实例。

整体效果完全像 `value` 被`value.toString()` 方法转换成字符串, 然后字符串被附加到这个字符串构建器上。

??? note "查看英文原文"

    Appends the string representation of the specified object `value` to this string builder and returns this instance.
    
    The overall effect is exactly as if the `value` were converted to a string by the `value.toString()` method,
    and then that string was appended to this string builder.

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue override fun append(value: Char): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L40)

### 2. Common

```kotlin
@IgnorableReturnValue override fun append(value: CharSequence?): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L41)

### 3. Common

```kotlin
@IgnorableReturnValue override fun append(value: CharSequence?, startIndex: Int, endIndex: Int): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L42)

### 4. Common

```kotlin
@IgnorableReturnValue public fun append(value: Any?): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L55)

### 5. Common

```kotlin
@SinceKotlin("1.3")
    @IgnorableReturnValue public fun append(value: Boolean): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L63)

将指定的布尔的字符串表示式 `value` 附加到此字符串构建器,并返回此实例。

整体效果完全像 `value` 被`value.toString()` 方法转换成字符串, 然后字符串被附加到这个字符串构建器上。

### 6. Common

```kotlin
@SinceKotlin("1.9")
    @IgnorableReturnValue public fun append(value: Int): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L72)

将指定的 `value` 的字符串表示方式附加到此字符串构建器, 并返回此实例 。

整体效果完全像 `value` 被`value.toString()` 方法转换成字符串, 然后字符串被附加到这个字符串构建器上。

### 7. Common

```kotlin
@SinceKotlin("1.9")
    @IgnorableReturnValue public fun append(value: Long): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L81)

将指定的长 `value` 的字符串表示方式附加到此字符串构建器,并返回此实例。

整体效果完全像 `value` 被`value.toString()` 方法转换成字符串, 然后字符串被附加到这个字符串构建器上。

### 8. Common

```kotlin
@SinceKotlin("1.9")
    @IgnorableReturnValue public fun append(value: Float): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L90)

将指定的浮标`value`的字符串表示方式附加到此字符串构建器,并返回此实例。

整体效果完全像 `value` 被`value.toString()` 方法转换成字符串, 然后字符串被附加到这个字符串构建器上。

### 9. Common

```kotlin
@SinceKotlin("1.9")
    @IgnorableReturnValue public fun append(value: Double): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L99)

将指定的双倍 `value` 的字符串表示方式附加到此字符串构建器, 并返回此实例 。

整体效果完全像 `value` 被`value.toString()` 方法转换成字符串, 然后字符串被附加到这个字符串构建器上。

### 10. Common

```kotlin
@SinceKotlin("1.4")
    @IgnorableReturnValue public fun append(value: CharArray): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L108)

将指定字符数组中的字符数组 `value` 中的字符附加到此字符串构建器,并返回此实例。

从指数0开始,字符按顺序附后。

### 11. Common

```kotlin
@SinceKotlin("1.3")
    @IgnorableReturnValue public fun append(value: String?): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L116)

将指定的字符串 `value` 附加到此字符串构建器并返回此实例。

如果 `value` 是 `null` ,则附上四个字符`"null"`。

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
    val result = source.`append`('o')
    println(result)
}
```

```text title="输出"
kotlino
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
