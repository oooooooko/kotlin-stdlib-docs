# toBooleanStrict

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回 `true`,如果此字符串的内容等于“ true” ,则返回 `false`,如果它等于“false”,则返回 `true`, 并另丢一个例外。

`String?.toBoolean`. 无效字符串上的函数也有宽度版本。请注意,此函数对大小写敏感。

@sample 样本.text.Strings.toBooleanScritt

??? note "查看英文原文"

    Returns `true` if the content of this string is equal to the word "true", `false` if it is equal to "false",
    and throws an exception otherwise.
    
    There is also a lenient version of the function available on nullable String, `String?.toBoolean`.
    Note that this function is case-sensitive.
    
    @sample samples.text.Strings.toBooleanStrict

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.5")
public fun String.toBooleanStrict(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1621)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    println("true".toBooleanStrict())
    assertFails { "True".toBooleanStrict() }
    assertFails { "TRUE".toBooleanStrict() }

    println("false".toBooleanStrict())
    assertFails { "False".toBooleanStrict() }
    assertFails { "FALSE".toBooleanStrict() }

    assertFails { "abc".toBooleanStrict() }
}
```

```text title="输出"
true
false
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L634)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
