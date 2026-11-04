# AtomicReference

`kotlin.concurrent.atomics` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

对象引用,可原子更新。

具体平台的具体实施细节:

以原住民后端为目标的 `AtomicReference` 中,有 `T` 型的变异变量,并用原子方式更新。关于原子保障的更多信息,请阅读和写作见 `kotlin.concurrent.Volatile` 。

以JVM为目标时,有 `AtomicReference` 例的例子由[java.util.contil. contitution.totoic.AtomicReference](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/atomic/AtomicReference.html).)所代表(关于保障不稳定存取的详情和原子更新,参见Java语言规格(17.4记忆模型)。

JS和Wasm `AtomicReference`执行得微不足道,而且由于这些平台不支持多行,因此不完全安全。

@constructor 创建带有指定值的新的`AtomicReference` 初始化。

??? note "查看英文原文"

    An object reference that may be updated atomically.
    
    Platform-specific implementation details:
    
    When targeting the Native backend, `AtomicReference` stores a volatile variable of type `T` and atomically updates it.
    For additional details about atomicity guarantees for reads and writes see `kotlin.concurrent.Volatile`.
    
    When targeting the JVM, instances of `AtomicReference` are represented by
    [java.util.concurrent.atomic.AtomicReference](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/atomic/AtomicReference.html).
    For details about guarantees of volatile accesses and updates of atomics refer to The Java Language Specification (17.4 Memory Model).
    
    For JS and Wasm `AtomicReference` is implemented trivially and is not thread-safe since these platforms do not support multi-threading.
    
    @constructor Creates a new `AtomicReference` initialized with the specified value.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.1")
@ExperimentalAtomicApi
public expect class AtomicReference<T> public constructor(value: T)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/Atomics.common.kt#L522)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.concurrent.atomics.*

fun main() {
    val value = kotlin.concurrent.atomics.AtomicReference(1)
    println(value)
}
```

```text title="输出"
1
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
