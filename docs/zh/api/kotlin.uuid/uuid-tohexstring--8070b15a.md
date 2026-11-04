# Uuid.toHexString

`kotlin.uuid` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回此 uuid 的十六进制字符串表示法,无连字符。

所产生的字符串以小写形式排列,由32个字符组成。字符串中每个十六进制数字顺序代表 uud 的下四个位数,从第一个数字中最重要的四个位数开始,到最后一个数字中最小的4位数。

返回的字符串相当于:```kotlin
uuid.toByteArray().toHexString()
```

@see Uuid.parseHex @sample 样本.uuud.Uuids.toHexString

??? note "查看英文原文"

    Returns the hexadecimal string representation of this uuid without hyphens.
    
    The resulting string is in lowercase and consists of 32 characters. Each hexadecimal digit
    in the string sequentially represents the next 4 bits of the uuid, starting from the most
    significant 4 bits in the first digit to the least significant 4 bits in the last digit.
    
    The returned string is equivalent to:
    ```kotlin
    uuid.toByteArray().toHexString()
    ```
    
    @see Uuid.parseHex
    @sample samples.uuid.Uuids.toHexString

## 声明与重载

### 1. Common

```kotlin
public fun toHexString(): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/Uuid.kt#L181)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid = Uuid.fromULongs(0x550E8400E29B41D4uL, 0xA716446655440000uL)
    println(uuid.toHexString())
}
```

```text title="输出"
550e8400e29b41d4a716446655440000
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L100)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
