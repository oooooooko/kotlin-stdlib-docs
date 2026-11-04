# toRawBits

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

根据 IEEE 754 浮点“双格式”位版式,返回指定浮点值的位表示值为 `Long` , 以保存 `NaN` 的准确布局。

??? note "查看英文原文"

    Returns a bit representation of the specified floating-point value as `Long`
    according to the IEEE 754 floating-point "double format" bit layout,
    preserving `NaN` values exact layout.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Double.toRawBits(): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/KotlinH.kt#L50)

### 2. Common

```kotlin
@SinceKotlin("1.2")
public expect fun Float.toRawBits(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/KotlinH.kt#L71)

根据 IEEE 754 浮点“单格式”位版式,返回指定浮点值的位表示值为 `Int` , 以保存 `NaN` 的准确布局。

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
    val source = 5.5
    val result = source.`toRawBits`()
    println(result)
}
```

```text title="输出"
4617878467915022336
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
