# setValue

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

扩展经营人,允许将`V`型动产转让给与`V`型动产相同的动产。

@receiver 财产是指 `V` 型动产,没有接收人,即它指的是顶级财产,或对接收人有约束。

示例:

```
class Login(val username: String, var incorrectAttemptCounter: Int = 0)
val defaultLogin = Login("Admin")
var defaultLoginAttempts by defaultLogin::incorrectAttemptCounter
// equivalent to
var defaultLoginAttempts: Int
    get() = defaultLogin.incorrectAttemptCounter
    set(value) { defaultLogin.incorrectAttemptCounter = value }
```

??? note "查看英文原文"

    An extension operator that allows delegating a mutable property of type `V`
    to a property reference to a mutable property of the same type `V`.
    
    @receiver A property reference to a mutable property of type `V`.
    The reference is without a receiver, i.e. it either references a top-level property or
    has the receiver bound to it.
    
    Example:
    
    ```
    class Login(val username: String, var incorrectAttemptCounter: Int = 0)
    val defaultLogin = Login("Admin")
    var defaultLoginAttempts by defaultLogin::incorrectAttemptCounter
    // equivalent to
    var defaultLoginAttempts: Int
        get() = defaultLogin.incorrectAttemptCounter
        set(value) { defaultLogin.incorrectAttemptCounter = value }
    ```

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline operator fun <V> KMutableProperty0<V>.setValue(thisRef: Any?, property: KProperty<*>, value: V)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/PropertyReferenceDelegates.kt#L35)

### 2. Common

```kotlin
@SinceKotlin("1.4")
@kotlin.internal.InlineOnly
public inline operator fun <T, V> KMutableProperty1<T, V>.setValue(thisRef: T, property: KProperty<*>, value: V)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/properties/PropertyReferenceDelegates.kt#L84)

扩展经营人,允许将可变成员或可变财产`V`型的扩展财产委托给可变成员或可变财产的扩展经营人,但该财产的属性是指可变成员或可变财产的扩展成员或可变财产,其类型为 `V` 型的扩展成员或可变财产。

@receiver 财产是指`V`型或其亚型的只读或可变财产,该财产是指`T`型无约束接收器。

示例:

```
class Login(val username: String, var incorrectAttemptCounter: Int)
var Login.attempts by Login::incorrectAttemptCounter
// equivalent to
var Login.attempts: Int
    get() = this.incorrectAttemptCounter
    set(value) { this.incorrectAttemptCounter = value }
```

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

val demoProperty = 42
var demoMutable = 42
fun demoFunction(value: Int): Int = value + 1

fun main() {
    val source = ::demoMutable
    val result = source.`setValue`(1, ::demoProperty, 1)
    println(result)
}
```

```text title="输出"
kotlin.Unit
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
