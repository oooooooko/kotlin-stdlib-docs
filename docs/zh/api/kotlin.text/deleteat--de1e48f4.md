# deleteAt

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

从此字符串构建器中删除指定的 `index` 字符,并返回此实例。

如果在指定的 `index` 时的`Char`是补充代码点的一部分,该方法不会删除整个补充字符。

@param指数 `Char` 指数要删除。

@throws 指数外在值 例外,如果 `index` 不受这个字符串构建器的制约的话。

??? note "查看英文原文"

    Removes the character at the specified `index` from this string builder and returns this instance.
    
    If the `Char` at the specified `index` is part of a supplementary code point, this method does not remove the entire supplementary character.
    
    @param index the index of `Char` to remove.
    
    @throws IndexOutOfBoundsException if `index` is out of bounds of this string builder.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue public expect fun StringBuilder.deleteAt(index: Int): StringBuilder
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringBuilder.kt#L395)

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
    val source = StringBuilder("kotlin")
    val result = source.`deleteAt`(0)
    println(result)
}
```

```text title="输出"
otlin
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
