# contentEquals

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

检查两个指定的数组是否 * 结构 * 等同。

两个阵列如果大小相同,则被视为结构上相等,相应的指数中各要素相同。
使用 `equals`Z`Any.equals` 函数对元素进行平等比较。
对于浮动点数,这意味着`NaN`等于本身,而`-0.0`不等于`0.0`。

如果两个数组均为`null`,则也认为这些数组在结构上是平等的。

如果阵列包含嵌套阵列,请使用 `contentDeepEquals` 来对元素进行递现比较。

@param 其它与此阵列比较的数组。 @return `true`,如果两个阵列结构相等,则 `false` 。

@sample 样本、采集物、阵列、实际操作、阵列、

??? note "查看英文原文"

    Checks if the two specified arrays are *structurally* equal to one another.
    
    Two arrays are considered structurally equal if they have the same size, and elements at corresponding indices are equal.
    Elements are compared for equality using the `equals``Any.equals` function.
    For floating point numbers, this means `NaN` is equal to itself and `-0.0` is not equal to `0.0`.
    
    The arrays are also considered structurally equal if both are `null`.
    
    If the arrays contain nested arrays, use `contentDeepEquals` to recursively compare their elements.
    
    @param other the array to compare with this array.
    @return `true` if the two arrays are structurally equal, `false` otherwise.
    
    @sample samples.collections.Arrays.ContentOperations.arrayContentEquals

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun <T> Array<out T>?.contentEquals(other: Array<out T>?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8227)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun ByteArray?.contentEquals(other: ByteArray?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8246)

检查两个指定的数组是否 * 结构 * 等同。

两个阵列如果大小相同,则被视为结构上相等,相应的指数中各要素相同。

如果两个数组均为`null`,则也认为这些数组在结构上是平等的。

@param 其它与此阵列比较的数组。 @return `true`,如果两个阵列结构相等,则 `false` 。

@sample 样本. 采集资料. 阵列. 关联操作. 内部阵列

### 3. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun ShortArray?.contentEquals(other: ShortArray?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8261)

检查两个指定的数组是否 * 结构 * 等同。

两个阵列如果大小相同,则被视为结构上相等,相应的指数中各要素相同。

如果两个数组均为`null`,则也认为这些数组在结构上是平等的。

@param 其它与此阵列比较的数组。 @return `true`,如果两个阵列结构相等,则 `false` 。

@sample 样本. 采集资料. 阵列. 关联操作. 内部阵列

### 4. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun IntArray?.contentEquals(other: IntArray?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8276)

检查两个指定的数组是否 * 结构 * 等同。

两个阵列如果大小相同,则被视为结构上相等,相应的指数中各要素相同。

如果两个数组均为`null`,则也认为这些数组在结构上是平等的。

@param 其它与此阵列比较的数组。 @return `true`,如果两个阵列结构相等,则 `false` 。

@sample 样本. 采集资料. 阵列. 关联操作. 内部阵列

### 5. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun LongArray?.contentEquals(other: LongArray?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8291)

检查两个指定的数组是否 * 结构 * 等同。

两个阵列如果大小相同,则被视为结构上相等,相应的指数中各要素相同。

如果两个数组均为`null`,则也认为这些数组在结构上是平等的。

@param 其它与此阵列比较的数组。 @return `true`,如果两个阵列结构相等,则 `false` 。

@sample 样本. 采集资料. 阵列. 关联操作. 内部阵列

### 6. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun FloatArray?.contentEquals(other: FloatArray?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8306)

检查两个指定的数组是否 * 结构 * 等同。

两个阵列如果大小相同,则被视为结构上相等,相应的指数中各要素相同。
使用 `equals`Z`Any.equals` 函数对元素进行平等比较。
这意味着`NaN`等于它本身,`-0.0`不等于`0.0`。

如果两个数组均为`null`,则也认为这些数组在结构上是平等的。

@param 其它与此阵列比较的数组。 @return `true`,如果两个阵列结构相等,则 `false` 。

