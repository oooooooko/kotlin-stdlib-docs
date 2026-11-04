# sum

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回序列中所有元素的和。

操作为 _flintinal_。

??? note "查看英文原文"

    Returns the sum of all elements in the sequence.
    
    The operation is _terminal_.

## 声明与重载

### 1. Common

```kotlin
@kotlin.jvm.JvmName("sumOfByte")
public fun Sequence<Byte>.sum(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3464)

### 2. Common

```kotlin
@kotlin.jvm.JvmName("sumOfShort")
public fun Sequence<Short>.sum(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3478)

### 3. Common

```kotlin
@kotlin.jvm.JvmName("sumOfInt")
public fun Sequence<Int>.sum(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3492)

### 4. Common

```kotlin
@kotlin.jvm.JvmName("sumOfLong")
public fun Sequence<Long>.sum(): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3506)

### 5. Common

```kotlin
@kotlin.jvm.JvmName("sumOfFloat")
public fun Sequence<Float>.sum(): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3520)

### 6. Common

```kotlin
@kotlin.jvm.JvmName("sumOfDouble")
public fun Sequence<Double>.sum(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L3534)

### 7. Common

```kotlin
@kotlin.jvm.JvmName("sumOfUInt")
@SinceKotlin("1.5")
public fun Sequence<UInt>.sum(): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_USequences.kt#L20)

### 8. Common

```kotlin
@kotlin.jvm.JvmName("sumOfULong")
@SinceKotlin("1.5")
public fun Sequence<ULong>.sum(): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_USequences.kt#L35)

### 9. Common

```kotlin
@kotlin.jvm.JvmName("sumOfUByte")
@SinceKotlin("1.5")
public fun Sequence<UByte>.sum(): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_USequences.kt#L50)

### 10. Common

```kotlin
@kotlin.jvm.JvmName("sumOfUShort")
@SinceKotlin("1.5")
public fun Sequence<UShort>.sum(): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_USequences.kt#L65)

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
    val result = source.`sum`()
    println(result)
}
```

```text title="输出"
6
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
