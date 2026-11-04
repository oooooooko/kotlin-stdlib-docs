# titlecase

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

使用不变化位置的 Unicode 映射规则将此字符转换为标题 。

此函数支持一对多个字符字符映射, 因此返回的字符串长度可以大于一个。 例如, `'\uFB00'.titlecase()` 返回 `"\u0046\u0066"`, `'\uFB00'` 是 ALTIN SMALLIGATURE FF 字符 (`ﬀ`) 。 如果此字符没有标题的字符映射, 则返回 `uppercase` 的结果 。

@sample 样本.text.Chars.标题

??? note "查看英文原文"

    Converts this character to title case using Unicode mapping rules of the invariant locale.
    
    This function supports one-to-many character mapping, thus the length of the returned string can be greater than one.
    For example, `'\uFB00'.titlecase()` returns `"\u0046\u0066"`,
    where `'\uFB00'` is the LATIN SMALL LIGATURE FF character (`ﬀ`).
    If this character has no title case mapping, the result of `uppercase` is returned instead.
    
    @sample samples.text.Chars.titlecase

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.5")
public fun Char.titlecase(): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L194)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    val chars = listOf('a', 'ǅ', 'ŉ', '+', 'ß')
    val titlecaseChar = chars.map { it.titlecaseChar() }
    val titlecase = chars.map { it.titlecase() }
    println(titlecaseChar)
    println(titlecase)
}
```

```text title="输出"
[A, ǅ, ŉ, +, ß]
[A, ǅ, ʼN, +, Ss]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L131)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
