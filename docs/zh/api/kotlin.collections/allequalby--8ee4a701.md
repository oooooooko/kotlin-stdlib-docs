# allEqualBy

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果数组中的所有元素产生与给定的 `selector` 函数相同的值,则返回 `true`。

返回`true`的空数组。

`selector` 值按结构平等(`==`)顺序比较,如果第一个元素的`selector`值等于其后每个元素的`selector`值,则所有元素都以`selector`值等值。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本. 生成. 等同。 所有平等的阵列样本. 全部平白

??? note "查看英文原文"

    Returns `true` if all elements in the array yield the same value
    produced by the given `selector` function.
    
    Returns `true` for an empty array.
    
    The `selector` values are compared sequentially using structural equality (`==`),
    and all elements are considered equal by the `selector` value if the `selector`
    value of the first element equals the `selector` value of every subsequent element.
    
    For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
    and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.
    
    @sample samples.generated.allequal.AllEqualArraySamples.allEqualBy

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <T, K> Array<out T>.allEqualBy(selector: (T) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14925)

### 2. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> ByteArray.allEqualBy(selector: (Byte) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14958)

如果数组中的所有元素产生与给定的 `selector` 函数相同的值,则返回 `true`。

返回`true`的空数组。

`selector` 值按结构平等(`==`)顺序比较,如果第一个元素的`selector`值等于其后每个元素的`selector`值,则所有元素都以`selector`值等值。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本. 生成. eall相等。 所有平基- yte Aray 样本。 allEqualBy

### 3. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> ShortArray.allEqualBy(selector: (Short) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14991)

如果数组中的所有元素产生与给定的 `selector` 函数相同的值,则返回 `true`。

返回`true`的空数组。

`selector` 值按结构平等(`==`)顺序比较,如果第一个元素的`selector`值等于其后每个元素的`selector`值,则所有元素都以`selector`值等值。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本. 生成. eall相等。 所有等同的短光阵列样本。 allEqualBy

### 4. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> IntArray.allEqualBy(selector: (Int) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15024)

如果数组中的所有元素产生与给定的 `selector` 函数相同的值,则返回 `true`。

返回`true`的空数组。

`selector` 值按结构平等(`==`)顺序比较,如果第一个元素的`selector`值等于其后每个元素的`selector`值,则所有元素都以`selector`值等值。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本. 生成. eall相等。 AllEqualIntAraySamples.allEqualBy

### 5. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> LongArray.allEqualBy(selector: (Long) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15057)

如果数组中的所有元素产生与给定的 `selector` 函数相同的值,则返回 `true`。

返回`true`的空数组。

`selector` 值按结构平等(`==`)顺序比较,如果第一个元素的`selector`值等于其后每个元素的`selector`值,则所有元素都以`selector`值等值。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本. 生成. eall等。 AllEqualLong ArraySamples.allEqualBy

### 6. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> FloatArray.allEqualBy(selector: (Float) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15090)

如果数组中的所有元素产生与给定的 `selector` 函数相同的值,则返回 `true`。

返回`true`的空数组。

`selector` 值按结构平等(`==`)顺序比较,如果第一个元素的`selector`值等于其后每个元素的`selector`值,则所有元素都以`selector`值等值。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本. 生成. eall等。 所有平面浮转Array 样本。 allEqualBy

### 7. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> DoubleArray.allEqualBy(selector: (Double) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15123)

如果数组中的所有元素产生与给定的 `selector` 函数相同的值,则返回 `true`。

返回`true`的空数组。

`selector` 值按结构平等(`==`)顺序比较,如果第一个元素的`selector`值等于其后每个元素的`selector`值,则所有元素都以`selector`值等值。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本. 生成. 等同。 所有等同的多相相异的AraySamples.allEqualBy

### 8. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> BooleanArray.allEqualBy(selector: (Boolean) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15156)

如果数组中的所有元素产生与给定的 `selector` 函数相同的值,则返回 `true`。

返回`true`的空数组。

`selector` 值按结构平等(`==`)顺序比较,如果第一个元素的`selector`值等于其后每个元素的`selector`值,则所有元素都以`selector`值等值。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本. 生成. eall相等。

### 9. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> CharArray.allEqualBy(selector: (Char) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L15189)

