# KType.isMarkedNullable

`kotlin.reflect` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

如果源代码中标明该类型无效,则`true`。

对于 Kotlin 类型, 这意味着允许使用这种类型来表示 `null` 值。 实际上, 它意味着在结尾处以一个问号声明该类型。 对于非 Kotlin 类型, 它意味着使用这种类型声明的类型或符号附加注释, 带有运行时间- 保留无效性注释, 如 `javax.annotation.Nullable` 。

请注意,即使 `isMarkedNullable` 是假的,该类型的值仍可能为 `null` 。如果它是具有无效上限的类型参数类型,则可能发生这种情况:

```
fun <T> foo(t: T) {
    // isMarkedNullable == false for t's type, but t can be null here when T = "Any?"
}
```

??? note "查看英文原文"

    `true` if this type was marked nullable in the source code.
    
    For Kotlin types, it means that `null` value is allowed to be represented by this type.
    In practice it means that the type was declared with a question mark at the end.
    For non-Kotlin types, it means the type or the symbol which was declared with this type
    is annotated with a runtime-retained nullability annotation such as `javax.annotation.Nullable`.
    
    Note that even if `isMarkedNullable` is false, values of the type can still be `null`.
    This may happen if it is a type of the type parameter with a nullable upper bound:
    
    ```
    fun <T> foo(t: T) {
        // isMarkedNullable == false for t's type, but t can be null here when T = "Any?"
    }
    ```

## 声明与重载

### 1. Common

```kotlin
public val isMarkedNullable: Boolean
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/reflect/KType.kt#L35)

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
import kotlin.reflect.*

fun main() {
    val source = typeOf<List<String>>()
    val result = source.`isMarkedNullable`
    println(result)
}
```

```text title="输出"
false
```

此示例需要 `kotlin-reflect:2.4.21`。

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
