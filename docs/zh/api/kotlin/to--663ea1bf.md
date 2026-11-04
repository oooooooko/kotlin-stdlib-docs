# to

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

创建 `Pair` 型的图普, 并创建 `that` 型的图普。

这样做可以有助于创造 `Map` 字,噪音较少,例如: @sample 样本。 收集。 Maps. 证明. mapfromPairs

??? note "查看英文原文"

    Creates a tuple of type `Pair` from this and `that`.
    
    This can be useful for creating `Map` literals with less noise, for example:
    @sample samples.collections.Maps.Instantiation.mapFromPairs

## 声明与重载

### 1. Common

```kotlin
public infix fun <A, B> A.to(that: B): Pair<A, B>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Tuples.kt#L38)

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
