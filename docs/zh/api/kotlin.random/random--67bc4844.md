# Random

`kotlin.random` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

由随机数生成算法执行的抽象类。

同伴对象`Random.Default` 是默认的 `Random` 实例。

获取随机发电机使用 `Random` 功能的种子实例。

@sample 样本. 随机. 随机

??? note "查看英文原文"

    An abstract class that is implemented by random number generator algorithms.
    
    The companion object `Random.Default` is the default instance of `Random`.
    
    To get a seeded instance of random generator use `Random` function.
    
    @sample samples.random.Randoms.defaultRandom

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
public abstract class Random
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L12)

### 2. Common

```kotlin
@SinceKotlin("1.3")
public fun Random(seed: Int): Random
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L314)

a 返回所给`seed` `Int` 值的可重复随机数生成发电机种子。

同一种子的两个发电机在科特林运行时间的同一版本内产生同样的序列值。

*注:* 未来版本的Kotlin可能会改变这个种子数生成器的算法,以便它返回与目前不同的某一种子的序列值。

在 JVM 上, 返回的发电机不安全, 无法使用线条。 无法在不同步的情况下从多个线条中引用它 。

@sample 样本. 随机性. 兰多姆. 种子兰多姆

### 3. Common

```kotlin
@SinceKotlin("1.3")
public fun Random(seed: Long): Random
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L329)

a 返回所给`seed` `Long` 值的可重复随机数生成发电机种子。

同一种子的两个发电机在科特林运行时间的同一版本内产生同样的序列值。

*注:* 未来版本的Kotlin可能会改变这个种子数生成器的算法,以便它返回与目前不同的某一种子的序列值。

在 JVM 上, 返回的发电机不安全, 无法使用线条。 无法在不同步的情况下从多个线条中引用它 。

@sample 样本. 随机性. 兰多姆. 种子兰多姆

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.sin
import kotlin.random.Random
import kotlin.test.assertTrue



fun main() {
    val randomValues = List(10) { Random.nextInt(0, 100) }
    // prints new sequence every time
    println(randomValues)

    val nextValues = List(10) { Random.nextInt(0, 100) }
    println(nextValues)
    println(randomValues != nextValues)
}
```

```text title="输出"
[98, 80, 29, 18, 13, 1, 73, 6, 42, 78]
[98, 5, 35, 94, 26, 43, 42, 77, 37, 6]
true
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/random/randoms.kt#L14)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.sin
import kotlin.random.Random
import kotlin.test.assertTrue



fun main() {
    fun getRandomList(random: Random): List<Int> =
        List(10) { random.nextInt(0, 100) }

    val randomValues1 = getRandomList(Random(42))
    // prints the same sequence every time
    println(randomValues1)

    val randomValues2 = getRandomList(Random(42))
    // random with the same seed produce the same sequence
    println(randomValues1 == randomValues2)

    val randomValues3 = getRandomList(Random(0))
    // random with another seed produce another sequence
    println(randomValues3)
}
```

```text title="输出"
[33, 40, 41, 2, 41, 32, 21, 40, 69, 87]
true
[14, 48, 57, 67, 82, 7, 61, 27, 14, 59]
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/random/randoms.kt#L25)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
