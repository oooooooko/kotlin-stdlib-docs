# slice

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回包含在指定的`indices`范围内指数要素的列表。

??? note "查看英文原文"

    Returns a list containing elements at indices in the specified `indices` range.

## 声明与重载

### 1. Common

```kotlin
public fun <T> Array<out T>.slice(indices: IntRange): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4566)

### 2. Common

```kotlin
public fun ByteArray.slice(indices: IntRange): List<Byte>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4574)

### 3. Common

```kotlin
public fun ShortArray.slice(indices: IntRange): List<Short>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4582)

### 4. Common

```kotlin
public fun IntArray.slice(indices: IntRange): List<Int>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4590)

### 5. Common

```kotlin
public fun LongArray.slice(indices: IntRange): List<Long>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4598)

### 6. Common

```kotlin
public fun FloatArray.slice(indices: IntRange): List<Float>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4606)

### 7. Common

```kotlin
public fun DoubleArray.slice(indices: IntRange): List<Double>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4614)

### 8. Common

```kotlin
public fun BooleanArray.slice(indices: IntRange): List<Boolean>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4622)

### 9. Common

```kotlin
public fun CharArray.slice(indices: IntRange): List<Char>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4630)

### 10. Common

```kotlin
public fun <T> Array<out T>.slice(indices: Iterable<Int>): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4638)

返回包含指定`indices`元素的列表 。

### 11. Common

```kotlin
public fun ByteArray.slice(indices: Iterable<Int>): List<Byte>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4651)

返回包含指定`indices`元素的列表 。

### 12. Common

```kotlin
public fun ShortArray.slice(indices: Iterable<Int>): List<Short>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4664)

返回包含指定`indices`元素的列表 。

### 13. Common

```kotlin
public fun IntArray.slice(indices: Iterable<Int>): List<Int>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4677)

返回包含指定`indices`元素的列表 。

### 14. Common

```kotlin
public fun LongArray.slice(indices: Iterable<Int>): List<Long>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4690)

返回包含指定`indices`元素的列表 。

### 15. Common

```kotlin
public fun FloatArray.slice(indices: Iterable<Int>): List<Float>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4703)

返回包含指定`indices`元素的列表 。

### 16. Common

```kotlin
public fun DoubleArray.slice(indices: Iterable<Int>): List<Double>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4716)

返回包含指定`indices`元素的列表 。

### 17. Common

```kotlin
public fun BooleanArray.slice(indices: Iterable<Int>): List<Boolean>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4729)

返回包含指定`indices`元素的列表 。

### 18. Common

```kotlin
public fun CharArray.slice(indices: Iterable<Int>): List<Char>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4742)

返回包含指定`indices`元素的列表 。

### 19. Common

```kotlin
public fun <T> List<T>.slice(indices: IntRange): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L877)

### 20. Common

```kotlin
public fun <T> List<T>.slice(indices: Iterable<Int>): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L885)

返回包含指定`indices`元素的列表 。

### 21. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.slice(indices: IntRange): List<UInt>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2263)

### 22. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.slice(indices: IntRange): List<ULong>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2273)

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.slice(indices: IntRange): List<UByte>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2283)

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.slice(indices: IntRange): List<UShort>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2293)

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.slice(indices: Iterable<Int>): List<UInt>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2303)

返回包含指定`indices`元素的列表 。

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.slice(indices: Iterable<Int>): List<ULong>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2318)

返回包含指定`indices`元素的列表 。

### 27. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.slice(indices: Iterable<Int>): List<UByte>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2333)

返回包含指定`indices`元素的列表 。

### 28. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.slice(indices: Iterable<Int>): List<UShort>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2348)

返回包含指定`indices`元素的列表 。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*

val data = listOf("foo", "bar")

val empty = listOf<String>()

fun main() {

        val list = listOf('A', 'B', 'C', 'D')

        println(list.slice(IntRange.EMPTY))

        // ABCD
        // 0123
        println(list.slice(1..3))
        println(list.slice(3 downTo 1))

        val iter = listOf(2, 0, 3)
        println(list.slice(iter))

        for (range in listOf(-1 until 0, 0 until 2, 2..2)) {
            val bounds = "range: $range"
            val exClass = IndexOutOfBoundsException::class
            assertFailsWith(exClass, bounds) { listOf("x").slice(range) }
            assertFailsWith(exClass, bounds) { listOf("x").slice(range.asIterable()) }
        }
    
}
```

```text title="输出"
[]
[B, C, D]
[D, C, B]
[C, A, D]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/ListSpecificTest.kt#L26)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
