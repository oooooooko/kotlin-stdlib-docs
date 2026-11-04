# BuilderInference

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

这是兼容旧代码的注解示例。现代 Kotlin 在需要时会自动启用构建器类型推断，该注解已弃用。

??? note "查看英文原文"

    Allows to infer generic type arguments of a function from the calls in the annotated function parameter of that function.
    
    When this annotation is placed on a generic function parameter of a function,
    it enables to infer the type arguments of that generic function from the lambda body passed to that parameter.
    
    The calls that affect inference are either members of the receiver type of an annotated function parameter or
    extensions for that type. The extensions must be themselves annotated with `@BuilderInference`.
    
    Example: we declare
    ```
    fun <T> sequence(@BuilderInference block: suspend SequenceScope<T>.() -> Unit): Sequence<T>
    ```
    and use it like
    ```
    val result = sequence { yield("result") }
    ```
    Here the type argument of the resulting sequence is inferred to `String` from
    the argument of the `SequenceScope.yield` function, that is called inside the lambda passed to `sequence`.
    
    **Note:** This annotation is deprecated and should no longer be used. The compiler automatically enables builder inference for builder calls when needed.

## 声明与重载

### 1. Common

```kotlin
@Target(VALUE_PARAMETER, FUNCTION, PROPERTY)
@Retention(AnnotationRetention.BINARY)
@SinceKotlin("1.3")
@ExperimentalTypeInference
@Deprecated("BuilderInference annotation must not be used anymore. Builder inference is enabled automatically for builder calls if needed.")
@DeprecatedSinceKotlin(warningSince = "2.0", errorSince = "2.5", hiddenSince = "2.6")
public annotation class BuilderInference
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotations/Inference.kt#L11)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun <T> collect(@BuilderInference block: MutableList<T>.() -> Unit): List<T> = mutableListOf<T>().apply(block)
fun main() { val values = collect { add("Kotlin"); add("stdlib") }; println(values) }
```

```text title="输出"
[Kotlin, stdlib]
```

## 版本与来源

本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。
