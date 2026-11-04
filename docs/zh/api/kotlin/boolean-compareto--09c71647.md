# Boolean.compareTo

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将此 `Boolean` 与指定的 `Boolean`Z`other` 排序比较 。 如果两者对等,则返回为零,
如果`this``Boolean`是`false`,`other`是`true`,则为负数。
如果`this``Boolean`是`true`,而`other`是`false`,则为正数。

换句话说, `false` 被认为是“低于” `true` 。

@sample 样本.misc.Boolean样本比较

??? note "查看英文原文"

    Compares this `Boolean` with the specified `Boolean``other` for order. Returns zero if both are equal to each other,
    a negative number if `this``Boolean` is `false` and `other` is `true`,
    or a positive number if `this``Boolean` is `true` and `other` is `false`.
    
    In other words, `false` is considered to be "less than" `true`.
    
    @sample samples.misc.BooleanSamples.compareTo

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.IntrinsicConstEvaluation
    public override fun compareTo(other: Boolean): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Boolean.kt#L38)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.assertTrue



fun main() {
    // false is equal to false, and true is equal to true
    println(false.compareTo(false))
    println(true.compareTo(true))

    // But false is less than true, and true is greater than false
    println(false.compareTo(true) < 0)
    println(true.compareTo(false) > 0)
}
```

```text title="输出"
0
0
true
true
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/BooleanSamples.kt#L12)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
