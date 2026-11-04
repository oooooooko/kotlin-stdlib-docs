# AtomicInt

`kotlin.concurrent.atomics` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

`Int` 值, 可以通过原子方式更新 。

具体平台的具体实施细节:

以原住民后端为目标的 `AtomicInt` 中,储存了一个波动的`Int`变量,并按原子方式更新。关于原子保障的更多信息,请阅读并写作,请见 `kotlin.concurrent.Volatile` 。

当以JVM为目标时,有 `AtomicInt` 例的例子由[java.util.contil.contic.totomic Integer](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/atomic/AtomicInteger.html).)所代表(关于保障不稳定存取的详情和原子更新,参见Java语言规格(17.4记忆模型)。

JS和Wasm `AtomicInt`执行得微不足道,而且由于这些平台不支持多行,因此不完全安全。

@constructor 创建带有指定值的新的`AtomicInt` 初始化。

??? note "查看英文原文"

    An `Int` value that may be updated atomically.
    
    Platform-specific implementation details:
    
    When targeting the Native backend, `AtomicInt` stores a volatile `Int` variable and atomically updates it.
    For additional details about atomicity guarantees for reads and writes see `kotlin.concurrent.Volatile`.
    
    When targeting the JVM, instances of `AtomicInt` are represented by
    [java.util.concurrent.atomic.AtomicInteger](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/atomic/AtomicInteger.html).
    For details about guarantees of volatile accesses and updates of atomics refer to The Java Language Specification (17.4 Memory Model).
    
    For JS and Wasm `AtomicInt` is implemented trivially and is not thread-safe since these platforms do not support multi-threading.
    
    @constructor Creates a new `AtomicInt` initialized with the specified value.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("2.1")
@ExperimentalAtomicApi
public expect class AtomicInt public constructor(value: Int)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/concurrent/atomics/Atomics.common.kt#L15)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.concurrent.atomics.*
import kotlin.test.*



fun main() {

        println(AtomicInt(42).toString())
    
}
```

```text title="输出"
42
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/concurrent/atomics/AtomicCommonTest.kt#L82)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
