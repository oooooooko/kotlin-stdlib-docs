# AbstractDoubleTimeSource

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

用于执行时间源的抽象分类, 返回其`unit` 值, 即`Double` 的读数。

@property 单位,表示该时间源的读数的单位。

??? note "查看英文原文"

    An abstract class used to implement time sources that return their readings as `Double` values in the specified `unit`.
    
    @property unit The unit in which this time source's readings are expressed.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalTime
@Deprecated(
    "Using AbstractDoubleTimeSource is no longer recommended, use AbstractLongTimeSource instead.",
    level = DeprecationLevel.ERROR
)
public abstract class AbstractDoubleTimeSource(protected val unit: DurationUnit) : TimeSource.WithComparableMarks
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSources.kt#L90)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.time.*
class ManualClock : AbstractDoubleTimeSource(DurationUnit.MILLISECONDS) {
    var reading = 0.0
    override fun read(): Double = reading
    fun unitName(): String = unit.name
}
fun main() {
    val clock = ManualClock()
    val mark = clock.markNow()
    clock.reading = 25.0
    println(clock.unitName())
    println(mark.elapsedNow())
}
```

```text title="输出"
MILLISECONDS
25ms
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
