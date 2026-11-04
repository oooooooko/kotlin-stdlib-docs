# ClosedFloatingPointRange.lessThanOrEquals

`kotlin.ranges` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

比较范围域类型的两个值,如果第一个值小于或等于第二个值,则返回为真实。

??? note "查看英文原文"

    Compares two values of range domain type and returns true if first is less than or equal to second.

## 声明与重载

### 1. Common

```kotlin
public fun lessThanOrEquals(a: T, b: T): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ranges/Ranges.kt#L84)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() {
    val range: ClosedFloatingPointRange<Double> = 1.0..3.0
    println(2.0 in range)
    println(range.lessThanOrEquals(1.0, 3.0))
    println(range.lessThanOrEquals(Double.NaN, 3.0))
}
```

```text title="输出"
true
true
false
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
