# elementAt

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回给定 `index` 的元素,如果 `index` 超出此数组的界限,则返回 `IndexOutOfBoundsException` 或 扔出 `IndexOutOfBoundsException`。

@sample 样本、采集的样本、采集的样本、元素、元素

??? note "查看英文原文"

    Returns an element at the given `index` or throws an `IndexOutOfBoundsException` if the `index` is out of bounds of this array.
    
    @sample samples.collections.Collections.Elements.elementAt

## 声明与重载

### 1. Common

```kotlin
public expect fun <T> Array<out T>.elementAt(index: Int): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L674)

### 2. Common

```kotlin
public expect fun ByteArray.elementAt(index: Int): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L681)

### 3. Common

```kotlin
public expect fun ShortArray.elementAt(index: Int): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L688)

### 4. Common

```kotlin
public expect fun IntArray.elementAt(index: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L695)

### 5. Common

```kotlin
public expect fun LongArray.elementAt(index: Int): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L702)

### 6. Common

```kotlin
public expect fun FloatArray.elementAt(index: Int): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L709)

### 7. Common

```kotlin
public expect fun DoubleArray.elementAt(index: Int): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L716)

### 8. Common

```kotlin
public expect fun BooleanArray.elementAt(index: Int): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L723)

### 9. Common

```kotlin
public expect fun CharArray.elementAt(index: Int): Char
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L730)

### 10. Common

```kotlin
public fun <T> Iterable<T>.elementAt(index: Int): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L81)

返回给定 `index` 的元素,如果 `index` 超出此收藏的范围,则返回 `IndexOutOfBoundsException` 或 扔出 `IndexOutOfBoundsException` 。

@sample 样本、采集的样本、采集的样本、元素、元素

### 11. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> List<T>.elementAt(index: Int): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L92)

返回给定 `index` 的元素,如果 `index` 超出该列表的界限,则返回`IndexOutOfBoundsException` 或扔出 `IndexOutOfBoundsException` 。

@sample 样本、采集的样本、采集的样本、元素、元素

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public expect fun UIntArray.elementAt(index: Int): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L323)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public expect fun ULongArray.elementAt(index: Int): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L332)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public expect fun UByteArray.elementAt(index: Int): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L341)

### 15. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public expect fun UShortArray.elementAt(index: Int): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L350)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val list = listOf(1, 2, 3)
    println(list.elementAt(0))
    println(list.elementAt(2))
    assertFailsWith<IndexOutOfBoundsException> { list.elementAt(3) }

    val emptyList = emptyList<Int>()
    assertFailsWith<IndexOutOfBoundsException> { emptyList.elementAt(0) }
}
```

```text title="输出"
1
3
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1302)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
