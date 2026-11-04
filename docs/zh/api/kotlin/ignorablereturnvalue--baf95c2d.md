# IgnorableReturnValue

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

表示附加说明的功能的调用是可忽略的。 不可忽视的调用不会引发科特林的返回值检查器的警告,即使没有使用。

只有在与“ 返回值检查” 特性一起使用时, 此注释才有意义。 设置它而不启用相应的特性将导致编译器错误 。

请注意,这一特征目前是试验性的,这种注释可以改变,而无需进一步通知或折旧周期,这尤其涉及注释的目标清单。

??? note "查看英文原文"

    Expresses that calls of the annotated function are ignorable.
    Ignorable calls would not trigger a warning from Kotlin's return value checker, even if they are not used.
    
    This annotation only makes sense when used together with the 'Return value checker' feature.
    Placing it without enabling the corresponding feature would result in a compiler error.
    
    Please note that this feature is currently experimental and this annotation may be changed without further notice
    or deprecation cycle. This, in particular, concerns annotation's target list.

## 声明与重载

### 1. Common

```kotlin
@Target(AnnotationTarget.FUNCTION)
@MustBeDocumented
@SinceKotlin("2.2")
public annotation class IgnorableReturnValue
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotations/ReturnValue.kt#L8)

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
    val value = kotlin.IgnorableReturnValue()
    println(value)
}
```

```text title="输出"
@kotlin.IgnorableReturnValue()
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
