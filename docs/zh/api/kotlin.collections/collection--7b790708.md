# Collection

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

通用元素集。 界面可以对包含元素进行迭接,检查收藏中是否含有某种元素。 复杂的操作以这一功能为基础,以 `kotlin.collections` 扩展功能的形式提供。

此接口支持的功能仅以只读方式访问收藏; 读/ write 访问通过 `MutableCollection` 接口支持。

`Collection`是包含多个不同同质元素的物体的最高端界面。其他更具体的界面,如`List`、 `Set` 和`Map`,扩展`Collection`,以提供更具体的保证,说明元素的储存和存取方式,并提供更丰富的功能。

`Collection`执行可能对于包含元素的顺序和独特性有不同的保障,例如,`List`中包含元素的订购,可能含有重复,而`Set`中包含元素的安装可能不包含重复,也没有对其规定特别命令。

`Collection.contains` 行为是具体执行行为,但通常使用 `Any.equals` 来比较平等要素。

`Collection` 并不要求`toString`、 `equals` 和 `hashCode` 功能和实施可以自由继承默认行为。 更多专业界面可以扩展`Collection`( 类似 `List`、 `Set` 和 `Map`) , 可能会施加更严格的要求。

@param E 即收藏中所含元素的类型。 收藏的元素类型是元素类型的共变。

??? note "查看英文原文"

    A generic collection of elements. The interface allows iterating over contained elements
    and checking whether something is contained within the collection. Complex operations are built upon this
    functionality and provided in form of `kotlin.collections` extension functions.
    
    Functions in this interface support only read-only access to the collection;
    read/write access is supported through the `MutableCollection` interface.
    
    `Collection` is a top-level interface for objects aggregating multiple different homogenous elements. Other more specific interfaces,
    like `List`, `Set`, and `Map` extend `Collection` to provide more specific guarantees on how elements are stored and accessed, as well
    as provide richer functionality.
    
    `Collection` implementation may have different guarantees on the order and uniqueness of contained elements,
    for example, elements contained in a `List` are ordered and could contain duplicates, while elements contained in
    a `Set` may not contain duplicates and there is no particular order imposed on them.
    
    `Collection.contains` behavior is implementation-specific, but usually, it uses `Any.equals` to compare elements
    for equality.
    
    `Collection` does not impose any requirements for `toString`, `equals` and `hashCode` functions
    and implementations are free to inherit a default behavior.
    More specialized interfaces extending `Collection` (like `List`, `Set` and `Map`) may impose stricter requirements.
    
    @param E the type of elements contained in the collection. The collection is covariant in its element type.

## 声明与重载

### 1. Common

```kotlin
public expect interface Collection<out E> : Iterable<E>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L33)

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
import kotlin.collections.*

fun main() {
    val value = listOf(1, 2, 3)
    println(value)
}
```

```text title="输出"
[1, 2, 3]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
