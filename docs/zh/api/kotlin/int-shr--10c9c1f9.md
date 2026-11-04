# Int.shr

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将此值右移`bitCount`位数位数,用符号位数的复制件填充最左位数。

请注意,`bitCount` 中只有五个最低级位作为移动距离。 因此,实际使用的移动距离总是在`0..31` 之间。

??? note "查看英文原文"

    Shifts this value right by the `bitCount` number of bits, filling the leftmost bits with copies of the sign bit.
    
    Note that only the five lowest-order bits of the `bitCount` are used as the shift distance.
    The shift distance actually used is therefore always in the range `0..31`.

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.IntrinsicConstEvaluation
    public infix fun shr(bitCount: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L1053)

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
    val result = source.`shr`(2)
    println(result)
}
```

```text title="输出"
1
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
