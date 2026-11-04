# toUByte

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将字符串分割为已签名的 `UByte` 号, 并返回结果 。 @throws 号格式例外, 如果字符串不是数字的有效表示 。

??? note "查看英文原文"

    Parses the string as a signed `UByte` number and returns the result.
    @throws NumberFormatException if the string is not a valid representation of a number.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.5")
public fun String.toUByte(): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UStrings.kt#L47)

### 2. Common

```kotlin
@SinceKotlin("1.5")
public fun String.toUByte(radix: Int): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UStrings.kt#L54)

将字符串分割为已签名的 `UByte` 号, 并返回结果 。 @throws 号数字格式例外, 如果字符串不是有效的数字表示。 @throws 非法配置除外, 当 `radix` 号不是用于字符串转换为数字的有效 RADIX 时, 则不在此列 。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.text.*

fun main() {
    val source = "42"
    val result = source.`toUByte`()
    println(result)
}
```

```text title="输出"
42
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
