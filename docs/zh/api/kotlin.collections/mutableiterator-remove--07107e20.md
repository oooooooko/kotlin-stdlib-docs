# MutableIterator.remove

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

从底部收藏中删除此迭代器返回的最后元素 。

@throws 非法居留除外,如果尚未拨打 `next` ,或者最近拨打`next`,或者随后又打了`remove`。

??? note "查看英文原文"

    Removes from the underlying collection the last element returned by this iterator.
    
    @throws IllegalStateException if `next` has not been called yet,
    or the most recent `next` call has already been followed by a `remove` call.

## 声明与重载

### 1. Common

```kotlin
public fun remove(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Iterator.kt#L32)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*

val TEST_LIST = arrayOf(2, 0, 9, 7, 1).toList()

private fun <T> snapshotDoesNotCreateView(array: Array<T>, snapshot: (Array<T>) -> List<T>) {
        val first = array.first()
        val last = array.last()

        val list = snapshot(array)
        println(list[0])
        array[0] = last
        println(list[0])
    }

fun main() {

        val a = mutableListOf(1, 2, 3)
        val it = a.iterator()
        assertFailsWith<IllegalStateException> { it.remove() }
    
}
```

```text title="输出"

```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/js/JsCollectionsTest.kt#L76)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
