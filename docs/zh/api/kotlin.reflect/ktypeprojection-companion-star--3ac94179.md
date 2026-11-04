# KTypeProjection.Companion.STAR

`kotlin.reflect` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

星体投影,用 `*` 字符表示。例如, `KClass<*>` ,`*`是星体投影。详情见[科特林语言文档](https://kotlinlang.org/docs/reference/generics.html#star-projections))。

??? note "查看英文原文"

    Star projection, denoted by the `*` character.
    For example, in the type `KClass<*>`, `*` is the star projection.
    See the [Kotlin language documentation](https://kotlinlang.org/docs/reference/generics.html#star-projections)
    for more information.

## 声明与重载

### 1. Common

```kotlin
public val STAR: KTypeProjection
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/reflect/KTypeProjection.kt#L58)

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
import kotlin.reflect.*

fun main() {
    val source = kotlin.reflect.KTypeProjection.Companion
    val result = source.`STAR`
    println(result)
}
```

```text title="输出"
*
```

此示例需要 `kotlin-reflect:2.4.21`。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
