# getOrElse

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回给定 `index` 的元素,如果 `index` 超出此数组的界限,则返回调用 `defaultValue` 函数的结果。

@sample 样本,采集资料,阵列, 资产, 植物, 有机植物

??? note "查看英文原文"

    Returns an element at the given `index` or the result of calling the `defaultValue` function if the `index` is out of bounds of this array.
    
    @sample samples.collections.Arrays.Usage.getOrElse

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Array<out T>.getOrElse(index: Int, defaultValue: (Int) -> T): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1469)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun ByteArray.getOrElse(index: Int, defaultValue: (Int) -> Byte): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1482)

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun ShortArray.getOrElse(index: Int, defaultValue: (Int) -> Short): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1495)

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun IntArray.getOrElse(index: Int, defaultValue: (Int) -> Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1508)

### 5. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun LongArray.getOrElse(index: Int, defaultValue: (Int) -> Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1521)

### 6. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun FloatArray.getOrElse(index: Int, defaultValue: (Int) -> Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1534)

### 7. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun DoubleArray.getOrElse(index: Int, defaultValue: (Int) -> Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1547)

### 8. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun BooleanArray.getOrElse(index: Int, defaultValue: (Int) -> Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1560)

### 9. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharArray.getOrElse(index: Int, defaultValue: (Int) -> Char): Char
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L1573)

### 10. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> List<T>.getOrElse(index: Int, defaultValue: (Int) -> T): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L300)

返回给定 `index` 的元素,如果 `index` 超出此列表的界限,则返回调用 `defaultValue` 函数的结果。

@sample 样本,采集的样本, 收集的样本, 元素, 元素, 开发的 Orelse

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.getOrElse(index: Int, defaultValue: (Int) -> UInt): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L739)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.getOrElse(index: Int, defaultValue: (Int) -> ULong): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L754)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.getOrElse(index: Int, defaultValue: (Int) -> UByte): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L769)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.getOrElse(index: Int, defaultValue: (Int) -> UShort): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L784)

### 15. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <K, V> Map<K, V>.getOrElse(key: K, defaultValue: () -> V): V
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L360)

如果给定 `key` 值存在,则返回该值的值,如果该值不是`null`,则返回该值。否则返回 `defaultValue` 函数的结果。

注意: 如果地图预计包含 `null` 值, 则不建议使用此函数。 使用 `getOrElseIfNull` 或 `getOrElseIfMissing` 来表达在键被映射为 `null` 值时返回的意向 。

@sample 样本 采集 地图 地图 地图 草图 草图

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = listOf(1, 2, 3)
    println(list.getOrElse(0) { 42 })
    println(list.getOrElse(2) { 42 })
    println(list.getOrElse(3) { 42 })
    println(list.getOrElse(-1) { 42 })

    val emptyList = emptyList<Int>()
    println(emptyList.getOrElse(0) { "no int" })
}
```

```text title="输出"
1
3
42
42
no int
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1345)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
