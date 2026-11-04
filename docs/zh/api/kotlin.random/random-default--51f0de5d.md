# Random.Default

`kotlin.random` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

默认随机数生成器 。

这个生成器是安全的, 它的方法可以从多个线索中引用。

@sample 样本. 随机. 随机

??? note "查看英文原文"

    The default random number generator.
    
    This generator is thread-safe, its methods can be invoked from multiple threads.
    
    @sample samples.random.Randoms.defaultRandom

## 声明与重载

### 1. Common

```kotlin
public companion object Default : Random(), Serializable
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L269)

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

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
