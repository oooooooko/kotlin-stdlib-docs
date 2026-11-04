# requireNotNull

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

检查参数是否为 `null`，成功时返回非空值，失败时抛出 `IllegalArgumentException`。它声明了非空契约，因此对满足智能转换条件的变量，检查后可以直接访问其成员。带消息的重载只在参数为 `null` 时计算消息。

??? note "查看英文原文"

    Throws an `IllegalArgumentException` if the `value` is null. Otherwise returns the not null value.

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun <T : Any> requireNotNull(value: T?): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt#L42)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun <T : Any> requireNotNull(value: T?, lazyMessage: () -> Any): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt#L54)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
fun textLength(text: String?): Int {
    requireNotNull(text)
    return text.length
}

fun main() {
    println(textLength("Kotlin"))
    println(requireNotNull("stdlib") { "text is required" })

    try {
        textLength(null)
    } catch (e: IllegalArgumentException) {
        println("${e::class.simpleName}: ${e.message}")
    }

    try {
        requireNotNull(null as String?) { "text is required" }
    } catch (e: IllegalArgumentException) {
        println("${e::class.simpleName}: ${e.message}")
    }
}
```

```text title="输出"
6
stdlib
IllegalArgumentException: Required value was null.
IllegalArgumentException: text is required
```

## 版本与来源

本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。
