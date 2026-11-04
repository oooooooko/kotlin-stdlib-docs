# OpenEndRange.contains

`kotlin.ranges` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

检查指定的 `value` 是否属于此范围。

一个数值如果大于或等于 `start` 约束值,且严格少于`endExclusive`约束值,则属于无限制范围。

@sample 样本. ranges.Ranges.OpenENDRange Contains

??? note "查看英文原文"

    Checks whether the specified `value` belongs to the range.
    
    A value belongs to the open-ended range if it is greater than or equal to the `start` bound and strictly less than the `endExclusive` bound.
    
    @sample samples.ranges.Ranges.openEndRangeContains

## 声明与重载

### 1. Common

```kotlin
public operator fun contains(value: T): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ranges/Range.kt#L62)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val range = 1..<10
    println(5 in range)
    // The range includes the lower bound, but the upper bound is excluded
    println(1 in range)
    println(10 in range)
    println(9 in range)
    // Values lying outside bounds are not contained within the range
    println(0 in range)
    println(11 in range)

    val stringRange = "AA"..<"ZZ"
    println("AA" in stringRange)
    println("AB" in stringRange)
    println("ZZ" in stringRange)
    // Note that "contains" relies on "compareTo" implementation, so in some cases results may not be intuitive.
    // Here, "ZYX" is lexicographically greater than "AA", but lower than "ZZ", thus the range contains it.
    println("ZYX" in stringRange)
}
```

```text title="输出"
true
true
false
true
false
false
true
true
false
true
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L160)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
