# KProperty1.get

`kotlin.reflect` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回该属性的当前值。

@param接收者是用来获取财产价值的接收者,例如,如果这是该类成员的财产,应该是等级实例,如果是该类成员的财产,应该是扩展接收者,如果是最高级的扩展财产。

??? note "查看英文原文"

    Returns the current value of the property.
    
    @param receiver the receiver which is used to obtain the value of the property.
                    For example, it should be a class instance if this is a member property of that class,
                    or an extension receiver if this is a top level extension property.

## 声明与重载

### 1. Common

```kotlin
public fun get(receiver: T): V
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/reflect/KProperty.kt#L61)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.reflect.KMutableProperty1
class Counter(var count: Int)
fun main() {
    val property: KMutableProperty1<Counter, Int> = Counter::count
    val counter = Counter(1)
    println(property.get(counter))
    property.set(counter, 42)
    println(counter.count)
}
```

```text title="输出"
1
42
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
