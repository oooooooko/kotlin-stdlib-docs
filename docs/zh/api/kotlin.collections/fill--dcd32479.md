# fill

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

以指定的 `element` 值填充此数组或其子组合。

从Index 开始填充范围( 包括) 开始, 默认为 0。 @param 到 Index 结束( 排他) 填充范围, 默认为此数组的大小 。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

??? note "查看英文原文"

    Fills this array or its subrange with the specified `element` value.
    
    @param fromIndex the start of the range (inclusive) to fill, 0 by default.
    @param toIndex the end of the range (exclusive) to fill, size of this array by default.
    
    @throws IndexOutOfBoundsException if `fromIndex` is less than zero or `toIndex` is greater than the size of this array.
    @throws IllegalArgumentException if `fromIndex` is greater than `toIndex`.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
public expect fun <T> Array<T>.fill(element: T, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9180)

### 2. Common

```kotlin
@SinceKotlin("1.3")
public expect fun ByteArray.fill(element: Byte, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9192)

### 3. Common

```kotlin
@SinceKotlin("1.3")
public expect fun ShortArray.fill(element: Short, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9204)

### 4. Common

```kotlin
@SinceKotlin("1.3")
public expect fun IntArray.fill(element: Int, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9216)

### 5. Common

```kotlin
@SinceKotlin("1.3")
public expect fun LongArray.fill(element: Long, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9228)

### 6. Common

```kotlin
@SinceKotlin("1.3")
public expect fun FloatArray.fill(element: Float, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9240)

### 7. Common

```kotlin
@SinceKotlin("1.3")
public expect fun DoubleArray.fill(element: Double, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9252)

### 8. Common

```kotlin
@SinceKotlin("1.3")
public expect fun BooleanArray.fill(element: Boolean, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9264)

### 9. Common

```kotlin
@SinceKotlin("1.3")
public expect fun CharArray.fill(element: Char, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9276)

### 10. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.fill(element: UInt, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4423)

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.fill(element: ULong, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4438)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.fill(element: UByte, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4453)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.fill(element: UShort, fromIndex: Int = 0, toIndex: Int = size): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4468)

### 14. Common

```kotlin
@SinceKotlin("1.2")
public expect fun <T> MutableList<T>.fill(value: T): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/CollectionsH.kt#L28)

将所提供`value`填充的清单填充。

清单中的每个元素都由`value`替换。

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
import kotlin.collections.*

fun main() {
    val source = arrayOf(1, 2, 3)
    val result = source.`fill`(1)
    println(result)
}
```

```text title="输出"
kotlin.Unit
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
