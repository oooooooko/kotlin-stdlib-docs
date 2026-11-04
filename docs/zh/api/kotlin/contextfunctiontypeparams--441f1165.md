# ContextFunctionTypeParams

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

说明式功能类型意味着上下文接收器的序号为 `count` ,因此,`@ContextFunctionTypeParams(2) @ExtensionFunctionType Function4<String, Int, Double, Byte, Unit>`是`context(String, Int) Double.(Byte) -> Unit`的正常代表。

仅与@ExtensionFunctionType相同,这种注解假定不会用于源代码,而喜欢如上例那样的明显功能型语法。

没有必要再增加选择加入的限制, 因为只有打开了`-Xcontext-receivers`号实验编译器旗帜的用户才能引用这个注解, 并且没有后向/前向的兼容性保证。

??? note "查看英文原文"

    Signifies that the annotated functional type has the prefix of size `count` for context receivers.
    Thus, `@ContextFunctionTypeParams(2) @ExtensionFunctionType Function4<String, Int, Double, Byte, Unit>` is a normalized representation of
    `context(String, Int) Double.(Byte) -> Unit`.
    
    Just the same as @ExtensionFunctionType, this annotation is not assumed to be used in source code, preferring the explicit function type
    syntax, like in the example above.
    
    There's no need in any additional opt-in limitations because this annotation might only be referenced by users
    who turned on an experimental `-Xcontext-receivers` compiler flag, for which there are no backward/forward compatibilities guarantees.

## 声明与重载

### 1. Common

```kotlin
@Target(TYPE)
@MustBeDocumented
@SinceKotlin("1.7")
public annotation class ContextFunctionTypeParams(val count: Int)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Annotations.kt#L102)

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
    val value = kotlin.ContextFunctionTypeParams(2)
    println(value)
}
```

```text title="输出"
@kotlin.ContextFunctionTypeParams(count=2)
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
