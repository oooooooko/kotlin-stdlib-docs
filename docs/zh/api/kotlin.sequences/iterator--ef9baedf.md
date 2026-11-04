# iterator

`kotlin.sequences` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

建立一个`Iterator` 低沉的产值 逐个生成值。

如果消费代码停止使用没有`Iterator.hasNext`返回`false`的循环器, 则计算中的其余部分将完全无法运行。 特别是, 这意味着 `finally` 块块可能未执行:

```
val singleElementIterator = iterator {
    try {
        yield(1)
        // no code after the `yield(1)` line will be executed!
    } finally {
        println("This line will not run")
    }
}
// only get the first element, do not attempt evaluating the rest of them
if (singleElementIterator.hasNext()) {
    println(singleElementIterator.next())
}
```

@sample 样本、采集资料、序列、建筑、建造@sample样本、收集资料、可操作材料、建筑、可操作材料、

??? note "查看英文原文"

    Builds an `Iterator` lazily yielding values one by one.
    
    If the consuming code stops using the iterator without `Iterator.hasNext` returning `false` first,
    the remainder of the computation will not run at all.
    In particular, it means that `finally` blocks may be left unexecuted:
    
    ```
    val singleElementIterator = iterator {
        try {
            yield(1)
            // no code after the `yield(1)` line will be executed!
        } finally {
            println("This line will not run")
        }
    }
    // only get the first element, do not attempt evaluating the rest of them
    if (singleElementIterator.hasNext()) {
        println(singleElementIterator.next())
    }
    ```
    
    @sample samples.collections.Sequences.Building.buildIterator
    @sample samples.collections.Iterables.Building.iterable

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
@Suppress("DEPRECATION")
public fun <T> iterator(@BuilderInference block: suspend SequenceScope<T>.() -> Unit): Iterator<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/SequenceBuilder.kt#L45)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val iterable = Iterable {
        iterator {
            yield(42)
            yieldAll(1..5 step 2)
        }
    }
    val result = iterable.mapIndexed { index, value -> "$index: $value" }
    println(result)

    // can be iterated many times
    repeat(2) {
        val sum = iterable.sum()
        println(sum)
    }
}
```

```text title="输出"
[0: 42, 1: 1, 2: 3, 3: 5]
51
51
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/iterables.kt#L26)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
