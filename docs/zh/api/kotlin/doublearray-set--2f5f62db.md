# DoubleArray.set

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

将给定的 `index` 的数组元素设置为 `value` 。

使用索引运算符可以调用此方法 :```
array`index` = value
```

如果 `index` 超出了此阵列的界限, 投出 `IndexOutOfBoundsException` , 但 Kotlin/ JS 中的行为未指明, 投出`IndexOutOfBoundsException`, 而在 Kotlin/ Wasm 中, 将升起一个 [ 字符串( https://webassembly.github.io/spec/core/intro/overview.html#trap) ) , 除非在连接可执行文件时指定了 `-Xwasm-enable-array-range-checks` 编译器的旗帜 。

??? note "查看英文原文"

    Sets the array element at the given `index` to the given `value`.
    
    This method can be called using the index operator:
    ```
    array`index` = value
    ```
    
    If the `index` is out of bounds of this array, throws an `IndexOutOfBoundsException` except in Kotlin/JS
    where the behavior is unspecified, and in Kotlin/Wasm where a [trap](https://webassembly.github.io/spec/core/intro/overview.html#trap) will be raised instead,
    unless `-Xwasm-enable-array-range-checks` compiler flag was specified when linking an executable.

## 声明与重载

### 1. Common

```kotlin
public operator fun set(index: Int, value: Double): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Arrays.kt#L422)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.*

fun main() {
    val source = doubleArrayOf(1.0, 2.0, 3.0)
    val result = source.`set`(0, 2.0)
    println(result)
}
```

```text title="输出"
kotlin.Unit
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
