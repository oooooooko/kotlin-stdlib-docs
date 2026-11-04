# ObservableProperty.afterChange

`kotlin.properties` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

财产更改后调回。 调回时, 财产的价值已经更改 。

??? note "查看英文原文"

    The callback which is called after the change of the property is made. The value of the property
    has already been changed when this callback is invoked.

## 声明与重载

### 1. Common

```kotlin
protected open fun afterChange(property: KProperty<*>, oldValue: V, newValue: V): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/ObservableProperty.kt#L25)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.properties.ObservableProperty
import kotlin.reflect.KProperty
class NonNegative(initial: Int) : ObservableProperty<Int>(initial) {
    override fun beforeChange(property: KProperty<*>, oldValue: Int, newValue: Int): Boolean = newValue >= 0
    override fun afterChange(property: KProperty<*>, oldValue: Int, newValue: Int) {
        println("${property.name}: $oldValue -> $newValue")
    }
}
fun main() {
    val delegate = NonNegative(1)
    var count by delegate
    println(count)
    count = 2
    count = -1
    println(count)
    println(delegate.toString())
}
```

```text title="输出"
1
count: 1 -> 2
2
ObservableProperty(value=2)
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
