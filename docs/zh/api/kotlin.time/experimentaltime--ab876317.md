# ExperimentalTime

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

此注释标志着标准库 API 用于测量时间和工作时间的实验预览。

> 注意该 API 处于预览状态, 将来极有可能被更改。 如果您开发了一个图书馆, 则不要使用它, 因为您的图书馆将会变成与标准图书馆未来版本不兼容的二进制 。

任何附加`@ExperimentalTime`的附加说明的声明的使用都必须接受,为此,必须说明使用`OptIn`的注释,例如`@OptIn(ExperimentalTime::class)`, 或使用汇编者的论点`-opt-in=kotlin.time.ExperimentalTime`。

??? note "查看英文原文"

    This annotation marks the experimental preview of the standard library API for measuring time and working with durations.
    
    > Note that this API is in a preview state and has a very high chance of being changed in the future.
    Do not use it if you develop a library since your library will become binary incompatible
    with the future versions of the standard library.
    
    Any usage of a declaration annotated with `@ExperimentalTime` must be accepted either by
    annotating that usage with the `OptIn` annotation, e.g. `@OptIn(ExperimentalTime::class)`,
    or by using the compiler argument `-opt-in=kotlin.time.ExperimentalTime`.

## 声明与重载

### 1. Common

```kotlin
@RequiresOptIn(level = RequiresOptIn.Level.ERROR)
@MustBeDocumented
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
@SinceKotlin("1.3")
public annotation class ExperimentalTime
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/ExperimentalTime.kt#L10)

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
import kotlin.time.*

fun main() {
    val value = kotlin.time.ExperimentalTime()
    println(value)
}
```

```text title="输出"
@kotlin.time.ExperimentalTime()
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
