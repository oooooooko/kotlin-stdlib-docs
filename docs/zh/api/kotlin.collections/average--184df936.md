# average

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回数组元素的平均值。

??? note "查看英文原文"

    Returns an average value of elements in the array.

## 声明与重载

### 1. Common

```kotlin
@kotlin.jvm.JvmName("averageOfByte")
public fun Array<out Byte>.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27702)

### 2. Common

```kotlin
@kotlin.jvm.JvmName("averageOfShort")
public fun Array<out Short>.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27716)

### 3. Common

```kotlin
@kotlin.jvm.JvmName("averageOfInt")
public fun Array<out Int>.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27730)

### 4. Common

```kotlin
@kotlin.jvm.JvmName("averageOfLong")
public fun Array<out Long>.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27744)

### 5. Common

```kotlin
@kotlin.jvm.JvmName("averageOfFloat")
public fun Array<out Float>.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27758)

### 6. Common

```kotlin
@kotlin.jvm.JvmName("averageOfDouble")
public fun Array<out Double>.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27772)

### 7. Common

```kotlin
public fun ByteArray.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27786)

### 8. Common

```kotlin
public fun ShortArray.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27799)

### 9. Common

```kotlin
public fun IntArray.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27812)

### 10. Common

```kotlin
public fun LongArray.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27825)

### 11. Common

```kotlin
public fun FloatArray.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27838)

### 12. Common

```kotlin
public fun DoubleArray.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27851)

### 13. Common

```kotlin
@kotlin.jvm.JvmName("averageOfByte")
public fun Iterable<Byte>.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3975)

返回收藏元素的平均值。

### 14. Common

```kotlin
@kotlin.jvm.JvmName("averageOfShort")
public fun Iterable<Short>.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3989)

返回收藏元素的平均值。

### 15. Common

```kotlin
@kotlin.jvm.JvmName("averageOfInt")
public fun Iterable<Int>.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L4003)

返回收藏元素的平均值。

### 16. Common

```kotlin
@kotlin.jvm.JvmName("averageOfLong")
public fun Iterable<Long>.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L4017)

返回收藏元素的平均值。

### 17. Common

```kotlin
@kotlin.jvm.JvmName("averageOfFloat")
public fun Iterable<Float>.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L4031)

返回收藏元素的平均值。

### 18. Common

```kotlin
@kotlin.jvm.JvmName("averageOfDouble")
public fun Iterable<Double>.average(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L4045)

返回收藏元素的平均值。

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
import kotlin.collections.*

fun main() {
    val source = arrayOf(1, 2, 3)
    val result = source.`average`()
    println(result)
}
```

```text title="输出"
2.0
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
