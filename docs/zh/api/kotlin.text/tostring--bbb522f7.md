# toString

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回指定 `radix` 的`Byte`值的字符串表示值。

@throws 非法设备除外,当`radix`不是数字转换为字符串的有效弧度时。

??? note "查看英文原文"

    Returns a string representation of this `Byte` value in the specified `radix`.
    
    @throws IllegalArgumentException when `radix` is not a valid radix for number to string conversion.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Byte.toString(radix: Int): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L650)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Short.toString(radix: Int): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L658)

返回指定 `radix` 的`Short`值的字符串表示值。

@throws 非法设备除外,当`radix`不是数字转换为字符串的有效弧度时。

### 3. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Int.toString(radix: Int): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L666)

返回指定 `radix` 的`Int`值的字符串表示值。

@throws 非法设备除外,当`radix`不是数字转换为字符串的有效弧度时。

### 4. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Long.toString(radix: Int): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L674)

返回指定 `radix` 的`Long`值的字符串表示值。

@throws 非法设备除外,当`radix`不是数字转换为字符串的有效弧度时。

### 5. Common

```kotlin
@SinceKotlin("1.5")
//@kotlin.internal.InlineOnly
public /*inline*/ fun UByte.toString(radix: Int): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UStrings.kt#L10)

### 6. Common

```kotlin
@SinceKotlin("1.5")
//@kotlin.internal.InlineOnly
public /*inline*/ fun UShort.toString(radix: Int): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UStrings.kt#L19)

返回指定 `radix` 的`Short`值的字符串表示值。

@throws 非法设备除外,当`radix`不是数字转换为字符串的有效弧度时。

### 7. Common

```kotlin
@SinceKotlin("1.5")
//@kotlin.internal.InlineOnly
public /*inline*/ fun UInt.toString(radix: Int): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UStrings.kt#L29)

返回指定 `radix` 的`Int`值的字符串表示值。

@throws 非法设备除外,当`radix`不是数字转换为字符串的有效弧度时。

### 8. Common

```kotlin
@SinceKotlin("1.5")
public fun ULong.toString(radix: Int): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/UStrings.kt#L38)

返回指定 `radix` 的`Long`值的字符串表示值。

@throws 非法设备除外,当`radix`不是数字转换为字符串的有效弧度时。

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
    val source = 5.toByte()
    val result = source.`toString`(2)
    println(result)
}
```

```text title="输出"
101
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
