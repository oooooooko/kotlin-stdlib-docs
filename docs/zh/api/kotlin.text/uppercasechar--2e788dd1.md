# uppercaseChar

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

使用不变区块的 Unicode 映射规则将此字符转换为大写 。

此函数执行一对一字符映射。 要支持一对多字符映射, 请使用 `uppercase` 函数。 如果此字符没有映射等同, 则返回字符本身 。

@sample 样本.text.Chars. opcase

??? note "查看英文原文"

    Converts this character to upper case using Unicode mapping rules of the invariant locale.
    
    This function performs one-to-one character mapping.
    To support one-to-many character mapping use the `uppercase` function.
    If this character has no mapping equivalent, the character itself is returned.
    
    @sample samples.text.Chars.uppercase

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.5")
public expect fun Char.uppercaseChar(): Char
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L157)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    val chars = listOf('a', 'ω', '1', 'ŉ', 'A', '+', 'ß')
    val uppercaseChar = chars.map { it.uppercaseChar() }
    val uppercase = chars.map { it.uppercase() }
    println(uppercaseChar)
    println(uppercase)
}
```

```text title="输出"
[A, Ω, 1, ŉ, A, +, ß]
[A, Ω, 1, ʼN, A, +, SS]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L85)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