如果数组中的所有元素产生与给定的 `selector` 函数相同的值,则返回 `true`。

返回`true`的空数组。

`selector` 值按结构平等(`==`)顺序比较,如果第一个元素的`selector`值等于其后每个元素的`selector`值,则所有元素都以`selector`值等值。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本. 生成. eall相等。 AllEqualCharAraySamples.allEqualBy

### 10. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <T, K> Iterable<T>.allEqualBy(selector: (T) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L2035)

如果收藏中的所有元素产生与给定的`selector`函数产生的相同价值,则返回`true`。

空收藏返回`true`。

`selector` 值按结构平等(`==`)顺序比较,如果第一个元素的`selector`值等于其后每个元素的`selector`值,则所有元素都以`selector`值等值。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本. 生成. eall相等。 所有平等可使用性 样本.allEqualBy

### 11. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public inline fun <K> UIntArray.allEqualBy(selector: (UInt) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6335)

如果数组中的所有元素产生与给定的 `selector` 函数相同的值,则返回 `true`。

返回`true`的空数组。

`selector` 值按结构平等(`==`)顺序比较,如果第一个元素的`selector`值等于其后每个元素的`selector`值,则所有元素都以`selector`值等值。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本. 生成. eall相等。 AllEqualUINT AraySamples.allEqualBy

### 12. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public inline fun <K> ULongArray.allEqualBy(selector: (ULong) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6369)

如果数组中的所有元素产生与给定的 `selector` 函数相同的值,则返回 `true`。

返回`true`的空数组。

`selector` 值按结构平等(`==`)顺序比较,如果第一个元素的`selector`值等于其后每个元素的`selector`值,则所有元素都以`selector`值等值。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本. 生成. eall相等。 AllEqualULongArraySamples.allEqualBy

### 13. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public inline fun <K> UByteArray.allEqualBy(selector: (UByte) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6403)

如果数组中的所有元素产生与给定的 `selector` 函数相同的值,则返回 `true`。

返回`true`的空数组。

`selector` 值按结构平等(`==`)顺序比较,如果第一个元素的`selector`值等于其后每个元素的`selector`值,则所有元素都以`selector`值等值。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本. 生成. eall相等。 AllEqualUByte ArraySamples.allEqualBy

### 14. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public inline fun <K> UShortArray.allEqualBy(selector: (UShort) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6437)

如果数组中的所有元素产生与给定的 `selector` 函数相同的值,则返回 `true`。

返回`true`的空数组。

`selector` 值按结构平等(`==`)顺序比较,如果第一个元素的`selector`值等于其后每个元素的`selector`值,则所有元素都以`selector`值等值。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本. 生成. eall相等。 AllEqualUShort ArraySamples.allEqualBy

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(arrayOf<String>().allEqualBy { it.length })
    println(arrayOf("apple").allEqualBy { it.length })

    val values = arrayOf("apple", "mango", "peach")
    println(values.allEqualBy { it.length })
    println(values.allEqualBy { it })
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualArraySamples.kt#L30)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(byteArrayOf().allEqualBy { it * it })
    println(byteArrayOf(1).allEqualBy { it * it })

    val values = byteArrayOf(1, -1, 1)
    println(values.allEqualBy { it * it })
    println(values.allEqualBy { abs(it.toInt()) })
    println(values.allEqualBy { it * it * it })
}
```

```text title="输出"
true
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualByteArraySamples.kt#L31)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(shortArrayOf().allEqualBy { it * it })
    println(shortArrayOf(1).allEqualBy { it * it })

    val values = shortArrayOf(1, -1, 1)
    println(values.allEqualBy { it * it })
    println(values.allEqualBy { abs(it.toInt()) })
    println(values.allEqualBy { it * it * it })
}
```

```text title="输出"
true
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualShortArraySamples.kt#L31)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(intArrayOf().allEqualBy { it * it })
    println(intArrayOf(1).allEqualBy { it * it })

    val values = intArrayOf(1, -1, 1)
    println(values.allEqualBy { it * it })
    println(values.allEqualBy { abs(it) })
    println(values.allEqualBy { it * it * it })
}
```

```text title="输出"
true
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualIntArraySamples.kt#L31)

### 示例 5 · JVM

