# PropertyDelegateProvider.provideDelegate

`kotlin.properties` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回给定对象的属性的委托。

此功能可用于扩展创建财产执行授权对象的逻辑(例如进行验证检查)。

@param 此文件是要求财产代表处理的物品。 @param财产是财产元数据。 @return财产代表是财产代表。

??? note "查看英文原文"

    Returns the delegate of the property for the given object.
    
    This function can be used to extend the logic of creating the object (e.g. perform validation checks)
    to which the property implementation is delegated.
    
    @param thisRef the object for which property delegate is requested.
    @param property the metadata for the property.
    @return the property delegate.

## 声明与重载

### 1. Common

```kotlin
public operator fun provideDelegate(thisRef: T, property: KProperty<*>): D
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/Interfaces.kt#L67)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.properties.PropertyDelegateProvider
import kotlin.properties.ReadOnlyProperty
fun main() {
    val provider = PropertyDelegateProvider<Any?, ReadOnlyProperty<Any?, String>> { _, property ->
        println("provide: ${property.name}")
        ReadOnlyProperty { _, _ -> "ready" }
    }
    val status by provider
    println(status)
}
```

```text title="输出"
provide: status
ready
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
