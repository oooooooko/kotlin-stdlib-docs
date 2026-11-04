# sortDescending

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

依自然排序顺序对数组中的元素进行排序。

类型是 _stair_。 这意味着等元素在排序后保持彼此相对的顺序 。

??? note "查看英文原文"

    Sorts elements in the array in-place descending according to their natural sort order.
    
    The sort is _stable_. It means that equal elements preserve their order relative to each other after sorting.

## 声明与重载

### 1. Common

```kotlin
public fun <T : Comparable<T>> Array<out T>.sortDescending(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7413)

### 2. Common

```kotlin
public fun ByteArray.sortDescending(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7422)

依自然排序顺序对数组中的元素进行排序。

### 3. Common

```kotlin
public fun ShortArray.sortDescending(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7432)

依自然排序顺序对数组中的元素进行排序。

### 4. Common

```kotlin
public fun IntArray.sortDescending(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7442)

依自然排序顺序对数组中的元素进行排序。

### 5. Common

```kotlin
public fun LongArray.sortDescending(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7452)

依自然排序顺序对数组中的元素进行排序。

### 6. Common

```kotlin
public fun FloatArray.sortDescending(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7462)

依自然排序顺序对数组中的元素进行排序。

### 7. Common

```kotlin
public fun DoubleArray.sortDescending(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7472)

依自然排序顺序对数组中的元素进行排序。

### 8. Common

```kotlin
public fun CharArray.sortDescending(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7482)

依自然排序顺序对数组中的元素进行排序。

### 9. Common

```kotlin
@SinceKotlin("1.4")
public fun <T : Comparable<T>> Array<out T>.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9852)

排序数组中指定范围内的数组元素。这些元素按自然排序顺序排序。

类型是 _stair_。 这意味着等元素在排序后保持彼此相对的顺序 。

@param 从Index 开始( 包括) 到 排序 @param 到 Index 结束( 不包括) 到 排序 。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 10. Common

```kotlin
@SinceKotlin("1.4")
public fun ByteArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9869)

排序数组中指定范围内的数组元素。这些元素按自然排序顺序排序。

@param 从Index 开始( 包括) 到 排序 @param 到 Index 结束( 不包括) 到 排序 。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 11. Common

```kotlin
@SinceKotlin("1.4")
public fun ShortArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9885)

排序数组中指定范围内的数组元素。这些元素按自然排序顺序排序。

@param 从Index 开始( 包括) 到 排序 @param 到 Index 结束( 不包括) 到 排序 。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 12. Common

```kotlin
@SinceKotlin("1.4")
public fun IntArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9901)

排序数组中指定范围内的数组元素。这些元素按自然排序顺序排序。

@param 从Index 开始( 包括) 到 排序 @param 到 Index 结束( 不包括) 到 排序 。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 13. Common

```kotlin
@SinceKotlin("1.4")
public fun LongArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9917)

排序数组中指定范围内的数组元素。这些元素按自然排序顺序排序。

@param 从Index 开始( 包括) 到 排序 @param 到 Index 结束( 不包括) 到 排序 。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 14. Common

```kotlin
@SinceKotlin("1.4")
public fun FloatArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9933)

排序数组中指定范围内的数组元素。这些元素按自然排序顺序排序。

@param 从Index 开始( 包括) 到 排序 @param 到 Index 结束( 不包括) 到 排序 。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 15. Common

```kotlin
@SinceKotlin("1.4")
public fun DoubleArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9949)

排序数组中指定范围内的数组元素。这些元素按自然排序顺序排序。

@param 从Index 开始( 包括) 到 排序 @param 到 Index 结束( 不包括) 到 排序 。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 16. Common

```kotlin
@SinceKotlin("1.4")
public fun CharArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9965)

排序数组中指定范围内的数组元素。这些元素按自然排序顺序排序。

@param 从Index 开始( 包括) 到 排序 @param 到 Index 结束( 不包括) 到 排序 。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 17. Common

```kotlin
public fun <T : Comparable<T>> MutableList<T>.sortDescending(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1195)

依自然排序顺序排序列表中的元素。

类型是 _stair_。 这意味着等元素在排序后保持彼此相对的顺序 。

### 18. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.sortDescending(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3543)

依自然排序顺序对数组中的元素进行排序。

### 19. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.sortDescending(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3555)

依自然排序顺序对数组中的元素进行排序。

### 20. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.sortDescending(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3567)

依自然排序顺序对数组中的元素进行排序。

### 21. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.sortDescending(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3579)

依自然排序顺序对数组中的元素进行排序。

### 22. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UIntArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4791)

排序数组中指定范围内的数组元素。这些元素按自然排序顺序排序。

@param 从Index 开始( 包括) 到 排序 @param 到 Index 结束( 不包括) 到 排序 。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 23. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun ULongArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4808)

排序数组中指定范围内的数组元素。这些元素按自然排序顺序排序。

@param 从Index 开始( 包括) 到 排序 @param 到 Index 结束( 不包括) 到 排序 。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 24. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UByteArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4825)

排序数组中指定范围内的数组元素。这些元素按自然排序顺序排序。

@param 从Index 开始( 包括) 到 排序 @param 到 Index 结束( 不包括) 到 排序 。

@throws 指数外溢值,如果`fromIndex`小于0或`toIndex`大于该阵列的大小,则除外。 @throws 非法参数外溢值,如果`fromIndex` 大于`toIndex`,则不在此列。

### 25. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UShortArray.sortDescending(fromIndex: Int, toIndex: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4842)

排序数组中指定范围内的数组元素。这些元素按自然排序顺序排序。

@param 从Index 开始( 包括) 到 排序 @param 到 Index 结束( 不包括) 到 排序 。

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
    val result = source.`sortDescending`()
    println(result)
}
```

```text title="输出"
kotlin.Unit
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
