# MutableList.set

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将本列表中指定位置的元素替换为指定元素。

@return 元素先前的位置 。

@throws 指数外溢值,如果`index`低于或大于或等于该清单中的`size`,则除外。

@sample 样本,采集的样本, 收集的样本, 列表, 集集

??? note "查看英文原文"

    Replaces the element at the specified position in this list with the specified element.
    
    @return the element previously at the specified position.
    
    @throws IndexOutOfBoundsException if `index` is less than zero or greater than or equal to `size` of this list.
    
    @sample samples.collections.Collections.Lists.set

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
    public operator fun set(index: Int, element: E): E
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L367)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val list = mutableListOf(1, 2, 3)

    list[1] = 42
    println(list)

    assertFailsWith<IndexOutOfBoundsException> { list[4] = 4 }
}
```

```text title="输出"
[1, 42, 3]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L420)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
