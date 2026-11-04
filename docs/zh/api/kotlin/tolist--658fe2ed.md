# toList

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将此对转换成列表。 @sample 样本. misc. tuples. pair ToList

??? note "查看英文原文"

    Converts this pair into a list.
    @sample samples.misc.Tuples.pairToList

## 声明与重载

### 1. Common

```kotlin
public fun <T> Pair<T, T>.toList(): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Tuples.kt#L46)

### 2. Common

```kotlin
public fun <T> Triple<T, T, T>.toList(): List<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Tuples.kt#L80)

将此三重转换为列表。 @sample 样本. misc. tuples. triple ToList

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val mixedList: List<Any> = Pair(1, "a").toList()
    println(mixedList)
    println(mixedList[0] is Int)
    println(mixedList[1] is String)

    val intList: List<Int> = Pair(0, 1).toList()
    println(intList)
}
```

```text title="输出"
[1, a]
true
true
[0, 1]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/tuples.kt#L23)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val mixedList: List<Any> = Triple(1, "a", 0.5).toList()
    println(mixedList)
    println(mixedList[0] is Int)
    println(mixedList[1] is String)
    println(mixedList[2] is Double)

    val intList: List<Int> = Triple(0, 1, 2).toList()
    println(intList)
}
```

```text title="输出"
[1, a, 0.5]
true
true
true
[0, 1, 2]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/tuples.kt#L34)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
