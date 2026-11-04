# repeat

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

执行给定的 `action` 函数指定 `times` 的编号。

当前迭代的零基指数作为参数被传递到 `action` 函数中。

如果`times`参数为负值或等于零,则不援引`action`函数。

@sample 样本.misc. control Flow.repeat

??? note "查看英文原文"

    Executes the given function `action` specified number of `times`.
    
    A zero-based index of current iteration is passed as a parameter to the `action` function.
    
    If the `times` parameter is negative or equal to zero, the `action` function is not invoked.
    
    @sample samples.misc.ControlFlow.repeat

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun repeat(times: Int, action: (Int) -> Unit)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Standard.kt#L149)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    // greets three times
    repeat(3) {
        println("Hello")
    }

    // greets with an index
    repeat(3) { index ->
        println("Hello with index $index")
    }

    repeat(0) {
        error("We should not get here!")
    }
}
```

```text title="输出"
Hello
Hello
Hello
Hello with index 0
Hello with index 1
Hello with index 2
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/controlFlow.kt#L12)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
