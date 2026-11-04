# ReadOnlyProperty

`kotlin.properties` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

可用于实施只读属性财产代表的基界面。

提供这些只是方便;只要您的财产代表拥有相同的签名方法,您不必扩展该接口。

@param T 属于获得授权的财产的物品类型。 @param V 属于财产价值类型。

??? note "查看英文原文"

    Base interface that can be used for implementing property delegates of read-only properties.
    
    This is provided only for convenience; you don't have to extend this interface
    as long as your property delegate has methods with the same signatures.
    
    @param T the type of object which owns the delegated property.
    @param V the type of the property value.

## 声明与重载

### 1. Common

```kotlin
public fun interface ReadOnlyProperty<in T, out V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/Interfaces.kt#L10)

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
import kotlin.properties.*

fun main() {
    val value = kotlin.properties.ReadOnlyProperty<Any?, Int> { _, _ -> 42 }
    println(value)
}
```

```text title="输出"
ExampleKt$$Lambda$1/0x0000007001001000@33909752
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
