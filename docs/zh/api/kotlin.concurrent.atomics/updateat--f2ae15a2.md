# updateAt

`kotlin.concurrent.atomics` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

使用 `transform` 函数在给定指数上更新这个`AtomicIntArray`元素的原子值。

重新计算结果可以不止一次援引`transform`,例如,当同时更新特定指数的整数值,同时适用`transform`,或者由于虚假的比较和假设失败,结果可能发生,后者是具体执行的,不应依赖。

在不支持多行平台(JS和Wam)上,这项操作的执行微不足道, `transform` 号将被精确援引一次。

推荐保持 `transform` 的快速 并且没有副作用

@throws 索引外观,但 `index` 超出此数组界限的除外。

@sample 样本. 共流. 原子学. 原子内皮电图阵列. 更新

??? note "查看英文原文"

    Atomically updates the element of this `AtomicIntArray` at the given index using the `transform` function.
    
    `transform` may be invoked more than once to recompute a result.
    That may happen, for example,
    when an integer value at the specified index was concurrently updated while `transform` was applied,
    or due to a spurious compare-and-set failure.
    The latter is implementation-specific, and it should not be relied upon.
    
    On platforms that do no support multi-threading (JS and Wasm), this operation has a trivial implementation
    and `transform` will be invoked exactly once.
    
    It's recommended to keep `transform` fast and free of side effects.
    
    @throws IndexOutOfBoundsException if the `index` is out of bounds of this array.
    
    @sample samples.concurrent.atomics.AtomicIntArray.updateAt

## 声明与重载

### 1. Common

```kotlin
@Suppress("EXPECTED_DECLARATION_WITH_BODY", "WRONG_INVOCATION_KIND")
@SinceKotlin("2.2")
@ExperimentalAtomicApi
@InlineOnly
public expect inline fun AtomicIntArray.updateAt(index: Int, transform: (Int) -> Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L195)

### 2. Common

```kotlin
@Suppress("EXPECTED_DECLARATION_WITH_BODY", "WRONG_INVOCATION_KIND")
@SinceKotlin("2.2")
@ExperimentalAtomicApi
@InlineOnly
public expect inline fun AtomicLongArray.updateAt(index: Int, transform: (Long) -> Long): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L464)

使用 `transform` 函数在给定指数上更新这个`AtomicLongArray`元素的原子值。

重新计算结果可以不止一次援引`transform`,例如,当同时更新特定指数的长值,同时适用`transform`,或者由于虚假的比较和假设的失败,结果可能发生,后者是具体执行的,不应依赖。

在不支持多行平台(JS和Wam)上,这项操作的执行微不足道, `transform` 号将被精确援引一次。

推荐保持 `transform` 的快速 并且没有副作用

@throws 索引外观,但 `index` 超出此数组界限的除外。

@sample 样本. 共流. 原子学. 原子学. 原子麦克隆阵列. 更新

### 3. Common

```kotlin
@Suppress("EXPECTED_DECLARATION_WITH_BODY", "WRONG_INVOCATION_KIND")
@SinceKotlin("2.2")
@ExperimentalAtomicApi
@InlineOnly
public expect inline fun <T> AtomicArray<T>.updateAt(index: Int, transform: (T) -> T): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L681)

使用 `transform` 函数在给定指数上更新这个`AtomicArray`元素的原子值。

重新计算结果可以不止一次援引`transform`,例如,当在适用`transform`时同时更新了特定指数的参考时,或者由于虚假的比较和假设的失败,这种情况可能发生,后者是具体执行的,不应依赖。

在不支持多行平台(JS和Wam)上,这项操作的执行微不足道, `transform` 号将被精确援引一次。

推荐保持 `transform` 的快速 并且没有副作用

@throws 索引外观,但 `index` 超出此数组界限的除外。

@sample 样本. 共流. 原子学. 原子阵列. 更新

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.atomics.AtomicArray
import kotlin.test.assertFailsWith



fun main() {
    val a = AtomicIntArray(intArrayOf(1, 2, 3))
    a.updateAt(1) { currentValue -> currentValue * 10 }
    println(a.toString())

    // The index is out of array bounds
    assertFailsWith<IndexOutOfBoundsException> { a.updateAt(10) { it } }
}
```

```text title="输出"
[1, 20, 3]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomicArrays.kt#L141)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.atomics.AtomicArray
import kotlin.test.assertFailsWith



fun main() {
    val a = AtomicLongArray(longArrayOf(1L, 2L, 3L))
    a.updateAt(1) { currentValue -> currentValue * 10L }
    println(a.toString())

    // The index is out of array bounds
    assertFailsWith<IndexOutOfBoundsException> { a.updateAt(10) { it } }
}
```

```text title="输出"
[1, 20, 3]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomicArrays.kt#L303)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.atomics.AtomicArray
import kotlin.test.assertFailsWith



fun main() {
    val a = AtomicArray(arrayOf("hello", "concurrent", "world"))
    a.updateAt(1) { currentValue -> currentValue.uppercase() }
    println(a.toString())

    // The index is out of array bounds
    assertFailsWith<IndexOutOfBoundsException> { a.updateAt(10) { it } }
}
```

```text title="输出"
[hello, CONCURRENT, world]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomicArrays.kt#L423)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
