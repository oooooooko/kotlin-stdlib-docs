# arrayOfNulls

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回给定 `size` 的给定类型对象的数组,该数组以无效值初始化。

@throws 运行时间例外,如果指定的 `size` 是负值 。

??? note "查看英文原文"

    Returns an array of objects of the given type with the given `size`, initialized with null values.
    
    @throws RuntimeException if the specified `size` is negative.

## 声明与重载

### 1. Common

```kotlin
@Suppress("REIFIED_TYPE_PARAMETER_NO_INLINE")
public expect fun <reified T> arrayOfNulls(size: Int): Array<T?>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Library.kt#L21)

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
