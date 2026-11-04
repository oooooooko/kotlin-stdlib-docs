# typeOf

`kotlin.reflect` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回给定的 `T` 型重新编码的运行时间代表, 以 `KType` 例。

请注意,在 JVM 上, 创建的型号没有附加说明( `KType.annotations` 返回空列表) , 即使源代码中的类型是附加说明的 。 未来版本中可能会添加类型说明支持 。

??? note "查看英文原文"

    Returns a runtime representation of the given reified type `T` as an instance of `KType`.
    
    Note that on JVM, the created type has no annotations (`KType.annotations` returns an empty list)
    even if the type in the source code is annotated. Support for type annotations might be added in a future version.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.6")
public inline fun <reified T> typeOf(): KType
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/reflect/typeOf.kt#L8)

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
    val value = typeOf<List<String>>()
    println(value)
}
```

```text title="输出"
kotlin.collections.List<kotlin.String>
```

此示例需要 `kotlin-reflect:2.4.21`。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
