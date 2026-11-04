# KTypeProjection

`kotlin.reflect` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

类型预测。类型预测通常是类型使用中另一种类型的参数。例如, `Array<out Number>` ,`out Number`是`Number`类代表的类型的共变预测。

类型预测要么是星体预测,要么是由特定类型加上可选差异组成的实体。

详情见[科特林语文件](https://kotlinlang.org/docs/reference/generics.html#type-projections))。

??? note "查看英文原文"

    Represents a type projection. Type projection is usually the argument to another type in a type usage.
    For example, in the type `Array<out Number>`, `out Number` is the covariant projection of the type represented by the class `Number`.
    
    Type projection is either the star projection, or an entity consisting of a specific type plus optional variance.
    
    See the [Kotlin language documentation](https://kotlinlang.org/docs/reference/generics.html#type-projections)
    for more information.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.1")
public data class KTypeProjection constructor(
    /**
     * The use-site variance specified in the projection, or `null` if this is a star projection.
     */
    public val variance: KVariance?,
    /**
     * The type specified in the projection, or `null` if this is a star projection.
     */
    public val type: KType?
)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/reflect/KTypeProjection.kt#L15)

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
    val value = kotlin.reflect.KTypeProjection(kotlin.reflect.KVariance.IN, typeOf<List<String>>())
    println(value)
}
```

```text title="输出"
in kotlin.collections.List<kotlin.String>
```

此示例需要 `kotlin-reflect:2.4.21`。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
