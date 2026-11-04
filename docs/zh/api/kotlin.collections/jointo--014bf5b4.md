# joinTo

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将所有元素的字符串附加在后面,这些元素使用 `separator` ,如果提供,则使用给定的 `prefix` 和`postfix`。

如果收藏没有元素,函数仅附加 `prefix` ,然后是`postfix`至`buffer`(默认为空)。

如果收藏量巨大, 您可以指定一个非负值为 `limit` , 这样, 首个`limit`元素将被附加, 之后是 `truncated` 字符串( 默认为 "... " )。

@return, `buffer` 论点及其所附要素。

@sample 样本、采集、采集、转化、加入

??? note "查看英文原文"

    Appends the string from all the elements separated using `separator` and using the given `prefix` and `postfix` if supplied.
    
    If the collection has no elements, the function appends only `prefix` followed by `postfix` to `buffer` (both are empty by default).
    
    If the collection is huge, you can specify a non-negative value of `limit`, in which case only the first `limit`
    elements will be appended, followed by the `truncated` string (which defaults to "...").
    
    @return the `buffer` argument with appended elements.
    
    @sample samples.collections.Collections.Transformations.joinTo

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
public fun <T, A : Appendable> Array<out T>.joinTo(buffer: A, separator: CharSequence = ", ", prefix: CharSequence = "", postfix: CharSequence = "", limit: Int = -1, truncated: CharSequence = "...", transform: ((T) -> CharSequence)? = null): A
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27147)

### 2. Common

```kotlin
@IgnorableReturnValue
public fun <A : Appendable> ByteArray.joinTo(buffer: A, separator: CharSequence = ", ", prefix: CharSequence = "", postfix: CharSequence = "", limit: Int = -1, truncated: CharSequence = "...", transform: ((Byte) -> CharSequence)? = null): A
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27174)

### 3. Common

```kotlin
@IgnorableReturnValue
public fun <A : Appendable> ShortArray.joinTo(buffer: A, separator: CharSequence = ", ", prefix: CharSequence = "", postfix: CharSequence = "", limit: Int = -1, truncated: CharSequence = "...", transform: ((Short) -> CharSequence)? = null): A
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27204)

### 4. Common

```kotlin
@IgnorableReturnValue
public fun <A : Appendable> IntArray.joinTo(buffer: A, separator: CharSequence = ", ", prefix: CharSequence = "", postfix: CharSequence = "", limit: Int = -1, truncated: CharSequence = "...", transform: ((Int) -> CharSequence)? = null): A
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27234)

### 5. Common

```kotlin
@IgnorableReturnValue
public fun <A : Appendable> LongArray.joinTo(buffer: A, separator: CharSequence = ", ", prefix: CharSequence = "", postfix: CharSequence = "", limit: Int = -1, truncated: CharSequence = "...", transform: ((Long) -> CharSequence)? = null): A
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27264)

### 6. Common

```kotlin
@IgnorableReturnValue
public fun <A : Appendable> FloatArray.joinTo(buffer: A, separator: CharSequence = ", ", prefix: CharSequence = "", postfix: CharSequence = "", limit: Int = -1, truncated: CharSequence = "...", transform: ((Float) -> CharSequence)? = null): A
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27294)

### 7. Common

```kotlin
@IgnorableReturnValue
public fun <A : Appendable> DoubleArray.joinTo(buffer: A, separator: CharSequence = ", ", prefix: CharSequence = "", postfix: CharSequence = "", limit: Int = -1, truncated: CharSequence = "...", transform: ((Double) -> CharSequence)? = null): A
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27324)

### 8. Common

```kotlin
@IgnorableReturnValue
public fun <A : Appendable> BooleanArray.joinTo(buffer: A, separator: CharSequence = ", ", prefix: CharSequence = "", postfix: CharSequence = "", limit: Int = -1, truncated: CharSequence = "...", transform: ((Boolean) -> CharSequence)? = null): A
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27354)

### 9. Common

```kotlin
@IgnorableReturnValue
public fun <A : Appendable> CharArray.joinTo(buffer: A, separator: CharSequence = ", ", prefix: CharSequence = "", postfix: CharSequence = "", limit: Int = -1, truncated: CharSequence = "...", transform: ((Char) -> CharSequence)? = null): A
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Arrays.kt#L27384)

### 10. Common

```kotlin
@IgnorableReturnValue
public fun <T, A : Appendable> Iterable<T>.joinTo(buffer: A, separator: CharSequence = ", ", prefix: CharSequence = "", postfix: CharSequence = "", limit: Int = -1, truncated: CharSequence = "...", transform: ((T) -> CharSequence)? = null): A
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt#L3917)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.*



fun main() {
    val sb = StringBuilder("An existing string and a list: ")
    val numbers = listOf(1, 2, 3)
    println(numbers.joinTo(sb, prefix = "[", postfix = "]").toString())

    val lotOfNumbers: Iterable<Int> = 1..100
    val firstNumbers = StringBuilder("First five numbers: ")
    println(lotOfNumbers.joinTo(firstNumbers, limit = 5).toString())

    // If the receiver is empty, the result only contains prefix and postfix
    println(emptyList<Int>().joinTo(StringBuilder()).toString().isEmpty())
    println(emptyList<Int>().joinTo(StringBuilder(), prefix = "[", postfix = "]").toString())
}
```

```text title="输出"
An existing string and a list: [1, 2, 3]
First five numbers: 1, 2, 3, 4, 5, ...
true
[]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/collections/collections.kt#L852)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
