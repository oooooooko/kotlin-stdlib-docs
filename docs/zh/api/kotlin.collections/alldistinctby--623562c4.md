# allDistinctBy

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果对数组中的元素应用给定的 `selector` 函数产生的全部值彼此不同,则返回 `true`。

返回`true`的空数组。

`selector` 值是使用结构平等( `==` )进行比较的,一旦发现 `false` 的值重复值,该操作将返回 `false` 。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本, 生成. 全部 。 All Distinct AraySamples, all DistinctBy

??? note "查看英文原文"

    Returns `true` if all values produced by applying the given `selector` function to the
    elements in the array are distinct from each other.
    
    Returns `true` for an empty array.
    
    The `selector` values are compared using structural equality (`==`).
    The operation returns `false` as soon as a duplicate `selector` value is found.
    
    For selector values of floating-point types (`Double`, `Float`), `NaN` is considered equal to `NaN`,
    and `-0.0` is considered not equal to `0.0`, consistent with `Double.equals` and `Float.equals`.
    
    @sample samples.generated.alldistinct.AllDistinctArraySamples.allDistinctBy

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <T, K> Array<out T>.allDistinctBy(selector: (T) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14493)

### 2. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> ByteArray.allDistinctBy(selector: (Byte) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14518)

如果对数组中的元素应用给定的 `selector` 函数产生的全部值彼此不同,则返回 `true`。

返回`true`的空数组。

`selector` 值是使用结构平等( `==` )进行比较的,一旦发现 `false` 的值重复值,该操作将返回 `false` 。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本. 生成. all distinctByte 分布式标本。 全部 DistinctByte 都生成

### 3. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> ShortArray.allDistinctBy(selector: (Short) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14543)

如果对数组中的元素应用给定的 `selector` 函数产生的全部值彼此不同,则返回 `true`。

返回`true`的空数组。

`selector` 值是使用结构平等( `==` )进行比较的,一旦发现 `false` 的值重复值,该操作将返回 `false` 。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本, 生成. all different. All distictShortAraySamples. all distinctBy 全部生成。 全 DistentShortAraySamples. 所有 DistinctBy 样本 全部生成

### 4. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> IntArray.allDistinctBy(selector: (Int) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14568)

如果对数组中的元素应用给定的 `selector` 函数产生的全部值彼此不同,则返回 `true`。

返回`true`的空数组。

`selector` 值是使用结构平等( `==` )进行比较的,一旦发现 `false` 的值重复值,该操作将返回 `false` 。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本. 生成. all distinctIntAraySamples. 全部 DistinctBy 样本

### 5. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> LongArray.allDistinctBy(selector: (Long) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14593)

如果对数组中的元素应用给定的 `selector` 函数产生的全部值彼此不同,则返回 `true`。

返回`true`的空数组。

`selector` 值是使用结构平等( `==` )进行比较的,一旦发现 `false` 的值重复值,该操作将返回 `false` 。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本, 生成. all distinctLong 光束样本, 全部 DistinctBy

### 6. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> FloatArray.allDistinctBy(selector: (Float) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14618)

如果对数组中的元素应用给定的 `selector` 函数产生的全部值彼此不同,则返回 `true`。

返回`true`的空数组。

`selector` 值是使用结构平等( `==` )进行比较的,一旦发现 `false` 的值重复值,该操作将返回 `false` 。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本。 生成的样本。 全部 DistinctFloatArray 样本。 全部 DistinctBy

### 7. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> DoubleArray.allDistinctBy(selector: (Double) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14643)

如果对数组中的元素应用给定的 `selector` 函数产生的全部值彼此不同,则返回 `true`。

返回`true`的空数组。

`selector` 值是使用结构平等( `==` )进行比较的,一旦发现 `false` 的值重复值,该操作将返回 `false` 。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本. 生成. all distinctDouble Array 样本.all distinctBy

### 8. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> BooleanArray.allDistinctBy(selector: (Boolean) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14668)

如果对数组中的元素应用给定的 `selector` 函数产生的全部值彼此不同,则返回 `true`。

返回`true`的空数组。

`selector` 值是使用结构平等( `==` )进行比较的,一旦发现 `false` 的值重复值,该操作将返回 `false` 。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本, 生成的样本, 全部。 All distinctBoolean Array 样本, 全部 DistinctBy

### 9. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <K> CharArray.allDistinctBy(selector: (Char) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L14693)

