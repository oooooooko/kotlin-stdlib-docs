# Uuid.Companion.parseHex

`kotlin.uuid` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

以`Uuid.toHexString`中描述的十六进制字符串表示法为单位。

此函数不区分大小写,对于有效的`hexString`, 持有下列财产:```kotlin
val uuid = Uuid.parseHex(hexString)
assertEquals(uuid.toHexString(), hexString.lowercase())
```

@param 十六进制字符串 代表 Uuid 的 32 个字符十六进制字符串。 @throws 非法 参数例外 如果 `hexString` 不是 32 个字符 十六进制字符串。 @return A 符号由指定的十六进制字符串表示 。

@see Uuid.toHexString @see Uuid.parse HexOrNull @sample 样本.uuid.Uuids.parseHex

??? note "查看英文原文"

    Parses a uuid from the hexadecimal string representation as described in `Uuid.toHexString`.
    
    This function is case-insensitive, and for a valid `hexString`, the following property holds:
    ```kotlin
    val uuid = Uuid.parseHex(hexString)
    assertEquals(uuid.toHexString(), hexString.lowercase())
    ```
    
    @param hexString A 32-character hexadecimal string representing the uuid, without hyphens.
    @throws IllegalArgumentException If the `hexString` is not a 32-character hexadecimal string.
    @return A uuid represented by the specified hexadecimal string.
    
    @see Uuid.toHexString
    @see Uuid.parseHexOrNull
    @sample samples.uuid.Uuids.parseHex

## 声明与重载

### 1. Common

```kotlin
public fun parseHex(hexString: String): Uuid
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L497)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid = Uuid.parseHex("550E8400e29b41d4A716446655440000") // case insensitive
    println(uuid)

    assertFailsWith<IllegalArgumentException> { Uuid.parseHex("~550E8400e29b41d4A716446655440000~") }
}
```

```text title="输出"
550e8400-e29b-41d4-a716-446655440000
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L208)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
