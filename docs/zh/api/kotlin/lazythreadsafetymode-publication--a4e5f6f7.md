# LazyThreadSafetyMode.PUBLICATION

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

初始化函数可同时调用多个次于未初始化 `Lazy` 实例值,但只有一个计算值将用作`Lazy`实例值,并且所有线索都将可见。

@sample 样本.lazy.LazySamples.lazySafe 出版物样本

??? note "查看英文原文"

    Initializer function can be called several times on concurrent access to an uninitialized `Lazy` instance value,
    but only one computed value will be used as the value of a `Lazy` instance and will be visible by all threads.
    
    @sample samples.lazy.LazySamples.lazySafePublicationSample

## 声明与重载

### 1. Common

```kotlin
PUBLICATION,
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Lazy.kt#L72)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

fun main() {
    val value = kotlin.LazyThreadSafetyMode.PUBLICATION
    println(value)
}
```

```text title="输出"
PUBLICATION
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
