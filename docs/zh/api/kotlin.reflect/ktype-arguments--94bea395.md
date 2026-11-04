# KType.arguments

`kotlin.reflect` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

用于分类器参数的输入参数。 例如, 在 `Array<out Number>` 类型中, 唯一的输入参数是 `out Number` 。

如果这种类型的清单是基于内部类,则返回的清单中首先包含为最底层类提供的分类参数,然后是其外层类等。例如,在`Outer<A, B>.Inner<C, D>`类中,返回的清单是“`C, D, A, B`”。

??? note "查看英文原文"

    Type arguments passed for the parameters of the classifier in this type.
    For example, in the type `Array<out Number>` the only type argument is `out Number`.
    
    In case this type is based on an inner class, the returned list contains the type arguments provided for the innermost class first,
    then its outer class, and so on.
    For example, in the type `Outer<A, B>.Inner<C, D>` the returned list is ``C, D, A, B``.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.1")
    public val arguments: List<KTypeProjection>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/reflect/KType.kt#L24)

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
    val source = typeOf<List<String>>()
    val result = source.`arguments`
    println(result)
}
```

```text title="输出"
[kotlin.String]
```

此示例需要 `kotlin-reflect:2.4.21`。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
