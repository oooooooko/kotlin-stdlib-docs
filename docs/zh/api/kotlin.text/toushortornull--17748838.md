# toUShortOrNull

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将字符串分割为 `UShort` 号, 如果字符串不是数字的有效表示, 则返回结果或 `null` 。

??? note "查看英文原文"

    Parses the string as an `UShort` number and returns the result
    or `null` if the string is not a valid representation of a number.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.5")
public fun String.toUShortOrNull(): UShort?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UStrings.kt#L132)

### 2. Common

```kotlin
@SinceKotlin("1.5")
public fun String.toUShortOrNull(radix: Int): UShort?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UStrings.kt#L139)

将字符串分割为 `UShort` 号, 如果字符串不是数字的有效表示, 则返回结果或 `null` 。

@throws 非法设备除外,当 `radix` 不是一个有效的 字符串转换为数字的 RADIX 时。

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
    val result = source.`toUShortOrNull`()
    println(result)
}
```

```text title="输出"
42
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
