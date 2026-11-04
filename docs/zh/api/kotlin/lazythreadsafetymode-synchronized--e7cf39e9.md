# LazyThreadSafetyMode.SYNCHRONIZED

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

使用锁以确保只有一条线可以初始化 `Lazy` 实例,并确保所有线条都能看到初始化值。 所使用的锁既包括平台,也包括执行的细节。

@sample 样本.lazy.LazySamples.lazySyncronizizizedSampl 样本

??? note "查看英文原文"

    Uses a lock to ensure that only a single thread can initialize a `Lazy` instance,
    and ensures that initialized value is visible by all threads.
    The lock used is both platform- and implementation- specific detail.
    
    @sample samples.lazy.LazySamples.lazySynchronizedSample

## 声明与重载

### 1. Common

```kotlin
SYNCHRONIZED,
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Lazy.kt#L63)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

fun main() {
    val value = kotlin.LazyThreadSafetyMode.SYNCHRONIZED
    println(value)
}
```

```text title="输出"
SYNCHRONIZED
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
