# isWhitespace

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

确定字符是否为空白。

如果一个字符的 Unicode 中`category``Char.category`
是`CharCategory.SPACE_SEPARATOR`、`CharCategory.LINE_SEPARATOR`、`CharCategory.PARAGRAPH_SEPARATOR`、
或它是一个`CharCategory.CONTROL`字符在范围内`U+0009..U+000D`或`U+001C..U+001F`.

如果字符为空白,则返回 `true` 。

@sample 样本.text.Chars.isWhitespace

??? note "查看英文原文"

    Determines whether a character is whitespace.
    
    A character is considered whitespace if either its Unicode `category``Char.category`
    is one of `CharCategory.SPACE_SEPARATOR`, `CharCategory.LINE_SEPARATOR`, `CharCategory.PARAGRAPH_SEPARATOR`,
    or it is a `CharCategory.CONTROL` character in range `U+0009..U+000D` or `U+001C..U+001F`.
    
    Returns `true` if the character is whitespace.
    
    @sample samples.text.Chars.isWhitespace

## 声明与重载

### 1. Common

```kotlin
public expect fun Char.isWhitespace(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L327)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    val chars = listOf(' ', '\t', '\n', '1', 'a', '\u00A0')
    val (whitespaces, notWhitespaces) = chars.partition { it.isWhitespace() }
    // whitespace char codes
    println(whitespaces.map(Char::code))
    // non-whitespace chars
    println(notWhitespaces)
}
```

```text title="输出"
[32, 9, 10, 160]
[1, a]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L59)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
