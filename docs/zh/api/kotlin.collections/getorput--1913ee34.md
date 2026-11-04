# getOrPut

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果数值存在而不是`null`,则返回给定的`key`的值。
否则,调用 `defaultValue` 函数,
将其结果输入给定键下的地图, 并返回呼叫结果 。

注意: 如果地图预计包含 `null` 值, 则不建议使用此函数。 使用 `getOrPutIfNull` 或 `getOrPutIfMissing` 来表达在键被映射为 `null` 值时要做什么的意向 。

当给定的 `key` 不在本地图中或被映射为 `null`时, `defaultValue`的结果, 即使 `null` 也被置于密钥下的地图中。 如果给定的 `defaultValue` 投出例外, 例外将被重新丢弃 。

请注意,如果同时修改地图,则不能保证操作是原子操作。

@throws 纳米点数除以指定`key`或`defaultValue`的结果为`null`,而本地图不支持8,0000005 键或值。

@sample 样本 采集 地图 地图 地图 草图 草图

??? note "查看英文原文"

    Returns the value for the given `key` if the value is present and not `null`.
    Otherwise, calls the `defaultValue` function,
    puts its result into the map under the given key, and returns the call result.
    
    Note: it's not recommended to use this function if the map is expected to contain `null` values.
    Use either `getOrPutIfNull`, or `getOrPutIfMissing` instead to express the intent
    what to do when the key is mapped to `null` value more clearly.
    
    When the given `key` is not in this map or is mapped to a `null`, the result of `defaultValue`,
    even if `null`, is put into the map under the key.
    If `defaultValue` throws an exception, the exception is rethrown.
    
    Note that the operation is not guaranteed to be atomic if the map is being modified concurrently.
    
    @throws NullPointerException if the specified `key` or the result of `defaultValue` is `null`,
      and this map does not support `null` keys or values.
    
    @sample samples.collections.Maps.Usage.getOrPut

## 声明与重载

### 1. Common

```kotlin
public inline fun <K, V> MutableMap<K, V>.getOrPut(key: K, defaultValue: () -> V): V
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L439)

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
    val source = linkedMapOf("a" to 1, "b" to 2)
    val result = source.`getOrPut`("a", { 42 })
    println(result)
}
```

```text title="输出"
1
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
