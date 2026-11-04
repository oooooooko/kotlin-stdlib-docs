# StringBuilder.setLength

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将此字符串构建器的长度设置为指定的 `newLength` 。

如果 `newLength` 低于当前长度, 则将其修改为指定的 `newLength` 。 否则, 字符串构建器上将附加无效字符“\ u00000 ” , 直到其长度低于 `newLength` 长度 。

请注意, Kotlin/ JS `set` 操作员功能具有非连续执行时间复杂性。 因此, 增加字符串构建器的长度, 然后以索引方式更新每个字符可能会减缓您的程序 。

@throws 指数外延 或 `newLength` 低于 0 的 `IllegalArgumentException` 。

??? note "查看英文原文"

    Sets the length of this string builder to the specified `newLength`.
    
     If the `newLength` is less than the current length, it is changed to the specified `newLength`.
     Otherwise, null characters '\u0000' are appended to this string builder until its length is less than the `newLength`.
    
     Note that in Kotlin/JS `set` operator function has non-constant execution time complexity.
     Therefore, increasing length of this string builder and then updating each character by index may slow down your program.
    
     @throws IndexOutOfBoundsException or `IllegalArgumentException` if `newLength` is less than zero.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
    public fun setLength(newLength: Int)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L285)

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
    val source = StringBuilder("kotlin")
    val result = source.`setLength`(2)
    println(result)
}
```

```text title="输出"
kotlin.Unit
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
