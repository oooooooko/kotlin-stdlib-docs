# associateBy

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回 a `Map` 包含从给定字符序列中字符的字符,字符序列由从 `keySelector` 函数返回的键索引,每个字符都适用。

如果任何两个字符在 `keySelector` 之前返回相同的键, 最后一个键会被添加到地图中 。

返回的地图保留了原始字符序列的输入迭代顺序。

@sample 样本. 文本. strings. AsociateBy

??? note "查看英文原文"

    Returns a `Map` containing the characters from the given char sequence indexed by the key
    returned from `keySelector` function applied to each character.
    
    If any two characters would have the same key returned by `keySelector` the last one gets added to the map.
    
    The returned map preserves the entry iteration order of the original char sequence.
    
    @sample samples.text.Strings.associateBy

## 声明与重载

### 1. Common

```kotlin
public inline fun <K> CharSequence.associateBy(keySelector: (Char) -> K): Map<K, Char>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L695)

### 2. Common

```kotlin
public inline fun <K, V> CharSequence.associateBy(keySelector: (Char) -> K, valueTransform: (Char) -> V): Map<K, V>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L710)

a `Map` 返回包含`valueTransform` 提供的值,并用 `keySelector` 函数索引适用于给定字符序列的字符。

如果任何两个字符在 `keySelector` 之前返回相同的键, 最后一个键会被添加到地图中 。

返回的地图保留了原始字符序列的输入迭代顺序。

@sample 样本.text.Strings.Associate By Compeciate By Value Transformat

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val string = "bonne journée"
    // associate each character by its code
    val result = string.associateBy { char -> char.code }
    // notice each char code occurs only once
    println(result)
}
```

```text title="输出"
{98=b, 111=o, 110=n, 101=e, 32= , 106=j, 117=u, 114=r, 233=é}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L198)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val string = "bonne journée"
    // associate each character by the code of its upper case equivalent and transform the character to upper case
    val result = string.associateBy({ char -> char.uppercaseChar().code }, { char -> char.uppercaseChar() })
    // notice each char code occurs only once
    println(result)
}
```

```text title="输出"
{66=B, 79=O, 78=N, 69=E, 32= , 74=J, 85=U, 82=R, 201=É}
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L207)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
