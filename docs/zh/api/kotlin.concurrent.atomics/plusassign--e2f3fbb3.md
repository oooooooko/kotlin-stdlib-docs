# plusAssign

`kotlin.concurrent.atomics` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

原子将`given value``delta` 添加到`AtomicInt`的当前值中。

@sample 样本. 结合体. 原子学. 原子工程 附加物

??? note "查看英文原文"

    Atomically adds the `given value``delta` to the current value of this `AtomicInt`.
    
    @sample samples.concurrent.atomics.AtomicInt.plusAssign

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.1")
@ExperimentalAtomicApi
public operator fun AtomicInt.plusAssign(delta: Int): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/Atomics.common.kt#L100)

### 2. Common

```kotlin
@SinceKotlin("2.1")
@ExperimentalAtomicApi
public operator fun AtomicLong.plusAssign(delta: Long): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/Atomics.common.kt#L319)

原子将`given value``delta` 添加到`AtomicLong`的当前值中。

@sample 样本. 结合体. 原子学. 原子学. 原子学Long.+Asign

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.thread



fun main() {
    val counter = AtomicInt(7)
    counter += 10
    println(counter.load())
}
```

```text title="输出"
17
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomics.kt#L77)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.thread



fun main() {
    val counter = AtomicLong(7)
    counter += 10
    println(counter.load())
}
```

```text title="输出"
17
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomics.kt#L222)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
