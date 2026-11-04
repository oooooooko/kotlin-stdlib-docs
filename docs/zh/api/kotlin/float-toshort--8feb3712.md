# Float.toShort

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

旧的直接转换已弃用。示例为兼容旧代码演示而抑制错误；新代码先显式转为 `Int`。

??? note "查看英文原文"

    Converts this `Float` value to `Short`.
    
    The resulting `Short` value is equal to `this.toInt().toShort()`.

## 声明与重载

### 1. Common

```kotlin
@Deprecated("Unclear conversion. To achieve the same result convert to Int explicitly and then to Short.", ReplaceWith("toInt().toShort()"))
    @DeprecatedSinceKotlin(warningSince = "1.3", errorSince = "1.5")
    @kotlin.internal.IntrinsicConstEvaluation
    public override fun toShort(): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Primitives.kt#L1862)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() { val value = 65.5f; println(value.toChar()); println(value.toByte()); println(value.toShort()); println(value.toInt().toChar()) }
```

```text title="输出"
A
65
65
A
```

## 版本与来源

本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。
