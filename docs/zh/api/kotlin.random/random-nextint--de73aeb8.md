# Random.nextInt

`kotlin.random` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

从随机号码生成器中获取下一个随机的 `Int` 。

产生`Int`随机值,平均分布在`Int.MIN_VALUE`至`Int.MAX_VALUE`之间(含)。

@sample 样本. 随机. 兰多姆. 下游

??? note "查看英文原文"

    Gets the next random `Int` from the random number generator.
    
    Generates an `Int` random value uniformly distributed between `Int.MIN_VALUE` and `Int.MAX_VALUE` (inclusive).
    
    @sample samples.random.Randoms.nextInt

## 声明与重载

### 1. Common

```kotlin
public open fun nextInt(): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L35)

### 2. Common

```kotlin
public open fun nextInt(until: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L44)

从随机数生成器中获取下一个不负数的`Int`, 其数量小于指定的 `until` 装束。

产生`Int` 随机值,统一分布在`0`(含)和指定的`until`约束(不含)之间。

@param直到必须呈阳性。

@throws 非法设备,如果`until`为负或零,则不在此限。

@sample 样本. 随机. 兰多姆. 下游

### 3. Common

```kotlin
public open fun nextInt(from: Int, until: Int): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/random/Random.kt#L57)

从指定范围内随机数字生成器中获取下一个随机的 `Int` 。

产生`Int` 随机值,在指定的`from`(含)和`until`(排他)界限之间统一分布。

@throws 非法采购,如果`from`大于或等于 `until` ,则不在此列。

@sample 样本. 随机. 兰多姆. 下游

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.sin
import kotlin.random.Random
import kotlin.test.assertTrue



fun main() {
    val randomInts = List(5) { Random.nextInt() }
    println(randomInts)
    val sortedRandomInts = randomInts.sorted()
    println(sortedRandomInts)
}
```

```text title="输出"
[-664942724, 1630502718, -985679184, 823598579, 151027799]
[-985679184, -664942724, 151027799, 823598579, 1630502718]
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/random/randoms.kt#L111)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.math.sin
import kotlin.random.Random
import kotlin.test.assertTrue



fun main() {
    val menu = listOf("Omelette", "Porridge", "Cereal", "Chicken", "Pizza", "Pasta")
    val forBreakfast = Random.nextInt(until = 3).let { menu[it] }
    val forLunch = Random.nextInt(from = 3, until = 6).let { menu[it] }
    // new meals every time
    println("Today I want $forBreakfast for breakfast, and $forLunch for lunch.")
}
```

```text title="输出"
Today I want Omelette for breakfast, and Pasta for lunch.
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/random/randoms.kt#L119)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
