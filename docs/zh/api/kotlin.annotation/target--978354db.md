# Target

`kotlin.annotation` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

这种元注解表示代号元素的种类,这些代号元素可能是注解的目标。

如果注解声明没有标注的元注,则注解适用于下列要素: `CLASS` 、 `PROPERTY` 、 `FIELD` 、 `FIELD` 、`LOCAL_VARIABLE`、`VALUE_PARAMETER`、`CONSTRUCTOR`、`FUNCTION`、`PROPERTY_GETTER`、`PROPERTY_GETTER`、 `PROPERTY_SETTER` 。

@property 允许使用允许注注解目标的具体目标列表

??? note "查看英文原文"

    This meta-annotation indicates the kinds of code elements which are possible targets of an annotation.
    
    If the target meta-annotation is not present on an annotation declaration, the annotation is applicable to the following elements:
    `CLASS`, `PROPERTY`, `FIELD`, `LOCAL_VARIABLE`, `VALUE_PARAMETER`, `CONSTRUCTOR`, `FUNCTION`, `PROPERTY_GETTER`, `PROPERTY_SETTER`.
    
    @property allowedTargets list of allowed annotation targets

## 声明与重载

### 1. Common

```kotlin
@Target(AnnotationTarget.ANNOTATION_CLASS)
@MustBeDocumented
public annotation class Target(vararg val allowedTargets: AnnotationTarget)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotation/Annotations.kt#L63)

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
import kotlin.annotation.*

fun main() {
    val value = kotlin.annotation.Target(kotlin.annotation.AnnotationTarget.ANNOTATION_CLASS)
    println(value)
}
```

```text title="输出"
@kotlin.annotation.Target(allowedTargets=[ANNOTATION_CLASS])
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
