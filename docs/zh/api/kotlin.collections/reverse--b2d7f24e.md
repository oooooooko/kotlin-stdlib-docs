# reverse

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将数组中的元素反转为位置。

??? note "查看英文原文"

    Reverses elements in the array in-place.

## 声明与重载

### 1. Common

```kotlin
public fun <T> Array<T>.reverse(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6606)

### 2. Common

```kotlin
public fun ByteArray.reverse(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6621)

### 3. Common

```kotlin
public fun ShortArray.reverse(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6636)

### 4. Common

```kotlin
public fun IntArray.reverse(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6651)

### 5. Common

```kotlin
public fun LongArray.reverse(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6666)

### 6. Common

```kotlin
public fun FloatArray.reverse(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6681)

### 7. Common

```kotlin
public fun DoubleArray.reverse(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6696)

### 8. Common

```kotlin
public fun BooleanArray.reverse(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6711)

### 9. Common

```kotlin
public fun CharArray.reverse(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6726)

### 10. Common

```kotlin
@SinceKotlin("1.4")
public fun <T> Array<T>.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6741)

将数组的元素在指定范围内反转。

@param 从Index开始(包括) 向后移动。 @param 到Index 向后(不包括) 向后移动。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 11. Common

```kotlin
@SinceKotlin("1.4")
public fun ByteArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6764)

将数组的元素在指定范围内反转。

@param 从Index开始(包括) 向后移动。 @param 到Index 向后(不包括) 向后移动。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 12. Common

```kotlin
@SinceKotlin("1.4")
public fun ShortArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6787)

将数组的元素在指定范围内反转。

@param 从Index开始(包括) 向后移动。 @param 到Index 向后(不包括) 向后移动。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 13. Common

```kotlin
@SinceKotlin("1.4")
public fun IntArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6810)

将数组的元素在指定范围内反转。

@param 从Index开始(包括) 向后移动。 @param 到Index 向后(不包括) 向后移动。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 14. Common

```kotlin
@SinceKotlin("1.4")
public fun LongArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6833)

将数组的元素在指定范围内反转。

@param 从Index开始(包括) 向后移动。 @param 到Index 向后(不包括) 向后移动。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 15. Common

```kotlin
@SinceKotlin("1.4")
public fun FloatArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6856)

将数组的元素在指定范围内反转。

@param 从Index开始(包括) 向后移动。 @param 到Index 向后(不包括) 向后移动。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 16. Common

```kotlin
@SinceKotlin("1.4")
public fun DoubleArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6879)

将数组的元素在指定范围内反转。

@param 从Index开始(包括) 向后移动。 @param 到Index 向后(不包括) 向后移动。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 17. Common

```kotlin
@SinceKotlin("1.4")
public fun BooleanArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6902)

将数组的元素在指定范围内反转。

@param 从Index开始(包括) 向后移动。 @param 到Index 向后(不包括) 向后移动。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 18. Common

```kotlin
@SinceKotlin("1.4")
public fun CharArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L6925)

将数组的元素在指定范围内反转。

@param 从Index开始(包括) 向后移动。 @param 到Index 向后(不包括) 向后移动。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 19. Common

```kotlin
public expect fun <T> MutableList<T>.reverse(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1143)

将列表中的元素反转为位置。

### 20. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.reverse(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3235)

### 21. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.reverse(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3245)

### 22. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.reverse(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3255)

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.reverse(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3265)

### 24. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3275)

将数组的元素在指定范围内反转。

@param 从Index开始(包括) 向后移动。 @param 到Index 向后(不包括) 向后移动。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 25. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3291)

将数组的元素在指定范围内反转。

@param 从Index开始(包括) 向后移动。 @param 到Index 向后(不包括) 向后移动。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 26. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3307)

将数组的元素在指定范围内反转。

@param 从Index开始(包括) 向后移动。 @param 到Index 向后(不包括) 向后移动。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 27. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.reverse(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3323)

将数组的元素在指定范围内反转。

@param 从Index开始(包括) 向后移动。 @param 到Index 向后(不包括) 向后移动。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.collections.*

fun main() {
    val source = arrayOf(1, 2, 3)
    val result = source.`reverse`()
    println(result)
}
```

```text title="输出"
kotlin.Unit
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
