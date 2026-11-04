# ExperimentalContracts

`kotlin.contracts` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

该标记区分了试验性合同申报API, 用于在宣布用户功能合同时选择加入该特征。

任何附加`@ExperimentalContracts`的附加说明的声明的使用都必须接受,为此,必须说明使用`OptIn`的注释,例如`@OptIn(ExperimentalContracts::class)`, 或使用汇编者的论点`-opt-in=kotlin.contracts.ExperimentalContracts`。

??? note "查看英文原文"

    This marker distinguishes the experimental contract declaration API and is used to opt-in for that feature
    when declaring contracts of user functions.
    
    Any usage of a declaration annotated with `@ExperimentalContracts` must be accepted either by
    annotating that usage with the `OptIn` annotation, e.g. `@OptIn(ExperimentalContracts::class)`,
    or by using the compiler argument `-opt-in=kotlin.contracts.ExperimentalContracts`.

## 声明与重载

### 1. Common

```kotlin
@Retention(AnnotationRetention.BINARY)
@SinceKotlin("1.3")
@RequiresOptIn
@MustBeDocumented
public annotation class ExperimentalContracts
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/contracts/ContractBuilder.kt#L11)

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
import kotlin.contracts.*

fun main() {
    val value = kotlin.contracts.ExperimentalContracts()
    println(value)
}
```

```text title="输出"
@kotlin.contracts.ExperimentalContracts()
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
