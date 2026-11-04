# endsWith

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果此字符串以指定的后缀结尾, 返回 `true` 。

@param 后缀是此字符串结尾的后缀。 @param 忽略标记标记显示字符串字符是否应该与`suffix` 字符比较, 以不区分大小写的方式进行; 默认情况下, 比较是区分大小写 。

@sample 样本. text. strings.ends without subixCaseSensicive @sample 样本. text. strings.ends without sixCase Incentive

??? note "查看英文原文"

    Returns `true` if this string ends with the specified suffix.
    
    @param suffix the suffix with which this string should end with.
    @param ignoreCase the flag indicating if the string characters should be compared with the `suffix` characters
     in a case-insensitive manner; by default, comparison is case-sensitive.
    
    @sample samples.text.Strings.endsWithSuffixCaseSensitive
    @sample samples.text.Strings.endsWithSuffixCaseInsensitive

## 声明与重载

### 1. Common

```kotlin
public expect fun String.endsWith(suffix: String, ignoreCase: Boolean = false): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L484)

### 2. Common

```kotlin
public fun CharSequence.endsWith(char: Char, ignoreCase: Boolean = false): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L882)

如果字符序列以指定字符结束,则返回 `true` 。

### 3. Common

```kotlin
public fun CharSequence.endsWith(suffix: CharSequence, ignoreCase: Boolean = false): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L908)

如果字符序列以指定的后缀结束,则返回 `true` 。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val str = "abcde"
    println(str.endsWith("cde"))
    println(str.endsWith("CDE"))
    println(str.endsWith("bcd"))
    println(str.endsWith("_abcde"))
}
```

```text title="输出"
true
false
false
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L908)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val str = "abcde"
    println(str.endsWith("cde", ignoreCase = true))
    println(str.endsWith("CDE", ignoreCase = true))
    println(str.endsWith("bcd", ignoreCase = true))
}
```

```text title="输出"
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L917)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
