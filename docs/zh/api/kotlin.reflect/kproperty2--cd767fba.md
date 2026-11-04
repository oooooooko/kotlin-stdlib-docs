# KProperty2

`kotlin.reflect` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

代表财产,其业务需要两个接收者作为参数,例如按类别申报的扩展财产。

@param D 第一接收者的类型。 如果在某一类中,扩展财产是宣布该财产的类别,或该类中的任何子类别。 @param E 是第二接收者的类型。如果在某一类中,扩展财产是扩展财产的类型。 @param V是财产价值的类型。

??? note "查看英文原文"

    Represents a property, operations on which take two receivers as parameters,
    such as an extension property declared in a class.
    
    @param D the type of the first receiver. In case of the extension property in a class this is
           the type of the declaring class of the property, or any subclass of that class.
    @param E the type of the second receiver. In case of the extension property in a class this is
           the type of the extension receiver.
    @param V the type of the property value.

## 声明与重载

### 1. Common

```kotlin
public expect interface KProperty2<D, E, out V> : KProperty<V>, (D, E) -> V
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/reflect/KProperty.kt#L87)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.reflect.KMutableProperty2
import kotlin.reflect.full.memberExtensionProperties
class Labels(var prefix: String) {
    var Int.label: String
        get() = "$prefix$this"
        set(value) { prefix = value }
}
fun main() {
    @Suppress("UNCHECKED_CAST")
    val property = Labels::class.memberExtensionProperties.single() as KMutableProperty2<Labels, Int, String>
    val labels = Labels("item-")
    println(property.get(labels, 7))
    property.set(labels, 7, "new-")
    println(property.get(labels, 7))
}
```

```text title="输出"
item-7
new-7
```

此示例需要 `kotlin-reflect:2.4.21`。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
