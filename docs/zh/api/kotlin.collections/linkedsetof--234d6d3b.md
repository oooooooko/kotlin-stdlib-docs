# linkedSetOf

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回空的新 `LinkedHashSet`。
@sample 样本、 采集、 收集、 收藏、 配置、 空链接的哈什塞特

??? note "查看英文原文"

    Returns an empty new `LinkedHashSet`.
    @sample samples.collections.Collections.Sets.emptyLinkedHashSet

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public inline fun <T> linkedSetOf(): LinkedHashSet<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sets.kt#L88)

### 2. Common

```kotlin
public fun <T> linkedSetOf(vararg elements: T): LinkedHashSet<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sets.kt#L96)

返回新的`LinkedHashSet` , 并包含给定元素。 集的元素按指定顺序迭代。 @sample 样本. collects. Sets. leteldHashSet

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val set: LinkedHashSet<Int> = linkedSetOf<Int>()

    set.add(1)
    set.add(3)
    set.add(2)

    println(set)
}
```

```text title="输出"
[1, 3, 2]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L641)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val set: LinkedHashSet<Int> = linkedSetOf(1, 3, 2)

    println(set)

    set.remove(3)
    set += listOf(5, 4)
    println(set)
}
```

```text title="输出"
[1, 3, 2]
[1, 2, 5, 4]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L652)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
