# toLong

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将字符串划为 `Long` 号。

字符串必须包含一个可选导导导导`+`或`-`符号和小数位数(`0-9`),
符合有效的 `Long` 值范围(在 `Long.MIN_VALUE..Long.MAX_VALUE` 内),
否则`NumberFormatException`就会被扔掉

@throws 编号格式例外,如果字符串不是`Long`的有效表示。
@sample 样本. text. numbers. to Long

??? note "查看英文原文"

    Parses the string to a `Long` number.
    
    The string must consist of an optional leading `+` or `-` sign and decimal digits (`0-9`),
    and fit the valid `Long` value range (within `Long.MIN_VALUE..Long.MAX_VALUE`),
    otherwise a `NumberFormatException` will be thrown.
    
    @throws NumberFormatException if the string is not a valid representation of a `Long`.
    @sample samples.text.Numbers.toLong

## 声明与重载

### 1. Common

```kotlin
public expect fun String.toLong(): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L607)

### 2. Common

```kotlin
public expect fun String.toLong(radix: Int): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L619)

将字符串分割为 `Long` 号并返回结果 。 @throws 号格式例外, 如果字符串不是有效数字的表示值。 @throws 非法配置除外, 当 `radix` 号不是用于字符串转换为数字的有效 RADIX 时。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.assertFailsWith



fun main() {
    println("0".toLong())
    println("42".toLong())
    println("042".toLong())
    println("-42".toLong())
    // Long.MAX_VALUE
    println("9223372036854775807".toLong())
    // Long overflow
    assertFailsWith<NumberFormatException> { "9223372036854775808".toLong() }
    // 'a' is not a digit
    assertFailsWith<NumberFormatException> { "-1a".toLong() }
    // underscore
    assertFailsWith<NumberFormatException> { "1_000".toLong() }
    // whitespaces
    assertFailsWith<NumberFormatException> { " 1000 ".toLong() }
}
```

```text title="输出"
0
42
42
-42
9223372036854775807
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/Numbers.kt#L121)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
