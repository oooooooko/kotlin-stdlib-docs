# fetchAndIncrement

`kotlin.concurrent.atomics` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

原子递增此 `AtomicInt` 的当前值, 并返回旧值 。

@sample 样本. 结合体. 原子学. 原子学. 化学学. 人类学. 人类学. 人类学. 人类学. 人类学. 人类学. 人类学. 人类学. 人类学. 人类学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋和海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋和海洋 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋学. 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 . 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 和 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋 海洋

??? note "查看英文原文"

    Atomically increments the current value of this `AtomicInt` by one and returns the old value.
    
    @sample samples.concurrent.atomics.AtomicInt.fetchAndIncrement

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.1")
@ExperimentalAtomicApi
public fun AtomicInt.fetchAndIncrement(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/Atomics.common.kt#L118)

### 2. Common

```kotlin
@SinceKotlin("2.1")
@ExperimentalAtomicApi
public fun AtomicLong.fetchAndIncrement(): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/Atomics.common.kt#L337)

原子递增此 `AtomicLong` 的当前值, 并返回旧值 。

@sample 样本. 结合体. 原子学. 原子学Long. fetchand Incrowting

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.thread



fun main() {
    val a = AtomicInt(7)
    println(a.fetchAndIncrement())
    println(a.load())
}
```

```text title="输出"
7
8
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomics.kt#L91)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.thread



fun main() {
    val a = AtomicLong(7)
    println(a.fetchAndIncrement())
    println(a.load())
}
```

```text title="输出"
7
8
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomics.kt#L236)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
