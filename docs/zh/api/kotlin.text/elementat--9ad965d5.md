# elementAt

`kotlin.text` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回给定 `index` 的字符,如果 `index` 超出此字符序列的界限,则返回 `index` 或扔出 `IndexOutOfBoundsException` 。

@sample 样本. 文本. 链条. elementAt

??? note "查看英文原文"

    Returns a character at the given `index` or throws an `IndexOutOfBoundsException` if the `index` is out of bounds of this char sequence.
    
    @sample samples.text.Strings.elementAt

## 声明与重载

### 1. Common

```kotlin
public expect fun CharSequence.elementAt(index: Int): Char
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Strings.kt#L20)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.test.*



fun main() {
    val string = "kotlin"
    println(string.elementAt(0))
    println(string.elementAt(5))
    assertFailsWith<IndexOutOfBoundsException> { string.elementAt(-1) }
    assertFailsWith<IndexOutOfBoundsException> { string.elementAt(6) }

    val empty = ""
    assertFailsWith<IndexOutOfBoundsException> { empty.elementAt(0) }
}
```

```text title="输出"
k
n
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/text/strings.kt#L103)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
