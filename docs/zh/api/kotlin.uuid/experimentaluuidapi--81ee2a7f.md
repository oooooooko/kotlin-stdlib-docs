# ExperimentalUuidApi

`kotlin.uuid` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

这个注解标志着实验性的 Kotlin Uuid API。

> 请注意使用附加说明的API,特别是如果正在开发图书馆,因为图书馆可能会变成与标准图书馆未来版本不相容的二进制。

任何附加`@ExperimentalUuidApi`的附加说明的声明的使用都必须接受,为此,必须说明使用`OptIn`的注释,例如`@OptIn(ExperimentalUuidApi::class)`, 或使用汇编者的论点`-opt-in=kotlin.uuid.ExperimentalUuidApi`。

??? note "查看英文原文"

    This annotation marks the experimental Kotlin Uuid API.
    
    > Beware using the annotated API especially if you're developing a library, since your library might become binary incompatible
    with the future versions of the standard library.
    
    Any usage of a declaration annotated with `@ExperimentalUuidApi` must be accepted either by
    annotating that usage with the `OptIn` annotation, e.g. `@OptIn(ExperimentalUuidApi::class)`,
    or by using the compiler argument `-opt-in=kotlin.uuid.ExperimentalUuidApi`.

## 声明与重载

### 1. Common

```kotlin
@RequiresOptIn(level = RequiresOptIn.Level.ERROR)
@Retention(AnnotationRetention.BINARY)
@Target(
    CLASS,
    ANNOTATION_CLASS,
    PROPERTY,
    FIELD,
    LOCAL_VARIABLE,
    VALUE_PARAMETER,
    CONSTRUCTOR,
    FUNCTION,
    PROPERTY_GETTER,
    PROPERTY_SETTER,
    TYPEALIAS
)
@MustBeDocumented
@SinceKotlin("2.0")
public annotation class ExperimentalUuidApi
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/uuid/ExperimentalUuidApi.kt#L10)

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
import kotlin.uuid.*

fun main() {
    val value = kotlin.uuid.ExperimentalUuidApi()
    println(value)
}
```

```text title="输出"
@kotlin.uuid.ExperimentalUuidApi()
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
