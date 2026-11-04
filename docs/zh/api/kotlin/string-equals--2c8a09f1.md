# String.equals

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

表示 `other` 天体等于 `String` 。

`other` 对象等于此 `String` , 如果且只有它也是一个 `String`, 它与此字符串具有相同的 `length` , 并且字符串中相同位置的字符数是等同的, 则该对象等于 `String` 。

@sample 样本. 文本. 链条. 弦

??? note "查看英文原文"

    Indicates if `other` object is equal to this `String`.
    
    An `other` object is equal to this `String` if and only if it is also a `String`,
    it has the same `length` as this String,
    and characters at the same positions in each string are equal to each other.
    
    @sample samples.text.Strings.stringEquals

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.IntrinsicConstEvaluation
    public override fun equals(other: Any?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/String.kt#L43)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println("" == "")
    println("abc" == "abc")

    println("abc" == "abcd")
    println("abc" == "Abc")
    // If a character's case doesn't matter, strings could be compared in a case-insensitive manner
    println("abc".equals("Abc", ignoreCase = true))

    val builder = StringBuilder("abc")
    println(builder)
    // Although the builder holds the same character sequence, it is not a String
    println("abc".equals(builder))
}
```

```text title="输出"
true
true
false
false
true
abc
false
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L999)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
