# OptionalExpectation

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

这是一个最小多平台编译示例。`common.kt` 属于 common 源集；注解没有 actual 实现时会被擦除，通用函数仍可正常使用。

??? note "查看英文原文"

    Marks an expected annotation class that it isn't required to have actual counterparts in all platforms.
    
    This annotation is only applicable to `expect` annotation classes in multi-platform projects and marks that class as "optional".
    Optional expected class is allowed to have no corresponding actual class on the platform. Optional annotations can only be used
    to annotate something, not as types in signatures. If an optional annotation has no corresponding actual class on a platform,
    the annotation entries where it's used are simply erased when compiling code on that platform.
    
    Note: this annotation is experimental, see `ExperimentalMultiplatform` on how to opt-in for it.

## 声明与重载

### 1. Common

```kotlin
@Target(ANNOTATION_CLASS)
@Retention(AnnotationRetention.BINARY)
@ExperimentalMultiplatform
public annotation class OptionalExpectation
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotations/Multiplatform.kt#L37)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() { println(taggedValue()) }
```

```text title="输出"
common annotation, no actual required
```

```kotlin title="common.kt"
@file:OptIn(kotlin.ExperimentalMultiplatform::class)
@OptionalExpectation
expect annotation class OptionalTrace()
@OptionalTrace
fun taggedValue(): String = "common annotation, no actual required"
```

编译选项：`-Xmulti-platform` `-Xcommon-sources={common.kt}`

## 版本与来源

本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。
