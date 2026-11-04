# coerceAtLeast

`kotlin.ranges` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

确保该值不低于指定的 `minimumValue` 。

@return 如果大于或等于 `minimumValue` 或`minimumValue`,则此值。

@sample 样本.比较性可比较的Ops.coerceAtLonet

??? note "查看英文原文"

    Ensures that this value is not less than the specified `minimumValue`.
    
    @return this value if it's greater than or equal to the `minimumValue` or the `minimumValue` otherwise.
    
    @sample samples.comparisons.ComparableOps.coerceAtLeastComparable

## 声明与重载

### 1. Common

```kotlin
public fun <T : Comparable<T>> T.coerceAtLeast(minimumValue: T): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1239)

### 2. Common

```kotlin
public fun Byte.coerceAtLeast(minimumValue: Byte): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1250)

确保该值不低于指定的 `minimumValue` 。

@return 如果大于或等于 `minimumValue` 或`minimumValue`,则此值。

@sample 样本.比较性比较性可比较有机物.冷却

### 3. Common

```kotlin
public fun Short.coerceAtLeast(minimumValue: Short): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1261)

确保该值不低于指定的 `minimumValue` 。

@return 如果大于或等于 `minimumValue` 或`minimumValue`,则此值。

@sample 样本.比较性比较性可比较有机物.冷却

### 4. Common

```kotlin
public fun Int.coerceAtLeast(minimumValue: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1272)

确保该值不低于指定的 `minimumValue` 。

@return 如果大于或等于 `minimumValue` 或`minimumValue`,则此值。

@sample 样本.比较性比较性可比较有机物.冷却

### 5. Common

```kotlin
public fun Long.coerceAtLeast(minimumValue: Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1283)

确保该值不低于指定的 `minimumValue` 。

@return 如果大于或等于 `minimumValue` 或`minimumValue`,则此值。

@sample 样本.比较性比较性可比较有机物.冷却

### 6. Common

```kotlin
public fun Float.coerceAtLeast(minimumValue: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1294)

确保该值不低于指定的 `minimumValue` 。

@return 如果大于或等于 `minimumValue` 或`minimumValue`,则此值。

@sample 样本.比较性比较性可比较有机物.冷却

### 7. Common

```kotlin
public fun Double.coerceAtLeast(minimumValue: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1305)

确保该值不低于指定的 `minimumValue` 。

@return 如果大于或等于 `minimumValue` 或`minimumValue`,则此值。

@sample 样本.比较性比较性可比较有机物.冷却

### 8. Common

```kotlin
@SinceKotlin("1.5")
public fun UInt.coerceAtLeast(minimumValue: UInt): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L400)

确保该值不低于指定的 `minimumValue` 。

@return 如果大于或等于 `minimumValue` 或`minimumValue`,则此值。

@sample 样本.比较性比较性可比较的有机物. 冷却

### 9. Common

```kotlin
@SinceKotlin("1.5")
public fun ULong.coerceAtLeast(minimumValue: ULong): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L412)

确保该值不低于指定的 `minimumValue` 。

@return 如果大于或等于 `minimumValue` 或`minimumValue`,则此值。

@sample 样本.比较性比较性可比较的有机物. 冷却

### 10. Common

```kotlin
@SinceKotlin("1.5")
public fun UByte.coerceAtLeast(minimumValue: UByte): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L424)

确保该值不低于指定的 `minimumValue` 。

@return 如果大于或等于 `minimumValue` 或`minimumValue`,则此值。

@sample 样本.比较性比较性可比较的有机物. 冷却

### 11. Common

```kotlin
@SinceKotlin("1.5")
public fun UShort.coerceAtLeast(minimumValue: UShort): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L436)

确保该值不低于指定的 `minimumValue` 。

@return 如果大于或等于 `minimumValue` 或`minimumValue`,则此值。

@sample 样本.比较性比较性可比较的有机物. 冷却

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    println(DayOfWeek.WEDNESDAY.coerceAtLeast(DayOfWeek.MONDAY))
    println(DayOfWeek.WEDNESDAY.coerceAtLeast(DayOfWeek.FRIDAY))
}
```

```text title="输出"
WEDNESDAY
FRIDAY
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L37)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    println(10.coerceAtLeast(5))
    println(10.coerceAtLeast(20))
}
```

```text title="输出"
10
20
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L25)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    println(10u.coerceAtLeast(5u))
    println(10u.coerceAtLeast(20u))
}
```

```text title="输出"
10
20
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L31)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
