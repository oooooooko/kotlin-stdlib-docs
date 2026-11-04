# digitToIntOrNull

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回此 Char 所代表的小数位数的数值,如果此 Char 不是有效的小数位数,则返回 `null` 。

如果 Char 的数值为 `isDigit` , 则AChar 代表小数数字。 在这种情况下, 返回字符的 Unicode 位数小数值 。

@sample 样本.text.Chars.digitimital ToIntOrnull

??? note "查看英文原文"

    Returns the numeric value of the decimal digit that this Char represents, or `null` if this Char is not a valid decimal digit.
    
    A Char is considered to represent a decimal digit if `isDigit` is true for the Char.
    In this case, the Unicode decimal digit value of the character is returned.
    
    @sample samples.text.Chars.digitToIntOrNull

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.5")
public fun Char.digitToIntOrNull(): Int?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L45)

### 2. Common

```kotlin
@SinceKotlin("1.5")
public fun Char.digitToIntOrNull(radix: Int): Int?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Char.kt#L59)

返回该字符在指定的 `radix` 或 `null` 中代表的位数的数值,如果该字符不是指定的 `radix` 中有效的位数。
如果 `radix` 不在`2..36`范围,则丢弃例外 。

如果以下之一至少属实,则Char 被视为代表指定 `radix`中的一位位数:
- `isDigit`是字符的`true`,字符的十进制数字值小于指定的`radix`。 在这种情况下,返回十进制位数值。
- 查尔是拉丁字母“A”通过“Z”的一个大写字母之一,而其`code`还不到`radix + 'A'.code - 10`。 在这种情况下,`this.code - 'A'.code + 10`被退回。
- 查尔是拉丁字母“a” 中一个小写字母“z” , 其`code` 低于 `radix + 'a'.code - 10`。 在这种情况下,`this.code - 'a'.code + 10`被退回。
- 查尔是拉丁字母“\ uFF21”中 的完整拉丁字母之一, 其 `code` 低于 `radix + 0xFF21 - 10`。 在这种情况下,`this.code - 0xFF21 + 10`被退回。
- 查尔是拉丁字母"\ uFF41"中 和它的"FF5A" 及其`code`小于`radix + 0xFF41 - 10`. 在这种情况下,`this.code - 0xFF41 + 10`被退回。

@sample 样本.text.Chars.digitimital ToIntOrnull

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*
import kotlin.test.*



fun main() {
    println('5'.digitToIntOrNull())
    println('3'.digitToIntOrNull(radix = 8))
    println('A'.digitToIntOrNull(radix = 16))
    println('K'.digitToIntOrNull(radix = 36))

    // radix argument should be in 2..36
    assertFails { '0'.digitToIntOrNull(radix = 1) }
    assertFails { '1'.digitToIntOrNull(radix = 100) }
    // only 0 and 1 digits are valid for binary numbers
    println('5'.digitToIntOrNull(radix = 2))
    // radix = 10 is used by default
    println('A'.digitToIntOrNull())
    // symbol '+' is not a digit in any radix
    println('+'.digitToIntOrNull())
    // Only Latin letters are valid for digits greater than 9.
    println('β'.digitToIntOrNull(radix = 36))
}
```

```text title="输出"
5
3
10
20
null
null
null
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/char.kt#L201)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
