# shuffle

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

随机地在位置上打乱此数组中的元素 。

??? note "查看英文原文"

    Randomly shuffles elements in this array in-place.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public fun <T> Array<T>.shuffle(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7182)

### 2. Common

```kotlin
@SinceKotlin("1.4")
public fun ByteArray.shuffle(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7190)

### 3. Common

```kotlin
@SinceKotlin("1.4")
public fun ShortArray.shuffle(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7198)

### 4. Common

```kotlin
@SinceKotlin("1.4")
public fun IntArray.shuffle(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7206)

### 5. Common

```kotlin
@SinceKotlin("1.4")
public fun LongArray.shuffle(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7214)

### 6. Common

```kotlin
@SinceKotlin("1.4")
public fun FloatArray.shuffle(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7222)

### 7. Common

```kotlin
@SinceKotlin("1.4")
public fun DoubleArray.shuffle(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7230)

### 8. Common

```kotlin
@SinceKotlin("1.4")
public fun BooleanArray.shuffle(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7238)

### 9. Common

```kotlin
@SinceKotlin("1.4")
public fun CharArray.shuffle(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7246)

### 10. Common

```kotlin
@SinceKotlin("1.4")
public fun <T> Array<T>.shuffle(random: Random): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7254)

使用指定的 `random` 实例作为随机性源随机地随机打乱此数组中的元素。

见:[现代的Fisher-Yates打乱算法](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm).)

### 11. Common

```kotlin
@SinceKotlin("1.4")
public fun ByteArray.shuffle(random: Random): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7269)

使用指定的 `random` 实例作为随机性源随机地随机打乱此数组中的元素。

见:[现代的Fisher-Yates打乱算法](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm).)

### 12. Common

```kotlin
@SinceKotlin("1.4")
public fun ShortArray.shuffle(random: Random): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7284)

使用指定的 `random` 实例作为随机性源随机地随机打乱此数组中的元素。

见:[现代的Fisher-Yates打乱算法](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm).)

### 13. Common

```kotlin
@SinceKotlin("1.4")
public fun IntArray.shuffle(random: Random): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7299)

使用指定的 `random` 实例作为随机性源随机地随机打乱此数组中的元素。

见:[现代的Fisher-Yates打乱算法](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm).)

### 14. Common

```kotlin
@SinceKotlin("1.4")
public fun LongArray.shuffle(random: Random): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7314)

使用指定的 `random` 实例作为随机性源随机地随机打乱此数组中的元素。

见:[现代的Fisher-Yates打乱算法](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm).)

### 15. Common

```kotlin
@SinceKotlin("1.4")
public fun FloatArray.shuffle(random: Random): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7329)

使用指定的 `random` 实例作为随机性源随机地随机打乱此数组中的元素。

见:[现代的Fisher-Yates打乱算法](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm).)

### 16. Common

```kotlin
@SinceKotlin("1.4")
public fun DoubleArray.shuffle(random: Random): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7344)

使用指定的 `random` 实例作为随机性源随机地随机打乱此数组中的元素。

见:[现代的Fisher-Yates打乱算法](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm).)

### 17. Common

```kotlin
@SinceKotlin("1.4")
public fun BooleanArray.shuffle(random: Random): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7359)

使用指定的 `random` 实例作为随机性源随机地随机打乱此数组中的元素。

见:[现代的Fisher-Yates打乱算法](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm).)

### 18. Common

```kotlin
@SinceKotlin("1.4")
public fun CharArray.shuffle(random: Random): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L7374)

使用指定的 `random` 实例作为随机性源随机地随机打乱此数组中的元素。

见:[现代的Fisher-Yates打乱算法](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm).)

### 19. Common

```kotlin
@SinceKotlin("1.3")
public fun <T> MutableList<T>.shuffle(random: Random): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1158)

使用指定的 `random` 实例作为随机性源随机地随机打乱此列表中的元素。

见:[现代的Fisher-Yates打乱算法](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm).)

### 20. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UIntArray.shuffle(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3443)

### 21. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun ULongArray.shuffle(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3452)

### 22. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UByteArray.shuffle(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3461)

### 23. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UShortArray.shuffle(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3470)

### 24. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UIntArray.shuffle(random: Random): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3479)

使用指定的 `random` 实例作为随机性源随机地随机打乱此数组中的元素。

见:[现代的Fisher-Yates打乱算法](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm).)

### 25. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun ULongArray.shuffle(random: Random): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3495)

使用指定的 `random` 实例作为随机性源随机地随机打乱此数组中的元素。

见:[现代的Fisher-Yates打乱算法](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm).)

### 26. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UByteArray.shuffle(random: Random): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3511)

使用指定的 `random` 实例作为随机性源随机地随机打乱此数组中的元素。

见:[现代的Fisher-Yates打乱算法](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm).)

### 27. Common

```kotlin
@SinceKotlin("1.4")
@ExperimentalUnsignedTypes
public fun UShortArray.shuffle(random: Random): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L3527)

使用指定的 `random` 实例作为随机性源随机地随机打乱此数组中的元素。

见:[现代的Fisher-Yates打乱算法](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm).)

### 28. Common

```kotlin
@SinceKotlin("1.2")
public expect fun <T> MutableList<T>.shuffle(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/CollectionsH.kt#L36)

随机地将列表中的元素打乱 。

见:[现代的Fisher-Yates打乱算法](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm).)

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
    val result = source.`shuffle`()
    println(result)
}
```

```text title="输出"
kotlin.Unit
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
