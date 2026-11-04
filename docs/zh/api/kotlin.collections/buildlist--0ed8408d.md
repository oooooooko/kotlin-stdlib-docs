# buildList

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

使用给定的 `builderAction` 以`MutableList` 以 `MutableList` 以 以 popping a `MutableList` 并返回含有相同元素的只读列表的方式新建一个只读的 `List` 。

`builderAction` 的接收者名单仅在该函数内有效。在函数之外使用它会产生一种未指明的行为。

退回的名单可序列(JVM) 。

@sample 样本采集 建筑建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑 建筑

??? note "查看英文原文"

    Builds a new read-only `List` by populating a `MutableList` using the given `builderAction`
    and returning a read-only list with the same elements.
    
    The list passed as a receiver to the `builderAction` is valid only inside that function.
    Using it outside of the function produces an unspecified behavior.
    
    The returned list is serializable (JVM).
    
    @sample samples.collections.Builders.Lists.buildListSample

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
@Suppress("LEAKED_IN_PLACE_LAMBDA", "WRONG_INVOCATION_KIND", "DEPRECATION")
public inline fun <E> buildList(@BuilderInference builderAction: MutableList<E>.() -> Unit): List<E>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L172)

### 2. Common

```kotlin
@SinceKotlin("1.6")
@kotlin.internal.InlineOnly
@Suppress("LEAKED_IN_PLACE_LAMBDA", "WRONG_INVOCATION_KIND", "DEPRECATION")
public inline fun <E> buildList(capacity: Int, @BuilderInference builderAction: MutableList<E>.() -> Unit): List<E>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L196)

使用给定的 `builderAction` 以`MutableList` 以 `MutableList` 以 以 popping a `MutableList` 并返回含有相同元素的只读列表的方式新建一个只读的 `List` 。

`builderAction` 的接收者名单仅在该函数内有效。在函数之外使用它会产生一种未指明的行为。

退回的名单可序列(JVM) 。

`capacity` 用于暗示`builderAction`中增加的预期要素数量。

@throws 非法辩护,如果给定的`capacity`为负数,则例外。

@sample 样本采集。 建筑者、 建立数据库数据库

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val x = listOf('b', 'c')

    val y = buildList {
        add('a')
        addAll(x)
        add('d')
    }

    println(y)
}
```

```text title="输出"
[a, b, c, d]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/builders.kt#L8)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val x = listOf('b', 'c')

    val y = buildList(x.size + 2) {
        add('a')
        addAll(x)
        add('d')
    }

    println(y)
}
```

```text title="输出"
[a, b, c, d]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/builders.kt#L21)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
