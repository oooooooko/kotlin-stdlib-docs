# mapKeys

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回新地图, 返回新地图, 其条目具有通过对此条目中每个条目应用 `transform` 函数获得的密钥
`Map` 和此映射的值 。

如果任何两个条目被映射到等键上,后一个条目的值将覆盖与前一个条目相关的值。

返回的地图保留原始地图的条目迭代顺序。

@sample 样本采集 地图 变形图 地图 钥匙

??? note "查看英文原文"

    Returns a new Map with entries having the keys obtained by applying the `transform` function to each entry in this
    `Map` and the values of this map.
    
    In case if any two entries are mapped to the equal keys, the value of the latter one will overwrite
    the value associated with the former one.
    
    The returned map preserves the entry iteration order of the original map.
    
    @sample samples.collections.Maps.Transformations.mapKeys

## 声明与重载

### 1. Common

```kotlin
public inline fun <K, V, R> Map<out K, V>.mapKeys(transform: (Map.Entry<K, V>) -> R): Map<R, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L613)

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

        val expected = mapOf(1u to "one", 2u to "two", 3u to "three")
        println(uintArrayOf(2u, 3u).associateWithTo(expected.toMutableMap()) { it.toString() })
        println(ubyteArrayOf(2u, 3u).associateWithTo(expected.mapKeys { it.key.toUByte() }.toMutableMap()) { it.toString() })
        println(ushortArrayOf(2u, 3u).associateWithTo(expected.mapKeys { it.key.toUShort() }.toMutableMap()) { it.toString() })
        println(ulongArrayOf(2u, 3u).associateWithTo(expected.mapKeys { it.key.toULong() }.toMutableMap()) { it.toString() })
    
}
```

```text title="输出"
{1=one, 2=2, 3=3}
{1=one, 2=2, 3=3}
{1=one, 2=2, 3=3}
{1=one, 2=2, 3=3}
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/collections/UnsignedArraysTest.kt#L828)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
