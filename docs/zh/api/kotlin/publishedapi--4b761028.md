# PublishedApi

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

当适用于具有内部可见度的阶层或成员时,可以使用公共内线功能,并有效地予以公开。

公共内线功能不能使用非公共的API,因为如果这些非公共的API参考线被嵌入,这些非公共的API参考线将违反对呼叫地点的出入限制(见[对公共API内线功能的限制](https://kotlinlang.org/docs/inline-functions.html#restrictions-for-public-api-inline-functions)).)

为了克服这一限制, `internal` 声明可加上`@PublishedApi`说明:这允许将这一声明称为公共内线功能;宣布实际上公开,这在二进制兼容性维护方面应予考虑。

??? note "查看英文原文"

    When applied to a class or a member with internal visibility allows using it from public inline functions and
    makes it effectively public.
    
    Public inline functions cannot use non-public API, since if they are inlined, those non-public API references
    would violate access restrictions at a call site
    (see [restrictions for public API inline functions](https://kotlinlang.org/docs/inline-functions.html#restrictions-for-public-api-inline-functions)).
    
    To overcome this restriction an `internal` declaration can be annotated with the `@PublishedApi` annotation:
    - this allows calling that declaration from public inline functions;
    - the declaration becomes effectively public, and this should be considered with respect to binary compatibility maintaining.

## 声明与重载

### 1. Common

```kotlin
@Target(AnnotationTarget.CLASS, AnnotationTarget.CONSTRUCTOR, AnnotationTarget.FUNCTION, AnnotationTarget.PROPERTY)
@Retention(AnnotationRetention.BINARY)
@MustBeDocumented
@SinceKotlin("1.1")
public annotation class PublishedApi
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Annotations.kt#L176)

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
    val value = kotlin.PublishedApi()
    println(value)
}
```

```text title="输出"
@kotlin.PublishedApi()
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
