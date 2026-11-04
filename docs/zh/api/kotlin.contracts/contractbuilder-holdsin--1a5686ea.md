# ContractBuilder.holdsIn

`kotlin.contracts` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

指定条件,该条件作为接收器参数通过,保证在函数参数 `lambda` 的正文中为真实。

注:接收者只接受代表条件的受限布尔表达式,其中表达式可能只包括定义合同或否定合同的功能的布尔参数。

??? note "查看英文原文"

    Specifies the condition, passed as a receiver argument, that is guaranteed to be true in the body of a function parameter `lambda`.
    
    Note: the receiver accepts only a restricted boolean expression representing the condition, where the expression may include
    only the boolean parameter of the function defining the contract, or its negation.

## 声明与重载

### 1. Common

```kotlin
@ExperimentalExtendedContracts
    @ContractsDsl
    @SinceKotlin("2.2") // Technically 2.2.20
    public infix fun <R> Boolean.holdsIn(lambda: Function<R>): HoldsIn
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contracts/ContractBuilder.kt#L114)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.contracts.*
inline fun whenEnabled(enabled: Boolean, block: () -> Unit) {
    contract { enabled holdsIn block; callsInPlace(block, InvocationKind.AT_MOST_ONCE) }
    if (enabled) block()
}
fun main() { val enabled = true; whenEnabled(enabled) { println("enabled=$enabled") } }
```

```text title="输出"
enabled=true
```

编译选项：`-Xallow-holdsin-contract`

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
