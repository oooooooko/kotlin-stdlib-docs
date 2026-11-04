# MutableListIterator.set

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将以`next`或`previous`返回的最后一个元素替换为指定的元素`element`。

@throws 非法居留除外,如果尚未拨打 `next` 或 `previous` ,或者最近的 `next` 或`previous`呼叫后,又打了 `remove` 或`add`。

??? note "查看英文原文"

    Replaces the last element returned by `next` or `previous` with the specified element `element`.
    
    @throws IllegalStateException if neither `next` nor `previous` has not been called yet,
    or the most recent `next` or `previous` call has already been followed by a `remove` or `add` call.

## 声明与重载

### 1. Common

```kotlin
public fun set(element: T): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Iterator.kt#L96)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*

private fun Iterator<*>.seekEnd() {
    while (hasNext()) {
        next()
    }
}

fun main() {

        val original = mutableListOf(2, 3, 4)
        val iter = original.asReversed().listIterator()

        while (iter.hasNext()) {
            val v = iter.next()
            iter.set(v * v)
        }

        println(original)
    
}
```

```text title="输出"
[4, 9, 16]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/ReversedViewsTest.kt#L256)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
