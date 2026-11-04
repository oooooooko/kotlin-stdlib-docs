# digitToChar

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回代表此小数位数的Char。如果值不在此 `0..9` 范围,则丢弃例外。

如果该值为 `0..9` ,则返回数字为小数的Char, 代码为`'0'.code + this`。

@sample 样本.text.Chars.digitigitho ToChar

??? note "查看英文原文"

    Returns the Char that represents this decimal digit.
    Throws an exception if this value is not in the range `0..9`.
    
    If this value is in `0..9`, the decimal digit Char with code `'0'.code + this` is returned.
    
    @sample samples.text.Chars.digitToChar

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.5")
public fun Int.digitToChar(): Char
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L78)

### 2. Common

```kotlin
@SinceKotlin("1.5")
public fun Int.digitToChar(radix: Int): Char
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L94)

返回在指定的 `radix` 中代表这个数字数字值的Char。如果 `radix` 不在`2..36` 范围,或者如果该数值不在`0 until radix` 范围,则抛出异常。

如果此值小于 `10` ,则返回数字为`'0'.code + this`的十进制字符。否则,返回代码为`'A'.code + this - 10`的大写拉丁字母。

@sample 样本.text.Chars.digitigitho ToChar

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*
import kotlin.test.*



fun main() {
    println(5.digitToChar())
    println(3.digitToChar(radix = 8))
    println(10.digitToChar(radix = 16))
    println(20.digitToChar(radix = 36))

    // radix argument should be in 2..36
    assertFails { 0.digitToChar(radix = 1) }
    assertFails { 1.digitToChar(radix = 100) }
    // only 0 and 1 digits are valid for binary numbers
    assertFails { 5.digitToChar(radix = 2) }
    // radix = 10 is used by default
    assertFails { 10.digitToChar() }
    // a negative integer is not a digit in any radix
    assertFails { (-1).digitToChar() }
}
```

```text title="输出"
5
3
A
K
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L221)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
