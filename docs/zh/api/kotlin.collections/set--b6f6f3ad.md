# Set

`kotlin.collections` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

通用的无顺序的独特元素集合。 界面可以检查元素是否包含其中的一个元素, 并对所有元素进行循环。 复杂的操作以这一功能为基础, 并以 `kotlin.collections` 扩展功能的形式提供。

具体实施是 `Set` 如何界定元素的独特性。 如果没有另外说明,则`Set`执行通常使用`Any.equals`来区分元素。然而,这不是区分元素的唯一方法,有些实施可能使用优惠平等,或者比较其某些属性的元素。建议明确说明执行`Set`的类别如何区分元素。

此接口支持方法只支持只读访问集; 读/ write访问通过 `MutableSet` 接口支持。

与`List`不同的是, `Set` 没有保证任何特定的迭代令,但是,某些执行可自由获得固定迭代令,例如“较小”的迭代令,在某种意义上,元素在“较大”之前就被查看。

与 `Collection` 执行不同, `Set`执行必须超越 `Any.toString` 、 `Any.equals`和 `Any.hashCode` 功能并提供执行 : - `Set.toString` 应返回含有迭代顺序中包含元素的字符串表示的字符串。 - `Set.equals` 考虑两组相等,条件是它们包含相同数量的内容,并且一组中的每个元素都包含在另一组中。 与其它`equals`执行项目不同, `Set.equals` 考虑两组相等,即使它们属于不同类别; 这里的唯一要求是两组必须执行 `Set` 接口。 - `Set.hashCode` 应作为元素的哈瓦码总和使用以下算法计算:```kotlin
  var hashCode: Int = 0
  for (element in this) hashCode += element.hashCode()
  ```

@param E 组装所含元素的类型。 组装在元素类型中具有共变性。

??? note "查看英文原文"

    A generic unordered collection of unique elements. The interface allows checking if an element is contained by it
    and iterating over all elements. Complex operations are built upon this functionality
    and provided in form of `kotlin.collections` extension functions.
    
    It is implementation-specific how `Set` defines element's uniqueness. If not stated otherwise, `Set` implementations are usually
    distinguishing elements using `Any.equals`. However, it is not the only way to distinguish elements, and some implementations may use
    referential equality or compare elements by some of their properties. It is recommended to explicitly specify how a class
    implementing `Set` distinguish elements.
    
    Methods in this interface support only read-only access to the set;
    read/write access is supported through the `MutableSet` interface.
    
    Unlike `List`, `Set` does not guarantee any particular order for iteration. However, particular implementations
    are free to have fixed iteration order, like "smaller", in some sense, elements are visited prior to "larger". In this case,
    it is recommended to explicitly document ordering guarantees for the `Set` implementation.
    
    Unlike `Collection` implementations, `Set` implementations must override `Any.toString`, `Any.equals` and `Any.hashCode` functions
    and provide implementations such that:
    - `Set.toString` should return a string containing string representation of contained elements in iteration order.
    - `Set.equals` should consider two sets equal if and only if they contain the same number of elements and each element
      from one set is contained in another set. Unlike some other `equals` implementations, `Set.equals`
      should consider two sets equal even if they are instances of different classes; the only requirement here is that both sets have
      to implement `Set` interface.
    - `Set.hashCode` should be computed as a sum of elements' hash codes using the following algorithm:
      ```kotlin
      var hashCode: Int = 0
      for (element in this) hashCode += element.hashCode()
      ```
    
    @param E the type of elements contained in the set. The set is covariant in its element type.

## 声明与重载

### 1. Common

```kotlin
public expect interface Set<out E> : Collection<E>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/Collections.kt#L426)

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
    val value = linkedSetOf(1, 2, 3)
    println(value)
}
```

```text title="输出"
[1, 2, 3]
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
