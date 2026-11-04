# Pair

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

代表两个值的通用对数值。

与此类中的值无关, 任何目的都可以使用。 配对物证价值的语义, 即两个元素等同时, 两对是等的 。

将它分解成数值的一个例子: @sample 样本.misc.Tuples.pair 结构

@param 一种第一值的类型。 @param B 类型为 第二值。 @property 第一值为 @property 第一次值为 @property 第二次值为 @constructor 创建了一个新的对等实例。

??? note "查看英文原文"

    Represents a generic pair of two values.
    
    There is no meaning attached to values in this class, it can be used for any purpose.
    Pair exhibits value semantics, i.e. two pairs are equal if both components are equal.
    
    An example of decomposing it into values:
    @sample samples.misc.Tuples.pairDestructuring
    
    @param A type of the first value.
    @param B type of the second value.
    @property first First value.
    @property second Second value.
    @constructor Creates a new instance of Pair.

## 声明与重载

### 1. Common

```kotlin
@kotlin.js.JsImplicitExport(couldBeConvertedToExplicitExport = true)
public data class Pair<out A, out B>(
    public val first: A,
    public val second: B
) : Serializable
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Tuples.kt#L11)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val (a, b) = Pair(1, "x")
    println(a)
    println(b)
}
```

```text title="输出"
1
x
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/tuples.kt#L8)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
