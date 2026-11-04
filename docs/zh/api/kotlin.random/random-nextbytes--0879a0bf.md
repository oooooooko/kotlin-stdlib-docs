# Random.nextBytes

`kotlin.random` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

填充指定 `array` 字节的子序列,从`fromIndex`(含)开始,以随机字节结束`toIndex`(不含)。

@return `array` , 加上以随机字节填充的子项。

@sample 样本. 随机. 兰多姆. 下游Bytes

??? note "查看英文原文"

    Fills a subrange of the specified byte `array` starting from `fromIndex` inclusive and ending `toIndex` exclusive
    with random bytes.
    
    @return `array` with the subrange filled with random bytes.
    
    @sample samples.random.Randoms.nextBytes

## 声明与重载

### 1. Common

```kotlin
@IgnorableReturnValue
    public open fun nextBytes(array: ByteArray, fromIndex: Int = 0, toIndex: Int = array.size): ByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L217)

### 2. Common

```kotlin
@IgnorableReturnValue
    public open fun nextBytes(array: ByteArray): ByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L251)

以随机字节填充指定的 `array` 字节并返回 。

@return `array` 填充随机字节。

@sample 样本. 随机. 兰多姆. 下游Bytes

### 3. Common

```kotlin
public open fun nextBytes(size: Int): ByteArray
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L261)

创建指定 `size` 的字节阵列, 以随机字节填充 。

@sample 样本. 随机. 兰多姆. 下游Bytes

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.sin
import kotlin.random.Random
import kotlin.test.assertTrue



fun main() {
    val bytes = ByteArray(4)
    println(bytes.contentToString())

    Random.nextBytes(bytes, 1, 3)
    // second and third bytes are generated, rest unchanged
    println(bytes.contentToString())

    Random.nextBytes(bytes)
    // all bytes are newly generated
    println(bytes.contentToString())

    val newBytes = Random.nextBytes(5)
    // a new byte array filled with random values
    println(newBytes.contentToString())
}
```

```text title="输出"
[0, 0, 0, 0]
[0, 102, 112, 0]
[-89, -117, 83, 38]
[78, 26, 56, 123, 95]
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/random/randoms.kt#L65)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
