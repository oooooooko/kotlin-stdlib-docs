# copyOf

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回新数组,该数组是原始数组的复制件。

@sample 样本,采集资料,阵列,操作总合,复制

??? note "查看英文原文"

    Returns new array which is a copy of the original array.
    
    @sample samples.collections.Arrays.CopyOfOperations.copyOf

## 声明与重载

### 1. Common

```kotlin
public expect fun <T> Array<T>.copyOf(): Array<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8676)

### 2. Common

```kotlin
public expect fun ByteArray.copyOf(): ByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8683)

### 3. Common

```kotlin
public expect fun ShortArray.copyOf(): ShortArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8690)

### 4. Common

```kotlin
public expect fun IntArray.copyOf(): IntArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8697)

### 5. Common

```kotlin
public expect fun LongArray.copyOf(): LongArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8704)

### 6. Common

```kotlin
public expect fun FloatArray.copyOf(): FloatArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8711)

### 7. Common

```kotlin
public expect fun DoubleArray.copyOf(): DoubleArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8718)

### 8. Common

```kotlin
public expect fun BooleanArray.copyOf(): BooleanArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8725)

### 9. Common

```kotlin
public expect fun CharArray.copyOf(): CharArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8732)

### 10. Common

```kotlin
public expect fun ByteArray.copyOf(newSize: Int): ByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8739)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 必要时以零值 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将填充复制数组中的额外元素,并填充零值。

@sample 样本收集资料

### 11. Common

```kotlin
public expect fun ShortArray.copyOf(newSize: Int): ShortArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8750)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 必要时以零值 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将填充复制数组中的额外元素,并填充零值。

@sample 样本收集资料

### 12. Common

```kotlin
public expect fun IntArray.copyOf(newSize: Int): IntArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8761)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 必要时以零值 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将填充复制数组中的额外元素,并填充零值。

@sample 样本收集资料

### 13. Common

```kotlin
public expect fun LongArray.copyOf(newSize: Int): LongArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8772)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 必要时以零值 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将填充复制数组中的额外元素,并填充零值。

@sample 样本收集资料

### 14. Common

```kotlin
public expect fun FloatArray.copyOf(newSize: Int): FloatArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8783)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 必要时以零值 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将填充复制数组中的额外元素,并填充零值。

@sample 样本收集资料

### 15. Common

```kotlin
public expect fun DoubleArray.copyOf(newSize: Int): DoubleArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8794)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 必要时以零值 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将填充复制数组中的额外元素,并填充零值。

@sample 样本收集资料

### 16. Common

```kotlin
public expect fun BooleanArray.copyOf(newSize: Int): BooleanArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8805)

返回新数组, 后者是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被删减, 要么在结尾处添加, 必要时以 `false` 值 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则复制数组中的额外元素将填充 `false` 值。

@sample 样本收集资料

### 17. Common

```kotlin
public expect fun CharArray.copyOf(newSize: Int): CharArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8816)

返回新数组, 后者是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被删减, 要么在结尾处加注, 必要时加注 null char ( `\u0000` ) 值 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则复制数组中的额外元素将填充为 narkchar ( `\u0000` ) 值。

@sample 样本收集资料

### 18. Common

```kotlin
public expect fun <T> Array<T>.copyOf(newSize: Int): Array<T?>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8827)

返回新数组, 后者是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被删减, 要么在结尾处添加, 必要时以 `null` 值 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则复制数组中的额外元素将填充 `null` 值。

@sample 样本收集资料

### 19. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@kotlin.internal.InlineOnly
public inline fun <T> Array<T>.copyOf(newSize: Int, init: (Int) -> T): Array<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8838)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 计算结果为调用指定的 `init` 函数 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将复制数组中的额外元素填充为计算值,计算方法是调用指定的 `init` 函数。

函数 `init` 依次被调用,用于从对应源数组大小的指数到`newSize`的每个阵列元素。它应该返回一个阵列元素的值,并根据其索引值。