如果对数组中的元素应用给定的 `selector` 函数产生的全部值彼此不同,则返回 `true`。

返回`true`的空数组。

`selector` 值是使用结构平等( `==` )进行比较的,一旦发现 `false` 的值重复值,该操作将返回 `false` 。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本, 生成的样本。 All DistinctCharAraySamples, all distinctBy 全部 DistinctBy 样本

### 10. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
public inline fun <T, K> Iterable<T>.allDistinctBy(selector: (T) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1979)

如果对收藏元素应用给定的 `selector` 函数产生的全部数值彼此不同,则返回 `true`。

空收藏返回`true`。

`selector` 值是使用结构平等( `==` )进行比较的,一旦发现 `false` 的值重复值,该操作将返回 `false` 。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本, 生成的样本, 全部。 所有 DistinciterablesSamples, 全部 DistinctBy 样本 。

### 11. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public inline fun <K> UIntArray.allDistinctBy(selector: (UInt) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6139)

如果对数组中的元素应用给定的 `selector` 函数产生的全部值彼此不同,则返回 `true`。

返回`true`的空数组。

`selector` 值是使用结构平等( `==` )进行比较的,一旦发现 `false` 的值重复值,该操作将返回 `false` 。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本。 生成的样本。 全部 DistinctUint Array 样本。 全部 DistinctBy

### 12. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public inline fun <K> ULongArray.allDistinctBy(selector: (ULong) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6165)

如果对数组中的元素应用给定的 `selector` 函数产生的全部值彼此不同,则返回 `true`。

返回`true`的空数组。

`selector` 值是使用结构平等( `==` )进行比较的,一旦发现 `false` 的值重复值,该操作将返回 `false` 。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本, 生成. all distinctULong 光束样本。 全部 DistinctBy

### 13. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public inline fun <K> UByteArray.allDistinctBy(selector: (UByte) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6191)

如果对数组中的元素应用给定的 `selector` 函数产生的全部值彼此不同,则返回 `true`。

返回`true`的空数组。

`selector` 值是使用结构平等( `==` )进行比较的,一旦发现 `false` 的值重复值,该操作将返回 `false` 。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本, 生成的样本, 全部。 All distinctUByte ArraySamples. all distinctBy

### 14. Common

```kotlin
@SinceKotlin("2.4")
@ExperimentalStdlibApi
@ExperimentalUnsignedTypes
public inline fun <K> UShortArray.allDistinctBy(selector: (UShort) -> K): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L6217)

如果对数组中的元素应用给定的 `selector` 函数产生的全部值彼此不同,则返回 `true`。

返回`true`的空数组。

`selector` 值是使用结构平等( `==` )进行比较的,一旦发现 `false` 的值重复值,该操作将返回 `false` 。

对于浮点类型(`Double`,`Float`)的选取值,`NaN` 的值为`NaN`,而`-0.0`的值不等于`0.0`,与`Double.equals`和`Float.equals`一致。

@sample 样本, 生成的样本, 全部。 All distinctUShort AraySamples, all distinctBy

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(arrayOf<String>().allDistinctBy { it.length })
    println(arrayOf("apple").allDistinctBy { it.length })

    val values = arrayOf("apple", "mango", "peach")
    println(values.allDistinctBy { it.length })
    println(values.allDistinctBy { it })
}
```

```text title="输出"
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctArraySamples.kt#L30)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(byteArrayOf().allDistinctBy { it * it })
    println(byteArrayOf(1).allDistinctBy { it * it })

    val values = byteArrayOf(1, -1, 2)
    println(values.allDistinctBy { it * it })
    println(values.allDistinctBy { it })
}
```

```text title="输出"
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctByteArraySamples.kt#L30)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(shortArrayOf().allDistinctBy { it * it })
    println(shortArrayOf(1).allDistinctBy { it * it })

    val values = shortArrayOf(1, -1, 2)
    println(values.allDistinctBy { it * it })
    println(values.allDistinctBy { it })
}
```

```text title="输出"
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctShortArraySamples.kt#L30)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(intArrayOf().allDistinctBy { it * it })
    println(intArrayOf(1).allDistinctBy { it * it })

    val values = intArrayOf(1, -1, 2)
    println(values.allDistinctBy { it * it })
    println(values.allDistinctBy { it })
}
```

