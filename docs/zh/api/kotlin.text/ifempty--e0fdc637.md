# ifEmpty

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果字符序列不是空的, 返回此字符序列, 如果字符序列为空, 返回此字符序列, 返回到调用 `defaultValue` 函数的结果, 如果字符序列为空 。

@sample 样本. 文本. strrings.stringififimpty

??? note "查看英文原文"

    Returns this char sequence if it's not empty
    or the result of calling `defaultValue` function if the char sequence is empty.
    
    @sample samples.text.Strings.stringIfEmpty

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
@kotlin.internal.InlineOnly
public inline fun <C, R> C.ifEmpty(defaultValue: () -> R): R where C : CharSequence, C : R
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L349)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val empty = ""

    val emptyOrNull: String? = empty.ifEmpty { null }
    println(emptyOrNull)

    val emptyOrDefault = empty.ifEmpty { "default" }
    println(emptyOrDefault)

    val nonEmpty = "abc"
    val sameString = nonEmpty.ifEmpty { "def" }
    println(nonEmpty === sameString)
}
```

```text title="输出"
null
default
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L327)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
