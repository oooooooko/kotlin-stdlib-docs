# lastOrNull

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果字符序列为空,则返回最后一个字符,或 `null` 。

@sample 样本. 文本. 链条. 最后一次

??? note "查看英文原文"

    Returns the last character, or `null` if the char sequence is empty.
    
    @sample samples.text.Strings.last

## 声明与重载

### 1. Common

```kotlin
public fun CharSequence.lastOrNull(): Char?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L213)

### 2. Common

```kotlin
public inline fun CharSequence.lastOrNull(predicate: (Char) -> Boolean): Char?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L222)

返回与给定 `predicate` 匹配的最后字符,如果没有找到此字符,则返回 `null`。

@sample 样本. 文本. 链条. 最后一次

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val string = "Kotlin 1.4.0"
    println(string.last())
    println(string.last { it.isLetter() })
    println(string.lastOrNull { it > 'z' })
    assertFails { string.last { it > 'z' } }

    val emptyString = ""
    println(emptyString.lastOrNull())
    assertFails { emptyString.last() }
}
```

```text title="输出"
0
n
null
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L599)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
