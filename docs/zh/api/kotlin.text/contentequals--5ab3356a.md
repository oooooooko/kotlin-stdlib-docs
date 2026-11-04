# contentEquals

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果此字符序列的内容等于指定的 `other` 的内容, 即两个字符序列的字符数相同, 则返回 `true`。

@sample 样本.text.Strings. contentequals

??? note "查看英文原文"

    Returns `true` if the contents of this char sequence are equal to the contents of the specified `other`,
    i.e. both char sequences contain the same number of the same characters in the same order.
    
    @sample samples.text.Strings.contentEquals

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.5")
public expect infix fun CharSequence?.contentEquals(other: CharSequence?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1568)

### 2. Common

```kotlin
@SinceKotlin("1.5")
public expect fun CharSequence?.contentEquals(other: CharSequence?, ignoreCase: Boolean): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Strings.kt#L1577)

如果此字符序列的内容等于指定的 `other` 的内容,则返回 `true`, 且可选择忽略大小写差异 。

@param 忽略 `true` Case `true` , 以忽略字符案例, 比较内容 。

@sample 样本.text.Strings. contentequals

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val stringBuilder = StringBuilder()
    stringBuilder.append("Kot").append("lin")
    println(stringBuilder)
    println(stringBuilder contentEquals "Kotlin")

    stringBuilder.setCharAt(0, 'k')
    println(stringBuilder)
    println("Kotlin".contentEquals(stringBuilder))
    println("Kotlin".contentEquals(stringBuilder, ignoreCase = true))
}
```

```text title="输出"
Kotlin
true
kotlin
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L621)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
