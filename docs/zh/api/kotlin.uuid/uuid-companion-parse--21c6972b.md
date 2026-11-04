# Uuid.Companion.parse

`kotlin.uuid` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

从支持的字符串表达式中, 分析一个名词 。

此函数支持解析标准十六进制和十六进制字符串表达式。 关于十六进制格式的细节, 请参考 `toHexDashString` 。 如果只想要解析十六进制和十六进制格式, 请使用 `parseHexDash` 。 关于十六进制格式的细节, 请参考 `toHexString` 。 如果只解析十六进制格式, 请使用 `parseHex` 。

请注意,此函数不区分大小写,意指小写和大写十六进制数字都有效。此外,今后可能引入对更多uuid格式的支持。因此,用户不应依赖拒绝目前不支持的格式。

@param uidString A 字符串,以一个支持的 uid 格式 。 @throws 非法 参数例外 , 如果 `uuidString` 不是一个支持的 uid 格式 。 @return A uid 等值指定的 uid 字符串 。

@see Uuid.parseHexDash @see Uuid.parse Hex @sample 样本.uuud.Uuids.parse

??? note "查看英文原文"

    Parses a uuid from one of the supported string representations.
    
    This function supports parsing the standard hex-and-dash and the hexadecimal string representations.
    For details about the hex-and-dash format, refer to `toHexDashString`.
    If parsing only the hex-and-dash format is desired, use `parseHexDash` instead.
    For details about the hexadecimal format, refer to `toHexString`.
    If parsing only the hexadecimal format is desired, use `parseHex` instead.
    
    Note that this function is case-insensitive,
    meaning both lowercase and uppercase hexadecimal digits are considered valid.
    Additionally, support for more uuid formats may be introduced in the future.
    Therefore, users should not rely on the rejection of formats not currently supported.
    
    @param uuidString A string in one of the supported uuid formats.
    @throws IllegalArgumentException If the `uuidString` is not in a supported uuid format.
    @return A uuid equivalent to the specified uuid string.
    
    @see Uuid.parseHexDash
    @see Uuid.parseHex
    @sample samples.uuid.Uuids.parse

## 声明与重载

### 1. Common

```kotlin
public fun parse(uuidString: String): Uuid
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L377)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    // Parsing is case-insensitive
    val uuid1 = Uuid.parse("550E8400-e29b-41d4-A716-446655440000") // hex-and-dash
    val uuid2 = Uuid.parse("550e8400E29b41D4a716446655440000") // hexadecimal

    println(uuid1 == uuid2)
    println(uuid1)
    println(uuid2)

    assertFailsWith<IllegalArgumentException> { Uuid.parse("I'm not a UUID, sorry") }
}
```

```text title="输出"
true
550e8400-e29b-41d4-a716-446655440000
550e8400-e29b-41d4-a716-446655440000
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L166)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
