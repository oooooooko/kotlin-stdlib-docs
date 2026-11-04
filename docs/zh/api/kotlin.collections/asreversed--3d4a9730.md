# asReversed

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回原列表的反向只读视图。原列表中的所有更改将反映在反向的样本中。 @sample 样本。 收藏。 ReveredOcions.asReveredList

??? note "查看英文原文"

    Returns a reversed read-only view of the original List.
    All changes made in the original list will be reflected in the reversed one.
    @sample samples.collections.ReversedViews.asReversedList

## 声明与重载

### 1. Common

```kotlin
public fun <T> List<T>.asReversed(): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/ReversedViews.kt#L72)

### 2. Common

```kotlin
@kotlin.jvm.JvmName("asReversedMutable")
public fun <T> MutableList<T>.asReversed(): MutableList<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/ReversedViews.kt#L79)

返回原变动列表的反向变动视图。原列表中的所有更改将反映在反向列表中,反之亦然。 @sample 样本。 collects.Revered Views.asReversedMutableList

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val original = mutableListOf('a', 'b', 'c', 'd', 'e')
    val originalReadOnly = original as List<Char>
    val reversed = originalReadOnly.asReversed()

    println(original)
    println(reversed)

    // changing the original list affects its reversed view
    original.add('f')
    println(original)
    println(reversed)

    original[original.lastIndex] = 'z'
    println(original)
    println(reversed)
}
```

```text title="输出"
[a, b, c, d, e]
[e, d, c, b, a]
[a, b, c, d, e, f]
[f, e, d, c, b, a]
[a, b, c, d, e, z]
[z, e, d, c, b, a]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/reversedViews.kt#L22)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val original = mutableListOf(1, 2, 3, 4, 5)
    val reversed = original.asReversed()

    println(original)
    println(reversed)

    // changing the reversed view affects the original list
    reversed.add(0)
    println(original)
    println(reversed)

    // changing the original list affects its reversed view
    original[2] = -original[2]
    println(original)
    println(reversed)
}
```

```text title="输出"
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
[0, 1, 2, 3, 4, 5]
[5, 4, 3, 2, 1, 0]
[0, 1, -2, 3, 4, 5]
[5, 4, 3, -2, 1, 0]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/reversedViews.kt#L41)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
