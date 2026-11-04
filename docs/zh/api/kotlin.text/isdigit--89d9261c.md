# isDigit

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果此字符是一个位数,则返回`true`。

如果一个字符的 `category` 是`CharCategory.DECIMAL_DIGIT_NUMBER`,则该字符视为数字。

@sample 样本.text.Chars.isDigit

??? note "查看英文原文"

    Returns `true` if this character is a digit.
    
    A character is considered to be a digit if its `category` is `CharCategory.DECIMAL_DIGIT_NUMBER`.
    
    @sample samples.text.Chars.isDigit

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.5")
public expect fun Char.isDigit(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L274)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    val chars = listOf('a', '+', '1')
    val (digits, notDigits) = chars.partition { it.isDigit() }
    println(digits)
    println(notDigits)
}
```

```text title="输出"
[1]
[a, +]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L25)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
