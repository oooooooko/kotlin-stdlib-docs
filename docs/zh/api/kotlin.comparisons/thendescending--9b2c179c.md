# thenDescending

`kotlin.comparisons` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将这个比较国和给定的`comparator`合并,因此后者只在前者认为价值相等时才适用。

@sample 样本.比较.比较.比较.然后

??? note "查看英文原文"

    Combines this comparator and the given `comparator` such that the latter is applied only
    when the former considered values equal.
    
    @sample samples.comparisons.Comparisons.thenDescending

## 声明与重载

### 1. Common

```kotlin
public infix fun <T> Comparator<T>.thenDescending(comparator: Comparator<in T>): Comparator<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/comparisons/Comparisons.kt#L211)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
fun main() {
    val list = listOf("A", "aa", "b", "bb", "a")

    val lengthThenCaseInsensitive = compareBy<String> { it.length }
        .thenDescending(String.CASE_INSENSITIVE_ORDER)

    val sorted = list.sortedWith(lengthThenCaseInsensitive)

    println(sorted)
}
```

```text title="输出"
[b, A, a, bb, aa]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/comparisons/comparisons.kt#L190)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
