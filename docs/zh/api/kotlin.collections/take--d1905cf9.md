# take

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回包含第一批`n`元素的列表 。

@throws 非法设备,如果`n`为负数,则不在此列。

@sample 样本 采集 采集 变形 采集

??? note "查看英文原文"

    Returns a list containing first `n` elements.
    
    @throws IllegalArgumentException if `n` is negative.
    
    @sample samples.collections.Collections.Transformations.take

## 声明与重载

### 1. Common

```kotlin
public fun <T> Array<out T>.take(n: Int): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4935)

### 2. Common

```kotlin
public fun ByteArray.take(n: Int): List<Byte>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4950)

### 3. Common

```kotlin
public fun ShortArray.take(n: Int): List<Short>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4972)

### 4. Common

```kotlin
public fun IntArray.take(n: Int): List<Int>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4994)

### 5. Common

```kotlin
public fun LongArray.take(n: Int): List<Long>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5016)

### 6. Common

```kotlin
public fun FloatArray.take(n: Int): List<Float>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5038)

### 7. Common

```kotlin
public fun DoubleArray.take(n: Int): List<Double>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5060)

### 8. Common

```kotlin
public fun BooleanArray.take(n: Int): List<Boolean>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5082)

### 9. Common

```kotlin
public fun CharArray.take(n: Int): List<Char>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L5104)

### 10. Common

```kotlin
public fun <T> Iterable<T>.take(n: Int): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L898)

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.take(n: Int): List<UInt>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2435)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.take(n: Int): List<ULong>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2459)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.take(n: Int): List<UByte>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2483)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.take(n: Int): List<UShort>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2507)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val chars = ('a'..'z').toList()
    println(chars.take(3))
    println(chars.takeWhile { it < 'f' })
    println(chars.takeLast(2))
    println(chars.takeLastWhile { it > 'w' })
}
```

```text title="输出"
[a, b, c]
[a, b, c, d, e]
[y, z]
[x, y, z]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L911)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
