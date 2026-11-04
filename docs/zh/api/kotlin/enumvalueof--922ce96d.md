# enumValueOf

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回`T`型号的内输入,并带有指定的 `name` 。

`name`必须完全匹配`T`(体格敏感)型号的现有酶常数。

@throws 非法允许例外,如果`T`内不存在与所指定的`name`没有对应的酶常数的话。
@sample样本.misc.Enums.enums nuum value ouues抽样

??? note "查看英文原文"

    Returns the enum entry of type `T` with the specified `name`.
    
    The `name` must exactly match an existing enum constant of type `T` (case-sensitive).
    
    @throws IllegalArgumentException if no enum constant with the specified `name` exists in `T`.
    @sample samples.misc.Enums.enumValueOfSample

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.1")
public expect inline fun <reified T : Enum<T>> enumValueOf(name: String): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Library.kt#L105)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.enums.enumEntries
import kotlin.test.*

enum class Direction { NORTH, SOUTH, EAST, WEST }

enum class Empty

fun main() {
    // enum class Direction { NORTH, SOUTH, EAST, WEST }

    val east = enumValueOf<Direction>("EAST")
    println(east)

    // The lookup fails if a string does not correspond to any of the enum entries
    assertFailsWith<IllegalArgumentException> { enumValueOf<Direction>("UP") }
    assertFailsWith<IllegalArgumentException> { enumValueOf<Direction>("") }

    // The lookup is case-sensitive and fails if the name doesn't match any constant
    assertFailsWith<IllegalArgumentException> { enumValueOf<Direction>("east") }
}
```

```text title="输出"
EAST
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/enums.kt#L15)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
