# lastOrNull

`kotlin.ranges` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果递进为空,返回最后一个元素,或 `null` 。

@sample 样本、采集的样本、采集的样本、采集的样本、元素、最后元素

??? note "查看英文原文"

    Returns the last element, or `null` if the progression is empty.
    
    @sample samples.collections.Collections.Elements.last

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.7")
public fun IntProgression.lastOrNull(): Int?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L122)

### 2. Common

```kotlin
@SinceKotlin("1.7")
public fun LongProgression.lastOrNull(): Long?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L132)

### 3. Common

```kotlin
@SinceKotlin("1.7")
public fun CharProgression.lastOrNull(): Char?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Ranges.kt#L142)

### 4. Common

```kotlin
@SinceKotlin("1.7")
public fun UIntProgression.lastOrNull(): UInt?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L88)

### 5. Common

```kotlin
@SinceKotlin("1.7")
public fun ULongProgression.lastOrNull(): ULong?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_URanges.kt#L98)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*
import kotlin.test.*



fun main() {
    val list = listOf(1, 2, 3, 4)
    println(list.last())
    println(list.last { it % 2 == 1 })
    println(list.lastOrNull { it < 0 })
    assertFails { list.last { it < 0 } }

    val emptyList = emptyList<Int>()
    println(emptyList.lastOrNull())
    assertFails { emptyList.last() }
}
```

```text title="输出"
4
3
null
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L1368)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
