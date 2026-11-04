# unzip

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一对列表,其中 * 1* 列表是从此数组中每对对的首值中构建的, * 秒* 列表是从此数组中每对的第二值中构建的。 @sample 样本。 收藏。 Arrays. transformations.unzipArray

??? note "查看英文原文"

    Returns a pair of lists, where
    *first* list is built from the first values of each pair from this array,
    *second* list is built from the second values of each pair from this array.
    @sample samples.collections.Arrays.Transformations.unzipArray

## 声明与重载

### 1. Common

```kotlin
public fun <T, R> Array<out Pair<T, R>>.unzip(): Pair<List<T>, List<R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Arrays.kt#L37)

### 2. Common

```kotlin
public fun <T, R> Iterable<Pair<T, R>>.unzip(): Pair<List<T>, List<R>>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Iterables.kt#L54)

返回一对列表,其中 * 1* 列表是从此收藏中每对的首个值中构建的, * 秒* 列表是从此收藏中每对的第二值中构建的。 @sample 样本. collects. iberables. operations. unzipIterable

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf(1 to 'a', 2 to 'b', 3 to 'c')
    println(list.unzip())
}
```

```text title="输出"
([1, 2, 3], [a, b, c])
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/iterables.kt#L54)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
