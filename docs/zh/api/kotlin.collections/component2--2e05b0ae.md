# component2

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

从数组返回 2 个 。

如果此阵列的大小小于2, 则投掷 `IndexOutOfBoundsException` , 但 Kotlin/ JS 中的行为未指明, 而在 Kotlin/ Wasm 中, 将升起一个[ 字符串( https://webassembly.github.io/spec/core/intro/overview.html#trap)) , 除非在连接可执行文件时指定了 `-Xwasm-enable-array-range-checks` 编译器的旗帜 。

??? note "查看英文原文"

    Returns 2nd *element* from the array.
    
    If the size of this array is less than 2, throws an `IndexOutOfBoundsException` except in Kotlin/JS
    where the behavior is unspecified, and in Kotlin/Wasm where
    a [trap](https://webassembly.github.io/spec/core/intro/overview.html#trap) will be raised instead,
    unless `-Xwasm-enable-array-range-checks` compiler flag was specified when linking an executable.

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun <T> Array<out T>.component2(): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L139)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun ByteArray.component2(): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L152)

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun ShortArray.component2(): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L165)

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun IntArray.component2(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L178)

### 5. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun LongArray.component2(): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L191)

### 6. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun FloatArray.component2(): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L204)

### 7. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun DoubleArray.component2(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L217)

### 8. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun BooleanArray.component2(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L230)

### 9. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun CharArray.component2(): Char
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L243)

### 10. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun <T> List<T>.component2(): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L32)

返回列表中的第二个*要素*。

如果此列表的大小小于 2, 则扔出 `IndexOutOfBoundsException` 。

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline operator fun UIntArray.component2(): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L83)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline operator fun ULongArray.component2(): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L98)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline operator fun UByteArray.component2(): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L113)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline operator fun UShortArray.component2(): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L128)

### 15. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun <K, V> Map.Entry<K, V>.component2(): V
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L314)

返回地图条目的值组成部分。

这种方法允许在使用地图时使用损坏声明,例如:```
for ((key, value) in map) {
    // do something with the key and the value
}
```

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
    val result = source.`component2`()
    println(result)
}
```

```text title="输出"
2
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
