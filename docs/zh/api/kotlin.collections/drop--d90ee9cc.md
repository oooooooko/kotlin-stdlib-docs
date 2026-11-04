# drop

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回包含除第一个`n`元素以外的所有元素的列表 。

@throws 非法设备,如果`n`为负数,则不在此列。

@sample 样本 采集 采集 变形 投放

??? note "查看英文原文"

    Returns a list containing all elements except first `n` elements.
    
    @throws IllegalArgumentException if `n` is negative.
    
    @sample samples.collections.Collections.Transformations.drop

## 声明与重载

### 1. Common

```kotlin
public fun <T> Array<out T>.drop(n: Int): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3428)

### 2. Common

```kotlin
public fun ByteArray.drop(n: Int): List<Byte>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3440)

### 3. Common

```kotlin
public fun ShortArray.drop(n: Int): List<Short>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3452)

### 4. Common

```kotlin
public fun IntArray.drop(n: Int): List<Int>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3464)

### 5. Common

```kotlin
public fun LongArray.drop(n: Int): List<Long>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3476)

### 6. Common

```kotlin
public fun FloatArray.drop(n: Int): List<Float>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3488)

### 7. Common

```kotlin
public fun DoubleArray.drop(n: Int): List<Double>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3500)

### 8. Common

```kotlin
public fun BooleanArray.drop(n: Int): List<Boolean>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3512)

### 9. Common

```kotlin
public fun CharArray.drop(n: Int): List<Char>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L3524)

### 10. Common

```kotlin
public fun <T> Iterable<T>.drop(n: Int): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L685)

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.drop(n: Int): List<UInt>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1663)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.drop(n: Int): List<ULong>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1677)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.drop(n: Int): List<UByte>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1691)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.drop(n: Int): List<UShort>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L1705)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val chars = ('a'..'z').toList()
    println(chars.drop(23))
    println(chars.dropLast(23))
    println(chars.dropWhile { it < 'x' })
    println(chars.dropLastWhile { it > 'c' })
}
```

```text title="输出"
[x, y, z]
[a, b, c]
[x, y, z]
[a, b, c]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L920)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
