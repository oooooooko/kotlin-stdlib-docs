# withDefault

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回此只读地图的折叠式, 以默认值为默认值, 并指定 `defaultValue` 函数 。

当原始地图不包含指定密钥的值,而以 `Map.getValue` 函数获得一个值时,例如当属性被下放到地图时,使用这个默认值。

当此地图已经有一个默认默认值, 并包含一个前拨 `withDefault` , 被此调用替换 。

@sample 样本收集. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. 地图. . 地图. 地图. 地图. 地图. . . 地图. . 地图. 地图. 地图. 地图. 地图. 地图. . 地图. 地图. . . . . . 地图. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

??? note "查看英文原文"

    Returns a wrapper of this read-only map, having the implicit default value provided with the specified function `defaultValue`.
    
    This implicit default value is used when the original map doesn't contain a value for the key specified
    and a value is obtained with `Map.getValue` function, for example when properties are delegated to the map.
    
    When this map already has an implicit default value provided with a former call to `withDefault`, it is being replaced by this call.
    
    @sample samples.collections.Maps.Usage.getValueWithDefault
    @sample samples.collections.Maps.Usage.getValueWithReplacedDefault

## 声明与重载

### 1. Common

```kotlin
public fun <K, V> Map<K, V>.withDefault(defaultValue: (key: K) -> V): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MapWithDefault.kt#L28)

### 2. Common

```kotlin
@kotlin.jvm.JvmName("withDefaultMutable")
public fun <K, V> MutableMap<K, V>.withDefault(defaultValue: (key: K) -> V): MutableMap<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/MapWithDefault.kt#L45)

返回此可变映射的折叠图, 以默认值为默认值, 并指定函数 `defaultValue` 。

当原始地图不包含指定密钥的值,而以 `Map.getValue` 函数获得一个值时,例如当属性被下放到地图时,使用这个默认值。

当此地图已经有一个默认默认值, 并包含一个前拨 `withDefault` , 被此调用替换 。

@sample 样本. 收集. Maps. Usage. get Valeue with Default @sample 样本. 收集. Maps. Usage.

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*

val map = hashMapOf<String, Any?>("a" to "all", "b" to null, "c" to 1, "xProperty" to 1.0)

val map2: MutableMap<String, CharSequence> = hashMapOf("a2" to "all")

var a: String by map

var b: Any? by map

var c: Int by map

var d: String? by map

var a2: String by map2.withDefault { "empty" }

fun main() {

        println(a)
        println(b)
        println(c)
        c = 2
        println(c)
        println(map["c"])

        println(a2)
        map2.remove("a2")
        println(a2)

        assertFailsWith<NoSuchElementException> { d }
        map["d"] = null
        println(d)
    
}
```

```text title="输出"
all
null
1
2
2
all
empty
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/properties/delegation/MapAccessorsTest.kt#L55)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
