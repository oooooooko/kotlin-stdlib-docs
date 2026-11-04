# flatMapTo

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将原始阵列中每个单元援引的 `transform` 函数的结果所产生的所有要素,都附于给定的`destination`。

??? note "查看英文原文"

    Appends all elements yielded from results of `transform` function being invoked on each element of original array, to the given `destination`.

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, R, C : MutableCollection<in R>> Array<out T>.flatMapTo(destination: C, transform: (T) -> Iterable<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12147)

### 2. Common

```kotlin
@IgnorableReturnValue
public inline fun <R, C : MutableCollection<in R>> ByteArray.flatMapTo(destination: C, transform: (Byte) -> Iterable<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12159)

### 3. Common

```kotlin
@IgnorableReturnValue
public inline fun <R, C : MutableCollection<in R>> ShortArray.flatMapTo(destination: C, transform: (Short) -> Iterable<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12171)

### 4. Common

```kotlin
@IgnorableReturnValue
public inline fun <R, C : MutableCollection<in R>> IntArray.flatMapTo(destination: C, transform: (Int) -> Iterable<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12183)

### 5. Common

```kotlin
@IgnorableReturnValue
public inline fun <R, C : MutableCollection<in R>> LongArray.flatMapTo(destination: C, transform: (Long) -> Iterable<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12195)

### 6. Common

```kotlin
@IgnorableReturnValue
public inline fun <R, C : MutableCollection<in R>> FloatArray.flatMapTo(destination: C, transform: (Float) -> Iterable<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12207)

### 7. Common

```kotlin
@IgnorableReturnValue
public inline fun <R, C : MutableCollection<in R>> DoubleArray.flatMapTo(destination: C, transform: (Double) -> Iterable<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12219)

### 8. Common

```kotlin
@IgnorableReturnValue
public inline fun <R, C : MutableCollection<in R>> BooleanArray.flatMapTo(destination: C, transform: (Boolean) -> Iterable<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12231)

### 9. Common

```kotlin
@IgnorableReturnValue
public inline fun <R, C : MutableCollection<in R>> CharArray.flatMapTo(destination: C, transform: (Char) -> Iterable<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12243)

### 10. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.jvm.JvmName("flatMapSequenceTo")
@IgnorableReturnValue
public inline fun <T, R, C : MutableCollection<in R>> Array<out T>.flatMapTo(destination: C, transform: (T) -> Sequence<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L12255)

### 11. Common

```kotlin
@IgnorableReturnValue
public inline fun <T, R, C : MutableCollection<in R>> Iterable<T>.flatMapTo(destination: C, transform: (T) -> Iterable<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1634)

将原始收藏的每个部分援引的 `transform` 函数的结果所产生的所有要素,都附于给定的`destination`。

### 12. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.jvm.JvmName("flatMapSequenceTo")
@IgnorableReturnValue
public inline fun <T, R, C : MutableCollection<in R>> Iterable<T>.flatMapTo(destination: C, transform: (T) -> Sequence<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1646)

将原始收藏的每个部分援引的 `transform` 函数的结果所产生的所有要素,都附于给定的`destination`。

### 13. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, R, C : MutableCollection<in R>> Map<out K, V>.flatMapTo(destination: C, transform: (Map.Entry<K, V>) -> Iterable<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L94)

将原始地图每个条目引用的 `transform` 函数的结果所产生的所有要素都附在给定的`destination`之后。

### 14. Common

```kotlin
@SinceKotlin("1.4")
@OptIn(kotlin.experimental.ExperimentalTypeInference::class)
@OverloadResolutionByLambdaReturnType
@kotlin.jvm.JvmName("flatMapSequenceTo")
@IgnorableReturnValue
public inline fun <K, V, R, C : MutableCollection<in R>> Map<out K, V>.flatMapTo(destination: C, transform: (Map.Entry<K, V>) -> Sequence<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Maps.kt#L106)

将原始地图每个条目引用的 `transform` 函数的结果所产生的所有要素都附在给定的`destination`之后。

### 15. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, C : MutableCollection<in R>> UIntArray.flatMapTo(destination: C, transform: (UInt) -> Iterable<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5351)

### 16. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, C : MutableCollection<in R>> ULongArray.flatMapTo(destination: C, transform: (ULong) -> Iterable<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5366)

### 17. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, C : MutableCollection<in R>> UByteArray.flatMapTo(destination: C, transform: (UByte) -> Iterable<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5381)

### 18. Common

```kotlin
@SinceKotlin("1.3")
@IgnorableReturnValue
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun <R, C : MutableCollection<in R>> UShortArray.flatMapTo(destination: C, transform: (UShort) -> Iterable<R>): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L5396)

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
