# Uuid.toString

`kotlin.uuid` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回此 uuid 的标准字符串表示法。

此函数返回与`toHexDashString`相同的值。

所产生的字符串以“xx”格式, 代表十六进制数字, 也称为“ hex- dash” 格式。 它以小写形式, 由36个字符组成。 字符串中的每个十六进制数字顺序代表 uuid 的下四个位数, 从第一个位数中最重要的四位数开始, 到最后一个位数中最小的四位数 。

这是uuuds 的标准文字表达格式,符合大多数软件环境中的uuid 解析逻辑。 [RFC 9562第4节](https://www.rfc-editor.org/rfc/rfc9562.html#section-4).)对此作了具体规定。

@see Uuid.parse @see Uuid.to HexDash String @sample 样本.uud.Uuids.to StringSample

??? note "查看英文原文"

    Returns the standard string representation of this uuid.
    
    This function returns the same value as `toHexDashString`.
    
    The resulting string is in the format "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    where 'x' represents a hexadecimal digit, also known as "hex-and-dash" format.
    It is in lowercase and consists of 36 characters. Each hexadecimal digit
    in the string sequentially represents the next 4 bits of the uuid, starting from the most
    significant 4 bits in the first digit to the least significant 4 bits in the last digit.
    
    This format is the standard textual representation of uuids and is compatible with
    uuid parsing logic found in most software environments. It is specified by
    [RFC 9562 section 4](https://www.rfc-editor.org/rfc/rfc9562.html#section-4).
    
    @see Uuid.parse
    @see Uuid.toHexDashString
    @sample samples.uuid.Uuids.toStringSample

## 声明与重载

### 1. Common

```kotlin
override fun toString(): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L128)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid = Uuid.fromULongs(0x550E8400E29B41D4uL, 0xA716446655440000uL)
    println(uuid.toString())
}
```

```text title="输出"
550e8400-e29b-41d4-a716-446655440000
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L88)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
