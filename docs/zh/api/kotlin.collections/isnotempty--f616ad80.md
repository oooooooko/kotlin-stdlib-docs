# isNotEmpty

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果数组不是空的,则返回 `true` 。

??? note "查看英文原文"

    Returns `true` if the array is not empty.

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Array<out T>.isNotEmpty(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9414)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun ByteArray.isNotEmpty(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9422)

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun ShortArray.isNotEmpty(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9430)

### 4. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun IntArray.isNotEmpty(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9438)

### 5. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun LongArray.isNotEmpty(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9446)

### 6. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun FloatArray.isNotEmpty(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9454)

### 7. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun DoubleArray.isNotEmpty(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9462)

### 8. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun BooleanArray.isNotEmpty(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9470)

### 9. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharArray.isNotEmpty(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L9478)

### 10. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Collection<T>.isNotEmpty(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L239)

如果收藏不是空的, 返回 `true`。 @sample 样本. collects. collects. collections. collectinations. collecties notEmpty 。 收藏不是空的, 返回 `true`。

### 11. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <K, V> Map<out K, V>.isNotEmpty(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L199)

如果地图不是空的, 返回 `true` 。 @sample 样本. collects.maps. Usage. mapIs notEmpty

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val empty = emptyList<Any>()
    println(empty.isNotEmpty())

    val collection = listOf('a', 'b', 'c')
    println(collection.isNotEmpty())
}
```

```text title="输出"
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L26)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
