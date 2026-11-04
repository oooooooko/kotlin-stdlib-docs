# MutableList.removeAt

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

从列表中删除指定 `index` 的元素。

`index`之后的所有元素都移到1个位置

已经删除的元素@return

@throws 指数外溢值,如果`index`低于或大于或等于该清单中的`size`,则除外。

@sample 样本、采集的样本、采集的样本、清单、移动的样本

??? note "查看英文原文"

    Removes an element at the specified `index` from the list.
    
    All elements placed after `index` are shifted 1 position left.
    
    @return the element that has been removed.
    
    @throws IndexOutOfBoundsException if `index` is less than zero or greater than or equal to `size` of this list.
    
    @sample samples.collections.Collections.Lists.removeAt

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
    public fun removeAt(index: Int): E
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L392)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val list = mutableListOf('a', 'b', 'c')

    list.removeAt(1)
    println(list)

    list.removeAt(0)
    println(list)

    assertFailsWith<IndexOutOfBoundsException> { list.removeAt(1) }
}
```

```text title="输出"
[a, c]
[c]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L398)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
