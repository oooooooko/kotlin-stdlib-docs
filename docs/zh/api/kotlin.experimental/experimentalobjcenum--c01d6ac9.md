# ExperimentalObjCEnum

`kotlin.experimental` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

此注解标志实验性`ObjCEnum`Z`kotlin.native.ObjCEnum`注解,该注解被视为实验性,不需受
为标准库提供的 [general compatibility guarantees](https://kotlinlang.org/docs/reference/evolution/components-stability.html) :
此类注解的行为可能改变,或注解在任何进一步发布中可完全删除。

> 请注意使用附加说明的说明,特别是如果正在开发图书馆,因为图书馆可能变成与标准图书馆未来版本不相容的二进制。

??? note "查看英文原文"

    This annotation marks the experimental `ObjCEnum``kotlin.native.ObjCEnum` annotation that is considered experimental and is not subject to the
    [general compatibility guarantees](https://kotlinlang.org/docs/reference/evolution/components-stability.html) given for the standard library:
    the behavior of such annotation may be changed or the annotation may be removed completely in any further release.
    
    > Beware using the annotated annotation especially if you're developing a library, since your library might become binary incompatible
    with the future versions of the standard library.

## 声明与重载

### 1. Common

```kotlin
@RequiresOptIn
@Target(AnnotationTarget.ANNOTATION_CLASS)
@Retention(AnnotationRetention.BINARY)
@MustBeDocumented
@SinceKotlin("2.3")
public annotation class ExperimentalObjCEnum
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/experimental/ExperimentalObjCEnum.kt#L8)

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
import kotlin.experimental.*

fun main() {
    val value = kotlin.experimental.ExperimentalObjCEnum()
    println(value)
}
```

```text title="输出"
@kotlin.experimental.ExperimentalObjCEnum()
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
