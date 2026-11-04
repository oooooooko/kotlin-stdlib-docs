# requireNoNulls

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回包含所有非 `null` 元素的原始收藏,如果有 `null` 元素,则投出 `IllegalArgumentException` 。

??? note "查看英文原文"

    Returns an original collection containing all the non-`null` elements, throwing an `IllegalArgumentException` if there are any `null` elements.

## 声明与重载

### 1. Common

```kotlin
public fun <T : Any> Array<T?>.requireNoNulls(): Array<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L26260)

### 2. Common

```kotlin
public fun <T : Any> Iterable<T?>.requireNoNulls(): Iterable<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3519)

### 3. Common

```kotlin
public fun <T : Any> List<T?>.requireNoNulls(): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3532)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*
import kotlin.math.pow
import kotlin.random.Random

fun testPlus(doPlus: (List<String>) -> List<String>) {
        val list = listOf("foo", "bar")
        val list2: List<String> = doPlus(list)
        println(list)
        println(list2)
    }

private fun testMinus(expected: List<String>? = null, doMinus: (List<String>) -> List<String>) {
        val a = listOf("foo", "bar", "bar")
        val b: List<String> = doMinus(a)
        val expected_ = expected ?: listOf("foo")
        println(b.toList())
    }

fun main() {

        val data = arrayListOf<String?>("foo", "bar")
        val notNull = data.requireNoNulls()
        println(notNull)

        val hasNulls = listOf("foo", null, "bar")

        assertFailsWith<IllegalArgumentException> {
            // should throw an exception as we have a null
            hasNulls.requireNoNulls()
        }
    
}
```

```text title="输出"
[foo, bar]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/CollectionTest.kt#L607)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
