# coerceAtMost

`kotlin.ranges` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

确保该值不超过指定的 `maximumValue` 。

@return 如果低于或等于`maximumValue`或`maximumValue`,则此值为@return。

@sample 样本.比较性可比较的Ops.coerceAt

??? note "查看英文原文"

    Ensures that this value is not greater than the specified `maximumValue`.
    
    @return this value if it's less than or equal to the `maximumValue` or the `maximumValue` otherwise.
    
    @sample samples.comparisons.ComparableOps.coerceAtMostComparable

## 声明与重载

### 1. Common

```kotlin
public fun <T : Comparable<T>> T.coerceAtMost(maximumValue: T): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1316)

### 2. Common

```kotlin
public fun Byte.coerceAtMost(maximumValue: Byte): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1327)

确保该值不超过指定的 `maximumValue` 。

@return 如果低于或等于`maximumValue`或`maximumValue`,则此值为@return。

@sample 样本.比较性比较性可比较有机物.腐蚀AtMost

### 3. Common

```kotlin
public fun Short.coerceAtMost(maximumValue: Short): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1338)

确保该值不超过指定的 `maximumValue` 。

@return 如果低于或等于`maximumValue`或`maximumValue`,则此值为@return。

@sample 样本.比较性比较性可比较有机物.腐蚀AtMost

### 4. Common

```kotlin
public fun Int.coerceAtMost(maximumValue: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1349)

确保该值不超过指定的 `maximumValue` 。

@return 如果低于或等于`maximumValue`或`maximumValue`,则此值为@return。

@sample 样本.比较性比较性可比较有机物.腐蚀AtMost

### 5. Common

```kotlin
public fun Long.coerceAtMost(maximumValue: Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1360)

确保该值不超过指定的 `maximumValue` 。

@return 如果低于或等于`maximumValue`或`maximumValue`,则此值为@return。

@sample 样本.比较性比较性可比较有机物.腐蚀AtMost

### 6. Common

```kotlin
public fun Float.coerceAtMost(maximumValue: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1371)

确保该值不超过指定的 `maximumValue` 。

@return 如果低于或等于`maximumValue`或`maximumValue`,则此值为@return。

@sample 样本.比较性比较性可比较有机物.腐蚀AtMost

### 7. Common

```kotlin
public fun Double.coerceAtMost(maximumValue: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1382)

确保该值不超过指定的 `maximumValue` 。

@return 如果低于或等于`maximumValue`或`maximumValue`,则此值为@return。

@sample 样本.比较性比较性可比较有机物.腐蚀AtMost

### 8. Common

```kotlin
@SinceKotlin("1.5")
public fun UInt.coerceAtMost(maximumValue: UInt): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L448)

确保该值不超过指定的 `maximumValue` 。

@return 如果低于或等于`maximumValue`或`maximumValue`,则此值为@return。

@sample 样本.比较性比较性可比较的Ops.coerceAtMotUnign

### 9. Common

```kotlin
@SinceKotlin("1.5")
public fun ULong.coerceAtMost(maximumValue: ULong): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L460)

确保该值不超过指定的 `maximumValue` 。

@return 如果低于或等于`maximumValue`或`maximumValue`,则此值为@return。

@sample 样本.比较性比较性可比较的Ops.coerceAtMotUnign

### 10. Common

```kotlin
@SinceKotlin("1.5")
public fun UByte.coerceAtMost(maximumValue: UByte): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L472)

确保该值不超过指定的 `maximumValue` 。

@return 如果低于或等于`maximumValue`或`maximumValue`,则此值为@return。

@sample 样本.比较性比较性可比较的Ops.coerceAtMotUnign

### 11. Common

```kotlin
@SinceKotlin("1.5")
public fun UShort.coerceAtMost(maximumValue: UShort): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L484)

确保该值不超过指定的 `maximumValue` 。

@return 如果低于或等于`maximumValue`或`maximumValue`,则此值为@return。

@sample 样本.比较性比较性可比较的Ops.coerceAtMotUnign

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    println(DayOfWeek.FRIDAY.coerceAtMost(DayOfWeek.SATURDAY))
    println(DayOfWeek.FRIDAY.coerceAtMost(DayOfWeek.WEDNESDAY))
}
```

```text title="输出"
FRIDAY
WEDNESDAY
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L55)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    println(10.coerceAtMost(5))
    println(10.coerceAtMost(20))
}
```

```text title="输出"
5
10
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L43)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    println(10u.coerceAtMost(5u))
    println(10u.coerceAtMost(20u))
}
```

```text title="输出"
5
10
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L49)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
