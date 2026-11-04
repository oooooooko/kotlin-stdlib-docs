# until

`kotlin.ranges` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

a 返回从此值到但排除指定的`to`值的数值。

如果`to`值小于或等于`this`值,则返回的范围为空。

??? note "查看英文原文"

    Returns a range from this value up to but excluding the specified `to` value.
    
    If the `to` value is less than or equal to `this` value, then the returned range is empty.

## 声明与重载

### 1. Common

```kotlin
public infix fun Int.until(to: Byte): IntRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1078)

### 2. Common

```kotlin
public infix fun Long.until(to: Byte): LongRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1087)

### 3. Common

```kotlin
public infix fun Byte.until(to: Byte): IntRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1096)

### 4. Common

```kotlin
public infix fun Short.until(to: Byte): IntRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1105)

### 5. Common

```kotlin
public infix fun Char.until(to: Char): CharRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1114)

### 6. Common

```kotlin
public infix fun Int.until(to: Int): IntRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1124)

### 7. Common

```kotlin
public infix fun Long.until(to: Int): LongRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1134)

### 8. Common

```kotlin
public infix fun Byte.until(to: Int): IntRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1143)

### 9. Common

```kotlin
public infix fun Short.until(to: Int): IntRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1153)

### 10. Common

```kotlin
public infix fun Int.until(to: Long): LongRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1163)

### 11. Common

```kotlin
public infix fun Long.until(to: Long): LongRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1173)

### 12. Common

```kotlin
public infix fun Byte.until(to: Long): LongRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1183)

### 13. Common

```kotlin
public infix fun Short.until(to: Long): LongRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1193)

### 14. Common

```kotlin
public infix fun Int.until(to: Short): IntRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1203)

### 15. Common

```kotlin
public infix fun Long.until(to: Short): LongRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1212)

### 16. Common

```kotlin
public infix fun Byte.until(to: Short): IntRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1221)

### 17. Common

```kotlin
public infix fun Short.until(to: Short): IntRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1230)

### 18. Common

```kotlin
@SinceKotlin("1.5")
public infix fun UByte.until(to: UByte): UIntRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L356)

### 19. Common

```kotlin
@SinceKotlin("1.5")
public infix fun UInt.until(to: UInt): UIntRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L367)

### 20. Common

```kotlin
@SinceKotlin("1.5")
public infix fun ULong.until(to: ULong): ULongRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L378)

### 21. Common

```kotlin
@SinceKotlin("1.5")
public infix fun UShort.until(to: UShort): UIntRange
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L389)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.ranges.*

fun main() {
    val source = 5
    val result = source.`until`(2.toByte())
    println(result)
}
```

```text title="输出"
5..1
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
