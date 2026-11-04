# AutoCloseable.close

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

关闭此资源 。

键,因此强烈建议使用`use`代之以职能,
正确关闭此资源, 不论是否出现例外 。

实施这一接口的人应该更加关注关闭业务可能失败的情况,建议关闭所有基本资源,在宣布例外之前,内部资源标记为关闭,这样的战略可以确保资源及时释放,避免资源包装或由另一资源包扎时可能出现的许多问题。

请注意,多次调用此函数可能会产生一些可见的副作用。 但是,强烈建议该接口的操作者使该函数成为无能的。

??? note "查看英文原文"

    Closes this resource.
    
    This function may throw, thus it is strongly recommended to use the `use` function instead,
    which closes this resource correctly whether an exception is thrown or not.
    
    Implementers of this interface should pay increased attention to cases where the close operation may fail.
    It is recommended that all underlying resources are closed and the resource internally is marked as closed
    before throwing an exception. Such a strategy ensures that the resources are released in a timely manner,
    and avoids many problems that could come up when the resource wraps, or is wrapped, by another resource.
    
    Note that calling this function more than once may have some visible side effect.
    However, implementers of this interface are strongly recommended to make this function idempotent.

## 声明与重载

### 1. Common

```kotlin
public fun close(): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/AutoCloseable.kt#L17)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class)

import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.math.*
import kotlin.random.*
import kotlin.ranges.*
import kotlin.reflect.*
import kotlin.sequences.*
import kotlin.text.*
import kotlin.time.*
import kotlin.time.Duration.Companion.seconds
import kotlin.time.Duration.Companion.milliseconds
import kotlin.uuid.*
import kotlin.io.encoding.*
import java.io.File
import kotlin.*

fun main() {
    val source = AutoCloseable { println("closed") }
    val result = source.`close`()
    println(result)
}
```

```text title="输出"
closed
kotlin.Unit
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
