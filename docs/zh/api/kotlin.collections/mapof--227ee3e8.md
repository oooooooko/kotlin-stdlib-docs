# mapOf

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回带有指定内容的新的只读地图,以一对列表给出,第一个值是密钥,第二个值是该数值。

如果多个对的密钥相同, 生成的地图将包含最后的对的值 。

地图条目按所指定的顺序迭代。

返回的地图可连号(JVM) 。

@sample 样本采集 地图 证明 地图 取自

??? note "查看英文原文"

    Returns a new read-only map with the specified contents, given as a list of pairs
    where the first value is the key and the second is the value.
    
    If multiple pairs have the same key, the resulting map will contain the value from the last of those pairs.
    
    Entries of the map are iterated in the order they were specified.
    
    The returned map is serializable (JVM).
    
    @sample samples.collections.Maps.Instantiation.mapFromPairs

## 声明与重载

### 1. Common

```kotlin
public fun <K, V> mapOf(vararg pairs: Pair<K, V>): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L42)

### 2. Common

```kotlin
@SinceKotlin("1.9")
public expect fun <K, V> mapOf(pair: Pair<K, V>): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L57)

返回新的只读地图,只绘制指定值的指定密钥。

返回的地图可连号(JVM) 。

@sample 样本采集 地图 证明 地图 取自

### 3. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun <K, V> mapOf(): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L68)

返回空的只读地图。

归还的地图可连序(JVM), @sample 样本,收集。

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
    val result = `mapOf`(Pair(1, "one"))
    println(result)
}
```

```text title="输出"
{1=one}
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
