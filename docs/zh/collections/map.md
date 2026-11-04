---
title: map · 逐个转换元素
description: Kotlin Iterable.map 的中文用法，包含集合转换、字段提取、可空结果、空集合和 forEach 对比的完整示例与输出。
---

# map：逐个转换元素

对集合里的每个元素执行一次转换，把每次转换的返回值按遍历顺序收集成一个 `List`。

**适合：** 数值计算、提取对象字段、生成展示文本，以及把一种数据结构转换成另一种。

| 项目 | 说明 |
| --- | --- |
| 文档基准 | `kotlin-stdlib 2.4.21` |
| 完整名称 | `kotlin.collections.map` |
| API 类型 | `Iterable<T>` 的扩展函数，`List`、`Set` 等可使用 |
| 返回类型 | `List<R>` |
| 引入版本 | Kotlin 1.0 |
| 平台 | Common API，可用于 JVM、JS、Native、Wasm |
| 本文范围 | `Iterable<T>.map`；数组、`Map`、字符串和 `Sequence` 的同名扩展另行介绍 |

## 函数签名

```kotlin title="函数签名"
inline fun <T, R> Iterable<T>.map(transform: (T) -> R): List<R>
```

| 部分 | 含义 |
| --- | --- |
| `T` | 原集合中元素的类型 |
| `R` | 转换后元素的类型，可以和 `T` 不同，也可以是可空类型 |
| `transform` | 接收一个原元素，返回一个转换结果 |
| `List<R>` | 按原集合的遍历顺序保存转换结果的列表 |

`map` 属于默认导入的 `kotlin.collections` 包，下面的示例都不需要额外 `import`。

## 1. 基础用法：把数字乘以 10

```kotlin title="基础转换" linenums="1"
fun main() {
    val numbers = listOf(1, 2, 3)
    val result = numbers.map { it * 10 }

    println(result)
    println(numbers)
}
```

```text title="输出"
[10, 20, 30]
[1, 2, 3]
```

`it` 是当前正在处理的元素。本例依次计算 `1 * 10`、`2 * 10`、`3 * 10`，返回三个结果组成的列表。

!!! tip "记住返回值"
    使用 `val result = ...` 接住结果。`map` 自身不会把转换结果写回原集合。

## 2. 实际场景：提取对象字段

从用户列表中取出姓名，得到可用于界面展示的字符串列表。

```kotlin title="提取用户姓名" linenums="1"
data class User(val id: Int, val name: String)

fun main() {
    val users = listOf(
        User(1, "小林"),
        User(2, "小周"),
        User(3, "小陈")
    )
    val names: List<String> = users.map { it.name }

    println(names)
    println(users.map(User::id))
}
```

```text title="输出"
[小林, 小周, 小陈]
[1, 2, 3]
```

元素类型由 `User` 变成了 `String`。当转换只读取一个属性时，也可以像 `User::id` 一样使用属性引用。

## 3. 可空结果：map 会保留 null

尝试把输入文本转换成整数。无法转换的文本由 `toIntOrNull()` 返回 `null`。

```kotlin title="保留与过滤空值" linenums="1"
fun main() {
    val inputs = listOf("12", "hello", "30")
    val withNulls: List<Int?> = inputs.map { it.toIntOrNull() }
    val withoutNulls: List<Int> = inputs.mapNotNull { it.toIntOrNull() }

    println(withNulls)
    println(withoutNulls)
}
```

```text title="输出"
[12, null, 30]
[12, 30]
```

`map` 保留每个转换结果，包括 `null`。需要丢弃转换结果中的 `null` 时，使用 `mapNotNull`。

## 4. 空集合：不会执行转换函数

```kotlin title="空集合行为" linenums="1"
fun main() {
    var calls = 0
    val result = emptyList<Int>().map {
        calls++
        it * 10
    }

    println(result)
    println("转换次数：$calls")
}
```

```text title="输出"
[]
转换次数：0
```

空集合的结果仍是空列表，不会调用 `transform`，不需要为此单独写 `isEmpty()` 判断。

## 5. 和 forEach 对比：是否需要结果列表

`map` 用于得到转换结果，`forEach` 用于执行遍历操作，例如逐项打印。

```kotlin title="map 与 forEach" linenums="1"
fun main() {
    val numbers = listOf(1, 2)
    val mapped = numbers.map { it * 10 }
    println("map 的结果：$mapped")

    val traversed = numbers.forEach { println("处理 $it") }
    println("forEach 的结果：$traversed")
}
```

```text title="输出"
map 的结果：[10, 20]
处理 1
处理 2
forEach 的结果：kotlin.Unit
```

!!! warning "只做操作时用 forEach"
    如果只是打印、记录日志或调用其他操作，使用 `forEach` 更直接。`map { println(it) }` 会把每次 `println` 的返回值收集成 `List<Unit>`，通常没有实际用途。

## 行为与边界

- **立即执行。** `Iterable.map` 在调用时遍历集合。集合上的多次 `map` 会逐次产生中间列表；需要延迟处理时，可以考虑 `Sequence` 的同名扩展。
- **顺序与数量。** 正常完成时，结果顺序与源集合的遍历顺序一致，结果数量与源元素数量相同。`Set` 的顺序取决于其具体实现。
- **异常会向外抛出。** 转换函数抛出异常时，本次转换中止，调用者不会拿到一个正常返回的部分结果列表。此前已经发生的副作用不会自动撤销。
- **不会自动深拷贝。** 如果转换返回原来的可变对象，结果列表仍引用这些对象；转换函数自身也可以修改对象，不能把 `map` 理解为“保证原数据永远不变”。
- **有限集合的开销。** 对有 `n` 个元素的集合，转换函数调用 `n` 次，并存储 `n` 个结果；若每次转换耗时固定，整体时间为 `O(n)`，结果存储为 `O(n)`。

## 相近 API 怎么选

| 需求 | 选择 |
| --- | --- |
| 每个元素转换成一个结果 | `map` |
| 转换后丢弃 `null` | `mapNotNull` |
| 转换时还需要元素下标 | `mapIndexed` |
| 每个元素转换成多个元素，再合并结果 | `flatMap` |
| 只保留满足条件的原元素 | `filter` |
| 只执行遍历操作 | `forEach` |
| 把转换结果加入已有集合 | `mapTo` |

## 版本与来源

本文以 **kotlin-stdlib 2.4.21** 为基准，完整程序均以 JVM 为运行平台。函数签名代码块用于说明 API，不是独立程序。

- [官方 API 参考：kotlin.collections.map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/map.html)
- [2.4.21 对应源码：_Collections.kt](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt)

官方 API 页面会随版本更新，固定版本的实现与 KDoc 请以源码标签为准。
