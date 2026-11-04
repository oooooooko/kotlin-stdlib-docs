# DslMarker

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

适用于批注类X时,X指定X定义了一种 DSL 语言

一般规则: - 隐含接收器可* 属于DSL @X * 的DSL @X* 如果标上相应的DSL标记注注 - 同一DSL的两个隐含接收器无法在同一范围内进入----最接近的赢者----其他可用的接收器与往常一样得到解决,但如果由此而解决的电话与这样的接收器有约束力,则是一个编译错误

标记规则:如果暗含接收者的类型有标记,或 - 其类型的分类器有标记,或其任何超级舱/顶面,则其暗含接收者视为有 @Ann 的标记。

??? note "查看英文原文"

    When applied to annotation class X specifies that X defines a DSL language
    
    The general rule:
    - an implicit receiver may *belong to a DSL @X* if marked with a corresponding DSL marker annotation
    - two implicit receivers of the same DSL are not accessible in the same scope
    - the closest one wins
    - other available receivers are resolved as usual, but if the resulting resolved call binds to such a receiver, it's a compilation error
    
    Marking rules: an implicit receiver is considered marked with @Ann if
    - its type is marked, or
    - its type's classifier is marked
    - or any of its superclasses/superinterfaces

## 声明与重载

### 1. Common

```kotlin
@Target(ANNOTATION_CLASS)
@Retention(BINARY)
@MustBeDocumented
@SinceKotlin("1.1")
public annotation class DslMarker
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Annotations.kt#L155)

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
    val value = kotlin.DslMarker()
    println(value)
}
```

```text title="输出"
@kotlin.DslMarker()
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
