# PropertyDelegateProvider

`kotlin.properties` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

可用于实施财产代表提供者的基础接口。

仅提供此功能方便; 只要代表提供方有相同的签名方法, 您不必扩展此接口 。

@param T 属于授权财产的物品类型。 @param D 属于该提供商提供的财产代表类型。

??? note "查看英文原文"

    Base interface that can be used for implementing property delegate providers.
    
    This is provided only for convenience; you don't have to extend this interface
    as long as your delegate provider has a method with the same signature.
    
    @param T the type of object which owns the delegated property.
    @param D the type of property delegates this provider provides.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
public fun interface PropertyDelegateProvider<in T, out D>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/Interfaces.kt#L56)

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
