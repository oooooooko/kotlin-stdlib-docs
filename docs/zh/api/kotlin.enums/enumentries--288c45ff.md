# enumEntries

`kotlin.enums` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回 `EnumEntries` 列表, 包含 `T` 型号给定的 enum 的所有 enum 条目 。

@see ENIMEENTERINTER @sample 样本:

??? note "查看英文原文"

    Returns `EnumEntries` list containing all enum entries for the given enum type `T`.
    
    @see EnumEntries
    @sample samples.misc.Enums.enumEntriesSample

## 声明与重载

### 1. Common

```kotlin
@WasExperimental(ExperimentalStdlibApi::class)
@SinceKotlin("2.0")
public inline fun <reified T : Enum<T>> enumEntries(): EnumEntries<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/enums/EnumEntries.kt#L30)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.enums.enumEntries

enum class Direction { NORTH, SOUTH, EAST, WEST }

enum class Empty

fun main() {
    // enum class Direction { NORTH, SOUTH, EAST, WEST }
    val entries = enumEntries<Direction>()
    println(entries)
    println(entries.indexOf(Direction.EAST))
    println(entries[1])

    // enum class Empty {}
    println(enumEntries<Empty>())
}
```

```text title="输出"
[NORTH, SOUTH, EAST, WEST]
2
SOUTH
[]
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/misc/enums.kt#L32)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
