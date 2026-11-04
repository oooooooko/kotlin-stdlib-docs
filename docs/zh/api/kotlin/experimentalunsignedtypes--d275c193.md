# ExperimentalUnsignedTypes

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

标记依赖实验无符号类型(包括这些类型本身)的API。

除非明确选择使用 `OptIn` 注解,例如 `@OptIn(ExperimentalUnsignedTypes::class)` ,或选择`-opt-in=kotlin.ExperimentalUnsignedTypes`编译器,否则,这种API的使用将报告为警告。

建议向API传播实验状态 取决于无符号类型 以这个注解来说明

??? note "查看英文原文"

    Marks the API that is dependent on the experimental unsigned types, including those types themselves.
    
    Usages of such API will be reported as warnings unless an explicit opt-in with
    the `OptIn` annotation, e.g. `@OptIn(ExperimentalUnsignedTypes::class)`,
    or with the `-opt-in=kotlin.ExperimentalUnsignedTypes` compiler option is given.
    
    It's recommended to propagate the experimental status to the API that depends on unsigned types by annotating it with this annotation.

## 声明与重载

### 1. Common

```kotlin
@RequiresOptIn(level = RequiresOptIn.Level.WARNING)
@MustBeDocumented
@Target(CLASS, ANNOTATION_CLASS, PROPERTY, FIELD, LOCAL_VARIABLE, VALUE_PARAMETER, CONSTRUCTOR, FUNCTION, PROPERTY_GETTER, PROPERTY_SETTER, TYPEALIAS)
@Retention(AnnotationRetention.BINARY)
public annotation class ExperimentalUnsignedTypes
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/unsigned/src/kotlin/annotations/Unsigned.kt#L13)

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
    val value = kotlin.ExperimentalUnsignedTypes()
    println(value)
}
```

```text title="输出"
@kotlin.ExperimentalUnsignedTypes()
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
