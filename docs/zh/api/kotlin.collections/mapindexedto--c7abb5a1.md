# mapIndexedTo

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将给定的 `transform` 函数应用到每个元素及其在原始数组中的索引,并将结果附加到给定的 `destination`. @param `transform` 函数,该函数采用元素的索引和元素本身,并返回对元素应用的变换结果。

??? note "查看英文原文"

    Applies the given `transform` function to each element and its index in the original array
    and appends the results to the given `destination`.
    @param `transform` function that takes the index of an element and the element itself
    and returns the result of the transform applied to the element.

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, R, C : MutableCollection<in R>> Array<out T>.mapIndexedTo(destination: C, transform: (index: Int, T) -> R): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13045)

### 2. Common

```kotlin
@IgnorableReturnValue
public inline fun <R, C : MutableCollection<in R>> ByteArray.mapIndexedTo(destination: C, transform: (index: Int, Byte) -> R): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13059)

### 3. Common

```kotlin
@IgnorableReturnValue
public inline fun <R, C : MutableCollection<in R>> ShortArray.mapIndexedTo(destination: C, transform: (index: Int, Short) -> R): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13073)

### 4. Common

```kotlin
@IgnorableReturnValue
public inline fun <R, C : MutableCollection<in R>> IntArray.mapIndexedTo(destination: C, transform: (index: Int, Int) -> R): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13087)

### 5. Common

```kotlin
@IgnorableReturnValue
public inline fun <R, C : MutableCollection<in R>> LongArray.mapIndexedTo(destination: C, transform: (index: Int, Long) -> R): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13101)

### 6. Common

```kotlin
@IgnorableReturnValue
public inline fun <R, C : MutableCollection<in R>> FloatArray.mapIndexedTo(destination: C, transform: (index: Int, Float) -> R): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13115)

### 7. Common

```kotlin
@IgnorableReturnValue
public inline fun <R, C : MutableCollection<in R>> DoubleArray.mapIndexedTo(destination: C, transform: (index: Int, Double) -> R): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13129)

### 8. Common

```kotlin
@IgnorableReturnValue
public inline fun <R, C : MutableCollection<in R>> BooleanArray.mapIndexedTo(destination: C, transform: (index: Int, Boolean) -> R): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13143)

### 9. Common

```kotlin
@IgnorableReturnValue
public inline fun <R, C : MutableCollection<in R>> CharArray.mapIndexedTo(destination: C, transform: (index: Int, Char) -> R): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L13157)

### 10. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, R, C : MutableCollection<in R>> Iterable<T>.mapIndexedTo(destination: C, transform: (index: Int, T) -> R): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1780)

将给定的 `transform` 函数应用到每个元素及其在原始收藏中的索引中,并将结果附加到给定的 `destination`. @param `transform` 函数,该函数采用元素的索引和元素本身,并返回对元素应用的变换的结果。

### 11. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, C : MutableCollection<in R>> UIntArray.mapIndexedTo(destination: C, transform: (index: Int, UInt) -> R): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5811)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, C : MutableCollection<in R>> ULongArray.mapIndexedTo(destination: C, transform: (index: Int, ULong) -> R): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5828)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, C : MutableCollection<in R>> UByteArray.mapIndexedTo(destination: C, transform: (index: Int, UByte) -> R): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5845)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, C : MutableCollection<in R>> UShortArray.mapIndexedTo(destination: C, transform: (index: Int, UShort) -> R): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5862)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() {
    println(listOf(1, 2).flatMapTo(mutableListOf<Int>()) { listOf(it, -it) })
    println(listOf(1, 2).flatMapIndexedTo(mutableListOf<Int>()) { index, value -> listOf(index, value) })
    println(listOf(1, 2).mapTo(mutableListOf<String>()) { "v$it" })
    println(listOf(1, 2).mapIndexedTo(mutableListOf<String>()) { index, value -> "$index:$value" })
    println(listOf(1, 2).mapNotNullTo(mutableListOf<Int>()) { it.takeIf { n -> n > 1 } })
    println(listOf(1, 2).mapIndexedNotNullTo(mutableListOf<Int>()) { index, value -> value.takeIf { index > 0 } })
    val values = linkedMapOf("a" to 1, "b" to 2)
    println(values.mapKeysTo(linkedMapOf<String, Int>()) { it.key.uppercase() })
    println(values.mapValues { it.value * 10 })
    println(values.mapValuesTo(linkedMapOf<String, Int>()) { it.value * 10 })
}
```

```text title="输出"
[1, -1, 2, -2]
[0, 1, 1, 2]
[v1, v2]
[0:1, 1:2]
[2]
[2]
{A=1, B=2}
{a=10, b=20}
{a=10, b=20}
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
