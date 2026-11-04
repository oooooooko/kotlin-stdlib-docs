# capitalize

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回此字符串的复制件, 其首字母标题使用默认语区规则进行缩写, 或如果原始字符串为空或已经以标题案例字母开头, 则返回原始字符串 。

字符标题通常与大写字母相同,但有一些例外。 带有特别标题案例表格的具体字符列表取决于基础平台。

@sample 样本. 文本. 链条. 资本化

??? note "查看英文原文"

    Returns a copy of this string having its first letter titlecased using the rules of the default locale,
    or the original string if it's empty or already starts with a title case letter.
    
    The title case of a character is usually the same as its upper case with several exceptions.
    The particular list of characters with the special title case form depends on the underlying platform.
    
    @sample samples.text.Strings.capitalize

## 声明与重载

### 1. Common

```kotlin
@Deprecated("Use replaceFirstChar instead.", ReplaceWith("replaceFirstChar { if (it.isLowerCase()) it.titlecase() else it.toString() }"))
@DeprecatedSinceKotlin(warningSince = "1.5")
public expect fun String.capitalize(): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L51)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println("abcd".capitalize())
    println("Abcd".capitalize())
}
```

```text title="输出"
Abcd
Abcd
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L8)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
