# appendLine

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

向此附加文件附加一条线性种子字符( `\n` ) 。

??? note "查看英文原文"

    Appends a line feed character (`\n`) to this Appendable.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun Appendable.appendLine(): Appendable
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Appendable.kt#L71)

### 2. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun Appendable.appendLine(value: CharSequence?): Appendable
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Appendable.kt#L77)

将值附加到给定的附加件和之后的线性种子字符(`\n`) 。

### 3. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun Appendable.appendLine(value: Char): Appendable
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Appendable.kt#L83)

将值附加到给定的附加件和之后的线性种子字符(`\n`) 。

### 4. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue public inline fun StringBuilder.appendLine(): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L542)

将线性种子字符( `\n`) 附加到此字符串构建器 。

### 5. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue public inline fun StringBuilder.appendLine(value: CharSequence?): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L547)

将 `value` 添加到此 `StringBuilder`, 并随后加上一条线进料字符( `\n` )。

### 6. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue public inline fun StringBuilder.appendLine(value: String?): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L552)

将 `value` 添加到此 `StringBuilder`, 并随后加上一条线进料字符( `\n` )。

### 7. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue public inline fun StringBuilder.appendLine(value: Any?): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L557)

将 `value` 添加到此 `StringBuilder`, 并随后加上一条线进料字符( `\n` )。

### 8. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue public inline fun StringBuilder.appendLine(value: CharArray): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L562)

将 `value` 添加到此 `StringBuilder`, 并随后加上一条线进料字符( `\n` )。

### 9. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue public inline fun StringBuilder.appendLine(value: Char): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L567)

将 `value` 添加到此 `StringBuilder`, 并随后加上一条线进料字符( `\n` )。

### 10. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
@IgnorableReturnValue public inline fun StringBuilder.appendLine(value: Boolean): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L572)

将 `value` 添加到此 `StringBuilder`, 并随后加上一条线进料字符( `\n` )。

### 11. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.appendLine(value: Byte): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L577)

将 `value` 添加到此 `StringBuilder`, 并随后加上一条线进料字符( `\n` )。

### 12. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.appendLine(value: Short): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L581)

将 `value` 添加到此 `StringBuilder`, 并随后加上一条线进料字符( `\n` )。

### 13. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.appendLine(value: Int): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L585)

将 `value` 添加到此 `StringBuilder`, 并随后加上一条线进料字符( `\n` )。

### 14. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.appendLine(value: Long): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L589)

将 `value` 添加到此 `StringBuilder`, 并随后加上一条线进料字符( `\n` )。

### 15. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.appendLine(value: Float): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L593)

将 `value` 添加到此 `StringBuilder`, 并随后加上一条线进料字符( `\n` )。

### 16. Common

```kotlin
@SinceKotlin("1.9")
@IgnorableReturnValue public expect fun StringBuilder.appendLine(value: Double): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L597)

将 `value` 添加到此 `StringBuilder`, 并随后加上一条线进料字符( `\n` )。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.random.Random
import kotlin.test.*
import kotlin.text.*



fun main() {

        val stringBuilder = StringBuilder()
        stringBuilder.appendLine('c')
        stringBuilder.appendLine("string")
        stringBuilder.appendLine(true)
        stringBuilder.appendLine(charArrayOf('a', 'r', 'r', 'a', 'y'))
        stringBuilder.appendLine()
        stringBuilder.appendLine("char sequence" as CharSequence)
        stringBuilder.appendLine(null as Any?)
        stringBuilder.appendLine("nonnull" as Any?)
        stringBuilder.appendLine(null as String?)
        stringBuilder.appendLine(null as CharSequence?)

        val expected =
            """
            c
            string
            true
            array
            
            char sequence
            null
            nonnull
            null
            null
            
            """.trimIndent()

        println(stringBuilder.toString())
    
}
```

```text title="输出"
c
string
true
array

char sequence
null
nonnull
null
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/text/StringBuilderTest.kt#L551)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
