# toULongArray

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回包含此通用数组全部元素的ULong 数组。

??? note "查看英文原文"

    Returns an array of ULong containing all of the elements of this generic array.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun Array<out ULong>.toULongArray(): ULongArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4979)

### 2. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@kotlin.internal.InlineOnly
public inline fun LongArray.toULongArray(): ULongArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UArrays.kt#L4988)

返回`ULongArray`类型的一个数组,这是此数组的复制件,其中每个元素都是对本数组相应元素的未指派重新解释。

### 3. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun Collection<ULong>.toULongArray(): ULongArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_UCollections.kt#L48)

返回包含此收藏全部元素的 ULong 数组。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*

private class OperationOnRange<E, R>(
        val element: E,
        val fromIndex: Int,
        val toIndex: Int,
        val expectedResult: R
    )

private fun UIntArray.toUByteArray(): UByteArray {
    return UByteArray(size) { get(it).toUByte() }
}

private fun UIntArray.toUShortArray(): UShortArray {
    return UShortArray(size) { get(it).toUShort() }
}

private fun UIntArray.toULongArray(): ULongArray {
    return ULongArray(size) { get(it).toULong() }
}

fun main() {

        val uintList = listOf(1u, 2u, 3u)
        val uintArray: UIntArray = uintList.toUIntArray()
        expect(3) { uintArray.size }
        println(uintArray.toList())

        val genericArray: Array<ULong> = arrayOf<ULong>(1u, 2u, 3u)
        val ulongArray: ULongArray = genericArray.toULongArray()
        expect(3) { ulongArray.size }
        println(ulongArray.toList())
    
}
```

```text title="输出"
[1, 2, 3]
[1, 2, 3]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/UnsignedArraysTest.kt#L374)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