```text title="输出"
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctIntArraySamples.kt#L30)

### 示例 5 · JVM

```kotlin title="示例 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(longArrayOf().allDistinctBy { it * it })
    println(longArrayOf(1L).allDistinctBy { it * it })

    val values = longArrayOf(1L, -1L, 2L)
    println(values.allDistinctBy { it * it })
    println(values.allDistinctBy { it })
}
```

```text title="输出"
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctLongArraySamples.kt#L30)

### 示例 6 · JVM

```kotlin title="示例 6" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(floatArrayOf().allDistinctBy { it * it })
    println(floatArrayOf(1.0f).allDistinctBy { it * it })

    val values = floatArrayOf(1.0f, -1.0f, 2.0f)
    println(values.allDistinctBy { it * it })
    println(values.allDistinctBy { it })
}
```

```text title="输出"
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctFloatArraySamples.kt#L33)

### 示例 7 · JVM

```kotlin title="示例 7" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(doubleArrayOf().allDistinctBy { it * it })
    println(doubleArrayOf(1.0).allDistinctBy { it * it })

    val values = doubleArrayOf(1.0, -1.0, 2.0)
    println(values.allDistinctBy { it * it })
    println(values.allDistinctBy { it })
}
```

```text title="输出"
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctDoubleArraySamples.kt#L33)

### 示例 8 · JVM

```kotlin title="示例 8" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(booleanArrayOf().allDistinctBy { if (it) 1 else 0 })
    println(booleanArrayOf(true).allDistinctBy { if (it) 1 else 0 })

    val values = booleanArrayOf(true, false)
    println(values.allDistinctBy { if (it) 1 else 0 })
    println(values.allDistinctBy { 0 })
}
```

```text title="输出"
true
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctBooleanArraySamples.kt#L30)

### 示例 9 · JVM

```kotlin title="示例 9" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(charArrayOf().allDistinctBy { it.uppercaseChar() })
    println(charArrayOf('a').allDistinctBy { it.uppercaseChar() })

    val values = charArrayOf('a', 'A', 'b')
    println(values.allDistinctBy { it.uppercaseChar() })
    println(values.allDistinctBy { it })
}
```

```text title="输出"
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctCharArraySamples.kt#L30)

### 示例 10 · JVM

```kotlin title="示例 10" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(listOf<String>().allDistinctBy { it.length })
    println(listOf("apple").allDistinctBy { it.length })

    val values = listOf("apple", "mango", "peach")
    println(values.allDistinctBy { it.length })
    println(values.allDistinctBy { it })
}
```

```text title="输出"
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctIterablesSamples.kt#L30)

### 示例 11 · JVM

```kotlin title="示例 11" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(uintArrayOf().allDistinctBy { it % 2u })
    println(uintArrayOf(1u).allDistinctBy { it % 2u })

    val values = uintArrayOf(1u, 3u, 2u)
    println(values.allDistinctBy { it % 2u })
    println(values.allDistinctBy { it })
}
```

```text title="输出"
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctUIntArraySamples.kt#L30)

### 示例 12 · JVM

```kotlin title="示例 12" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ulongArrayOf().allDistinctBy { it % 2uL })
    println(ulongArrayOf(1uL).allDistinctBy { it % 2uL })

    val values = ulongArrayOf(1uL, 3uL, 2uL)
    println(values.allDistinctBy { it % 2uL })
    println(values.allDistinctBy { it })
}
```

```text title="输出"
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctULongArraySamples.kt#L30)

### 示例 13 · JVM

```kotlin title="示例 13" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ubyteArrayOf().allDistinctBy { it.toUInt() % 2u })
    println(ubyteArrayOf(1u).allDistinctBy { it.toUInt() % 2u })

    val values = ubyteArrayOf(1u, 3u, 2u)
    println(values.allDistinctBy { it.toUInt() % 2u })
    println(values.allDistinctBy { it })
}
```

```text title="输出"
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctUByteArraySamples.kt#L30)

### 示例 14 · JVM

```kotlin title="示例 14" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println(ushortArrayOf().allDistinctBy { it.toUInt() % 2u })
    println(ushortArrayOf(1u).allDistinctBy { it.toUInt() % 2u })

    val values = ushortArrayOf(1u, 3u, 2u)
    println(values.allDistinctBy { it.toUInt() % 2u })
    println(values.allDistinctBy { it })
}
```

```text title="输出"
true
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/generated/alldistinct/AllDistinctUShortArraySamples.kt#L30)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
