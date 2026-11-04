# Instant.compareTo

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

与 `this` 的瞬间相比, 与 `other` 的瞬间相比。

如果此时代表与其它时相同的时刻( 意思是它们等同对方) , 返回零, 如果此时比其他时先, 返回零, 如果此时晚于另一个时, 返回负数 。

@sample 样本的样本 时间。

??? note "查看英文原文"

    Compares `this` instant with the `other` instant.
    
    Returns zero if this instant represents the same moment as the other (meaning they are equal to one another),
    a negative number if this instant is earlier than the other,
    and a positive number if this instant is later than the other.
    
    @sample samples.time.Instants.compareToSample

## 声明与重载

### 1. Common

```kotlin
public override operator fun compareTo(other: Instant): Int
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/Instant.kt#L232)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.time.*
import kotlin.time.Duration.Companion.hours
import kotlin.time.Duration.Companion.nanoseconds
import kotlin.time.Duration.Companion.seconds



fun main() {
    val instant1 = Instant.parse("1970-01-01T00:00:00Z") // The Unix epoch.
    val instant2 = Instant.parse("2025-01-06T13:36:44Z")
    val instant3 = Instant.fromEpochSeconds(0) // The Unix epoch.

    println(instant1 < instant2)
    println(instant3 > instant1)
    println(instant3 == instant1)
}
```

```text title="输出"
true
false
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/time/instants.kt#L92)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
