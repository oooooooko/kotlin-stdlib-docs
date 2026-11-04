# toIntOrNull

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果字符串不是 `Int` 的有效表示, 则将字符串分割为 `Int` 号, 或返回 `null` 。

字符串必须包含一个可选的 `+` 或`-`符号和小数位数(`0-9`),并符合`Int`值值的值范围(在`Int.MIN_VALUE..Int.MAX_VALUE`范围内),否则返回 `null` 。

@sample 样本.文本. 数字. 至Ornull

??? note "查看英文原文"

    Parses the string to an `Int` number or returns `null` if the string is not a valid representation of an `Int`.
    
    The string must consist of an optional leading `+` or `-` sign and decimal digits (`0-9`),
    and fit the valid `Int` value range (within `Int.MIN_VALUE..Int.MAX_VALUE`),
    otherwise `null` is returned.
    
    @sample samples.text.Numbers.toIntOrNull

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.1")
public fun String.toIntOrNull(): Int?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringNumberConversions.kt#L62)

### 2. Common

```kotlin
@SinceKotlin("1.1")
public fun String.toIntOrNull(radix: Int): Int?
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/StringNumberConversions.kt#L74)

将字符串分割为 `Int` 号, 如果字符串不是数字的有效表示, 则返回结果或 `null` 。

@throws 非法设备除外,当 `radix` 不是一个有效的 字符串转换为数字的 RADIX 时。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.assertFailsWith



fun main() {
    println("0".toIntOrNull())
    println("42".toIntOrNull())
    println("042".toIntOrNull())
    println("-42".toIntOrNull())
    // Int.MAX_VALUE
    println("2147483647".toIntOrNull())
    // Int overflow
    println("2147483648".toIntOrNull())
    // 'a' is not a digit
    println("-1a".toIntOrNull())
    // underscore
    println("1_00".toIntOrNull())
    // whitespaces
    println(" 22 ".toIntOrNull())
}
```

```text title="输出"
0
42
42
-42
2147483647
null
null
null
null
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/Numbers.kt#L103)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
