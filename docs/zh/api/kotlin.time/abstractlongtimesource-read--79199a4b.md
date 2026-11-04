# AbstractLongTimeSource.read

`kotlin.time` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

放弃这一受保护方法, 以返回目前对时间源的读数, 即 `unit` 属性所指定的单位的`Long` 号。

请注意, 首次使用 `markNow` 的这个方法返回的值是“ 零” 读数, 而此“ 零” 读数的差数是用来计算以后的值。 因此, 推荐不从第一次返回读数返回 `±Long.MAX_VALUE` , 因为这样会让这个时间源翻转到返回的时间标记的未来/ 过去边界 。

??? note "查看英文原文"

    This protected method should be overridden to return the current reading of the time source expressed as a `Long` number
    in the unit specified by the `unit` property.
    
    Note that the value returned by this method when `markNow` is called the first time is used as "zero" reading
    and the difference from this "zero" reading is calculated for subsequent values.
    Therefore, it's not recommended to return values farther than `±Long.MAX_VALUE` from the first returned reading
    as this will cause this time source flip over future/past boundary for the returned time marks.

## 声明与重载

### 1. Common

```kotlin
protected abstract fun read(): Long
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/time/TimeSources.kt#L29)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.time.*
class ManualClock : AbstractLongTimeSource(DurationUnit.MILLISECONDS) {
    var reading = 0L
    override fun read(): Long = reading
    fun unitName(): String = unit.name
}
fun main() {
    val clock = ManualClock()
    val mark = clock.markNow()
    clock.reading = 25L
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
