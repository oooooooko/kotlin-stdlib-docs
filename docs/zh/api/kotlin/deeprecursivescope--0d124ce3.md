# DeepRecursiveScope

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

作用域内部应使用 `callRecursive`；直接调用 `invoke` 已禁止，本例同时展示被抑制后的异常，便于迁移旧代码。

??? note "查看英文原文"

    A scope class for `DeepRecursiveFunction` function declaration that defines `callRecursive` methods to
    recursively call this function or another `DeepRecursiveFunction` putting the call activation frame on the heap.
    
    @param `T` function parameter type.
    @param `R` function result type.

## 声明与重载

### 1. Common

```kotlin
@RestrictsSuspension
@SinceKotlin("1.7")
@WasExperimental(ExperimentalStdlibApi::class)
public sealed class DeepRecursiveScope<T, R>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/DeepRecursive.kt#L85)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() {
    val sum = DeepRecursiveFunction<Int, Int> { n -> if (n == 0) 0 else n + callRecursive(n - 1) }
    println(sum(100))
    lateinit var invalid: DeepRecursiveFunction<Int, Int>
    invalid = DeepRecursiveFunction { n -> invalid(n) }
    try { invalid(1) } catch (error: UnsupportedOperationException) { println(error.message) }
}
```

```text title="输出"
5050
Should not be called from DeepRecursiveScope
```

## 版本与来源

本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。
