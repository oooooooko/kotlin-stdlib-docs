# HexFormat.Builder.number

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

定义正在构建的格式的 `HexFormat.number` 。

有关可用格式选项、其对格式化和分析结果的影响及其默认设置的细节,请查阅`NumberHexFormat`。

??? note "查看英文原文"

    Defines `HexFormat.number` of the format being built.
    
    Refer to `NumberHexFormat` for details about the available format options, their impact on formatting and
    parsing results, and their default settings.

## 声明与重载

### 1. Common

```kotlin
public val number: NumberHexFormat.Builder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L671)

### 2. Common

```kotlin
@InlineOnly
        public inline fun number(builderAction: NumberHexFormat.Builder.() -> Unit)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/HexFormat.kt#L722)

提供了`number`财产配置空间。

`builderAction` 的接收器是 `number` 属性。 因此, 牙套内部可以直接配置选项。 此方便功能旨在让多个选项配置在一个单个块内。 例如, 片段 :```kotlin
val format = HexFormat {
    number {
        prefix = "&#x"
        suffix = ";"
        removeLeadingZeros = true
    }
}
```等于:```kotlin
val format = HexFormat {
    number.prefix = "&#x"
    number.suffix = ";"
    number.removeLeadingZeros = true
}
```

有关可用格式选项、其对格式化和分析结果的影响及其默认设置的细节,请查阅`NumberHexFormat`。

@param 建筑商行动 适用于`number`财产的功能,为直接配置其选项提供了空间。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val numberHexFormat = HexFormat {
        upperCase = true
        number {
            removeLeadingZeros = true
            minLength = 4
            prefix = "0x"
        }
    }

    println(0x3a.toHexString(numberHexFormat))
    println("0x003A".hexToInt(numberHexFormat))
    // Parsing is case-insensitive
    println("0X003a".hexToInt(numberHexFormat))
}
```

```text title="输出"
0x003A
58
58
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/hexFormat.kt#L236)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
