# associateTo

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

弹出并返回`destination`变色图,配有由 `transform` 函数提供的配对键,适用于给定字符序列的每个字符。

如果两对中的任何一个有相同的键, 最后的键会被添加到地图上。

@sample 样本.text.Strings.Asociate To

??? note "查看英文原文"

    Populates and returns the `destination` mutable map with key-value pairs
    provided by `transform` function applied to each character of the given char sequence.
    
    If any of two pairs would have the same key the last one gets added to the map.
    
    @sample samples.text.Strings.associateTo

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> CharSequence.associateTo(destination: M, transform: (Char) -> Pair<K, V>): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L758)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val string = "bonne journée"
    // associate each character with its code
    val result = mutableMapOf<Char, Int>()
    string.associateTo(result) { char -> char to char.code }
    // notice each letter occurs only once
    println(result)
}
```

```text title="输出"
{b=98, o=111, n=110, e=101,  =32, j=106, u=117, r=114, é=233}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L236)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
