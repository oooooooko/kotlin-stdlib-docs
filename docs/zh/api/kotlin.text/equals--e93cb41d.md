# equals

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果此字符串等于 `other`, 则返回 `true`, 且可选择忽略字符 。

两个字符串如果长度相同,同一指数的字符相同,则视为相等。如果 `ignoreCase` 是真实的,则对每个字符的`Char.uppercaseChar().lowercaseChar()`的结果进行比较。

@param 忽略 Case `true` 来忽略字符串比较字符串的字符。 默认为 `false` 。

??? note "查看英文原文"

    Returns `true` if this string is equal to `other`, optionally ignoring character case.
    
    Two strings are considered to be equal if they have the same length and the same character at the same index.
    If `ignoreCase` is true, the result of `Char.uppercaseChar().lowercaseChar()` on each character is compared.
    
    @param ignoreCase `true` to ignore character case when comparing strings. By default `false`.

## 声明与重载

### 1. Common

```kotlin
public expect fun String?.equals(other: String?, ignoreCase: Boolean = false): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L440)

### 2. Common

```kotlin
public fun Char.equals(other: Char, ignoreCase: Boolean = false): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L215)

如果此字符等于 `other` 字符,则返回 `true` , 且可选择忽略字符。

如果每个字符的 `Char.uppercaseChar().lowercaseChar()` 产生相同的结果,则两个字符被视为等于忽略。

@param 忽略Case `true` 来忽略字符 。 默认为 `false`。
@sample样本.text.Chars.eques

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    println('a'.equals('a', false))
    println('a'.equals('A', false))
    println('a'.equals('A', true))
}
```

```text title="输出"
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L156)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
