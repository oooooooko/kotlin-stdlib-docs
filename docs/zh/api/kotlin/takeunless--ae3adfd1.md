# takeUnless

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

当 `predicate` 返回 `false` 时返回原对象；返回 `true` 时返回 `null`。适合用链式调用排除不符合要求的值。

??? note "查看英文原文"

    Returns `this` value if it _does not_ satisfy the given `predicate` or `null`, if it does.
    
    For detailed usage information see the documentation for [scope functions](https://kotlinlang.org/docs/reference/scope-functions.html#takeif-and-takeunless).

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
@SinceKotlin("1.1")
public inline fun <T> T.takeUnless(predicate: (T) -> Boolean): T?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Standard.kt#L135)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun main() { println(42.takeUnless { it < 0 }); println((-1).takeUnless { it < 0 }) }
```

```text title="输出"
42
null
```

## 版本与来源

本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。
