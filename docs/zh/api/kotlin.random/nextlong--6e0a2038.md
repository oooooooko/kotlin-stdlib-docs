# nextLong

`kotlin.random` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

从指定的 `range` 中的随机数字生成器中获取下一个随机的 `Long` 。

生成 `Long` 随机值,统一分布在指定的`range`:从`range.start`(含)到`range.endInclusive`(含)。

@throws 非法设备,如果 `range` 空的话,则不在此限。

??? note "查看英文原文"

    Gets the next random `Long` from the random number generator in the specified `range`.
    
    Generates a `Long` random value uniformly distributed in the specified `range`:
    from `range.start` inclusive to `range.endInclusive` inclusive.
    
    @throws IllegalArgumentException if `range` is empty.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
public fun Random.nextLong(range: LongRange): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L361)

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
import kotlin.random.*

fun main() {
    val source = Random(42)
    val result = source.`nextLong`(1L..3L)
    println(result)
}
```

```text title="输出"
3
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
