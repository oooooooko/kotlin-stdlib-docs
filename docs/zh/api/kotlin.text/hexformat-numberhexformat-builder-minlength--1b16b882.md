# HexFormat.NumberHexFormat.Builder.minLength

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

定义了正在构建的格式的 `NumberHexFormat.minLength` , 默认情况下为 `1` 。

价值必须是积极的。

格式选项如何影响格式化和分析结果,详见`NumberHexFormat.minLength`。

@throws 非法购置权,如果该财产被指定非正值,则不在此列。

@sample 样本. text. HexFormats. 编号.minLength

??? note "查看英文原文"

    Defines `NumberHexFormat.minLength` of the format being built, `1` by default.
    
    The value must be positive.
    
    Refer to `NumberHexFormat.minLength` for details about how the format option affects
    the formatting and parsing results.
    
    @throws IllegalArgumentException if a non-positive value is assigned to this property.
    
    @sample samples.text.HexFormats.Numbers.minLength

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.0")
            public var minLength: Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L597)

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
