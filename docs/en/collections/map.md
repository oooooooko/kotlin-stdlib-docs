---
title: map · Transform each element
---

# map: transform each element

`kotlin.collections` · **kotlin-stdlib 2.4.21**

Apply a function to every element of an iterable and collect the results in a `List`, preserving iteration order.
This page documents the `Iterable<T>` extension, available to collections such as `List` and `Set`. Array, string, map, and sequence overloads are separate APIs.

## Signature

```kotlin
inline fun <T, R> Iterable<T>.map(transform: (T) -> R): List<R>
```

`T` is the input element type. `R` is the result type and may differ from `T` or be nullable.
`transform` receives one input element and returns one result. No additional import is required.

## Basic conversion

Multiply each number by ten. The original list remains unchanged because the transformation only reads its elements.

```kotlin title="Example" linenums="1"
fun main() {
    val numbers = listOf(1, 2, 3)
    val result = numbers.map { it * 10 }

    println(result)
    println(numbers)
}
```

```text title="Output"
[10, 20, 30]
[1, 2, 3]
```

## Extract object fields

Convert a list of users into a list of names. Property references such as `User::id` are another concise way to select a field.

```kotlin title="Example" linenums="1"
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

```text title="Output"
[小林, 小周, 小陈]
[1, 2, 3]
```

## Nullable results

`map` keeps every transformation result, including `null`. Use `mapNotNull` to discard null results.

```kotlin title="Example" linenums="1"
fun main() {
    val inputs = listOf("12", "hello", "30")
    val withNulls: List<Int?> = inputs.map { it.toIntOrNull() }
    val withoutNulls: List<Int> = inputs.mapNotNull { it.toIntOrNull() }

    println(withNulls)
    println(withoutNulls)
}
```

```text title="Output"
[12, null, 30]
[12, 30]
```

## Empty collections

An empty source produces an empty result list without calling the transformation.

```kotlin title="Example" linenums="1"
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

```text title="Output"
[]
转换次数：0
```

## map versus forEach

Use `map` when you need transformed values. Use `forEach` for actions such as printing; it returns `Unit`.

```kotlin title="Example" linenums="1"
fun main() {
    val numbers = listOf(1, 2)
    val mapped = numbers.map { it * 10 }
    println("map 的结果：$mapped")

    val traversed = numbers.forEach { println("处理 $it") }
    println("forEach 的结果：$traversed")
}
```

```text title="Output"
map 的结果：[10, 20]
处理 1
处理 2
forEach 的结果：kotlin.Unit
```

## Behavior and edge cases

- `Iterable.map` executes eagerly. Chained transformations produce intermediate lists; sequence transformations provide a lazy alternative.
- On successful completion, result order follows source iteration order and result size equals source size. A set's iteration order depends on its implementation.
- Exceptions thrown by the transformation propagate to the caller. No result list is returned, and previous side effects are not rolled back.
- Results are not deep copies. A transformation can return references to existing mutable objects or modify them itself.
- For a finite source with `n` elements and constant-time transformations, time and result storage are both `O(n)`.

## Related APIs

| Task | API |
| --- | --- |
| Transform and discard nulls | `mapNotNull` |
| Include the element index | `mapIndexed` |
| Transform into multiple elements and flatten | `flatMap` |
| Keep matching source elements | `filter` |
| Perform an action | `forEach` |
| Append transformed results to an existing collection | `mapTo` |

## Version and sources

All complete programs on this page were verified on the JVM with Kotlin / stdlib **2.4.21**. The declaration is a Common API and is available on JVM, JS, Native, and Wasm.

- [Official API reference](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/map.html)
- [Pinned 2.4.21 source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/common/src/generated/_Collections.kt)
