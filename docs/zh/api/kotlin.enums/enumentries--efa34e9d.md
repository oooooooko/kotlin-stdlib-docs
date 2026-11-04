# EnumEntries

`kotlin.enums` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

专门实施 `List` 接口,其中包含 `E` . `EnumEntries`号特定单位的所有昆虫条目。 `EnumEntries`包含所有昆虫条目,其顺序以源代码中申报的顺序,与相应的 `Enum.ordinal` 值一致。

可从 `EnumClass.entries` 财产或`enumEntries`功能获得这种接口的实例。

执行说明 执行说明 基本业务,如`get`、`contains`和`indexOf`, 执行时间不变,可能比正常的`ArrayList<E>`。

??? note "查看英文原文"

    A specialized immutable implementation of `List` interface that
    contains all enum entries of the specified enum type `E`.
    `EnumEntries` contains all enum entries in the order they are declared in the source code,
    consistently with the corresponding `Enum.ordinal` values.
    
    An instance of this interface can be obtained from `EnumClass.entries` property or with `enumEntries` function.
    
    #### Implementation note
    All basic operations, such as `get`, `contains` and `indexOf`, are executed in constant time and are likely to be
    faster than regular `ArrayList<E>` counterparts.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public sealed interface EnumEntries<E : Enum<E>> : List<E>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/enums/EnumEntries.kt#L14)

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
import kotlin.enums.*

enum class Demo { FIRST, SECOND }

fun main() {
    val value = Demo.entries
    println(value)
}
```

```text title="输出"
[FIRST, SECOND]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
