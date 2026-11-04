# Random.nextDouble

`kotlin.random` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

获取下一个`Double` 随机值,在 0(包括) 和 1(不包括) 之间统一分布。

@sample 样本. 随机性. 兰多姆. 下个多布尔

??? note "查看英文原文"

    Gets the next random `Double` value uniformly distributed between 0 (inclusive) and 1 (exclusive).
    
    @sample samples.random.Randoms.nextDouble

## 声明与重载

### 1. Common

```kotlin
public open fun nextDouble(): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L167)

### 2. Common

```kotlin
public open fun nextDouble(until: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L174)

从随机数生成器中获取下一个不负数的`Double`, 其数量小于指定的 `until` 装束。

产生`Double`随机值,统一分布在0(含)和`until`(不含)之间。

`until` 必须是一鳍编号,否则行为将不予说明。

@throws 非法设备,如果`until`为负或零,则不在此限。

@sample 样本. 随机性. 兰多姆. 下个从中流出

### 3. Common

```kotlin
public open fun nextDouble(from: Double, until: Double): Double
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L187)

从指定范围内随机数字生成器中获取下一个随机的 `Double` 。

产生`Double` 随机值,在指定的`from`(含)和`until`(排他)界限之间统一分布。

`from`和`until`必须是有限的数字,否则行为将不予说明。

@throws 非法采购,如果`from`大于或等于 `until` ,则不在此列。

@sample 样本. 随机性. 兰多姆. 下个从中流出

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.sin
import kotlin.random.Random
import kotlin.test.assertTrue



fun main() {
    if (Random.nextDouble() <= 0.3) {
        println("There was 30% possibility of rainy weather today and it is raining.")
    } else {
        println("There was 70% possibility of sunny weather today and the sun is shining.")
    }
}
```

```text title="输出"
There was 30% possibility of rainy weather today and it is raining.
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/random/randoms.kt#L83)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.sin
import kotlin.random.Random
import kotlin.test.assertTrue



fun main() {
    val firstAngle = Random.nextDouble(until = Math.PI / 6);
    println(sin(firstAngle) < 0.5)

    val secondAngle = Random.nextDouble(from = Math.PI / 6, until = Math.PI / 2)
    val sinValue = sin(secondAngle)
    println(sinValue >= 0.5 && sinValue < 1.0)
}
```

```text title="输出"
true
true
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/random/randoms.kt#L92)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
