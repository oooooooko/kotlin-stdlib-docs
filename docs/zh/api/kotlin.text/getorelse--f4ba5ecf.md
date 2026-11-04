# getOrElse

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回给定 `index` 的字符,如果 `index` 超出此字符序列的界限,则返回调用 `defaultValue` 函数的结果。

@sample 样本,采集的样本, 收集的样本, 元素, 元素, 开发的 Orelse

??? note "查看英文原文"

    Returns a character at the given `index` or the result of calling the `defaultValue` function if the `index` is out of bounds of this char sequence.
    
    @sample samples.collections.Collections.Elements.getOrElse

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun CharSequence.getOrElse(index: Int, defaultValue: (Int) -> Char): Char
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L135)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val list = listOf(1, 2, 3)
    println(list.getOrElse(0) { 42 })
    println(list.getOrElse(2) { 42 })
    println(list.getOrElse(3) { 42 })
    println(list.getOrElse(-1) { 42 })

    val emptyList = emptyList<Int>()
    println(emptyList.getOrElse(0) { "no int" })
}
```

```text title="输出"
1
3
42
42
no int
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1345)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
