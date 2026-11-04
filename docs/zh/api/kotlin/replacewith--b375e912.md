# ReplaceWith

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

指定一个代码碎片,用于替换一个折旧函数、属性或类别。 IDE 等工具可以自动应用通过此注释指定的替换。

替换表达式。 它在使用的符号背景下被解释, 并可以引用包含类等的成员。 对于功能调用, 替换表达式可能包含折旧功能的参数名称, 替换时将替换为更新调用中所使用的实际参数 。 包含折旧函数或财产的文件中使用的导入无法访问; 如果替换表达式指的是任何这些进口, 则需要明确指定在 `imports` 参数中。 @property 导入时 。 需要导入的合格名称, 才能正确解决替换表达式中的引用 。

??? note "查看英文原文"

    Specifies a code fragment that can be used to replace a deprecated function, property or class. Tools such
    as IDEs can automatically apply the replacements specified through this annotation.
    
    @property expression The replacement expression. It is interpreted in the context
      of the symbol being used, and can reference members of enclosing classes etc.
      For function calls, the replacement expression may contain argument names of the deprecated function,
      which will be substituted with actual parameters used in the call being updated. The imports used in the file
      containing the deprecated function or property are NOT accessible; if the replacement expression refers
      on any of those imports, they need to be specified explicitly in the `imports` parameter.
    @property imports The qualified names that need to be imported in order for the references in the
      replacement expression to be resolved correctly.

## 声明与重载

### 1. Common

```kotlin
@Target()
@Retention(BINARY)
@MustBeDocumented
public annotation class ReplaceWith(val expression: String, vararg val imports: String)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Annotations.kt#L63)

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
    val value = kotlin.ReplaceWith("o", "o")
    println(value)
}
```

```text title="输出"
@kotlin.ReplaceWith(expression=o, imports=[o])
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
