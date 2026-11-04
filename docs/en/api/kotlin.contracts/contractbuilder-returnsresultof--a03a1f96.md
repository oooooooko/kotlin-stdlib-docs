# ContractBuilder.returnsResultOf

`kotlin.contracts` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

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

## Declarations and overloads

### 1. Common

```kotlin
@ContractsDsl
    @SinceKotlin("2.4")
    public fun <R> returnsResultOf(lambda: Function<R>)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contracts/ContractBuilder.kt#L125)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.contracts.*
inline fun <T> evaluate(block: () -> T): T {
    contract { callsInPlace(block, InvocationKind.EXACTLY_ONCE); returnsResultOf(block) }
    return block()
}
fun main() { println(evaluate { 42 }) }
```

```text title="Output"
42
```

Compiler options: `-Xallow-returns-result-of` `-Xreturn-value-checker=check`

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
