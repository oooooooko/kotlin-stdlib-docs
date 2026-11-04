# concatToString

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将`CharArray`中的字符连接到字符串中。

??? note "查看英文原文"

    Concatenates characters in this `CharArray` into a String.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public expect fun CharArray.concatToString(): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L265)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public expect fun CharArray.concatToString(startIndex: Int = 0, endIndex: Int = this.size): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L271)

将`CharArray`或其子项中的字符串连接到字符串中。

@param 开始 Index 字符子序列的起始( 包括) 。 0 默认为 。 @param 结尾为 Index 字符子序列的结尾( 排他) , 此数组的大小默认为 。

@throws 指数外溢值,如果`startIndex`小于0或`endIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`startIndex` 大于`endIndex`,则不在此列。

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
    val source = charArrayOf('a', 'b', 'c')
    val result = source.`concatToString`()
    println(result)
}
```

```text title="输出"
abc
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
