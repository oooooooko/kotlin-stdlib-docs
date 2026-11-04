# rangeTo

`kotlin.ranges` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

创建从`Comparable`值到指定的`that`值之间的范围。

此值必须小于或等于 `that` 值, 否则返回的范围将是空的 。

@sample 样本.ranges.Ranges.ranges.ranges.ranges to comparable

??? note "查看英文原文"

    Creates a range from this `Comparable` value to the specified `that` value.
    
    This value needs to be smaller than or equal to `that` value, otherwise the returned range will be empty.
    
    @sample samples.ranges.Ranges.rangeToComparable

## 声明与重载

### 1. Common

```kotlin
public operator fun <T : Comparable<T>> T.rangeTo(that: T): ClosedRange<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ranges/Ranges.kt#L31)

### 2. Common

```kotlin
@SinceKotlin("1.1")
public operator fun Double.rangeTo(that: Double): ClosedFloatingPointRange<Double>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ranges/Ranges.kt#L122)

创建从`Double`值到指定的`that`值之间的范围。

根据IEEE-754,数字与这一范围末端进行了比较。

@sample 样本. ranges.Ranges.Ranges.range todouble

### 3. Common

```kotlin
@SinceKotlin("1.1")
public operator fun Float.rangeTo(that: Float): ClosedFloatingPointRange<Float>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ranges/Ranges.kt#L206)

创建从`Float`值到指定的`that`值之间的范围。

根据IEEE-754,数字与这一范围末端进行了比较。

@sample 样本. ranges.Ranges.range toFloat

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
    val range = start..end
    println(range)

    println(Date.valueOf("2017-05-27") in range)
    println(Date.valueOf("2018-01-01") in range)
    println(Date.valueOf("2018-01-01") !in range)
}
```

```text title="输出"
2017-01-01..2017-12-31
true
false
true
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L26)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val range = 1.0..100.0
    println(range)

    println(3.14 in range)
    println(100.1 in range)
}
```

```text title="输出"
1.0..100.0
true
false
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L50)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val range = 1f..100f
    println(range)

    println(3.14f in range)
    println(100.1f in range)
}
```

```text title="输出"
1.0..100.0
true
false
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L68)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
