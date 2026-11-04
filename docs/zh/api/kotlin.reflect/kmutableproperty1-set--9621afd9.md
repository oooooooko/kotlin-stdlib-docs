# KMutableProperty1.set

`kotlin.reflect` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

修改财产的价值。

@param接收器接收器用来修改财产的价值。 例如,如果它是该类别成员的财产,应该是一个类别实例,如果是该类别成员的财产,或者如果是最高层扩展财产,应该是一个扩展接收器。 @param 值是该财产的新价值。

??? note "查看英文原文"

    Modifies the value of the property.
    
    @param receiver the receiver which is used to modify the value of the property.
                    For example, it should be a class instance if this is a member property of that class,
                    or an extension receiver if this is a top level extension property.
    @param value the new value to be assigned to this property.

## 声明与重载

### 1. Common

```kotlin
public fun set(receiver: T, value: V)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/reflect/KProperty.kt#L75)

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
