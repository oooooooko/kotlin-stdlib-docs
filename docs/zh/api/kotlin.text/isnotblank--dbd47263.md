# isNotBlank

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果此字符序列不是空的, 且包含一些字符, 除了空白字符, 则返回 `true` 。

@sample 样本. 文本. 链条. string is not blank

??? note "查看英文原文"

    Returns `true` if this char sequence is not empty and contains some characters except whitespace characters.
    
    @sample samples.text.Strings.stringIsNotBlank

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharSequence.isNotBlank(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L312)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    fun validateName(name: String): String {
        require(name.isNotBlank()) { "Name cannot be blank" }
        return name
    }

    println(validateName("Adam"))
    assertFails { validateName("") }
    assertFails { validateName("  \t\n") }
}
```

```text title="输出"
Adam
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L369)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
