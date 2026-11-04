# Deprecated

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

标记附加说明的声明为已折旧声明。

推荐不使用折旧的API元素, 通常因为它正在逐步取消或者有更好的替代物存在。

为了帮助逐步消除已折旧的API, 可以使用 `level` 的财产。 通常, 逐渐淘汰会经过“ 警告 ” 、 “ error” 、 “ 隐藏” 或“ 移动” 阶段: 首先和默认情况下, `DeprecationLevel.WARNING` 被用来通知API 消费者, 但不中断它们的编译或运行时间使用 。 然后, 一段时间后, 折旧水平会提高到 `DeprecationLevel.ERROR` , 这样就无法使用已折旧的 API 编译新的 Kotlin 代码 。 最后, API 要么完全删除, 要么隐藏( `DeprecationLevel.HIDDEN` ) , 其使用看起来就像未解决的参考 。 而 API 仍然保存在编成的代码中, 保持与先前编成的代码的二进式兼容性 。

@property 信息解释折旧并建议使用替代的 API。 @property 替换。 如果存在的话,请指定一个代码碎片,作为已折旧的 API 使用量的替换。 @property 级指定了折旧元素的使用在代码中如何报告。可能值请参见 `DeprecationLevel` enum。

??? note "查看英文原文"

    Marks the annotated declaration as deprecated.
    
    A deprecated API element is not recommended to use, typically because it's being phased out or a better alternative exists.
    
    To help removing deprecated API gradually, the property `level` could be used.
    Usually a gradual phase-out goes through the "warning", then "error", then "hidden" or "removed" stages:
    - First and by default, `DeprecationLevel.WARNING` is used to notify API consumers, but not to break their compilation or runtime usages.
    - Then, some time later the deprecation level is raised to `DeprecationLevel.ERROR`, so that no new Kotlin code can be compiled
      using the deprecated API.
    - Finally, the API is either removed entirely, or hidden (`DeprecationLevel.HIDDEN`) from code,
    so its usages look like unresolved references, while the API remains in the compiled code
    preserving binary compatibility with previously compiled code.
    
    @property message The message explaining the deprecation and recommending an alternative API to use.
    @property replaceWith If present, specifies a code fragment which should be used as a replacement for
     the deprecated API usage.
    @property level Specifies how the deprecated element usages are reported in code.
     See the `DeprecationLevel` enum for the possible values.

## 声明与重载

### 1. Common

```kotlin
@Target(CLASS, FUNCTION, PROPERTY, ANNOTATION_CLASS, CONSTRUCTOR, PROPERTY_SETTER, PROPERTY_GETTER, TYPEALIAS)
@MustBeDocumented
public annotation class Deprecated(
    val message: String,
    val replaceWith: ReplaceWith = ReplaceWith(""),
    val level: DeprecationLevel = DeprecationLevel.WARNING
)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Annotations.kt#L14)

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
    val value = kotlin.Deprecated("o")
    println(value)
}
```

```text title="输出"
@kotlin.Deprecated(message=o, replaceWith=@kotlin.ReplaceWith(expression=, imports=[]), level=WARNING)
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
