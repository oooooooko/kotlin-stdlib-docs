# IntroducedAt.constructor

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

版本号表示库自己的发布版本，并非 Kotlin 版本。注解参数必须带默认值，编译器生成旧签名以维持二进制兼容。

## 声明与重载

### 1. Common

```kotlin
(val version: String)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotations/VersionOverloads.kt#L82)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


fun greeting(name: String, @IntroducedAt("1.1") punctuation: String = "!"): String = "Hello, $name$punctuation"
fun main() { println(greeting("Kotlin")); println(greeting("Kotlin", "?")) }
```

```text title="输出"
Hello, Kotlin!
Hello, Kotlin?
```

## 版本与来源

本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。
