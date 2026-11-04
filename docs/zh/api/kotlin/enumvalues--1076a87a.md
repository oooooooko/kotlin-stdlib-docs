# enumValues

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回包含 `T` 号信号的 enum 条目的数组。

函数返回每个调用时的阵列的新实例。 阵列可能会变异, 因此与之合作时可能也需要防御性复制。 考虑使用 `kotlin.enums.enumEntries` 来作为更高效的替代方法, 返回不可更改的昆虫条目列表 。

@see Kotlin.enums.enums.entisies (挪威)

??? note "查看英文原文"

    Returns an array containing enum entries of the enum type `T`.
    
    The function returns a new instance of the array on every call.
    The array could be mutated, so working with it may also require defensive copying.
    Consider using `kotlin.enums.enumEntries` as a more efficient alternative
    returning an immutable list of enum entries.
    
    @see kotlin.enums.enumEntries

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun <reified T : Enum<T>> enumValues(): Array<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Library.kt#L92)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


enum class State { READY, DONE }
fun main() {
    println(arrayOfNulls<String>(3).contentToString())
    println(enumValues<State>().contentToString())
}
```

```text title="输出"
[null, null, null]
[READY, DONE]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
