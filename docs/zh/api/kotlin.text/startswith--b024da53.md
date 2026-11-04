# startsWith

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果字符串以指定的前缀开头,则返回 `true` 。

@param 前缀前缀, 以此开始此字符串。 @param 忽略标记标记显示字符串字符是否应该与`prefix` 字符比较, 且不区分大小写; 默认情况下, 比较是区分大小写 。

@sample 样本. text. strings. starts with PrefixCaseSensionive @sample 样本. text. strings. starts starts with PrefixCase Invisions. 启动 PrefixCase Intals. 启动与 PrefixCase Informations 启动 启动 启动 启动 启动 启动 启动 启动 与 PixCase Intalive 服务器

??? note "查看英文原文"

    Returns `true` if this string starts with the specified prefix.
    
    @param prefix the prefix from which this string should start with.
    @param ignoreCase the flag indicating if the string characters should be compared with the `prefix` characters
     in a case-insensitive manner; by default, comparison is case-sensitive.
    
    @sample samples.text.Strings.startsWithPrefixCaseSensitive
    @sample samples.text.Strings.startsWithPrefixCaseInsensitive

## 声明与重载

### 1. Common

```kotlin
public expect fun String.startsWith(prefix: String, ignoreCase: Boolean = false): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L459)

### 2. Common

```kotlin
public expect fun String.startsWith(prefix: String, startIndex: Int, ignoreCase: Boolean = false): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/kotlin/TextH.kt#L471)

如果从指定的偏移 `startIndex` 开始以指定的前缀为子字符串,则返回 `true`。

@param 前缀前缀, 使此字符串子字符串从 `startIndex` 开始以 . @param 开头 Index 开始指数( 包括) 。 @param 忽略了标记, 标记字符是否应该与 `prefix` 字符相对应, 以不区分大小写的方式比较; 默认情况下, 比较是区分大小写 。

@sample 样本. text. strings. starts with PrefixAt PostificAt PosticCaseSenvironical @sample 样本. text. strings. starts starts with PrefixAt PresidicalCase Incentive 启动 PreixAt PostPostPostPresical Case Inclimitive 启动启动 启动 启动 启动 启动 PrefixAt PostPresical Case Intal 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 启动 。

### 3. Common

```kotlin
public fun CharSequence.startsWith(char: Char, ignoreCase: Boolean = false): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L876)

如果字符序列以指定字符开头,则返回 `true` 。

### 4. Common

```kotlin
public fun CharSequence.startsWith(prefix: CharSequence, ignoreCase: Boolean = false): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L888)

如果字符序列以指定的前缀开始,则返回 `true` 。

### 5. Common

```kotlin
public fun CharSequence.startsWith(prefix: CharSequence, startIndex: Int, ignoreCase: Boolean = false): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L898)

如果从指定的 amble `startIndex` 开始以指定的前缀开始, 返回 `true` 。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val str = "abcde"
    println(str.startsWith("abc"))
    println(str.startsWith("ABC"))
    println(str.startsWith("bcd"))
    println(str.startsWith("abcdef"))
}
```

```text title="输出"
true
false
false
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L875)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val str = "abcde"
    println(str.startsWith("abc", ignoreCase = true))
    println(str.startsWith("ABC", ignoreCase = true))
    println(str.startsWith("bcd", ignoreCase = true))
}
```

```text title="输出"
true
true
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L884)

### 示例 3 · JVM

```kotlin title="示例 3" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val str = "abcde"
    println(str.startsWith("abc", startIndex = 1))
    println(str.startsWith("BCD", startIndex = 1))
    println(str.startsWith("bcd", startIndex = 1))
}
```

```text title="输出"
false
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L892)

### 示例 4 · JVM

```kotlin title="示例 4" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val str = "abcde"
    println(str.startsWith("abc", startIndex = 1, ignoreCase = true))
    println(str.startsWith("bcd", startIndex = 1, ignoreCase = true))
    println(str.startsWith("BCD", startIndex = 1, ignoreCase = true))
}
```

```text title="输出"
false
true
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L900)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
