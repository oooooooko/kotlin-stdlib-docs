# isLetter

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果此字符为字母,则返回`true`。

如果一个字符的 `category` 是 `CharCategory.UPPERCASE_LETTER`, 则该字符被视为字母。
`CharCategory.LOWERCASE_LETTER`, `CharCategory.TITLECASE_LETTER`, `CharCategory.MODIFIER_LETTER`,或`CharCategory.OTHER_LETTER`.

@sample 样本.text.Chars.is Thetter

??? note "查看英文原文"

    Returns `true` if this character is a letter.
    
    A character is considered to be a letter if its `category` is `CharCategory.UPPERCASE_LETTER`,
    `CharCategory.LOWERCASE_LETTER`, `CharCategory.TITLECASE_LETTER`, `CharCategory.MODIFIER_LETTER`, or `CharCategory.OTHER_LETTER`.
    
    @sample samples.text.Chars.isLetter

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.5")
public expect fun Char.isLetter(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L252)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    val chars = listOf('a', 'β', '+', '1')
    val (letters, notLetters) = chars.partition { it.isLetter() }
    println(letters)
    println(notLetters)
}
```

```text title="输出"
[a, β]
[+, 1]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L9)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
