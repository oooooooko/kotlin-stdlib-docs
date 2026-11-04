# ClosedFloatingPointRange.isEmpty

`kotlin.ranges` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 声明与重载

### 1. Common

```kotlin
override fun isEmpty(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/ranges/Ranges.kt#L82)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*

private fun assertFailsWithIllegalArgument(f: () -> Unit) = assertFailsWith<IllegalArgumentException> { f() }

fun main() {

        println((2..1).isEmpty())
        println((2L..0L).isEmpty())
        println((1.toShort()..(-1).toShort()).isEmpty())
        println((0.toByte()..(-1).toByte()).isEmpty())
        println((0f..-3.14f).isEmpty())
        println((-2.72..-3.14).isEmpty())
        println(('z'..'x').isEmpty())

        println((1 downTo 2).isEmpty())
        println((0L downTo 2L).isEmpty())
        println((2 downTo 1).isEmpty())
        println((2L downTo 0L).isEmpty())
        println(('a' downTo 'z').isEmpty())
        println(('z'..'a' step 2).isEmpty())

        println(("range".."progression").isEmpty())
    
}
```

```text title="输出"
true
true
true
true
true
true
true
true
true
false
false
true
true
true
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/ranges/RangeTest.kt#L327)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
