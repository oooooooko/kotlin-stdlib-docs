# lowercase

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

使用不变区块的 Unicode 映射规则将此字符转换为小写 。

此函数支持一对多个字符字符映射, 因此返回的字符串长度可以大于一个。 例如, `'\u0130'.lowercase()` 返回 `"\u0069\u0307"`, `'\u0130'` 即 $`'\u0130'` 与 DOT ABOV 字符( `İ`) 的 ALTIN CAPITAL 字母 I 匹配 。 如果此字符没有小于的大小写映射, 则返回此字符串的 `toString()` 的结果 。

@sample 样本.text.Chars.lowercase

??? note "查看英文原文"

    Converts this character to lower case using Unicode mapping rules of the invariant locale.
    
    This function supports one-to-many character mapping, thus the length of the returned string can be greater than one.
    For example, `'\u0130'.lowercase()` returns `"\u0069\u0307"`,
    where `'\u0130'` is the LATIN CAPITAL LETTER I WITH DOT ABOVE character (`İ`).
    If this character has no lower case mapping, the result of `toString()` of this char is returned.
    
    @sample samples.text.Chars.lowercase

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.5")
public expect fun Char.lowercase(): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L137)

### 2. Common

```kotlin
@SinceKotlin("1.5")
public expect fun String.lowercase(): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L40)

返回此字符串的复制件, 后用不变化位置的 Unicode 映射规则转换为小写 。

此函数支持一对多字符和多对一字符的绘图, 因此返回的字符串长度可能与原始字符串长度不同 。

@sample 样本. 文本. Strings. lowercase

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    val chars = listOf('A', 'Ω', '1', 'a', '+', 'İ')
    val lowercaseChar = chars.map { it.lowercaseChar() }
    val lowercase = chars.map { it.lowercase() }
    println(lowercaseChar)
    println(lowercase)
}
```

```text title="输出"
[a, ω, 1, a, +, i]
[a, ω, 1, a, +, i̇]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L104)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println("Iced frappé!".lowercase())
}
```

```text title="输出"
iced frappé!
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L281)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
