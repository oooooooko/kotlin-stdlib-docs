# isTitleCase

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果此字符为标题案例字母,则返回`true`。

如果一个字符的 `category` 是 `CharCategory.TITLECASE_LETTER`,则该字符被视为标题案例字母。

@sample 样本.text.chars.istitleCase

??? note "查看英文原文"

    Returns `true` if this character is a title case letter.
    
    A character is considered to be a title case letter if its `category` is `CharCategory.TITLECASE_LETTER`.
    
    @sample samples.text.Chars.isTitleCase

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.5")
public expect fun Char.isTitleCase(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L306)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    val chars = listOf('ǅ', 'ǈ', 'ǋ', 'ǲ', '1', 'A', 'a', '+')
    val (titleCases, notTitleCases) = chars.partition { it.isTitleCase() }
    println(titleCases)
    println(notTitleCases)
}
```

```text title="输出"
[ǅ, ǈ, ǋ, ǲ]
[1, A, a, +]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L123)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
