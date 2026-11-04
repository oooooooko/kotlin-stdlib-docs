# RegexOption

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

提供用于设置正则表达式选项的点点数值 。

请注意, enum 在不同平台上有不同的一套可能的选项, 并且可以延期。 避免在此enum 值上出现 `when` 的排他性匹配。 详情请参见 $`RegexOption` 的文档 。

??? note "查看英文原文"

    Provides enumeration values to use to set regular expression options.
    
    Note that the enum has different set of possible options on different platforms and
    can be extended later. Avoid exclusive `when` matches on this enum values.
    See the docs of `RegexOption` for the specific platform for details.

## 声明与重载

### 1. Common

```kotlin
public expect enum class RegexOption
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L211)

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
import kotlin.text.*

fun main() {
    val value = kotlin.text.RegexOption.CANON_EQ
    println(value)
}
```

```text title="输出"
CANON_EQ
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
