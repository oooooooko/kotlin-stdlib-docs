# associateByTo

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

弹出并返回`destination`的带有关键值对的可变图,键由适用于给定字符序列每个字符的`keySelector`函数提供,而字符本身是该字符的值。

如果任何两个字符在 `keySelector` 之前返回相同的键, 最后一个键会被添加到地图中 。

@sample 样本. 文本. strings. Asociate By To

??? note "查看英文原文"

    Populates and returns the `destination` mutable map with key-value pairs,
    where key is provided by the `keySelector` function applied to each character of the given char sequence
    and value is the character itself.
    
    If any two characters would have the same key returned by `keySelector` the last one gets added to the map.
    
    @sample samples.text.Strings.associateByTo

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, M : MutableMap<in K, in Char>> CharSequence.associateByTo(destination: M, keySelector: (Char) -> K): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L724)

### 2. Common

```kotlin
@IgnorableReturnValue
public inline fun <K, V, M : MutableMap<in K, in V>> CharSequence.associateByTo(destination: M, keySelector: (Char) -> K, valueTransform: (Char) -> V): M
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L741)

弹出并返回`destination`变色图,配有关键值对,键由`keySelector`函数提供,而值由适用于给定字符序列字符的`valueTransform`函数提供。

如果任何两个字符在 `keySelector` 之前返回相同的键, 最后一个键会被添加到地图中 。

@sample 样本.text.Strings.sociate By To To To To with Value Transform 样本

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

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val string = "bonne journée"
    // associate each character by the code of its upper case equivalent and transform the character to upper case
    val result = mutableMapOf<Int, Char>()
    string.associateByTo(result, { char -> char.uppercaseChar().code }, { char -> char.uppercaseChar() })
    // notice each char code occurs only once
    println(result)
}
```

```text title="输出"
{66=B, 79=O, 78=N, 69=E, 32= , 74=J, 85=U, 82=R, 201=É}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L226)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
