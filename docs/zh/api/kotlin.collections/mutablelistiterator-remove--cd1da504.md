# MutableListIterator.remove

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

从底部收藏中删除此迭代器返回的最后元素 。

@throws 非法居留除外,如果尚未拨打 `next` 或 `previous` ,或者最近的 `next` 或`previous`呼叫后,又打了 `remove` 或`add`。

??? note "查看英文原文"

    Removes from the underlying collection the last element returned by this iterator.
    
    @throws IllegalStateException if neither `next` nor `previous` has not been called yet,
    or the most recent `next` or `previous` call has already been followed by a `remove` or `add` call.

## 声明与重载

### 1. Common

```kotlin
override fun remove(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Iterator.kt#L88)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() {
    val values = mutableListOf(1, 2, 3)
    val iterator = values.listIterator()
    println(iterator.next())
    iterator.remove()
    println(values)
}
```

```text title="输出"
1
[2, 3]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
