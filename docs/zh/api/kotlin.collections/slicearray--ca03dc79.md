# sliceArray

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回包含此数组元素的数组, 以指定的 `indices` 值返回 。

??? note "查看英文原文"

    Returns an array containing elements of this array at specified `indices`.

## 声明与重载

### 1. Common

```kotlin
public fun <T> Array<T>.sliceArray(indices: Collection<Int>): Array<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4755)

### 2. Common

```kotlin
public fun ByteArray.sliceArray(indices: Collection<Int>): ByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4767)

### 3. Common

```kotlin
public fun ShortArray.sliceArray(indices: Collection<Int>): ShortArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4779)

### 4. Common

```kotlin
public fun IntArray.sliceArray(indices: Collection<Int>): IntArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4791)

### 5. Common

```kotlin
public fun LongArray.sliceArray(indices: Collection<Int>): LongArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4803)

### 6. Common

```kotlin
public fun FloatArray.sliceArray(indices: Collection<Int>): FloatArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4815)

### 7. Common

```kotlin
public fun DoubleArray.sliceArray(indices: Collection<Int>): DoubleArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4827)

### 8. Common

```kotlin
public fun BooleanArray.sliceArray(indices: Collection<Int>): BooleanArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4839)

### 9. Common

```kotlin
public fun CharArray.sliceArray(indices: Collection<Int>): CharArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4851)

### 10. Common

```kotlin
public fun <T> Array<T>.sliceArray(indices: IntRange): Array<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4863)

返回一个包含`indices` 范围内指数元素的数组。

### 11. Common

```kotlin
public fun ByteArray.sliceArray(indices: IntRange): ByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4871)

返回一个包含`indices` 范围内指数元素的数组。

### 12. Common

```kotlin
public fun ShortArray.sliceArray(indices: IntRange): ShortArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4879)

返回一个包含`indices` 范围内指数元素的数组。

### 13. Common

```kotlin
public fun IntArray.sliceArray(indices: IntRange): IntArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4887)

返回一个包含`indices` 范围内指数元素的数组。

### 14. Common

```kotlin
public fun LongArray.sliceArray(indices: IntRange): LongArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4895)

返回一个包含`indices` 范围内指数元素的数组。

### 15. Common

```kotlin
public fun FloatArray.sliceArray(indices: IntRange): FloatArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4903)

返回一个包含`indices` 范围内指数元素的数组。

### 16. Common

```kotlin
public fun DoubleArray.sliceArray(indices: IntRange): DoubleArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4911)

返回一个包含`indices` 范围内指数元素的数组。

### 17. Common

```kotlin
public fun BooleanArray.sliceArray(indices: IntRange): BooleanArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4919)

返回一个包含`indices` 范围内指数元素的数组。

### 18. Common

```kotlin
public fun CharArray.sliceArray(indices: IntRange): CharArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L4927)

返回一个包含`indices` 范围内指数元素的数组。

### 19. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.sliceArray(indices: Collection<Int>): UIntArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2363)

### 20. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.sliceArray(indices: Collection<Int>): ULongArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2372)

### 21. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.sliceArray(indices: Collection<Int>): UByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2381)

### 22. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.sliceArray(indices: Collection<Int>): UShortArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2390)

### 23. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UIntArray.sliceArray(indices: IntRange): UIntArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2399)

返回一个包含`indices` 范围内指数元素的数组。

### 24. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun ULongArray.sliceArray(indices: IntRange): ULongArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2408)

返回一个包含`indices` 范围内指数元素的数组。

### 25. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UByteArray.sliceArray(indices: IntRange): UByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2417)

返回一个包含`indices` 范围内指数元素的数组。

### 26. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun UShortArray.sliceArray(indices: IntRange): UShortArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L2426)

返回一个包含`indices` 范围内指数元素的数组。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.Instant
import kotlin.uuid.*



fun main() {
    val uuid = Uuid.parse("550e8400-e29b-41d4-a716-446655440000")
    val bytes = ByteArray(20)
    val buffer = java.nio.ByteBuffer.wrap(bytes)
    buffer.putUuid(index = 2, uuid)

    // The written 16 bytes are exactly equal to the uuid bytes
    val writtenBytes = bytes.sliceArray(2..<18)
    println(writtenBytes.contentEquals(uuid.toByteArray()))
}
```

```text title="输出"
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/uuid/uuid.kt#L47)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
