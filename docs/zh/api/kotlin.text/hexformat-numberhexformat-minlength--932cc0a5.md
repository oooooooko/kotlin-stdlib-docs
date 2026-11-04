# HexFormat.NumberHexFormat.minLength

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

指定用于表示数值的十六进制位数最小数,默认为`1`。

数值的十六进制表示法是将其二进制表示法的每个四位元块绘制成相应的十六进制数字,从最重要的位数开始计算。

格式化时: - 如果该选项低于十六进制代表的长度: - 如果 `removeLeadingZeros` 是 `true` , 则在长度与 `minLength` 匹配之前删除前导零。 - 如果 `removeLeadingZeros` 是 `false`, 则该代表的不变, 因为没有取消前导0 。 - 如果该选项大于十六进制代表的长度, 则在开始时将代表的零加零以达到指定的 `minLength` 。 - 如果该选项与十六进制代表的长度相符, 则代表的不变。

当分析时, 此选项将被忽略。 但是, 输入字符串中至少必须有一个十六进制数字。 如果十六进制数字数超过所分析的种类的能力, 则根据其位数大小, 超额的前位数字必须是零 。

@sample 样本. text. HexFormats. 编号.minLength

??? note "查看英文原文"

    Specifies the minimum number of hexadecimal digits to be used in the representation of a numeric value,
    `1` by default.
    
    The hexadecimal representation of a value is calculated by mapping each four-bit chunk of its binary
    representation to the corresponding hexadecimal digit, starting with the most significant bits.
    
    When formatting:
      - If this option is less than the length of the hexadecimal representation:
          - If `removeLeadingZeros` is `true`, leading zeros are removed until the length matches `minLength`.
          - If `removeLeadingZeros` is `false`, the representation remains unchanged, as no leading zeros are removed.
      - If this option is greater than the length of the hexadecimal representation, the
        representation is padded with zeros at the start to reach the specified `minLength`.
      - If this option matches the length of the hexadecimal representation, the representation remains unchanged.
    
    When parsing, this option is ignored. However, there must be at least one hexadecimal digit in the input
    string. If the number of hexadecimal digits exceeds the capacity of the type being parsed, based on its bit
    size, the excess leading digits must be zeros.
    
    @sample samples.text.HexFormats.Numbers.minLength

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.0")
        public val minLength: Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L487)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    // By default, minLength is 1 and removeLeadingZeros is false.
    println(0x3a.toHexString())

    // Specifying a minLength shorter than the hex representation with removeLeadingZeros set to false.
    println(0x3a.toHexString(HexFormat { number.minLength = 4 }))

    // Specifying a minLength shorter than the hex representation with removeLeadingZeros set to true.
    val shorterLengthFormat = HexFormat {
        number.removeLeadingZeros = true
        number.minLength = 4
    }
    println(0x3a.toHexString(shorterLengthFormat))
    println(0xff80ed.toHexString(shorterLengthFormat))

    // Specifying a minLength longer than the hex representation.
    // removeLeadingZeros is ignored in this case.
    val longerLengthFormat = HexFormat {
        number.removeLeadingZeros = true
        number.minLength = 12
    }
    println(0x3a.toHexString(longerLengthFormat))

    // When parsing, minLength is ignored.
    println("3a".hexToInt(longerLengthFormat))

    // The number of hex digits can be greater than what can fit into the type.
    println("00000000003a".hexToInt())
    println("0000ffffffff".hexToInt())
    // But excess leading digits must be zeros.
    assertFailsWith<IllegalArgumentException> { "000100000000".hexToInt() }
}
```

```text title="输出"
0000003a
0000003a
003a
ff80ed
00000000003a
58
58
-1
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L329)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