```kotlin title="示例 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(longArrayOf().allEqualBy { it * it })
    println(longArrayOf(1L).allEqualBy { it * it })

    val values = longArrayOf(1L, -1L, 1L)
    println(values.allEqualBy { it * it })
    println(values.allEqualBy { abs(it) })
    println(values.allEqualBy { it * it * it })
}
```

```text title="输出"
true
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualLongArraySamples.kt#L31)

### 示例 6 · JVM

```kotlin title="示例 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(floatArrayOf().allEqualBy { it * it })
    println(floatArrayOf(1.0f).allEqualBy { it * it })

    val values = floatArrayOf(1.0f, -1.0f, 1.0f)
    println(values.allEqualBy { it * it })
    println(values.allEqualBy { abs(it) })
    println(values.allEqualBy { it * it * it })
}
```

```text title="输出"
true
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualFloatArraySamples.kt#L31)

### 示例 7 · JVM

```kotlin title="示例 7" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.abs



fun main() {
    println(doubleArrayOf().allEqualBy { it * it })
    println(doubleArrayOf(1.0).allEqualBy { it * it })

    val values = doubleArrayOf(1.0, -1.0, 1.0)
    println(values.allEqualBy { it * it })
    println(values.allEqualBy { abs(it) })
    println(values.allEqualBy { it * it * it })
}
```

```text title="输出"
true
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualDoubleArraySamples.kt#L31)

### 示例 8 · JVM

```kotlin title="示例 8" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(booleanArrayOf().allEqualBy { 0 })
    println(booleanArrayOf(true).allEqualBy { 0 })

    val values = booleanArrayOf(true, false, true)
    println(values.allEqualBy { 0 })
    println(values.allEqualBy { if (it) 1 else 0 })
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualBooleanArraySamples.kt#L30)

### 示例 9 · JVM

```kotlin title="示例 9" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(charArrayOf().allEqualBy { it.uppercaseChar() })
    println(charArrayOf('a').allEqualBy { it.uppercaseChar() })

    val values = charArrayOf('a', 'A', 'a')
    println(values.allEqualBy { it.uppercaseChar() })
    println(values.allEqualBy { it.lowercaseChar() })
    println(values.allEqualBy { it })
}
```

```text title="输出"
true
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualCharArraySamples.kt#L30)

### 示例 10 · JVM

```kotlin title="示例 10" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(listOf<String>().allEqualBy { it.length })
    println(listOf("apple").allEqualBy { it.length })

    val values = listOf("apple", "mango", "peach")
    println(values.allEqualBy { it.length })
    println(values.allEqualBy { it })
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualIterablesSamples.kt#L30)

### 示例 11 · JVM

```kotlin title="示例 11" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(uintArrayOf().allEqualBy { it % 2u })
    println(uintArrayOf(1u).allEqualBy { it % 2u })

    val values = uintArrayOf(1u, 3u, 5u)
    println(values.allEqualBy { it % 2u })
    println(values.allEqualBy { it })
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualUIntArraySamples.kt#L30)

### 示例 12 · JVM

```kotlin title="示例 12" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ulongArrayOf().allEqualBy { it % 2uL })
    println(ulongArrayOf(1uL).allEqualBy { it % 2uL })

    val values = ulongArrayOf(1uL, 3uL, 5uL)
    println(values.allEqualBy { it % 2uL })
    println(values.allEqualBy { it })
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualULongArraySamples.kt#L30)

### 示例 13 · JVM

```kotlin title="示例 13" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ubyteArrayOf().allEqualBy { it.toUInt() % 2u })
    println(ubyteArrayOf(1u).allEqualBy { it.toUInt() % 2u })

    val values = ubyteArrayOf(1u, 3u, 5u)
    println(values.allEqualBy { it.toUInt() % 2u })
    println(values.allEqualBy { it })
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualUByteArraySamples.kt#L30)

### 示例 14 · JVM

```kotlin title="示例 14" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ushortArrayOf().allEqualBy { it.toUInt() % 2u })
    println(ushortArrayOf(1u).allEqualBy { it.toUInt() % 2u })

    val values = ushortArrayOf(1u, 3u, 5u)
    println(values.allEqualBy { it.toUInt() % 2u })
    println(values.allEqualBy { it })
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/allequal/AllEqualUShortArraySamples.kt#L30)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
