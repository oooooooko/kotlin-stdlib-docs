# OverloadResolutionByLambdaReturnType

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

根据从 lambda 参数返回的值类型,启用超载选择。

当两个或多个功能超载时, 函数的参数列表与其它参数列表相同, 且仅与函数参数的返回类型不同时, 此注释允许根据从 ambda 函数返回到此函数的值类型选择超载值 。

示例:```
@OverloadResolutionByLambdaReturnType
fun create(intProducer: () -> Int): Int

fun create(doubleProducer: () -> Double): Double

val newValue = create { 3.14 }
```

超载状态说明有助于分析从羊羔功能返回值,从而解决这一模糊问题。

如果选择超载时仍然无法选择其中之一,即使考虑到羊羔参数分析的结果,也使用这一注释来区分附加说明的超载。

注:这个注解是实验性的,请参见 `ExperimentalTypeInference` 关于如何选择加入。

??? note "查看英文原文"

    Enables overload selection based on the type of the value returned from lambda argument.
    
    When two or more function overloads have otherwise the same parameter lists that differ only in the return type
    of a functional parameter, this annotation enables overload selection by the type of the value returned from
    the lambda function passed to this functional parameter.
    
    Example:
    ```
    @OverloadResolutionByLambdaReturnType
    fun create(intProducer: () -> Int): Int
    
    fun create(doubleProducer: () -> Double): Double
    
    val newValue = create { 3.14 }
    ```
    
    The annotation being applied to one of overloads allows to resolve this ambiguity by analyzing what value is returned
    from the lambda function.
    
    This annotation is also used to discriminate the annotated overloads in case if overload selection still cannot
    choose one of them even taking in account the result of lambda parameter analysis. In that case a warning is reported.
    
    Note: this annotation is experimental, see `ExperimentalTypeInference` on how to opt-in for it.

## 声明与重载

### 1. Common

```kotlin
@Target(FUNCTION)
@Retention(AnnotationRetention.BINARY)
@SinceKotlin("1.4")
@ExperimentalTypeInference
public annotation class OverloadResolutionByLambdaReturnType
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotations/Inference.kt#L42)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


@OverloadResolutionByLambdaReturnType
fun choose(block: () -> Int, marker: Int = 0): String = "Int: ${block()}"
@OverloadResolutionByLambdaReturnType
fun choose(block: () -> String, marker: String = ""): String = "String: ${block()}"
fun main() { println(choose({ 42 })); println(choose({ "Kotlin" })) }
```

```text title="输出"
Int: 42
String: Kotlin
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
