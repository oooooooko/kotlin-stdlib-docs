# coerceIn

`kotlin.ranges` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

确保该值位于指定的范围 `minimumValue`.`maximumValue`。

@return 如果值在范围之内,则该值为`minimumValue`,如果该值小于`minimumValue`,则为`minimumValue`,如果该值大于80 000005,则为`maximumValue`。

@sample 样本.比较性比较性可比较的有机物. 腐蚀性

??? note "查看英文原文"

    Ensures that this value lies in the specified range `minimumValue`..`maximumValue`.
    
    @return this value if it's in the range, or `minimumValue` if this value is less than `minimumValue`, or `maximumValue` if this value is greater than `maximumValue`.
    
    @sample samples.comparisons.ComparableOps.coerceInComparable

## 声明与重载

### 1. Common

```kotlin
public fun <T : Comparable<T>> T.coerceIn(minimumValue: T?, maximumValue: T?): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1393)

### 2. Common

```kotlin
public fun Byte.coerceIn(minimumValue: Byte, maximumValue: Byte): Byte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1413)

确保该值位于指定的范围 `minimumValue`.`maximumValue`。

@return 如果值在范围之内,则该值为`minimumValue`,如果该值小于`minimumValue`,则为`minimumValue`,如果该值大于80 000005,则为`maximumValue`。

@sample 样本.比较性比较性可比较有机物.腐蚀In

### 3. Common

```kotlin
public fun Short.coerceIn(minimumValue: Short, maximumValue: Short): Short
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1427)

确保该值位于指定的范围 `minimumValue`.`maximumValue`。

@return 如果值在范围之内,则该值为`minimumValue`,如果该值小于`minimumValue`,则为`minimumValue`,如果该值大于80 000005,则为`maximumValue`。

@sample 样本.比较性比较性可比较有机物.腐蚀In

### 4. Common

```kotlin
public fun Int.coerceIn(minimumValue: Int, maximumValue: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1441)

确保该值位于指定的范围 `minimumValue`.`maximumValue`。

@return 如果值在范围之内,则该值为`minimumValue`,如果该值小于`minimumValue`,则为`minimumValue`,如果该值大于80 000005,则为`maximumValue`。

@sample 样本.比较性比较性可比较有机物.腐蚀In

### 5. Common

```kotlin
public fun Long.coerceIn(minimumValue: Long, maximumValue: Long): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1455)

确保该值位于指定的范围 `minimumValue`.`maximumValue`。

@return 如果值在范围之内,则该值为`minimumValue`,如果该值小于`minimumValue`,则为`minimumValue`,如果该值大于80 000005,则为`maximumValue`。

@sample 样本.比较性比较性可比较有机物.腐蚀In

### 6. Common

```kotlin
public fun Float.coerceIn(minimumValue: Float, maximumValue: Float): Float
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1469)

确保该值位于指定的范围 `minimumValue`.`maximumValue`。

@return 如果值在范围之内,则该值为`minimumValue`,如果该值小于`minimumValue`,则为`minimumValue`,如果该值大于80 000005,则为`maximumValue`。

@sample 样本.比较性比较性可比较有机物.腐蚀In

### 7. Common

```kotlin
public fun Double.coerceIn(minimumValue: Double, maximumValue: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1483)

确保该值位于指定的范围 `minimumValue`.`maximumValue`。

@return 如果值在范围之内,则该值为`minimumValue`,如果该值小于`minimumValue`,则为`minimumValue`,如果该值大于80 000005,则为`maximumValue`。

@sample 样本.比较性比较性可比较有机物.腐蚀In

### 8. Common

```kotlin
@SinceKotlin("1.1")
public fun <T : Comparable<T>> T.coerceIn(range: ClosedFloatingPointRange<T>): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1497)

确保这一数值为指定的 `range` 。

@return 如果值为`range`, 则值为 `range.start` , 如果值低于`range.start`, 则值为`range.start`, 如果值大于`range.endInclusive`, 则值为`range.endInclusive`。

@sample 样本.比较性比较性可比较的Ops.coerce InFloingPointRange

### 9. Common

```kotlin
public fun <T : Comparable<T>> T.coerceIn(range: ClosedRange<T>): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1516)

确保这一数值为指定的 `range` 。

@return 如果值为`range`, 则值为 `range.start` , 如果值低于`range.start`, 则值为`range.start`, 如果值大于`range.endInclusive`, 则值为`range.endInclusive`。

@sample 样本.比较性比较性可比较的有机物. 腐蚀性

### 10. Common

```kotlin
public fun Int.coerceIn(range: ClosedRange<Int>): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1535)

确保这一数值为指定的 `range` 。

@return 如果值为`range`, 则值为 `range.start` , 如果值低于`range.start`, 则值为`range.start`, 如果值大于`range.endInclusive`, 则值为`range.endInclusive`。

