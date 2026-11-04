# filterIsInstance

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回包含所有元素的序列, 元素为指定类型参数 R 。

操作是 _ 中间线 _ 和 _ 无国籍 。

@sample 样本、采集物、采集物、采集物、采集物、过滤器、过滤器

??? note "查看英文原文"

    Returns a sequence containing all elements that are instances of specified type parameter R.
    
    The operation is _intermediate_ and _stateless_.
    
    @sample samples.collections.Collections.Filtering.filterIsInstance

## 声明与重载

### 1. Common

```kotlin
public inline fun <reified R> Sequence<*>.filterIsInstance(): Sequence<@kotlin.internal.NoInfer R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Sequences.kt#L470)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    open class Animal(val name: String) {
        override fun toString(): String {
            return name
        }
    }
    class Dog(name: String): Animal(name)
    class Cat(name: String): Animal(name)

    val animals: List<Animal> = listOf(Cat("Scratchy"), Dog("Poochie"))
    val cats = animals.filterIsInstance<Cat>()

    println(cats)
}
```

```text title="输出"
[Scratchy]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1630)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