@sample 样本、采集资料、阵列、关联操作、双光谱

### 7. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun DoubleArray?.contentEquals(other: DoubleArray?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8323)

检查两个指定的数组是否 * 结构 * 等同。

两个阵列如果大小相同,则被视为结构上相等,相应的指数中各要素相同。
使用 `equals`Z`Any.equals` 函数对元素进行平等比较。
这意味着`NaN`等于它本身,`-0.0`不等于`0.0`。

如果两个数组均为`null`,则也认为这些数组在结构上是平等的。

@param 其它与此阵列比较的数组。 @return `true`,如果两个阵列结构相等,则 `false` 。

@sample 样本、采集资料、阵列、关联操作、双光谱

### 8. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun BooleanArray?.contentEquals(other: BooleanArray?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8340)

检查两个指定的数组是否 * 结构 * 等同。

两个阵列如果大小相同,则被视为结构上相等,相应的指数中各要素相同。

如果两个数组均为`null`,则也认为这些数组在结构上是平等的。

@param 其它与此阵列比较的数组。 @return `true`,如果两个阵列结构相等,则 `false` 。

@sample 样本. 采集资料. 阵列. 相关操作. 布尔- 亚阵列

### 9. Common

```kotlin
@SinceKotlin("1.4")
public expect infix fun CharArray?.contentEquals(other: CharArray?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L8355)

检查两个指定的数组是否 * 结构 * 等同。

两个阵列如果大小相同,则被视为结构上相等,相应的指数中各要素相同。

如果两个数组均为`null`,则也认为这些数组在结构上是平等的。

@param 其它与此阵列比较的数组。 @return `true`,如果两个阵列结构相等,则 `false` 。

@sample 样本采集资料 阵列、关联操作、焦 质

### 10. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public infix fun UIntArray?.contentEquals(other: UIntArray?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3891)

检查两个指定的数组是否 * 结构 * 等同。

两个阵列如果大小相同,则被视为结构上相等,相应的指数中各要素相同。

如果两个数组均为`null`,则也认为这些数组在结构上是平等的。

@param 其它与此阵列比较的数组。 @return `true`,如果两个阵列结构相等,则 `false` 。

@sample 样本. 采集资料. 阵列. 关联操作. 内部阵列

### 11. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public infix fun ULongArray?.contentEquals(other: ULongArray?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3909)

检查两个指定的数组是否 * 结构 * 等同。

两个阵列如果大小相同,则被视为结构上相等,相应的指数中各要素相同。

如果两个数组均为`null`,则也认为这些数组在结构上是平等的。

@param 其它与此阵列比较的数组。 @return `true`,如果两个阵列结构相等,则 `false` 。

@sample 样本. 采集资料. 阵列. 关联操作. 内部阵列

### 12. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public infix fun UByteArray?.contentEquals(other: UByteArray?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3927)

检查两个指定的数组是否 * 结构 * 等同。

两个阵列如果大小相同,则被视为结构上相等,相应的指数中各要素相同。

如果两个数组均为`null`,则也认为这些数组在结构上是平等的。

@param 其它与此阵列比较的数组。 @return `true`,如果两个阵列结构相等,则 `false` 。

@sample 样本. 采集资料. 阵列. 关联操作. 内部阵列

### 13. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public infix fun UShortArray?.contentEquals(other: UShortArray?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3945)

检查两个指定的数组是否 * 结构 * 等同。

两个阵列如果大小相同,则被视为结构上相等,相应的指数中各要素相同。

如果两个数组均为`null`,则也认为这些数组在结构上是平等的。

@param 其它与此阵列比较的数组。 @return `true`,如果两个阵列结构相等,则 `false` 。

@sample 样本. 采集资料. 阵列. 关联操作. 内部阵列

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
    val result = source.`contentEquals`(arrayOf(1, 2, 3))
    println(result)
}
```

```text title="输出"
true
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
