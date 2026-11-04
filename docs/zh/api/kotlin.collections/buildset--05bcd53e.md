# buildSet

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

使用给定的 `builderAction` 以`MutableSet` 以 `MutableSet` 以 popping a `MutableSet` 并返回含有相同元素的只读集, 构建新的只读 `Set` 。

被作为接收器传送到 `builderAction` 的集仅在该函数内有效。使用该集合在函数之外产生一种未指明的行为。

这套材料的成分按`builderAction`号新增加的顺序重新迭代。

返回的成套设备可序列(JVM) 。

@sample 样本采集 建筑建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑

??? note "查看英文原文"

    Builds a new read-only `Set` by populating a `MutableSet` using the given `builderAction`
    and returning a read-only set with the same elements.
    
    The set passed as a receiver to the `builderAction` is valid only inside that function.
    Using it outside of the function produces an unspecified behavior.
    
    Elements of the set are iterated in the order they were added by the `builderAction`.
    
    The returned set is serializable (JVM).
    
    @sample samples.collections.Builders.Sets.buildSetSample

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
@Suppress("LEAKED_IN_PLACE_LAMBDA", "WRONG_INVOCATION_KIND", "DEPRECATION")
public inline fun <E> buildSet(@BuilderInference builderAction: MutableSet<E>.() -> Unit): Set<E>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sets.kt#L122)

### 2. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
@Suppress("LEAKED_IN_PLACE_LAMBDA", "WRONG_INVOCATION_KIND", "DEPRECATION")
public inline fun <E> buildSet(capacity: Int, @BuilderInference builderAction: MutableSet<E>.() -> Unit): Set<E>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Sets.kt#L148)

使用给定的 `builderAction` 以`MutableSet` 以 `MutableSet` 以 popping a `MutableSet` 并返回含有相同元素的只读集, 构建新的只读 `Set` 。

被作为接收器传送到 `builderAction` 的集仅在该函数内有效。使用该集合在函数之外产生一种未指明的行为。

`capacity` 用于暗示`builderAction`中增加的预期要素数量。

这套材料的成分按`builderAction`号新增加的顺序重新迭代。

返回的成套设备可序列(JVM) 。

@throws 非法辩护,如果给定的`capacity`为负数,则例外。

@sample 样本采集。 建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑公司、建筑

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val x = setOf('a', 'b')

    val y = buildSet {
        add('b')
        addAll(x)
        add('c')
    }

    println(y)
}
```

```text title="输出"
[b, a, c]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/builders.kt#L36)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val x = setOf('a', 'b')

    val y = buildSet(x.size + 2) {
        add('b')
        addAll(x)
        add('c')
    }

    println(y)
}
```

```text title="输出"
[b, a, c]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/builders.kt#L49)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
