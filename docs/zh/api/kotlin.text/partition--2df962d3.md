# partition

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将原字符序列分割成一对字符序列,其中* 首字符序列包含 `predicate` 生成 `true` 的字符,而* 秒字符序列包含 `predicate` 生成 `false` 的字符。

@sample 样本. 文本. 链条. 部门

??? note "查看英文原文"

    Splits the original char sequence into a pair of char sequences,
    where *first* char sequence contains characters for which `predicate` yielded `true`,
    while *second* char sequence contains characters for which `predicate` yielded `false`.
    
    @sample samples.text.Strings.partition

## 声明与重载

### 1. Common

```kotlin
public inline fun CharSequence.partition(predicate: (Char) -> Boolean): Pair<CharSequence, CharSequence>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L2374)

### 2. Common

```kotlin
public inline fun String.partition(predicate: (Char) -> Boolean): Pair<String, String>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L2394)

将原始字符串分割成一对字符串,其中* 第一条* 字符串包含 `predicate` 生成 `true` 的字符,而 * 秒* 字符串包含 `predicate` 生成 `false` 的字符。

@sample 样本. 文本. 链条. 部门

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    fun isVowel(c: Char) = "aeuio".contains(c, ignoreCase = true)
    val string = "Discussion"
    val result = string.partition(::isVowel)
    println(result)
}
```

```text title="输出"
(iuio, Dscssn)
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L265)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
