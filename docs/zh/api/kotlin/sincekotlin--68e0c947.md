# SinceKotlin

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

指定声明出现位置的第一个 Kotlin 版本。使用声明并指定旧的 API 版本(通过 `-api-version` 命令行选项) 会导致错误 。

@property版本如下格式:`<major>.<minor>`或`<major>.<minor>.<patch>`,其中主要、次要和补丁
指非负整数,无前导零。

??? note "查看英文原文"

    Specifies the first version of Kotlin where a declaration has appeared.
    Using the declaration and specifying an older API version (via the `-api-version` command line option) will result in an error.
    
    @property version The version in the following formats: `<major>.<minor>` or `<major>.<minor>.<patch>`, where major, minor and patch
    are non-negative integer numbers without leading zeros.

## 声明与重载

### 1. Common

```kotlin
@Target(CLASS, PROPERTY, FIELD, CONSTRUCTOR, FUNCTION, PROPERTY_GETTER, PROPERTY_SETTER, TYPEALIAS)
@Retention(AnnotationRetention.BINARY)
@MustBeDocumented
public annotation class SinceKotlin(val version: String)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Annotations.kt#L143)

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
    val value = kotlin.SinceKotlin("o")
    println(value)
}
```

```text title="输出"
@kotlin.SinceKotlin(version=o)
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
