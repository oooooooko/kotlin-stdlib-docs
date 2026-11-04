# AbstractMutableMap.put

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

地图上指定的 `value` 和指定的`key`的关联关系。

这种方法被重新表述为抽象, 因为没有在基级中实施, 所以在具体变异的收集执行中必须总是被否决 。

@return 与密钥相关的上一个值,如果地图上没有密钥,则为 `null` 。

??? note "查看英文原文"

    Associates the specified `value` with the specified `key` in the map.
    
    This method is redeclared as abstract, because it's not implemented in the base class,
    so it must be always overridden in the concrete mutable collection implementation.
    
    @return the previous value associated with the key, or `null` if the key was not present in the map.

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
    abstract override fun put(key: K, value: V): V?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/collections/AbstractMutableMap.kt#L20)

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
    val source = object : AbstractMutableMap<String, Int>() { private val data = mutableMapOf("a" to 1); override val entries get() = data.entries; override fun put(key: String, value: Int) = data.put(key, value) }
    val result = source.`put`("a", 1)
    println(result)
}
```

```text title="输出"
1
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
