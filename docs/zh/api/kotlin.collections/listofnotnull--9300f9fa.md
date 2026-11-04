# listOfNotNull

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个新的只读列表, 单元素的列表, 如果不是空的, 则返回空列表, 如果元素是空的, 返回列表是可序列的( JVM) 。 @sample 样本. collects. collections. list. listofnotNull

??? note "查看英文原文"

    Returns a new read-only list either of single given element, if it is not null, or empty list if the element is null. The returned list is serializable (JVM).
    @sample samples.collections.Collections.Lists.listOfNotNull

## 声明与重载

### 1. Common

```kotlin
public fun <T : Any> listOfNotNull(element: T?): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L130)

### 2. Common

```kotlin
public fun <T : Any> listOfNotNull(vararg elements: T?): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Collections.kt#L136)

返回仅对给定元素的新的只读列表, 这些元素并非无效。 返回列表是可序列的( JVM) 。 @sample 样本. collects. collections. list. listOfnotNull

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val empty = listOfNotNull<Any>(null)
    println(empty)

    val singleton = listOfNotNull(42)
    println(singleton)

    val list = listOfNotNull(1, null, 2, null, 3)
    println(list)
}
```

```text title="输出"
[]
[42]
[1, 2, 3]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L215)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
