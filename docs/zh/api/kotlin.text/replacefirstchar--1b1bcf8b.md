# replaceFirstChar

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回此字符串的复制件, 其第一个字符由指定的 `transform` 的结果替换, 或如果原始字符串为空, 则返回原始字符串 。

@param 转换函数,它取第一个字符,返回该字符应用的变换结果。

@sample 样本. 文本. strings. replace FirstChar 样本

??? note "查看英文原文"

    Returns a copy of this string having its first character replaced with the result of the specified `transform`,
    or the original string if it's empty.
    
    @param transform function that takes the first character and returns the result of the transform applied to the character.
    
    @sample samples.text.Strings.replaceFirstChar

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.5")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@JvmName("replaceFirstCharWithChar")
@kotlin.internal.InlineOnly
public inline fun String.replaceFirstChar(transform: (Char) -> Char): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L819)

### 2. Common

```kotlin
@SinceKotlin("1.5")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@JvmName("replaceFirstCharWithCharSequence")
@kotlin.internal.InlineOnly
public inline fun String.replaceFirstChar(transform: (Char) -> CharSequence): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L836)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println("kotlin".replaceFirstChar { it.uppercase() })

    val sentence = "Welcome to Kotlin!"
    val words = sentence.split(' ');
    println(words.joinToString(separator = "_") { word -> word.replaceFirstChar { it.lowercase() } })
}
```

```text title="输出"
Kotlin
welcome_to_kotlin!
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L22)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
