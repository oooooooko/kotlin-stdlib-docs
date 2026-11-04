# Nothing

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

没有什么没有实例。 您无法使用任何东西来代表“ 从未存在的值 ” : 例如, 如果函数具有“ 不存在” 的返回类型, 这意味着它永远不会返回( 总是会丢出一个例外 ) 。

??? note "查看英文原文"

    Nothing has no instances. You can use Nothing to represent "a value that never exists": for example,
    if a function has the return type of Nothing, it means that it never returns (always throws an exception).

## 声明与重载

### 1. Common

```kotlin
public expect class Nothing // no constructor
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Nothing.kt#L9)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun fail(message: String): Nothing = throw IllegalStateException(message)
fun main() {
    try { fail("missing value") } catch (error: IllegalStateException) { println(error.message) }
    val value: String? = null
    println(value ?: "fallback")
}
```

```text title="输出"
missing value
fallback
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
