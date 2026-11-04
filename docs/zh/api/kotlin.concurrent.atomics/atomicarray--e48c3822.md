# AtomicArray

`kotlin.concurrent.atomics` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

元素可原子更新的通用对象数组。

具体平台的具体实施细节:

以原住民后端为目标的 `AtomicArray` 存储了 `Array` , 包含`T` 和原子更新元素。 有关原子保障的更多信息,请查看并写到 `kotlin.concurrent.Volatile` 。

在以JVM为目标时,有 `AtomicArray` 例的例子由[java.util.contil.contic.totomicReferenceArray](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/atomic/AtomicReferenceArray.html).)所代表(关于保障不稳定存取的详情和原子更新,参见《爪哇语言规格》(17.4记忆模型)。

JS和Wasm `AtomicArray`执行得微不足道,而且由于这些平台不支持多行,因此不完全安全。

??? note "查看英文原文"

    A generic array of objects in which elements may be updated atomically.
    
    Platform-specific implementation details:
    
    When targeting the Native backend, `AtomicArray` stores an `Array` with elements of type `T` and atomically updates it's elements.
    For additional details about atomicity guarantees for reads and writes see `kotlin.concurrent.Volatile`.
    
    When targeting the JVM, instances of `AtomicArray` are represented by
    [java.util.concurrent.atomic.AtomicReferenceArray](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/atomic/AtomicReferenceArray.html).
    For details about guarantees of volatile accesses and updates of atomics refer to The Java Language Specification (17.4 Memory Model).
    
    For JS and Wasm `AtomicArray` is implemented trivially and is not thread-safe since these platforms do not support multi-threading.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.1")
@ExperimentalAtomicApi
public expect class AtomicArray<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L552)

### 2. Common

```kotlin
@SinceKotlin("2.1")
@ExperimentalAtomicApi
@Suppress("UNCHECKED_CAST")
public inline fun <reified T> AtomicArray(size: Int, init: (Int) -> T): AtomicArray<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/AtomicArrays.common.kt#L650)

如果给定 `size` 的给定类型, 创建新的 `AtomicArray`, 并在此初始化每个元素, 并调用给定 `init` 函数 。

函数 `init` 由第一个数组元素依次对每个数组元素调用。 它应该返回一个数组元素的值, 并给定其索引 。

@throws 运行时间例外,如果指定的 `size` 是负值 。

@see 原子射线

@sample 样本. 共流. 原子学. 原子阵列. 尼尼特

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.atomics.AtomicArray
import kotlin.test.assertFailsWith



fun main() {
    val a = AtomicArray(3) { "a$it" }
    println(a.toString())

    // Size should be non-negative
    assertFailsWith<RuntimeException> { AtomicArray(-1) { "$it" } }
}
```

```text title="输出"
[a0, a1, a2]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomicArrays.kt#L344)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
