# Triple

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

代表三组数值

与该类中值没有关联, 任何用途都可以使用。 三重物证价值的语义学, 即所有三个组成部分都相等时, 两重三重是等的。 将其分解成值的例子 : @sample 样本. misc. Tuples. tripleDestructioning

@param 一种第一值 @param B 第二类 @param C 三种 @param C 第一类 @property 第一值 @property 第二类 @property 第三次 三级 @property

??? note "查看英文原文"

    Represents a triad of values
    
    There is no meaning attached to values in this class, it can be used for any purpose.
    Triple exhibits value semantics, i.e. two triples are equal if all three components are equal.
    An example of decomposing it into values:
    @sample samples.misc.Tuples.tripleDestructuring
    
    @param A type of the first value.
    @param B type of the second value.
    @param C type of the third value.
    @property first First value.
    @property second Second value.
    @property third Third value.

## 声明与重载

### 1. Common

```kotlin
@kotlin.js.JsImplicitExport(couldBeConvertedToExplicitExport = true)
public data class Triple<out A, out B, out C>(
    public val first: A,
    public val second: B,
    public val third: C
) : Serializable
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Tuples.kt#L52)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val (a, b, c) = Triple(2, "x", listOf(null))
    println(a)
    println(b)
    println(c)
}
```

```text title="输出"
2
x
[null]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/tuples.kt#L15)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
