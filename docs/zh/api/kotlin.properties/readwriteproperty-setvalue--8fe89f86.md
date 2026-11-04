# ReadWriteProperty.setValue

`kotlin.properties` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

设定给定对象的属性值。 @param 此文件是请求值的对象。 @param 属性是该属性的元数据。 @param 值是要设定的价值 。

??? note "查看英文原文"

    Sets the value of the property for the given object.
    @param thisRef the object for which the value is requested.
    @param property the metadata for the property.
    @param value the value to set.

## 声明与重载

### 1. Common

```kotlin
public operator fun setValue(thisRef: T, property: KProperty<*>, value: V)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/Interfaces.kt#L47)

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

val demoProperty = 42
var demoMutable = 42
fun demoFunction(value: Int): Int = value + 1

fun main() {
    val source = object : kotlin.properties.ReadWriteProperty<Any?, Int> { private var data = 42; override fun getValue(thisRef: Any?, property: kotlin.reflect.KProperty<*>) = data; override fun setValue(thisRef: Any?, property: kotlin.reflect.KProperty<*>, value: Int) { data = value } }
    val result = source.`setValue`(1, ::demoProperty, 1)
    println(result)
}
```

```text title="输出"
kotlin.Unit
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
