# toCollection

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将所有元素附加到给定的 `destination` 收藏中。

??? note "查看英文原文"

    Appends all elements to the given `destination` collection.

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
public fun <T, C : MutableCollection<in T>> Array<out T>.toCollection(destination: C): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11256)

### 2. Common

```kotlin
@IgnorableReturnValue
public fun <C : MutableCollection<in Byte>> ByteArray.toCollection(destination: C): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11267)

### 3. Common

```kotlin
@IgnorableReturnValue
public fun <C : MutableCollection<in Short>> ShortArray.toCollection(destination: C): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11278)

### 4. Common

```kotlin
@IgnorableReturnValue
public fun <C : MutableCollection<in Int>> IntArray.toCollection(destination: C): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11289)

### 5. Common

```kotlin
@IgnorableReturnValue
public fun <C : MutableCollection<in Long>> LongArray.toCollection(destination: C): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11300)

### 6. Common

```kotlin
@IgnorableReturnValue
public fun <C : MutableCollection<in Float>> FloatArray.toCollection(destination: C): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11311)

### 7. Common

```kotlin
@IgnorableReturnValue
public fun <C : MutableCollection<in Double>> DoubleArray.toCollection(destination: C): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11322)

### 8. Common

```kotlin
@IgnorableReturnValue
public fun <C : MutableCollection<in Boolean>> BooleanArray.toCollection(destination: C): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11333)

### 9. Common

```kotlin
@IgnorableReturnValue
public fun <C : MutableCollection<in Char>> CharArray.toCollection(destination: C): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L11344)

### 10. Common

```kotlin
@IgnorableReturnValue
public fun <T, C : MutableCollection<in T>> Iterable<T>.toCollection(destination: C): C
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L1480)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.random.Random
import kotlin.random.nextInt
import kotlin.test.*

fun <T, C : MutableCollection<T>> testOperation(before: List<T>, after: List<T>, expectedModified: Boolean, toMutableCollection: (List<T>) -> C) =
        fun(operation: (C.() -> Boolean)) {
            val list = toMutableCollection(before)
            println(list.operation())
            println(list)
        }

fun <T> testOperation(before: List<T>, after: List<T>, expectedModified: Boolean) =
        testOperation(before, after, expectedModified, { it.toMutableList() })

private fun <T> forAllStandardMutableLists(data: List<T>, block: (MutableList<T>) -> Unit) {
        block(data.toMutableList())
        block(ArrayDeque(data))
        buildList {
            addAll(data)
            block(this)
        }
    }

fun main() {

        val data = listOf("foo", "bar")

        testOperation(emptyList(), data, true).let { assertAdd ->
            assertAdd { addAll(data) }
            assertAdd { addAll(data.toTypedArray()) }
            assertAdd { addAll(data.toTypedArray().asIterable()) }
            assertAdd { addAll(data.asSequence()) }
        }

        testOperation(data, data, false, { it.toCollection(LinkedHashSet()) }).let { assertAdd ->
            assertAdd { addAll(data) }
            assertAdd { addAll(data.toTypedArray()) }
            assertAdd { addAll(data.toTypedArray().asIterable()) }
            assertAdd { addAll(data.asSequence()) }
        }
    
}
```

```text title="输出"
true
[foo, bar]
true
[foo, bar]
true
[foo, bar]
true
[foo, bar]
false
[foo, bar]
false
[foo, bar]
false
[foo, bar]
false
[foo, bar]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/MutableCollectionsTest.kt#L25)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
