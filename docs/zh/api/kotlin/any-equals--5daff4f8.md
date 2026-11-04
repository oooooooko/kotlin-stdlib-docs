# Any.equals

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

表示其他对象是否“等于”此对象。

执行工作必须满足下列要求:
* 弹性:对于任何非核值`x`,`x.equals(x)`应返回正态。
* 对称:对于任何非核值 `x` 和 `y`,`x.equals(y)`只有在`y.equals(x)` 返回真实时才应恢复为真实。
* 中转:对于任何非核值 `x`、`y`和`z`,如果`x.equals(y)`返回真实,`y.equals(z)`返回真实,那么`x.equals(z)`应该返回真实。
* 一致:对于任何非中值`x`和`y`,`x.equals(y)`多次援引时,只要`equals`比较对象的比较没有修改过任何资料,就始终如一地返回真实或一贯返回假。
* 永远不等于无效:对于任何非核值`x`,`x.equals(null)`应退回假的。

更多信息:有关[平等](https://kotlinlang.org/docs/reference/equality.html),科特林语)。

??? note "查看英文原文"

    Indicates whether some other object is "equal to" this one.
    
    Implementations must fulfil the following requirements:
    * Reflexive: for any non-null value `x`, `x.equals(x)` should return true.
    * Symmetric: for any non-null values `x` and `y`, `x.equals(y)` should return true if and only if `y.equals(x)` returns true.
    * Transitive: for any non-null values `x`, `y`, and `z`, if `x.equals(y)` returns true and `y.equals(z)` returns true, then `x.equals(z)` should return true.
    * Consistent: for any non-null values `x` and `y`, multiple invocations of `x.equals(y)` consistently return true or consistently return false, provided no information used in `equals` comparisons on the objects is modified.
    * Never equal to null: for any non-null value `x`, `x.equals(null)` should return false.
    
    Read more about [equality](https://kotlinlang.org/docs/reference/equality.html) in Kotlin.

## 声明与重载

### 1. Common

```kotlin
public open operator fun equals(other: Any?): Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Any.kt#L13)

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
    val source = Any()
    val result = source.`equals`(1)
    println(result)
}
```

```text title="输出"
false
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
