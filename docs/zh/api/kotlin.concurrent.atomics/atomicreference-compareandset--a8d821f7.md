# AtomicReference.compareAndSet

`kotlin.concurrent.atomics` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

存放于`new value``newValue`与此相进`AtomicReference`如果当前值等于`expected value``expectedValue`,
如果操作成功且只有在当前值不等于预期值时才返回真实值, 则返回为真实值 。

这个操作有所谓的强语义, 意思是如果并且只有在当前和预期值不相等时, 它才会返回虚假的 。

数值比较是参照。

@sample 样本. 共流. 原子学. 原子参考. 兼容和成

??? note "查看英文原文"

    Atomically stores the given `new value``newValue` into this `AtomicReference` if the current value equals the `expected value``expectedValue`,
    returns true if the operation was successful and false only if the current value was not equal to the expected value.
    
    This operation has so-called strong semantics,
    meaning that it returns false if and only if current and expected values are not equal.
    
    Comparison of values is done by reference.
    
    @sample samples.concurrent.atomics.AtomicReference.compareAndSet

## 声明与重载

### 1. Common

```kotlin
public fun compareAndSet(expectedValue: T, newValue: T): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/Atomics.common.kt#L562)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.thread



fun main() {
    val a = AtomicReference("aaa")
    // Current value "aaa" is equal to the expected value "aaa" -> compareAndSet succeeds.
    println(a.compareAndSet("aaa", "bbb"))
    println(a.load())

    // Current value "bbb" is not equal to the expected value "aaa" -> compareAndSet fails.
    println(a.compareAndSet("aaa", "kkk"))
    println(a.load())
}
```

```text title="输出"
true
bbb
false
bbb
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomics.kt#L375)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