@sample 样本.比较性比较性可比较有机物.腐蚀In

### 11. Common

```kotlin
public fun Long.coerceIn(range: ClosedRange<Long>): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1554)

确保这一数值为指定的 `range` 。

@return 如果值为`range`, 则值为 `range.start` , 如果值低于`range.start`, 则值为`range.start`, 如果值大于`range.endInclusive`, 则值为`range.endInclusive`。

@sample 样本.比较性比较性可比较有机物.腐蚀In

### 12. Common

```kotlin
@SinceKotlin("1.5")
public fun UInt.coerceIn(minimumValue: UInt, maximumValue: UInt): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L496)

确保该值位于指定的范围 `minimumValue`.`maximumValue`。

@return 如果值在范围之内,则该值为`minimumValue`,如果该值小于`minimumValue`,则为`minimumValue`,如果该值大于80 000005,则为`maximumValue`。

@sample 样本.比较性比较性可比较的有机物. COERCE

### 13. Common

```kotlin
@SinceKotlin("1.5")
public fun ULong.coerceIn(minimumValue: ULong, maximumValue: ULong): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L511)

确保该值位于指定的范围 `minimumValue`.`maximumValue`。

@return 如果值在范围之内,则该值为`minimumValue`,如果该值小于`minimumValue`,则为`minimumValue`,如果该值大于80 000005,则为`maximumValue`。

@sample 样本.比较性比较性可比较的有机物. COERCE

### 14. Common

```kotlin
@SinceKotlin("1.5")
public fun UByte.coerceIn(minimumValue: UByte, maximumValue: UByte): UByte
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L526)

确保该值位于指定的范围 `minimumValue`.`maximumValue`。

@return 如果值在范围之内,则该值为`minimumValue`,如果该值小于`minimumValue`,则为`minimumValue`,如果该值大于80 000005,则为`maximumValue`。

@sample 样本.比较性比较性可比较的有机物. COERCE

### 15. Common

```kotlin
@SinceKotlin("1.5")
public fun UShort.coerceIn(minimumValue: UShort, maximumValue: UShort): UShort
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L541)

确保该值位于指定的范围 `minimumValue`.`maximumValue`。

@return 如果值在范围之内,则该值为`minimumValue`,如果该值小于`minimumValue`,则为`minimumValue`,如果该值大于80 000005,则为`maximumValue`。

@sample 样本.比较性比较性可比较的有机物. COERCE

### 16. Common

```kotlin
@SinceKotlin("1.5")
public fun UInt.coerceIn(range: ClosedRange<UInt>): UInt
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L556)

确保这一数值为指定的 `range` 。

@return 如果值为`range`, 则值为 `range.start` , 如果值低于`range.start`, 则值为`range.start`, 如果值大于`range.endInclusive`, 则值为`range.endInclusive`。

@sample 样本.比较性比较性可比较的有机物. COERCE

### 17. Common

```kotlin
@SinceKotlin("1.5")
public fun ULong.coerceIn(range: ClosedRange<ULong>): ULong
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L576)

确保这一数值为指定的 `range` 。

@return 如果值为`range`, 则值为 `range.start` , 如果值低于`range.start`, 则值为`range.start`, 如果值大于`range.endInclusive`, 则值为`range.endInclusive`。

@sample 样本.比较性比较性可比较的有机物. COERCE

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    val workingDays = DayOfWeek.MONDAY..DayOfWeek.FRIDAY
    println(DayOfWeek.WEDNESDAY.coerceIn(workingDays))
    println(DayOfWeek.SATURDAY.coerceIn(workingDays))

    println(DayOfWeek.FRIDAY.coerceIn(DayOfWeek.SATURDAY, DayOfWeek.SUNDAY))
}
```

```text title="输出"
WEDNESDAY
FRIDAY
SATURDAY
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L83)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    println(10.coerceIn(1, 100))
    println(10.coerceIn(1..100))
    println(0.coerceIn(1, 100))
    println(500.coerceIn(1, 100))
    assertFailsWith<IllegalArgumentException> {
        10.coerceIn(100, 0)
    }
}
```

```text title="输出"
10
10
1
100
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L61)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    println(10.1.coerceIn(1.0..10.0))
    println(9.9.coerceIn(1.0..10.0))

    assertFailsWith<IllegalArgumentException> { 9.9.coerceIn(1.0..Double.NaN) }
}
```

```text title="输出"
10.0
9.9
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L92)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.time.DayOfWeek
import kotlin.test.assertFailsWith



fun main() {
    println(10u.coerceIn(1u, 100u))
    println(10u.coerceIn(1u..100u))
    println(0u.coerceIn(1u, 100u))
    println(500u.coerceIn(1u, 100u))
    assertFailsWith<IllegalArgumentException> {
        10u.coerceIn(100u, 0u)
    }
}
```

```text title="输出"
10
10
1
100
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparableOps.kt#L72)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
