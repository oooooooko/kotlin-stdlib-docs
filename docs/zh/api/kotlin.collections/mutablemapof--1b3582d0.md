# mutableMapOf

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回新的`MutableMap`空空。

返回的地图保留了输入迭代令。 @sample 样本。 采集。 Maps. 证实。 空的MableMap

??? note "查看英文原文"

    Returns an empty new `MutableMap`.
    
    The returned map preserves the entry iteration order.
    @sample samples.collections.Maps.Instantiation.emptyMutableMap

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.1")
@kotlin.internal.InlineOnly
public inline fun <K, V> mutableMapOf(): MutableMap<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L77)

### 2. Common

```kotlin
public fun <K, V> mutableMapOf(vararg pairs: Pair<K, V>): MutableMap<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/collections/Maps.kt#L87)

返回含有指定内容的`MutableMap`新值,以对应的列表给出,第一个组件是键,第二个是值。

如果多个对的密钥相同, 生成的地图将包含最后的对的值 。

地图条目按所指定的顺序迭代。

@sample 样本. 采集. Maps. 证实. 变换Map FromPairs @sample 样本. 采集. Maps. 证实. 空的变形图

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val string = "bonne journée"
    // associate each character by its code
    val result = mutableMapOf<Int, Char>()
    string.associateByTo(result) { char -> char.code }
    // notice each char code occurs only once
    println(result)
}
```

```text title="输出"
{98=b, 111=o, 110=n, 101=e, 32= , 106=j, 117=u, 114=r, 233=é}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L216)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
