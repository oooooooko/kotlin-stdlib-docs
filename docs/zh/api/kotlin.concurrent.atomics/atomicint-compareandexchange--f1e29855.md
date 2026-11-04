# AtomicInt.compareAndExchange

`kotlin.concurrent.atomics` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

存放于`new value``newValue`与此相进`AtomicInt`如果当前值等于`expected value``expectedValue`
返回旧值。

数值比较按数值进行。

@sample 样本. 结合体. 原子学. 原子学. 比较和变化

??? note "查看英文原文"

    Atomically stores the given `new value``newValue` into this `AtomicInt` if the current value equals the `expected value``expectedValue`
    and returns the old value in any case.
    
    Comparison of values is done by value.
    
    @sample samples.concurrent.atomics.AtomicInt.compareAndExchange

## 声明与重载

### 1. Common

```kotlin
public fun compareAndExchange(expectedValue: Int, newValue: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/Atomics.common.kt#L68)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.thread



fun main() {
    val a = AtomicInt(7)
    // Current value 7 is equal to the expected value 7 ->
    // compareAndExchange succeeds, stores the new value 10 and returns the old value 7.
    println(a.compareAndExchange(7, 10))
    println(a.load())

    // Current value 10 is not equal to the expected value 2 ->
    // compareAndExchange fails, does not store the new value and returns the current value 10.
    println(a.compareAndExchange(2, 12))
    println(a.load())
}
```

```text title="输出"
7
10
10
10
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomics.kt#L47)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
