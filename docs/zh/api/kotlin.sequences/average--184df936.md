# average

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回序列中元素的平均值。

操作为 _flintinal_。

??? note "查看英文原文"

    Returns an average value of elements in the sequence.
    
    The operation is _terminal_.

## 声明与重载

### 1. Common

```kotlin
@kotlin.jvm.JvmName("averageOfByte")
public fun Sequence<Byte>.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3368)

### 2. Common

```kotlin
@kotlin.jvm.JvmName("averageOfShort")
public fun Sequence<Short>.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3384)

### 3. Common

```kotlin
@kotlin.jvm.JvmName("averageOfInt")
public fun Sequence<Int>.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3400)

### 4. Common

```kotlin
@kotlin.jvm.JvmName("averageOfLong")
public fun Sequence<Long>.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3416)

### 5. Common

```kotlin
@kotlin.jvm.JvmName("averageOfFloat")
public fun Sequence<Float>.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3432)

### 6. Common

```kotlin
@kotlin.jvm.JvmName("averageOfDouble")
public fun Sequence<Double>.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3448)

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
import kotlin.sequences.*

fun main() {
    val source = sequenceOf(1, 2, 3)
    val result = source.`average`()
    println(result)
}
```

```text title="输出"
2.0
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
