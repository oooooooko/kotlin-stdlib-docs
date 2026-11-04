# indexOfFirst

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回匹配给定 `predicate`的第一个字符的索引,如果字符序列不包含这种字符,则返回 - 1。

@sample 样本. 文本. 链条. 首选索引

??? note "查看英文原文"

    Returns index of the first character matching the given `predicate`, or -1 if the char sequence does not contain such character.
    
    @sample samples.text.Strings.indexOfFirst

## 声明与重载

### 1. Common

```kotlin
public inline fun CharSequence.indexOfFirst(predicate: (Char) -> Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L157)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val string = "Kotlin knowledge"

    println(string.indexOfFirst { it == 'K' })
    println(string.indexOfFirst { it == 'k' })
    println(string.indexOfFirst { it == 'n' })
    println(string.indexOfFirst { it == ' ' })
    println(string.indexOfFirst { it == 'z' })

    val emptyString = "";
    println(emptyString.indexOfFirst { it == 'z' })
}
```

```text title="输出"
0
7
5
6
-1
-1
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L1116)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
