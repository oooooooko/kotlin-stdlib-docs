# associateWith

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

a `Map` 返回 键是给定字符序列中的字符, 并且每个字符应用的 `valueSelector` 函数生成了数值 。

如果任何两个字符相等, 最后一个字符会被添加到地图中 。

返回的地图保留了原始字符序列的输入迭代顺序。

@sample 样本. 文本. Strings. Associated

??? note "查看英文原文"

    Returns a `Map` where keys are characters from the given char sequence and values are
    produced by the `valueSelector` function applied to each character.
    
    If any two characters are equal, the last one gets added to the map.
    
    The returned map preserves the entry iteration order of the original char sequence.
    
    @sample samples.text.Strings.associateWith

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
public inline fun <V> CharSequence.associateWith(valueSelector: (Char) -> V): Map<Char, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L774)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val string = "bonne journée"
    // associate each character with its code
    val result = string.associateWith { char -> char.code }
    // notice each letter occurs only once
    println(result)
}
```

```text title="输出"
{b=98, o=111, n=110, e=101,  =32, j=106, u=117, r=114, é=233}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L246)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
