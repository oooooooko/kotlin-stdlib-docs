# associateWithTo

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

弹出并返回`destination`变色图,其中含有给定数组每个元素的键值对,键是元素本身,值由适用于该键的`valueSelector`函数提供。

如果任何两个元素相等, 最后一个元素会覆盖地图中的前一个值 。

@sample 样本、采集、采集、变形、关联

??? note "查看英文原文"

    Populates and returns the `destination` mutable map with key-value pairs for each element of the given array,
    where key is the element itself and value is provided by the `valueSelector` function applied to that key.
    
    If any two elements are equal, the last one overwrites the former value in the map.
    
    @sample samples.collections.Collections.Transformations.associateWithTo

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> Array<out K>.associateWithTo(destination: M, valueSelector: (K) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11095)

### 2. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in Byte, in V>> ByteArray.associateWithTo(destination: M, valueSelector: (Byte) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11112)

### 3. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in Short, in V>> ShortArray.associateWithTo(destination: M, valueSelector: (Short) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11130)

### 4. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in Int, in V>> IntArray.associateWithTo(destination: M, valueSelector: (Int) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11148)

### 5. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in Long, in V>> LongArray.associateWithTo(destination: M, valueSelector: (Long) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11166)

### 6. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in Float, in V>> FloatArray.associateWithTo(destination: M, valueSelector: (Float) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11184)

### 7. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in Double, in V>> DoubleArray.associateWithTo(destination: M, valueSelector: (Double) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11202)

### 8. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in Boolean, in V>> BooleanArray.associateWithTo(destination: M, valueSelector: (Boolean) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11220)

### 9. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in Char, in V>> CharArray.associateWithTo(destination: M, valueSelector: (Char) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11238)

### 10. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> Iterable<K>.associateWithTo(destination: M, valueSelector: (K) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1463)

弹出并返回`destination`变色图,其中含有对特定收藏每个元素的键值,键是元素本身,值由适用于该键的`valueSelector`函数提供。

如果任何两个元素相等, 最后一个元素会覆盖地图中的前一个值 。

@sample 样本、采集、采集、变形、关联

### 11. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in UInt, in V>> UIntArray.associateWithTo(destination: M, valueSelector: (UInt) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5091)

### 12. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in ULong, in V>> ULongArray.associateWithTo(destination: M, valueSelector: (ULong) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5110)

### 13. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in UByte, in V>> UByteArray.associateWithTo(destination: M, valueSelector: (UByte) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5129)

### 14. Common

```kotlin
@SinceKotlin("1.4")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <V, M : MutableMap<in UShort, in V>> UShortArray.associateWithTo(destination: M, valueSelector: (UShort) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5148)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    data class Person(val firstName: String, val lastName: String) {
        override fun toString(): String = "$firstName $lastName"
    }

    val scientists = listOf(Person("Grace", "Hopper"), Person("Jacob", "Bernoulli"), Person("Jacob", "Bernoulli"))
    val withLengthOfNames = mutableMapOf<Person, Int>()
    println(withLengthOfNames.isEmpty())

    scientists.associateWithTo(withLengthOfNames) { it.firstName.length + it.lastName.length }

    println(withLengthOfNames.isNotEmpty())
    // Jacob Bernoulli only occurs once in the map because only the last pair with the same key gets added
    println(withLengthOfNames)
}
```

```text title="输出"
true
true
{Grace Hopper=11, Jacob Bernoulli=14}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L802)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
