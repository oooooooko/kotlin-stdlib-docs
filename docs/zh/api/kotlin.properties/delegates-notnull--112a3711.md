# Delegates.notNull

`kotlin.properties` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个在非`null`值的读写/写字属性的产权代表,该属性不是在工程设计期间启动,而是在以后某个时候启动。在初始值被指定之前试图读取该属性,结果属于例外。

@sample 样本. 适当性. 代表. 而不是NullDelegate

??? note "查看英文原文"

    Returns a property delegate for a read/write property with a non-`null` value that is initialized not during
    object construction time but at a later time. Trying to read the property before the initial value has been
    assigned results in an exception.
    
    @sample samples.properties.Delegates.notNullDelegate

## 声明与重载

### 1. Common

```kotlin
public fun <T : Any> notNull(): ReadWriteProperty<Any?, T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/Delegates.kt#L14)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)
import kotlin.properties.Delegates
import kotlin.test.*



fun main() {
    var max: Int by Delegates.notNull()

    assertFailsWith<IllegalStateException> { println(max) }

    max = 10
    println(max)
}
```

```text title="输出"
10
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/samples/test/samples/properties/delegates.kt#L55)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
