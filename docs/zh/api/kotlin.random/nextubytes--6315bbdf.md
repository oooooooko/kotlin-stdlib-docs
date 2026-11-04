# nextUBytes

`kotlin.random` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

以随机字节填充指定的无符号字节 `array` 并返回它 。

@return `array` 填充随机字节。

??? note "查看英文原文"

    Fills the specified unsigned byte `array` with random bytes and returns it.
    
    @return `array` filled with random bytes.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@IgnorableReturnValue
public fun Random.nextUBytes(array: UByteArray): UByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/URandom.kt#L113)

### 2. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
public fun Random.nextUBytes(size: Int): UByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/URandom.kt#L126)

创建指定 `size` 的无签名字节数组, 以随机字节填充 。

### 3. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalUnsignedTypes
@IgnorableReturnValue
public fun Random.nextUBytes(array: UByteArray, fromIndex: Int = 0, toIndex: Int = array.size): UByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/URandom.kt#L133)

填充一个指定 `UByte` `array` 的子序列,从`fromIndex`(含)开始,以随机UBytes为唯一对象,填充 `toIndex` 。

@return `array` , 加上以随机字节填充的子项。

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
import kotlin.random.*

fun main() {
    val source = Random(42)
    val result = source.`nextUBytes`(ubyteArrayOf(1u, 2u, 3u))
    println(result.contentToString())
}
```

```text title="输出"
[204, 239, 57]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
