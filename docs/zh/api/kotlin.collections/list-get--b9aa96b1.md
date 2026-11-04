# List.get

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回列表中指定索引中的元素。

@throws 指数外溢值,如果`index`低于或大于或等于该清单中的`size`,则除外。

@sample 样本 采集 采集 列表 开始

??? note "查看英文原文"

    Returns the element at the specified index in the list.
    
    @throws IndexOutOfBoundsException if `index` is less than zero or greater than or equal to `size` of this list.
    
    @sample samples.collections.Collections.Lists.get

## 声明与重载

### 1. Common

```kotlin
public operator fun get(index: Int): E
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L230)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val list = listOf(1, 2, 3)

    println(list[0])
    println(list[2])
    assertFailsWith<IndexOutOfBoundsException> { list[3] }
}
```

```text title="输出"
1
3
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L411)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
