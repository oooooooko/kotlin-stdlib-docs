# Annotation

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

所有注解界面都暗含地安装了基地界面。请参看[科特林语言文档](https://kotlinlang.org/docs/reference/annotations.html))有关说明的更多信息。

??? note "查看英文原文"

    Base interface implicitly implemented by all annotation interfaces.
    See [Kotlin language documentation](https://kotlinlang.org/docs/reference/annotations.html) for more information
    on annotations.

## 声明与重载

### 1. Common

```kotlin
public expect interface Annotation
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Annotation.kt#L9)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


annotation class Label(val value: String)
fun main() { val label: Annotation = Label("example"); println(label.annotationClass.simpleName) }
```

```text title="输出"
Label
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
