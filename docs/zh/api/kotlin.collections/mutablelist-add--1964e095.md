# MutableList.add

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将指定元素添加到此列表的结尾。

@return `true` ,因为这一行动总是对清单进行修改。

@sample 样本 采集 采集 采集 列表 添加

??? note "查看英文原文"

    Adds the specified element to the end of this list.
    
    @return `true` because the list is always modified as the result of this operation.
    
    @sample samples.collections.Collections.Lists.add

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
    override fun add(element: E): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L315)

### 2. Common

```kotlin
public fun add(index: Int, element: E): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L379)

在指定的 `index` 的列表中插入元素。

指数为`index .. index + size - 1`的所有元素都移动了1个位置右转。

如果`index`等于 `size` ,`element`将附于本清单。

@throws 指数外溢值,如果`index`低于本清单的零或`size`以上,则除外。

@sample 样本、采集的样本、采集的样本、清单、添加的样本

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = mutableListOf('a', 'b', 'c')
    println(list.add('c'))
    println(list)
}
```

```text title="输出"
true
[a, b, c, c]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L334)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val list = mutableListOf('a', 'b', 'c')

    list.add(1, 'c')
    println(list)

    list.add(4, 'a')
    println(list)

    assertFailsWith<IndexOutOfBoundsException> { list.add(100500, 'a') }
}
```

```text title="输出"
[a, c, b, c]
[a, c, b, c, a]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L341)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
