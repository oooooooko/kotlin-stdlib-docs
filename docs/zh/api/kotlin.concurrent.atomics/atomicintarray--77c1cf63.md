# AtomicIntArray

`kotlin.concurrent.atomics` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

一系列元素可以原子更新的内插。

具体平台的具体实施细节:

以原住民后端为目标时, `AtomicIntArray` 储存了 `IntArray` 个元素, 并按原子弹更新了它的内容。 关于原子保障的更多信息,请阅读并写到 : `kotlin.concurrent.Volatile` 。

以JVM为目标时,有 `AtomicIntArray` 例的例子由[java.util.contil.contic.totomic IntegerArray](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/atomic/AtomicIntegerArray.html).)所代表(关于保障不稳定存取的详情和原子更新,参见Java语言规格(17.4记忆模型)。

JS和Wasm `AtomicIntArray`执行得微不足道,而且由于这些平台不支持多行,因此不完全安全。

??? note "查看英文原文"

    An array of ints in which elements may be updated atomically.
    
    Platform-specific implementation details:
    
    When targeting the Native backend, `AtomicIntArray` stores an `IntArray` and atomically updates it's elements.
    For additional details about atomicity guarantees for reads and writes see `kotlin.concurrent.Volatile`.
    
    When targeting the JVM, instances of `AtomicIntArray` are represented by
    [java.util.concurrent.atomic.AtomicIntegerArray](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/atomic/AtomicIntegerArray.html).
    For details about guarantees of volatile accesses and updates of atomics refer to The Java Language Specification (17.4 Memory Model).
    
    For JS and Wasm `AtomicIntArray` is implemented trivially and is not thread-safe since these platforms do not support multi-threading.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.1")
@ExperimentalAtomicApi
public expect class AtomicIntArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L15)

### 2. Common

```kotlin
@SinceKotlin("2.1")
@ExperimentalAtomicApi
public inline fun AtomicIntArray(size: Int, init: (Int) -> Int): AtomicIntArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L136)

在给定的 `size` 中新建`AtomicIntArray`, 初始化每个元素时, 调用给定的 `init` 函数 。

函数 `init` 由第一个数组元素依次对每个数组元素调用。 它应该返回一个数组元素的值, 并给定其索引 。

@throws 运行时间例外,如果指定的 `size` 是负值 。

@sample 样本. 共流. 原子学. 原子化学

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.atomics.AtomicArray
import kotlin.test.assertFailsWith



fun main() {
    val a = AtomicIntArray(3) { it * 10 }
    println(a.toString())
}
```

```text title="输出"
[0, 10, 20]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomicArrays.kt#L27)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
