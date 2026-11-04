# elementAtOrNull

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果 `index` 超出该数组的界限,则返回给定 `index` 或 `null` 的元素。

@sample 样本、采集的样本、采集的样本、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、、、元素、元素、元素、元素、元素、元素、元素、、、、、、、元素、、、、、、、、、、或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或

??? note "查看英文原文"

    Returns an element at the given `index` or `null` if the `index` is out of bounds of this array.
    
    @sample samples.collections.Collections.Elements.elementAtOrNull

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Array<out T>.elementAtOrNull(index: Int): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L854)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun ByteArray.elementAtOrNull(index: Int): Byte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L864)

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun ShortArray.elementAtOrNull(index: Int): Short?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L874)

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun IntArray.elementAtOrNull(index: Int): Int?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L884)

### 5. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun LongArray.elementAtOrNull(index: Int): Long?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L894)

### 6. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun FloatArray.elementAtOrNull(index: Int): Float?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L904)

### 7. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun DoubleArray.elementAtOrNull(index: Int): Double?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L914)

### 8. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun BooleanArray.elementAtOrNull(index: Int): Boolean?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L924)

### 9. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharArray.elementAtOrNull(index: Int): Char?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L934)

### 10. Common

```kotlin
public fun <T> Iterable<T>.elementAtOrNull(index: Int): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L138)

如果 `index` 超出该收藏的界限,则返回给定的 `index` 或 `null` 的元素。

@sample 样本、采集的样本、采集的样本、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、、、元素、元素、元素、元素、元素、元素、元素、、、、、、、元素、、、、、、、、、、或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或

### 11. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> List<T>.elementAtOrNull(index: Int): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L158)

如果 `index` 超出该列表的界限,则返回给定的 `index` 或 `null` 的元素。

@sample 样本、采集的样本、采集的样本、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、元素、、、元素、元素、元素、元素、元素、元素、元素、、、、、、、元素、、、、、、、、、、或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.elementAtOrNull(index: Int): UInt?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L419)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.elementAtOrNull(index: Int): ULong?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L431)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.elementAtOrNull(index: Int): UByte?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L443)

### 15. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.elementAtOrNull(index: Int): UShort?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L455)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = listOf(1, 2, 3)
    println(list.elementAtOrNull(0))
    println(list.elementAtOrNull(2))
    println(list.elementAtOrNull(3))

    val emptyList = emptyList<Int>()
    println(emptyList.elementAtOrNull(0))
}
```

```text title="输出"
1
3
null
null
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1313)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
