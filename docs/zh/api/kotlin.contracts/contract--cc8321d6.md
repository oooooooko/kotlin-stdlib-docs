# contract

`kotlin.contracts` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

契约效果类型由 `contract` DSL 构造，不能作为普通对象手动创建。编译器使用这些声明进行智能转换和初始化分析；它们不会自动检查函数体是否兑现承诺。

??? note "查看英文原文"

    Specifies the contract of a function.
    
    The contract description must be at the beginning of a function and have at least one effect.
    
    Only the top-level functions can have a contract for now.
    
    @param builder the lambda where the contract of a function is described with the help of the `ContractBuilder` members.

## 声明与重载

### 1. Common

```kotlin
/* @sample samples.contracts.returnsContract
* @sample samples.contracts.returnsTrueContract
* @sample samples.contracts.returnsFalseContract
* @sample samples.contracts.returnsNullContract
* @sample samples.contracts.returnsNotNullContract
* @sample samples.contracts.callsInPlaceAtMostOnceContract
* @sample samples.contracts.callsInPlaceAtLeastOnceContract
* @sample samples.contracts.callsInPlaceExactlyOnceContract
* @sample samples.contracts.callsInPlaceUnknownContract
*/
@ContractsDsl
@ExperimentalContracts
@InlineOnly
@SinceKotlin("1.3")
@Suppress("UNUSED_PARAMETER")
public inline fun contract(builder: ContractBuilder.() -> Unit)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contracts/ContractBuilder.kt#L198)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.contracts.*
fun isText(value: Any?): Boolean {
    contract { returns(true) implies (value is String) }
    return value is String
}
fun requireText(value: Any?) {
    contract { returns() implies (value is String) }
    require(value is String)
}
fun textOrNull(value: Any?): String? {
    contract { returnsNotNull() implies (value is String) }
    return value as? String
}
inline fun once(block: () -> Unit) {
    contract { callsInPlace(block, InvocationKind.EXACTLY_ONCE) }
    block()
}
fun main() {
    val value: Any? = "Kotlin"
    if (isText(value)) println(value.length)
    requireText(value)
    println(value.length)
    val result = textOrNull(value)
    println(result)
    val initialized: Int
    once { initialized = 42 }
    println(initialized)
}
```

```text title="输出"
6
6
Kotlin
42
```

## 版本与来源

本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。
