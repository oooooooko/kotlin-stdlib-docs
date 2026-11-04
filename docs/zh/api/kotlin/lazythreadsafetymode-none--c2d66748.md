# LazyThreadSafetyMode.NONE

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

没有使用锁定来同步访问和初始化 `Lazy` 实例值。 如果从多个线索访问此实例, 则其行为未指明 。

除非保证 `Lazy` 实例不会从不止一条线索上初始化,否则不应使用此模式。

??? note "查看英文原文"

    No locks are used to synchronize access and initialization of a `Lazy` instance value.
    If the instance is accessed from multiple threads, its behavior is unspecified.
    
    This mode should not be used unless the `Lazy` instance is guaranteed never to be initialized from more than one thread.

## 声明与重载

### 1. Common

```kotlin
NONE,
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Lazy.kt#L80)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

fun main() {
    val value = kotlin.LazyThreadSafetyMode.NONE
    println(value)
}
```

```text title="输出"
NONE
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
