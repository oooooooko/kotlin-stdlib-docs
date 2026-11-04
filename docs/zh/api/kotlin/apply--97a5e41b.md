# apply

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

调用指定的函数 `block` , 值为 `this` 的接收器, 并返回 `this` 值 。

详细使用情况信息见[范围函数]的文件(https://kotlinlang.org/docs/reference/scope-functions.html#apply).)

??? note "查看英文原文"

    Calls the specified function `block` with `this` value as its receiver and returns `this` value.
    
    For detailed usage information see the documentation for [scope functions](https://kotlinlang.org/docs/reference/scope-functions.html#apply).

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun <T> T.apply(block: T.() -> Unit): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Standard.kt#L76)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.util.*



fun main() {
    val vector = Vector<String>().apply {
        add("RED")
        add("GREEN")
        add("BLUE")
    }

    // iterator() extension is called here
    for (e in vector.elements()) {
        println("The element is $e")
    }
}
```

```text title="输出"
The element is RED
The element is GREEN
The element is BLUE
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/iterators.kt#L24)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
