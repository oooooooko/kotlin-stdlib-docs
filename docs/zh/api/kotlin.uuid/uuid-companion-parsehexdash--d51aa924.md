# Uuid.Companion.parseHexDash

`kotlin.uuid` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

以 `Uuid.toHexDashString` 中描述的标准十六和四弦表示法为单位。

此函数不区分大小写,对于有效的`hexDashString`, 持有下列财产:```kotlin
val uuid = Uuid.parseHexDash(hexDashString)
assertEquals(uuid.toHexDashString(), hexDashString.lowercase())
```

[FRC 9562第4节](https://www.rfc-editor.org/rfc/rfc9562.html#section-4).)具体规定了标准格式(Uuids),也称x-dash格式。

@param 六头蛇 以"xxxxxxxxxxxxxxxxxxxxxxxxxxxxashstring A 字符串"格式的"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
每个“ x” 是一个十六进制数字, 要么是小写,要么是大写。
@throws 非法参数例外 如果 `hexDashString` 不是36字符字符串
。
@return A uuid 等同指定的 uuid 字符串 。

@see Uuid.to HexDash String @see Uuid.parse HexDash OrNull @sample 样本.uud.Uuids.parse HexDash

??? note "查看英文原文"

    Parses a uuid from the standard hex-and-dash string representation as described in `Uuid.toHexDashString`.
    
    This function is case-insensitive, and for a valid `hexDashString`, the following property holds:
    ```kotlin
    val uuid = Uuid.parseHexDash(hexDashString)
    assertEquals(uuid.toHexDashString(), hexDashString.lowercase())
    ```
    
    The standard textual representation of uuids, also known as hex-and-dash format, is specified by
    [RFC 9562 section 4](https://www.rfc-editor.org/rfc/rfc9562.html#section-4).
    
    @param hexDashString A string in the format "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      where each 'x' is a hexadecimal digit, either lowercase or uppercase.
    @throws IllegalArgumentException If the `hexDashString` is not a 36-character string
      in the standard uuid format.
    @return A uuid equivalent to the specified uuid string.
    
    @see Uuid.toHexDashString
    @see Uuid.parseHexDashOrNull
    @sample samples.uuid.Uuids.parseHexDash

## 声明与重载

### 1. Common

```kotlin
public fun parseHexDash(hexDashString: String): Uuid
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L441)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid = Uuid.parseHexDash("550E8400-e29b-41d4-A716-446655440000") // case insensitive
    println(uuid)

    assertFailsWith<IllegalArgumentException> { Uuid.parseHexDash("550E8400/e29b/41d4/A716/446655440000") }
}
```

```text title="输出"
550e8400-e29b-41d4-a716-446655440000
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L192)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
