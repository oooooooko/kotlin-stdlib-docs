# Uuid.Companion.parseHexOrNull

`kotlin.uuid` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

剖析十六进制字符串表示式的一字,如 `Uuid.toHexString` 所述,如果字符串有不同格式,则返回 `null` 。

此函数不区分大小写,对于有效的`hexString`, 持有下列财产:```kotlin
val uuid = Uuid.parseHexOrNull(hexString)!!
assertEquals(uuid.toHexString(), hexString.lowercase())
```

@param 十六进制字符串 代表 Uuid 的 32 个字符十六进制字符串,无连字符。 @return A uuid 代表指定的十六进制字符串,如果字符串不符合格式,则为 `null`。

@see Uuid.toHexString @see Uuid.parseHex @sample 样本.uud.Uuids. parseHex Ornull

??? note "查看英文原文"

    Parses a uuid from the hexadecimal string representation as described in `Uuid.toHexString`,
    returning `null` if a string has a different format.
    
    This function is case-insensitive, and for a valid `hexString`, the following property holds:
    ```kotlin
    val uuid = Uuid.parseHexOrNull(hexString)!!
    assertEquals(uuid.toHexString(), hexString.lowercase())
    ```
    
    @param hexString A 32-character hexadecimal string representing the uuid, without hyphens.
    @return A uuid represented by the specified hexadecimal string, or `null`, if the string does not conform the format.
    
    @see Uuid.toHexString
    @see Uuid.parseHex
    @sample samples.uuid.Uuids.parseHexOrNull

## 声明与重载

### 1. Common

```kotlin
public fun parseHexOrNull(hexString: String): Uuid?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L522)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid = Uuid.parseHexOrNull("550E8400e29b41d4A716446655440000") // case insensitive
    println(uuid)

    println(Uuid.parseHexOrNull("~550E8400e29b41d4A716446655440000~"))
}
```

```text title="输出"
550e8400-e29b-41d4-a716-446655440000
null
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L216)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
