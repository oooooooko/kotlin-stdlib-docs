# Iterable

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

从此界面继承的分类可以作为一系列元素来表示,这些元素可以迭代 。 @param T 是循环的元素类型。迭代器在元素类型中是共变量 。

??? note "查看英文原文"

    Classes that inherit from this interface can be represented as a sequence of elements that can
    be iterated over.
    @param T the type of element being iterated over. The iterator is covariant in its element type.

## 声明与重载

### 1. Common

```kotlin
public expect interface Iterable<out T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L9)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <T> Iterable(crossinline iterator: () -> Iterator<T>): Iterable<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Iterables.kt#L10)

给 `iterator` 函数, `iterator` 函数构建了 `Iterable` 实例, 返回值通过该函数提供的 `Iterator` 。 @sample 样本. collects. itables. building. sublication.

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val iterable = Iterable {
        iterator {
            yield(42)
            yieldAll(1..5 step 2)
        }
    }
    val result = iterable.mapIndexed { index, value -> "$index: $value" }
    println(result)

    // can be iterated many times
    repeat(2) {
        val sum = iterable.sum()
        println(sum)
    }
}
```

```text title="输出"
[0: 42, 1: 1, 2: 3, 3: 5]
51
51
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/iterables.kt#L26)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
