# withIndex

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个懒惰的`Iterable`,该返回将原始数组的每个元素包成`IndexedValue`,包含元素的索引和元素本身。

??? note "查看英文原文"

    Returns a lazy `Iterable` that wraps each element of the original array
    into an `IndexedValue` containing the index of that element and the element itself.

## 声明与重载

### 1. Common

```kotlin
public fun <T> Array<out T>.withIndex(): Iterable<IndexedValue<T>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13290)

### 2. Common

```kotlin
public fun ByteArray.withIndex(): Iterable<IndexedValue<Byte>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13298)

### 3. Common

```kotlin
public fun ShortArray.withIndex(): Iterable<IndexedValue<Short>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13306)

### 4. Common

```kotlin
public fun IntArray.withIndex(): Iterable<IndexedValue<Int>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13314)

### 5. Common

```kotlin
public fun LongArray.withIndex(): Iterable<IndexedValue<Long>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13322)

### 6. Common

```kotlin
public fun FloatArray.withIndex(): Iterable<IndexedValue<Float>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13330)

### 7. Common

```kotlin
public fun DoubleArray.withIndex(): Iterable<IndexedValue<Double>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13338)

### 8. Common

```kotlin
public fun BooleanArray.withIndex(): Iterable<IndexedValue<Boolean>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13346)

### 9. Common

```kotlin
public fun CharArray.withIndex(): Iterable<IndexedValue<Char>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13354)

### 10. Common

```kotlin
public fun <T> Iterable<T>.withIndex(): Iterable<IndexedValue<T>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1825)

返回一个懒惰的`Iterable`,该元素将原始收藏的每个元素包成`IndexedValue`,包含元素的索引和元素本身。

### 11. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.withIndex(): Iterable<IndexedValue<UInt>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5935)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.withIndex(): Iterable<IndexedValue<ULong>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5945)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.withIndex(): Iterable<IndexedValue<UByte>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5955)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.withIndex(): Iterable<IndexedValue<UShort>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5965)

### 15. Common

```kotlin
public fun <T> Iterator<T>.withIndex(): Iterator<IndexedValue<T>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Iterators.kt#L19)

返回 `Iterator`,将原迭代器产生的每个元素包成`IndexedValue`,其中含有该元素的索引和元素本身。

@sample 样本、采集资料、与Indexiter的试样

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    val iterator = ('a'..'c').iterator()

    for ((index, value) in iterator.withIndex()) {
        println("The element at $index is $value")
    }
}
```

```text title="输出"
The element at 0 is a
The element at 1 is b
The element at 2 is c
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/iterators.kt#L55)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
