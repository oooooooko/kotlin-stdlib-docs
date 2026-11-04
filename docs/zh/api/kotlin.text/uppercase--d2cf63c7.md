# uppercase

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

使用不变区块的 Unicode 映射规则将此字符转换为大写 。

此函数支持一对多个字符字符映射, 因此返回的字符串长度可以大于一个。 例如, `'\uFB00'.uppercase()` 返回 `"\u0046\u0046"`, `'\uFB00'` 即 ALTIN SMALLIGATURE FF 字符 (`ﬀ`) 。 如果此字符没有大写映射, 则返回此字符串的 `toString()` 的结果 。

@sample 样本.text.Chars. opcase

??? note "查看英文原文"

    Converts this character to upper case using Unicode mapping rules of the invariant locale.
    
    This function supports one-to-many character mapping, thus the length of the returned string can be greater than one.
    For example, `'\uFB00'.uppercase()` returns `"\u0046\u0046"`,
    where `'\uFB00'` is the LATIN SMALL LIGATURE FF character (`ﬀ`).
    If this character has no upper case mapping, the result of `toString()` of this char is returned.
    
    @sample samples.text.Chars.uppercase

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.5")
public expect fun Char.uppercase(): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L169)

### 2. Common

```kotlin
@SinceKotlin("1.5")
public expect fun String.uppercase(): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L22)

返回此字符串的复制件, 使用不变化位置的 Unicode 映射规则转换成大写 。

此函数支持一对多字符和多对一字符的绘图, 因此返回的字符串长度可能与原始字符串长度不同 。

@sample 样本. 文本. 链条. 超大

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    val chars = listOf('a', 'ω', '1', 'ŉ', 'A', '+', 'ß')
    val uppercaseChar = chars.map { it.uppercaseChar() }
    val uppercase = chars.map { it.uppercase() }
    println(uppercaseChar)
    println(uppercase)
}
```

```text title="输出"
[A, Ω, 1, ŉ, A, +, ß]
[A, Ω, 1, ʼN, A, +, SS]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L85)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println("Iced frappé!".uppercase())
}
```

```text title="输出"
ICED FRAPPÉ!
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L286)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
