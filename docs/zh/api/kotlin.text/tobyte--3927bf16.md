# toByte

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将字符串划为 `Byte` 号。

字符串必须包含一个可选导导导导`+`或`-`符号和小数位数(`0-9`),
符合有效的 `Byte` 值范围(在 `Byte.MIN_VALUE..Byte.MAX_VALUE` 内),
否则`NumberFormatException`就会被扔掉

@throws 数字格式例外,如果字符串不是 `Byte`. @sample. @sample 样本. text. numbers.toByte 的有效表示值,则不在此列。

??? note "查看英文原文"

    Parses the string to a `Byte` number.
    
    The string must consist of an optional leading `+` or `-` sign and decimal digits (`0-9`),
    and fit the valid `Byte` value range (within `Byte.MIN_VALUE..Byte.MAX_VALUE`),
    otherwise a `NumberFormatException` will be thrown.
    
    @throws NumberFormatException if the string is not a valid representation of a `Byte`.
    @sample samples.text.Numbers.toByte

## 声明与重载

### 1. Common

```kotlin
public expect fun String.toByte(): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L550)

### 2. Common

```kotlin
public expect fun String.toByte(radix: Int): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L562)

将字符串分割为已签名的 `Byte` 号, 并返回结果 。 @throws 号数字格式例外, 如果字符串不是有效的数字表示。 @throws 非法配置除外, 当 `radix` 号不是用于字符串转换为数字的有效 RADIX 时, 则不在此列 。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.assertFailsWith



fun main() {
    println("0".toByte())
    println("42".toByte())
    println("042".toByte())
    println("-42".toByte())
    // Byte.MAX_VALUE
    println("127".toByte())
    // Byte overflow
    assertFailsWith<NumberFormatException> { "128".toByte() }
    // 'a' is not a digit
    assertFailsWith<NumberFormatException> { "-1a".toByte() }
    // underscore
    assertFailsWith<NumberFormatException> { "1_00".toByte() }
    // whitespaces
    assertFailsWith<NumberFormatException> { " 22 ".toByte() }
}
```

```text title="输出"
0
42
42
-42
127
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/Numbers.kt#L13)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
