# rangeUntil

`kotlin.ranges` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

创建一个不限名额的空域, 从 `Comparable` 值到指定的`that`值。

此值必须小于 `that` 值, 否则返回的范围将是空的 。

@sample 样本. ranges.Ranges.ranges. ranges. uniplicable

??? note "查看英文原文"

    Creates an open-ended range from this `Comparable` value to the specified `that` value.
    
    This value needs to be smaller than `that` value, otherwise the returned range will be empty.
    
    @sample samples.ranges.Ranges.rangeUntilComparable

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun <T : Comparable<T>> T.rangeUntil(that: T): OpenEndRange<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ranges/Ranges.kt#L60)

### 2. Common

```kotlin
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun Double.rangeUntil(that: Double): OpenEndRange<Double>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ranges/Ranges.kt#L163)

创建一个不限名额的空域, 从 `Double` 值到指定的`that`值。

根据IEEE-754,数字与这一范围末端进行了比较。

@sample 样本. ranges.Ranges.ranges.unittledouble

### 3. Common

```kotlin
@SinceKotlin("1.9")
@WasExperimental(ExperimentalStdlibApi::class)
public operator fun Float.rangeUntil(that: Float): OpenEndRange<Float>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ranges/Ranges.kt#L248)

创建一个不限名额的空域, 从 `Float` 值到指定的`that`值。

根据IEEE-754,数字与这一范围末端进行了比较。

@sample 样本. ranges.Ranges.ranges.untilFloat

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val start = Date.valueOf("2017-01-01")
    val end = Date.valueOf("2017-12-31")
    val range = start..<end
    println(range)

    println(Date.valueOf("2017-05-27") in range)
    println(Date.valueOf("2017-12-31") in range)
    println(Date.valueOf("2017-12-31") !in range)
}
```

```text title="输出"
2017-01-01..<2017-12-31
true
false
true
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L38)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val range = 1.0..<100.0
    println(range)

    println(3.14 in range)
    println(100.0 in range)
}
```

```text title="输出"
1.0..<100.0
true
false
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L59)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val range = 1f..<100f
    println(range)

    println(3.14f in range)
    println(100f in range)
}
```

```text title="输出"
1.0..<100.0
true
false
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L77)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
