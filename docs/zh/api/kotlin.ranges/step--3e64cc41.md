# step

`kotlin.ranges` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个递进,该递进与给定步骤的幅度相同。

@sample 样本. ranges.Ranges.step Int

??? note "查看英文原文"

    Returns a progression that goes over the same range with the given step.
    
    @sample samples.ranges.Ranges.stepInt

## 声明与重载

### 1. Common

```kotlin
public infix fun IntProgression.step(step: Int): IntProgression
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L992)

### 2. Common

```kotlin
public infix fun LongProgression.step(step: Long): LongProgression
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1002)

返回一个递进,该递进与给定步骤的幅度相同。

@sample 样本. ranges.Ranges.stepLong

### 3. Common

```kotlin
public infix fun CharProgression.step(step: Int): CharProgression
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L1012)

返回一个递进,该递进与给定步骤的幅度相同。

@sample 样本. ranges.Ranges.stepChar

### 4. Common

```kotlin
@SinceKotlin("1.5")
public infix fun UIntProgression.step(step: Int): UIntProgression
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L334)

返回一个递进,该递进与给定步骤的幅度相同。

@sample 样本. ranges.Ranges.stepUint

### 5. Common

```kotlin
@SinceKotlin("1.5")
public infix fun ULongProgression.step(step: Long): ULongProgression
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L345)

返回一个递进,该递进与给定步骤的幅度相同。

@sample 样本. ranges.Ranges.stepULong

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val ascendingProgression = 1..6 step 2
    val descendingProgression = 6 downTo 1 step 2
    println(ascendingProgression.toList())
    println(descendingProgression.toList())
}
```

```text title="输出"
[1, 3, 5]
[6, 4, 2]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L86)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val ascendingProgression = 1L..6L step 2L
    val descendingProgression = 6L downTo 1L step 2L
    println(ascendingProgression.toList())
    println(descendingProgression.toList())
}
```

```text title="输出"
[1, 3, 5]
[6, 4, 2]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L102)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val ascendingProgression = 'a'..'f' step 2
    val descendingProgression = 'f' downTo 'a' step 2
    println(ascendingProgression.toList())
    println(descendingProgression.toList())
}
```

```text title="输出"
[a, c, e]
[f, d, b]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L118)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val ascendingProgression = 1u..6u step 2
    val descendingProgression = 6u downTo 1u step 2
    println(ascendingProgression.toList())
    println(descendingProgression.toList())
}
```

```text title="输出"
[1, 3, 5]
[6, 4, 2]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L94)

### 示例 5 · JVM

```kotlin title="示例 5" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import java.sql.Date
import kotlin.test.assertFalse
import kotlin.test.assertTrue



fun main() {
    val ascendingProgression = 1UL..6UL step 2L
    val descendingProgression = 6UL downTo 1UL step 2L
    println(ascendingProgression.toList())
    println(descendingProgression.toList())
}
```

```text title="输出"
[1, 3, 5]
[6, 4, 2]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/ranges/ranges.kt#L110)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
