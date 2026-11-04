# associateByTo

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

弹出并返回`destination`的带有关键值对的可变图,键由适用于给定阵列每个元素的`keySelector`函数提供,而值是元素本身。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

@sample 样本收集、阵列、变形、联合原始武器

??? note "查看英文原文"

    Populates and returns the `destination` mutable map with key-value pairs,
    where key is provided by the `keySelector` function applied to each element of the given array
    and value is the element itself.
    
    If any two elements would have the same key returned by `keySelector` the last one gets added to the map.
    
    @sample samples.collections.Arrays.Transformations.associateArrayOfPrimitivesByTo

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, K, M : MutableMap<in K, in T>> Array<out T>.associateByTo(destination: M, keySelector: (T) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10493)

### 2. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, in Byte>> ByteArray.associateByTo(destination: M, keySelector: (Byte) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10510)

### 3. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, in Short>> ShortArray.associateByTo(destination: M, keySelector: (Short) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10527)

### 4. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, in Int>> IntArray.associateByTo(destination: M, keySelector: (Int) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10544)

### 5. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, in Long>> LongArray.associateByTo(destination: M, keySelector: (Long) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10561)

### 6. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, in Float>> FloatArray.associateByTo(destination: M, keySelector: (Float) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10578)

### 7. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, in Double>> DoubleArray.associateByTo(destination: M, keySelector: (Double) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10595)

### 8. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, in Boolean>> BooleanArray.associateByTo(destination: M, keySelector: (Boolean) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10612)

### 9. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, in Char>> CharArray.associateByTo(destination: M, keySelector: (Char) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10629)

### 10. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, K, V, M : MutableMap<in K, in V>> Array<out T>.associateByTo(destination: M, keySelector: (T) -> K, valueTransform: (T) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10646)

弹出并返回`destination`的移动图,配有关键值对,键由`keySelector`函数提供,而`valueTransform`函数则对给定阵列的各个元素提供。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

@sample 样本收集. 阵列. 变形. 联合原始物的阵列 与变异法相连接

### 11. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> ByteArray.associateByTo(destination: M, keySelector: (Byte) -> K, valueTransform: (Byte) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10663)

弹出并返回`destination`的移动图,配有关键值对,键由`keySelector`函数提供,而`valueTransform`函数则对给定阵列的各个元素提供。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

@sample 样本收集. 阵列. 变形. 联合原始物的阵列 与变异法相连接

### 12. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> ShortArray.associateByTo(destination: M, keySelector: (Short) -> K, valueTransform: (Short) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10680)

弹出并返回`destination`的移动图,配有关键值对,键由`keySelector`函数提供,而`valueTransform`函数则对给定阵列的各个元素提供。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

@sample 样本收集. 阵列. 变形. 联合原始物的阵列 与变异法相连接

### 13. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> IntArray.associateByTo(destination: M, keySelector: (Int) -> K, valueTransform: (Int) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10697)

弹出并返回`destination`的移动图,配有关键值对,键由`keySelector`函数提供,而`valueTransform`函数则对给定阵列的各个元素提供。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

@sample 样本收集. 阵列. 变形. 联合原始物的阵列 与变异法相连接

### 14. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> LongArray.associateByTo(destination: M, keySelector: (Long) -> K, valueTransform: (Long) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10714)

弹出并返回`destination`的移动图,配有关键值对,键由`keySelector`函数提供,而`valueTransform`函数则对给定阵列的各个元素提供。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

@sample 样本收集. 阵列. 变形. 联合原始物的阵列 与变异法相连接

### 15. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> FloatArray.associateByTo(destination: M, keySelector: (Float) -> K, valueTransform: (Float) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10731)

弹出并返回`destination`的移动图,配有关键值对,键由`keySelector`函数提供,而`valueTransform`函数则对给定阵列的各个元素提供。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

@sample 样本收集. 阵列. 变形. 联合原始物的阵列 与变异法相连接

### 16. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> DoubleArray.associateByTo(destination: M, keySelector: (Double) -> K, valueTransform: (Double) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10748)

弹出并返回`destination`的移动图,配有关键值对,键由`keySelector`函数提供,而`valueTransform`函数则对给定阵列的各个元素提供。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

@sample 样本收集. 阵列. 变形. 联合原始物的阵列 与变异法相连接

### 17. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> BooleanArray.associateByTo(destination: M, keySelector: (Boolean) -> K, valueTransform: (Boolean) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10765)

弹出并返回`destination`的移动图,配有关键值对,键由`keySelector`函数提供,而`valueTransform`函数则对给定阵列的各个元素提供。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

@sample 样本收集. 阵列. 变形. 联合原始物的阵列 与变异法相连接

### 18. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> CharArray.associateByTo(destination: M, keySelector: (Char) -> K, valueTransform: (Char) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L10782)

弹出并返回`destination`的移动图,配有关键值对,键由`keySelector`函数提供,而`valueTransform`函数则对给定阵列的各个元素提供。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

@sample 样本收集. 阵列. 变形. 联合原始物的阵列 与变异法相连接

### 19. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, K, M : MutableMap<in K, in T>> Iterable<T>.associateByTo(destination: M, keySelector: (T) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1397)

弹出并返回`destination`的带有关键值对的可变图,键由适用于给定收藏和价值每个元素的`keySelector`函数提供,而元素本身是该元素。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

@sample 样本、采集、采集、变形、关联

### 20. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, K, V, M : MutableMap<in K, in V>> Iterable<T>.associateByTo(destination: M, keySelector: (T) -> K, valueTransform: (T) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1414)

弹出并返回`destination`的带有关键值对的可变图,其中键由`keySelector`函数提供,而`valueTransform`函数提供,而`valueTransform`函数则对特定收藏的元素适用。

如果任何两个元素在`keySelector`之前都返回同一键,最后的键就会被添加到地图上。

@sample 样本、采集、采集、变异、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、结合、

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    data class Person(val firstName: String, val lastName: String) {
        override fun toString(): String = "$firstName $lastName"
    }

    val scientists = listOf(Person("Grace", "Hopper"), Person("Jacob", "Bernoulli"), Person("Johann", "Bernoulli"))

    val byLastName = mutableMapOf<String, Person>()
    println(byLastName.isEmpty())

    scientists.associateByTo(byLastName) { it.lastName }

    println(byLastName.isNotEmpty())
    // Jacob Bernoulli does not occur in the map because only the last pair with the same key gets added
    println(byLastName)
}
```

```text title="输出"
true
true
{Hopper=Grace Hopper, Bernoulli=Johann Bernoulli}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L744)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    data class Person(val firstName: String, val lastName: String)

    val scientists = listOf(Person("Grace", "Hopper"), Person("Jacob", "Bernoulli"), Person("Johann", "Bernoulli"))

    val byLastName = mutableMapOf<String, String>()
    println(byLastName.isEmpty())

    scientists.associateByTo(byLastName, { it.lastName }, { it.firstName} )

    println(byLastName.isNotEmpty())
    // Jacob Bernoulli does not occur in the map because only the last pair with the same key gets added
    println(byLastName)
}
```

```text title="输出"
true
true
{Hopper=Grace, Bernoulli=Johann}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L762)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