@sample 样本收集资料,Arrays, CompopiOffices, Array with Intiatives, 复制件, 激光器与装置

### 20. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@kotlin.internal.InlineOnly
public inline fun ByteArray.copyOf(newSize: Int, init: (Int) -> Byte): ByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8865)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 计算结果为调用指定的 `init` 函数 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将复制数组中的额外元素填充为计算值,计算方法是调用指定的 `init` 函数。

函数 `init` 依次被调用,用于从对应源数组大小的指数到`newSize`的每个阵列元素。它应该返回一个阵列元素的值,并根据其索引值。

@sample 样本收集资料 阵列、操作总合、环形阵列与工业家

### 21. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@kotlin.internal.InlineOnly
public inline fun ShortArray.copyOf(newSize: Int, init: (Int) -> Short): ShortArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8892)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 计算结果为调用指定的 `init` 函数 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将复制数组中的额外元素填充为计算值,计算方法是调用指定的 `init` 函数。

函数 `init` 依次被调用,用于从对应源数组大小的指数到`newSize`的每个阵列元素。它应该返回一个阵列元素的值,并根据其索引值。

@sample 样本收集、阵列、操作合作、短射线与工业

### 22. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@kotlin.internal.InlineOnly
public inline fun IntArray.copyOf(newSize: Int, init: (Int) -> Int): IntArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8919)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 计算结果为调用指定的 `init` 函数 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将复制数组中的额外元素填充为计算值,计算方法是调用指定的 `init` 函数。

函数 `init` 依次被调用,用于从对应源数组大小的指数到`newSize`的每个阵列元素。它应该返回一个阵列元素的值,并根据其索引值。

@sample 样本采集资料、阵列、操作总操作、内部阵列与工业器复印本

### 23. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@kotlin.internal.InlineOnly
public inline fun LongArray.copyOf(newSize: Int, init: (Int) -> Long): LongArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8946)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 计算结果为调用指定的 `init` 函数 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将复制数组中的额外元素填充为计算值,计算方法是调用指定的 `init` 函数。

函数 `init` 依次被调用,用于从对应源数组大小的指数到`newSize`的每个阵列元素。它应该返回一个阵列元素的值,并根据其索引值。

@sample 样本收集资料,Arrays, Compopiopo OFLongArray与工业家

### 24. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@kotlin.internal.InlineOnly
public inline fun FloatArray.copyOf(newSize: Int, init: (Int) -> Float): FloatArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8973)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 计算结果为调用指定的 `init` 函数 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将复制数组中的额外元素填充为计算值,计算方法是调用指定的 `init` 函数。

函数 `init` 依次被调用,用于从对应源数组大小的指数到`newSize`的每个阵列元素。它应该返回一个阵列元素的值,并根据其索引值。

@sample 样本收集资料,Arrays.Compopior OfffloatArray with Intiators 复制件, 激光器操作总合。

### 25. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@kotlin.internal.InlineOnly
public inline fun DoubleArray.copyOf(newSize: Int, init: (Int) -> Double): DoubleArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9000)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 计算结果为调用指定的 `init` 函数 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将复制数组中的额外元素填充为计算值,计算方法是调用指定的 `init` 函数。

函数 `init` 依次被调用,用于从对应源数组大小的指数到`newSize`的每个阵列元素。它应该返回一个阵列元素的值,并根据其索引值。

@sample 样本收集资料,Arrays, 操作总操作,多光电与工业

### 26. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@kotlin.internal.InlineOnly
public inline fun BooleanArray.copyOf(newSize: Int, init: (Int) -> Boolean): BooleanArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9027)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 计算结果为调用指定的 `init` 函数 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将复制数组中的额外元素填充为计算值,计算方法是调用指定的 `init` 函数。

函数 `init` 依次被调用,用于从对应源数组大小的指数到`newSize`的每个阵列元素。它应该返回一个阵列元素的值,并根据其索引值。

@sample 样本收集资料,Arrays.Compopior of Boolean Array with Initializer 复制件,《火炮与工业》

