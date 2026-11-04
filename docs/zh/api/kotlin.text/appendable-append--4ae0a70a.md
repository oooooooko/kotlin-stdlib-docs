# Appendable.append

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将指定的字符 `value` 附加到此附加文件并返回此实例。

@param 值此字符附加的字符 。

??? note "查看英文原文"

    Appends the specified character `value` to this Appendable and returns this instance.
    
    @param value the character to append.

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
    public fun append(value: Char): Appendable
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Appendable.kt#L15)

### 2. Common

```kotlin
@IgnorableReturnValue
    public fun append(value: CharSequence?): Appendable
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Appendable.kt#L23)

将指定的字符序列 `value` 附加到此附加文件并返回此实例。

@param 值为附件字符序列。如果 `value` 是 `null`,则本附录后面附上四个字符 `"null"`。

### 3. Common

```kotlin
@IgnorableReturnValue
    public fun append(value: CharSequence?, startIndex: Int, endIndex: Int): Appendable
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/text/Appendable.kt#L31)

将指定的字符序列 `value` 的子序列附加到此附加文件并返回此实例。

@param 值作为子序列附加的字符序列。 如果 `value` 是 `null` , 那么字符将被附加, 仿佛 `value` 包含四个字符 `"null"` 。 @param 开头 Index 包括子序列的起始( 包括) , 后继的起始( 包括) 后继的起始( 包括) 。 后继的结尾( 排他) 。

@throws 指数外向值或 `IllegalArgumentException` ,当 `startIndex` 或 `endIndex` 不在`value`字符序列指数范围或`startIndex > endIndex`时,则 `IllegalArgumentException` 。

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.random.Random
import kotlin.test.*
import kotlin.text.*



fun main() {

        StringBuilder("my trimToSize test").let { sb ->
            println(sb.length)
//            assertTrue(sb.capacity() >= sb.length)
            sb.append('1')
            sb.trimToSize()
            println(sb.length)
//            assertTrue(sb.capacity() >= sb.length)
        }
    
}
```

```text title="输出"
18
19
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/text/StringBuilderTest.kt#L482)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
