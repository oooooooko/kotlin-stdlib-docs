# Delegates.observable

`kotlin.properties` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个读写/ 写属性的产权代表, 该属性在更改时会调用指定的回调功能。 @param 初始值为该属性的初始值。 @param 更改在更改该属性后调回的回调。 当调回时, 属性的价值已经更改 。

@sample 样本. 适当性. 代表. 观察

??? note "查看英文原文"

    Returns a property delegate for a read/write property that calls a specified callback function when changed.
    @param initialValue the initial value of the property.
    @param onChange the callback which is called after the change of the property is made. The value of the property
     has already been changed when this callback is invoked.
    
     @sample samples.properties.Delegates.observableDelegate

## 声明与重载

### 1. Common

```kotlin
public inline fun <T> observable(initialValue: T, crossinline onChange: (property: KProperty<*>, oldValue: T, newValue: T) -> Unit):
            ReadWriteProperty<Any?, T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/Delegates.kt#L23)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.properties.Delegates



fun main() {
    var observed = false
    var max: Int by Delegates.observable(0) { property, oldValue, newValue ->
        observed = true
    }

    println(max)
    println(observed)

    max = 10
    println(max)
    println(observed)
}
```

```text title="输出"
0
false
10
true
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/properties/delegates.kt#L65)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
