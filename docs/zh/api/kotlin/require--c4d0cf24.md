# require

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

检查调用者传入的参数是否满足条件。条件为 `false` 时抛出 `IllegalArgumentException`；带 `lazyMessage` 的重载可以提供自定义错误消息，并且只在检查失败时计算消息。检查成功时继续执行。

??? note "查看英文原文"

    Throws an `IllegalArgumentException` if the `value` is false.
    
    @sample samples.misc.Preconditions.failRequireWithoutLazyMessage

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun require(value: Boolean): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt#L13)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun require(value: Boolean, lazyMessage: () -> Any): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt#L26)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
fun main() {
    require(3 > 0)
    println("argument valid")

    try {
        require(-1 > 0)
    } catch (e: IllegalArgumentException) {
        println("${e::class.simpleName}: ${e.message}")
    }

    try {
        require(-1 > 0) { "count must be positive" }
    } catch (e: IllegalArgumentException) {
        println("${e::class.simpleName}: ${e.message}")
    }
}
```

```text title="输出"
argument valid
IllegalArgumentException: Failed requirement.
IllegalArgumentException: count must be positive
```

## 版本与来源

本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。
