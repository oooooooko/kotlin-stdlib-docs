# isNullOrEmpty

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果此无效数组为空或空, 返回 `true`。 @sample 样本. cools. Arrays. Usage. alaryIsNullEmpty 。

??? note "查看英文原文"

    Returns `true` if this nullable array is either null or empty.
    @sample samples.collections.Arrays.Usage.arrayIsNullOrEmpty

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
@kotlin.internal.InlineOnly
public inline fun Array<*>?.isNullOrEmpty(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Arrays.kt#L53)

### 2. Common

```kotlin
@SinceKotlin("1.3")
@kotlin.internal.InlineOnly
public inline fun <T> Collection<T>?.isNullOrEmpty(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L246)

如果此无效收藏为空或空, 返回 `true` 。 @sample 样本. collects. collectives. collectives. collects. collorEmpty 。 collectIsNullOrmpty 收藏

### 3. Common

```kotlin
@SinceKotlin("1.3")
@kotlin.internal.InlineOnly
public inline fun <K, V> Map<out K, V>?.isNullOrEmpty(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L206)

如果此无效地图为空或空, 返回 `true` 。 @sample 样本. cools.maps. Usage.mapIsNullEmpty

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val nullList: List<Any>? = null
    println(nullList.isNullOrEmpty())

    val empty: List<Any>? = emptyList<Any>()
    println(empty.isNullOrEmpty())

    val collection: List<Char>? = listOf('a', 'b', 'c')
    println(collection.isNullOrEmpty())
}
```

```text title="输出"
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L44)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
