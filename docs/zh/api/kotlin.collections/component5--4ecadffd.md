# component5

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回数组中的 5 个 。

如果此阵列的大小小于5, 则投掷 `IndexOutOfBoundsException` , 但 Kotlin/ JS 中的行为未指明, 而在 Kotlin/ Wasm 中, 将升起一个[ 字符串( https://webassembly.github.io/spec/core/intro/overview.html#trap)) , 除非在连接可执行文件时指定了 `-Xwasm-enable-array-range-checks` 编译器的旗帜 。

??? note "查看英文原文"

    Returns 5th *element* from the array.
    
    If the size of this array is less than 5, throws an `IndexOutOfBoundsException` except in Kotlin/JS
    where the behavior is unspecified, and in Kotlin/Wasm where
    a [trap](https://webassembly.github.io/spec/core/intro/overview.html#trap) will be raised instead,
    unless `-Xwasm-enable-array-range-checks` compiler flag was specified when linking an executable.

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun <T> Array<out T>.component5(): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L490)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun ByteArray.component5(): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L503)

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun ShortArray.component5(): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L516)

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun IntArray.component5(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L529)

### 5. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun LongArray.component5(): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L542)

### 6. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun FloatArray.component5(): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L555)

### 7. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun DoubleArray.component5(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L568)

### 8. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun BooleanArray.component5(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L581)

### 9. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun CharArray.component5(): Char
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L594)

### 10. Common

```kotlin
@kotlin.internal.InlineOnly
public inline operator fun <T> List<T>.component5(): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L62)

返回列表中的第5项*要素*。

如果此列表的大小小于5, 则扔出 `IndexOutOfBoundsException` 。

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline operator fun UIntArray.component5(): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L263)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline operator fun ULongArray.component5(): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L278)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline operator fun UByteArray.component5(): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L293)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline operator fun UShortArray.component5(): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L308)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import java.math.BigInteger
import java.math.BigDecimal
import kotlin.test.*
import java.math.MathContext
import java.math.RoundingMode



fun main() {

        val (d1, d2, d3, d4, d5) = (1..5).map { BigDecimal(it.toString()) }
        val d7 = BigDecimal("7")

        println(d2 / d3)
        println(d3 / d2)
        println(d5 / d2)
        println(d7 / d2)
        println(d7 / d5)
    
}
```

```text title="输出"
1
2
2
4
1
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/jvm/test/numbers/BigNumbersTest.kt#L128)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
