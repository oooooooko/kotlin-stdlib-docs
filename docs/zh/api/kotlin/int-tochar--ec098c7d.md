# Int.toChar

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将这个`Int`值转换为 `Char` 。

如果该值在 `Char` 代码 `Char.MIN_VALUE..Char.MAX_VALUE` 的范围内,则由此得出的 `Char` 代码等于该值。

由此得出的`Char`代码代表的值为`Int`中最小的16位数。

??? note "查看英文原文"

    Converts this `Int` value to `Char`.
    
    If this value is in the range of `Char` codes `Char.MIN_VALUE..Char.MAX_VALUE`,
    the resulting `Char` code is equal to this value.
    
    The resulting `Char` code is represented by the least significant 16 bits of this `Int` value.

## 声明与重载

### 1. Common

```kotlin
@Suppress("OVERRIDE_DEPRECATION")
    @kotlin.internal.IntrinsicConstEvaluation
    public override fun toChar(): Char
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L1098)

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
import kotlin.*

fun main() {
    val source = 5
    val result = source.`toChar`()
    println(result)
}
```

```text title="输出"

```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
