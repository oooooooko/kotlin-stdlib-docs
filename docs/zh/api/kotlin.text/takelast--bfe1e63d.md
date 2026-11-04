# takeLast

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回此字符序列的子序列, 包含此字符序列中最后的 `n` 字符, 或如果此字符序列较短, 则返回整个字符序列的子序列 。

@throws 非法设备,如果`n`为负数,则不在此列。

@sample 样本. 文本. 链

??? note "查看英文原文"

    Returns a subsequence of this char sequence containing the last `n` characters from this char sequence, or the entire char sequence if this char sequence is shorter.
    
    @throws IllegalArgumentException if `n` is negative.
    
    @sample samples.text.Strings.take

## 声明与重载

### 1. Common

```kotlin
public fun CharSequence.takeLast(n: Int): CharSequence
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L585)

### 2. Common

```kotlin
public fun String.takeLast(n: Int): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L598)

返回含有最后`n`个字符的字符串,如果此字符串较短,则返回整个字符串。

@throws 非法设备,如果`n`为负数,则不在此列。

@sample 样本. 文本. 链

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val string = "<<<First Grade>>>"
    println(string.take(8))
    println(string.takeLast(8))
    println(string.takeWhile { !it.isLetter() })
    println(string.takeLastWhile { !it.isLetter() })
}
```

```text title="输出"
<<<First
Grade>>>
<<<
>>>
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L446)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
