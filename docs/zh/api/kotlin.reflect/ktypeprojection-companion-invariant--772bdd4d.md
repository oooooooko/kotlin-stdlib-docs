# KTypeProjection.Companion.invariant

`kotlin.reflect` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

创建给定类型的无变预测。 不变预测本身只是类型本身, 没有任何使用场点差异变换器。 例如, `Set<String>` 类型中的 `String` 是类 `String` 所代表的类型的无变预测 。

??? note "查看英文原文"

    Creates an invariant projection of a given type. Invariant projection is just the type itself,
    without any use-site variance modifiers applied to it.
    For example, in the type `Set<String>`, `String` is an invariant projection of the type represented by the class `String`.

## 声明与重载

### 1. Common

```kotlin
@JvmStatic
        public fun invariant(type: KType): KTypeProjection
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/reflect/KTypeProjection.kt#L66)

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
    val result = source.`invariant`(typeOf<List<String>>())
    println(result)
}
```

```text title="输出"
kotlin.collections.List<kotlin.String>
```

此示例需要 `kotlin-reflect:2.4.21`。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
