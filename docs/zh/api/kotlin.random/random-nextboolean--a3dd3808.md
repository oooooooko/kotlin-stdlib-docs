# Random.nextBoolean

`kotlin.random` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

获取下一个`Boolean`随机值。

@sample 样本. 随机. 兰多姆. 下博爱

??? note "查看英文原文"

    Gets the next random `Boolean` value.
    
    @sample samples.random.Randoms.nextBoolean

## 声明与重载

### 1. Common

```kotlin
public open fun nextBoolean(): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L160)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.sin
import kotlin.random.Random
import kotlin.test.assertTrue



fun main() {
    val presents = listOf("Candy", "Balloon", "Ball")
    // a random partition, the result may be different every time
    val (alicePresents, bobPresents) = presents.partition { Random.nextBoolean() }

    println("Alice receives $alicePresents")
    println("Bob receives $bobPresents")
}
```

```text title="输出"
Alice receives [Candy, Ball]
Bob receives [Balloon]
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/random/randoms.kt#L55)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
