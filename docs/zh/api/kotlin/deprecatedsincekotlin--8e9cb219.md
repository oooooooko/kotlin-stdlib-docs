# DeprecatedSinceKotlin

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

标记附加说明的声明为折旧声明。 与 `Deprecated` 相比, 报告的诊断严重性不是一个不变值, 但它因使用方的 API 版本而不同( 汇编使用方所在模块时的 `-api-version` 参数值为`-api-version` ) 。 如果 API 版本大于或等于 `hiddenSince` , 则声明无法从代码中查阅( 如它被 `DeprecationLevel.HIDDEN` 水平折旧) , 否则, 如果API 版本大于或等于`errorSince`, 则使用方将被标记为错误( 如 `DeprecationLevel.ERROR` ) , 否则, 如果 API 版本大于或等于 `warningSince` , 则该使用方将被标记为警告( 如 `DeprecationLevel.WARNING` ) , 否则, 注释将被忽略 。

@property 警告: 版本, 由此可以将这一折旧报告为警告。 @property 错误: 版本, 由此将这一折旧报告为错误。 @property 隐藏了版本: 说明声明不应以代码形式提供。

??? note "查看英文原文"

    Marks the annotated declaration as deprecated. In contrast to `Deprecated`, severity of the reported diagnostic is not a constant value,
    but differs depending on the API version of the usage (the value of the `-api-version` argument when compiling the module where
    the usage is located). If the API version is greater or equal than `hiddenSince`, the declaration will not be accessible from the code
    (as if it was deprecated with level `DeprecationLevel.HIDDEN`), otherwise if the API version is greater or equal than `errorSince`,
    the usage will be marked as an error (as with `DeprecationLevel.ERROR`), otherwise if the API version is greater or equal
    than `warningSince`, the usage will be marked as a warning (as with `DeprecationLevel.WARNING`), otherwise the annotation is ignored.
    
    @property warningSince The version, since which this deprecation should be reported as a warning.
    @property errorSince The version, since which this deprecation should be reported as a error.
    @property hiddenSince The version, since which the annotated declaration should not be available in code.

## 声明与重载

### 1. Common

```kotlin
@Target(CLASS, FUNCTION, PROPERTY, ANNOTATION_CLASS, CONSTRUCTOR, PROPERTY_SETTER, PROPERTY_GETTER, TYPEALIAS)
@MustBeDocumented
@SinceKotlin("1.4")
public annotation class DeprecatedSinceKotlin(
    val warningSince: String = "",
    val errorSince: String = "",
    val hiddenSince: String = ""
)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Annotations.kt#L42)

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
    val value = kotlin.DeprecatedSinceKotlin()
    println(value)
}
```

```text title="输出"
@kotlin.DeprecatedSinceKotlin(warningSince=, errorSince=, hiddenSince=)
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
