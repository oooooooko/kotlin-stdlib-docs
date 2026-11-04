# ContractBuilder.returnsResultOf

`kotlin.contracts` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

指定函数返回函数参数 `lambda` 的援引结果。

Kotlin的返回值检查器目前使用这一信息,并指示它查看 `lambda` 内部,以确定合同功能是否被忽视。

如果功能参数结果只返回到一个可能的执行路径(即`InvocationKind.AT_MOST_ONCE`, 情况),合同仍应提及它。如果该功能接受多个功能参数,则可以多次指定合同,并列出所有执行路径中的所有潜在引用。

例如:```kotlin
inline fun <T, R> T.selector(condition: (T) -> Boolean?, a: (T) -> R, b: (T) -> R): R? {
    contract {
        callsInPlace(a, InvocationKind.AT_MOST_ONCE)
        callsInPlace(b, InvocationKind.AT_MOST_ONCE)
        returnsResultOf(a)
        returnsResultOf(b)
    }
    return when (condition(this)) {
        true -> a(this)
        false -> b(this)
        null -> null
    }
}
````returnsResultOf` 合同提到`a`和 `b` ,因为其中每一个都至少在其中一条路径从功能返回。 `condition` 合同没有提及,因为没有从所有路径的函数返回。

此合同是实验性的, 只有在启用了“ 返回值检查” 功能的情况下, 才能使用 。

??? note "查看英文原文"

    Specifies that the function returns the result of the invocation of the function parameter `lambda`.
    
    This information is currently used by the Kotlin's return value checker and instructs it
    to look inside `lambda` to decide whether function with contract is ignorable.
    
    If the functional parameter result is returned only in one of the possible execution paths (i.e., in `InvocationKind.AT_MOST_ONCE` situation),
    contract still should mention it. If the function accepts multiple functional parameters, the contract may be specified several times
    and should list all potential invocations from all execution paths.
    
    For example:
    ```kotlin
    inline fun <T, R> T.selector(condition: (T) -> Boolean?, a: (T) -> R, b: (T) -> R): R? {
        contract {
            callsInPlace(a, InvocationKind.AT_MOST_ONCE)
            callsInPlace(b, InvocationKind.AT_MOST_ONCE)
            returnsResultOf(a)
            returnsResultOf(b)
        }
        return when (condition(this)) {
            true -> a(this)
            false -> b(this)
            null -> null
        }
    }
    ```
    `a` and `b` are mentioned in the `returnsResultOf` contract because each of them is returned from the function in at least one of the paths.
    `condition` is not mentioned in the contract because it is not returned from the function on all the paths.
    
    This contract is experimental, and it is allowed to use it only with the 'Return value checker' feature enabled.

## 声明与重载

### 1. Common

```kotlin
@ContractsDsl
    @SinceKotlin("2.4")
    public fun <R> returnsResultOf(lambda: Function<R>)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contracts/ContractBuilder.kt#L125)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.contracts.*
inline fun <T> evaluate(block: () -> T): T {
    contract { callsInPlace(block, InvocationKind.EXACTLY_ONCE); returnsResultOf(block) }
    return block()
}
fun main() { println(evaluate { 42 }) }
```

```text title="输出"
42
```

编译选项：`-Xallow-returns-result-of` `-Xreturn-value-checker=check`

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
