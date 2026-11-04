# Delegates.vetoable

`kotlin.properties` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个读写/ 写属性的产权代表, 该属性在修改时会调用指定的回调功能, 允许回调否决修改。 @param 初始值对财产的初始值进行否决。 @param 调整了尝试更改财产价值之前调用的回调。 当调回时, 属性的价值还没有改变。 如果回调返回 `true` , 则该属性的价值被设置为新值, 如果回调返回返回 `false` , 新值将被丢弃, 财产仍然保留旧值 。

@sample 样本. 适当性. 代表. 可见

??? note "查看英文原文"

    Returns a property delegate for a read/write property that calls a specified callback function when changed,
    allowing the callback to veto the modification.
    @param initialValue the initial value of the property.
    @param onChange the callback which is called before a change to the property value is attempted.
     The value of the property hasn't been changed yet, when this callback is invoked.
     If the callback returns `true` the value of the property is being set to the new value,
     and if the callback returns `false` the new value is discarded and the property remains its old value.
    
     @sample samples.properties.Delegates.vetoableDelegate
     @sample samples.properties.Delegates.throwVetoableDelegate

## 声明与重载

### 1. Common

```kotlin
public inline fun <T> vetoable(initialValue: T, crossinline onChange: (property: KProperty<*>, oldValue: T, newValue: T) -> Boolean):
            ReadWriteProperty<Any?, T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/Delegates.kt#L37)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.properties.Delegates



fun main() {
    var max: Int by Delegates.vetoable(0) { property, oldValue, newValue ->
        newValue > oldValue
    }

    println(max)

    max = 10
    println(max)

    max = 5
    println(max)
}
```

```text title="输出"
0
10
10
```

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/properties/delegates.kt#L26)

### 示例 2 · JVM

```kotlin title="示例 2" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.properties.Delegates
import kotlin.test.*



fun main() {
    var max: Int by Delegates.vetoable(0) { property, oldValue, newValue ->
        if (newValue > oldValue) true else throw IllegalArgumentException("New value must be larger than old value.")
    }

    println(max)

    max = 10
    println(max)

    assertFailsWith<IllegalArgumentException> { max = 5 }
}
```

```text title="输出"
0
10
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/properties/delegates.kt#L41)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