### 27. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@kotlin.internal.InlineOnly
public inline fun CharArray.copyOf(newSize: Int, init: (Int) -> Char): CharArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9054)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 计算结果为调用指定的 `init` 函数 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将复制数组中的额外元素填充为计算值,计算方法是调用指定的 `init` 函数。

函数 `init` 依次被调用,用于从对应源数组大小的指数到`newSize`的每个阵列元素。它应该返回一个阵列元素的值,并根据其索引值。

@sample 样本采集资料、阵列、操作合作、复印版

### 28. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.copyOf(): UIntArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4143)

### 29. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.copyOf(): ULongArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4155)

### 30. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.copyOf(): UByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4167)

### 31. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.copyOf(): UShortArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4179)

### 32. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.copyOf(newSize: Int): UIntArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4191)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 必要时以零值 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将填充复制数组中的额外元素,并填充零值。

### 33. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.copyOf(newSize: Int): ULongArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4205)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 必要时以零值 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将填充复制数组中的额外元素,并填充零值。

### 34. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.copyOf(newSize: Int): UByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4219)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 必要时以零值 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将填充复制数组中的额外元素,并填充零值。

### 35. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.copyOf(newSize: Int): UShortArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4233)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 必要时以零值 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将填充复制数组中的额外元素,并填充零值。

### 36. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UIntArray.copyOf(newSize: Int, init: (Int) -> UInt): UIntArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4247)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 计算结果为调用指定的 `init` 函数 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将复制数组中的额外元素填充为计算值,计算方法是调用指定的 `init` 函数。

函数 `init` 依次被调用,用于从对应源数组大小的指数到`newSize`的每个阵列元素。它应该返回一个阵列元素的值,并根据其索引值。

@sample 样本收集资料,Arrays.CompopiOffices. 复制OFUUUINARARIAINTIATION 内装装置

### 37. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun ULongArray.copyOf(newSize: Int, init: (Int) -> ULong): ULongArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4275)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 计算结果为调用指定的 `init` 函数 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将复制数组中的额外元素填充为计算值,计算方法是调用指定的 `init` 函数。

函数 `init` 依次被调用,用于从对应源数组大小的指数到`newSize`的每个阵列元素。它应该返回一个阵列元素的值,并根据其索引值。

@sample 样本收集资料,Arrays.Compopiopy OFULONARRARARIOTIONATIONS, 操作总操作,复制件, 复制件, 复制件, 复制件, 复制件, 复制件, 复制件, 复制件, 复制件, 复制件, 复制件, 复制件, 复制件, 复制件, 复制件, 复制件, 复制件

### 38. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UByteArray.copyOf(newSize: Int, init: (Int) -> UByte): UByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4303)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 计算结果为调用指定的 `init` 函数 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将复制数组中的额外元素填充为计算值,计算方法是调用指定的 `init` 函数。

函数 `init` 依次被调用,用于从对应源数组大小的指数到`newSize`的每个阵列元素。它应该返回一个阵列元素的值,并根据其索引值。

@sample 样本收集资料。 阵列、操作合作、复制版。

### 39. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun UShortArray.copyOf(newSize: Int, init: (Int) -> UShort): UShortArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4331)

返回新数组,该数组是原始数组的复制件, 重新缩放到给定的 `newSize` 。 副本要么被缩短, 要么在结尾处添加, 计算结果为调用指定的 `init` 函数 。

- `newSize`小于原始数组的大小,则将复制数组缩短为 `newSize` 。 - 如果`newSize`大于原始数组的大小,则将复制数组中的额外元素填充为计算值,计算方法是调用指定的 `init` 函数。

函数 `init` 依次被调用,用于从对应源数组大小的指数到`newSize`的每个阵列元素。它应该返回一个阵列元素的值,并根据其索引值。

@sample 样本、采集物、操作总合、美国工业和工业工业

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
    val result = source.`copyOf`()
    println(result.contentToString())
}
```

```text title="输出"
[1, 2, 3]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
