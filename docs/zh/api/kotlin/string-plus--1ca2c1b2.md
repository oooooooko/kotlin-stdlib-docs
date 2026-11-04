# String.plus

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回通过将给定 `other` 对象的字符串表示形式连接到此字符串而获得的字符串。

@sample 样本.text.strrings.stringPlus

??? note "查看英文原文"

    Returns a string obtained by concatenating this string with the string representation of the given `other` object.
    
    @sample samples.text.Strings.stringPlus

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.IntrinsicConstEvaluation
    public operator fun plus(other: Any?): String
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/String.kt#L16)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    println("Ko" + "dee")
    // 2 is not a string, but plus concatenates its string representation with the "Kotlin " string
    println("Kotlin " + 2)
    // list is converted to a String first and then concatenated with the "Numbers: " string
    println("Numbers: " + listOf(1, 2, 3))
}
```

```text title="输出"
Kodee
Kotlin 2
Numbers: [1, 2, 3]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L1016)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
