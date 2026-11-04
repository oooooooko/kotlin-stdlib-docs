# none

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果字符序列没有字符,则返回 `true`。

@sample 样本. 文本. Strings. noone

??? note "查看英文原文"

    Returns `true` if the char sequence has no characters.
    
    @sample samples.text.Strings.none

## 声明与重载

### 1. Common

```kotlin
public fun CharSequence.none(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L1863)

### 2. Common

```kotlin
public inline fun CharSequence.none(predicate: (Char) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L1872)

如果没有字符匹配给定的 `predicate`,则返回`true`。

@sample 样本. 文本. Strings. noone

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    // none is synonymous to isEmpty()
    println("str".none())
    println("".none())
}
```

```text title="输出"
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L522)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val string = "Kotlin"
    // All characters are letters
    println(string.none { it.isLetter() })
    // Some of them are lowercase letters
    println(string.none { it.isLowerCase() })
    // But there are no digits among them, thus none returns true only for this predicate
    println(string.none { it.isDigit() })

    // For an empty string `none` always return `true`
    println("".none { true })
    println("".none { false })
}
```

```text title="输出"
false
false
true
true
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L500)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
