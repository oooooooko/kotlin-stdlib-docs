# check

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

检查当前对象或程序状态是否满足要求。条件为 `false` 时抛出 `IllegalStateException`。它和 `require` 的主要区别是用途和异常类型：`require` 检查参数，`check` 检查状态。自定义消息只在失败时计算。

??? note "查看英文原文"

    Throws an `IllegalStateException` if the `value` is false.
    
    @sample samples.misc.Preconditions.failCheckWithLazyMessage

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun check(value: Boolean): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt#L75)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun check(value: Boolean, lazyMessage: () -> Any): Unit
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt#L90)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
fun main() {
    check(true)
    println("state valid")

    try {
        check(false)
    } catch (e: IllegalStateException) {
        println("${e::class.simpleName}: ${e.message}")
    }

    try {
        check(false) { "service is not initialized" }
    } catch (e: IllegalStateException) {
        println("${e::class.simpleName}: ${e.message}")
    }
}
```

```text title="输出"
state valid
IllegalStateException: Check failed.
IllegalStateException: service is not initialized
```

## 版本与来源

本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。
