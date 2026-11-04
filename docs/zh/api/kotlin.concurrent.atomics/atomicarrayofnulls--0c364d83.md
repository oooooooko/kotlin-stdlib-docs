# atomicArrayOfNulls

`kotlin.concurrent.atomics` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回给定的 `size` 的`AtomicArray` 中新的`AtomicArray`, 初始化为无效值。

@throws 运行时间例外,如果指定的 `size` 是负值 。

@sample 样本. 共流. 原子学. 原子阵列. 核分析

??? note "查看英文原文"

    Returns a new `AtomicArray` of the given type with the given `size`, initialized with null values.
    
    @throws RuntimeException if the specified `size` is negative.
    
    @sample samples.concurrent.atomics.AtomicArray.nullFactory

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.2")
@ExperimentalAtomicApi
@Suppress("NOTHING_TO_INLINE")
public inline fun <reified T> atomicArrayOfNulls(size: Int): AtomicArray<T?>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L669)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.atomics.AtomicArray
import kotlin.test.assertFailsWith



fun main() {
    val array = atomicArrayOfNulls<String>(3)
    println(array.toString())

    println(atomicArrayOfNulls<String>(0).toString())

    // Size should be non-negative
    assertFailsWith<RuntimeException> { atomicArrayOfNulls<String>(-1) }
}
```

```text title="输出"
[null, null, null]
[]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomicArrays.kt#L353)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
