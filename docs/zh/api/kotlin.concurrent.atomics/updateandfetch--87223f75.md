# updateAndFetch

`kotlin.concurrent.atomics` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

原子更新此 `AtomicInt` 的值, 以当前值调用 `transform` 函数获得的值, 并返回新值 。

重新计算结果可以不止一次援引`transform`,例如当原子整数值同时更新,而`transform`应用时,或者由于虚假的比较和假设失败,这种情况可能发生,后者是具体执行的,不应依赖。

在不支持多行平台(JS和Wam)上,这项操作的执行微不足道, `transform` 号将被精确援引一次。

推荐保持 `transform` 的快速 并且没有副作用

@sample 样本. 结合体. 原子学. 原子工程. 更新和扩展

??? note "查看英文原文"

    Atomically updates the value of this `AtomicInt` with the value obtained by calling the `transform` function on the current value
    and returns the new value.
    
    `transform` may be invoked more than once to recompute a result.
    That may happen, for example, when this atomic integer value was concurrently updated while `transform` was applied,
    or due to a spurious compare-and-set failure.
    The latter is implementation-specific, and it should not be relied upon.
    
    On platforms that do no support multi-threading (JS and Wasm), this operation has a trivial implementation
    and `transform` will be invoked exactly once.
    
    It's recommended to keep `transform` fast and free of side effects.
    
    @sample samples.concurrent.atomics.AtomicInt.updateAndFetch

## 声明与重载

### 1. Common

```kotlin
@Suppress("EXPECTED_DECLARATION_WITH_BODY", "WRONG_INVOCATION_KIND")
@SinceKotlin("2.2")
@ExperimentalAtomicApi
@InlineOnly
public expect inline fun AtomicInt.updateAndFetch(transform: (Int) -> Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/Atomics.common.kt#L207)

### 2. Common

```kotlin
@Suppress("EXPECTED_DECLARATION_WITH_BODY", "WRONG_INVOCATION_KIND")
@SinceKotlin("2.2")
@ExperimentalAtomicApi
@InlineOnly
public expect inline fun AtomicLong.updateAndFetch(transform: (Long) -> Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/Atomics.common.kt#L426)

原子更新此 `AtomicLong` 的值, 以当前值调用 `transform` 函数获得的值, 并返回新值 。

例如,当这一原子长期值同时更新,同时适用`transform`时,或者由于虚假的比较和假设失败,这种情况可能发生。 后者是具体执行的,不应依赖它。

在不支持多行平台(JS和Wam)上,这项操作的执行微不足道, `transform` 号将被精确援引一次。

推荐保持 `transform` 的快速 并且没有副作用

@sample 样本. 结合体. 原子学. 原子学Long. 更新和扩展

### 3. Common

```kotlin
@Suppress("EXPECTED_DECLARATION_WITH_BODY", "WRONG_INVOCATION_KIND")
@SinceKotlin("2.2")
@ExperimentalAtomicApi
@InlineOnly
public expect inline fun <T> AtomicReference<T>.updateAndFetch(transform: (T) -> T): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/Atomics.common.kt#L644)

原子更新此 `AtomicReference` 的值, 以当前值调用 `transform` 函数获得的值, 并返回新值 。

重新计算结果可以不止一次援引`transform`,例如,当原子参考同时更新,而使用`transform`时,或者由于虚假的比较和假设失败,这种情况可能发生,后者是具体执行的,不应依赖。

在不支持多行平台(JS和Wam)上,这项操作的执行微不足道, `transform` 号将被精确援引一次。

推荐保持 `transform` 的快速 并且没有副作用

@sample 样本. 结合体. 原子学. 原子参考. 更新和扩展

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.thread



fun main() {
    val a = AtomicInt(7)
    val updatedValue = a.updateAndFetch { currentValue ->
        when (currentValue % 2) {
            0 -> currentValue / 2
            else -> 3 * currentValue + 1
        }
    }
    println(updatedValue)
    println(a.load())
}
```

```text title="输出"
22
22
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomics.kt#L131)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.thread



fun main() {
    val a = AtomicLong(7L)
    val updatedValue = a.updateAndFetch { currentValue ->
        when (currentValue % 2) {
            0L -> currentValue / 2
            else -> 3 * currentValue + 1
        }
    }
    println(updatedValue)
    println(a.load())
}
```

```text title="输出"
22
22
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomics.kt#L277)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.concurrent.atomics.*
import kotlin.concurrent.thread



fun main() {
    data class Wallet(val owner: String, val balance: Long)

    val a = AtomicReference(Wallet("Kodee", 100_00L))
    val updatedWallet = a.updateAndFetch { wallet ->
        wallet.copy(balance = wallet.balance + 1_00) // Kodee got a buck!
    }
    println(updatedWallet)
    println(a.load())
}
```

```text title="输出"
Wallet(owner=Kodee, balance=10100)
Wallet(owner=Kodee, balance=10100)
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/concurrent/atomics/atomics.kt#L412)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
