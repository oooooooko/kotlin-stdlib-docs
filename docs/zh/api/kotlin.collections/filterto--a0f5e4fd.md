# filterTo

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将所有匹配给定 `predicate` 的元素附加到给定的`destination`。

@sample 样本 采集 采集 采集 过滤 过滤

??? note "查看英文原文"

    Appends all elements matching the given `predicate` to the given `destination`.
    
    @sample samples.collections.Collections.Filtering.filterTo

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, C : MutableCollection<in T>> Array<out T>.filterTo(destination: C, predicate: (T) -> Boolean): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4467)

### 2. Common

```kotlin
@IgnorableReturnValue
public inline fun <C : MutableCollection<in Byte>> ByteArray.filterTo(destination: C, predicate: (Byte) -> Boolean): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4478)

### 3. Common

```kotlin
@IgnorableReturnValue
public inline fun <C : MutableCollection<in Short>> ShortArray.filterTo(destination: C, predicate: (Short) -> Boolean): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4489)

### 4. Common

```kotlin
@IgnorableReturnValue
public inline fun <C : MutableCollection<in Int>> IntArray.filterTo(destination: C, predicate: (Int) -> Boolean): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4500)

### 5. Common

```kotlin
@IgnorableReturnValue
public inline fun <C : MutableCollection<in Long>> LongArray.filterTo(destination: C, predicate: (Long) -> Boolean): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4511)

### 6. Common

```kotlin
@IgnorableReturnValue
public inline fun <C : MutableCollection<in Float>> FloatArray.filterTo(destination: C, predicate: (Float) -> Boolean): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4522)

### 7. Common

```kotlin
@IgnorableReturnValue
public inline fun <C : MutableCollection<in Double>> DoubleArray.filterTo(destination: C, predicate: (Double) -> Boolean): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4533)

### 8. Common

```kotlin
@IgnorableReturnValue
public inline fun <C : MutableCollection<in Boolean>> BooleanArray.filterTo(destination: C, predicate: (Boolean) -> Boolean): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4544)

### 9. Common

```kotlin
@IgnorableReturnValue
public inline fun <C : MutableCollection<in Char>> CharArray.filterTo(destination: C, predicate: (Char) -> Boolean): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4555)

### 10. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, C : MutableCollection<in T>> Iterable<T>.filterTo(destination: C, predicate: (T) -> Boolean): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L866)

### 11. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <C : MutableCollection<in UInt>> UIntArray.filterTo(destination: C, predicate: (UInt) -> Boolean): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2207)

### 12. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <C : MutableCollection<in ULong>> ULongArray.filterTo(destination: C, predicate: (ULong) -> Boolean): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2221)

### 13. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <C : MutableCollection<in UByte>> UByteArray.filterTo(destination: C, predicate: (UByte) -> Boolean): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2235)

### 14. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <C : MutableCollection<in UShort>> UShortArray.filterTo(destination: C, predicate: (UShort) -> Boolean): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2249)

### 15. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> Map<out K, V>.filterTo(destination: M, predicate: (Map.Entry<K, V>) -> Boolean): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L661)

将所有匹配给定的 `predicate` 的条目添加到可变图中, 以 `destination` 参数给定的可变图中。

目的地地图@return
@sample样本, 采集, 模型, 燃烧, 过滤器 To

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val numbers: List<Int> = listOf(1, 2, 3, 4, 5, 6, 7)
    val evenNumbers = mutableListOf<Int>()
    val notMultiplesOf3 = mutableListOf<Int>()

    println(evenNumbers)

    numbers.filterTo(evenNumbers) { it % 2 == 0 }
    numbers.filterNotTo(notMultiplesOf3) { number -> number % 3 == 0 }

    println(evenNumbers)
    println(notMultiplesOf3)
}
```

```text title="输出"
[]
[2, 4, 6]
[1, 2, 4, 5, 7]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1575)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
