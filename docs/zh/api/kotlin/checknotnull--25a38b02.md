# checkNotNull

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

检查表示当前状态的值是否非空。成功时返回非空值，并支持对符合条件的变量进行智能转换；为 `null` 时抛出 `IllegalStateException`。它和 `requireNotNull` 的异常类型不同，适用于对象尚未初始化等状态错误。

??? note "查看英文原文"

    Throws an `IllegalStateException` if the `value` is null. Otherwise
    returns the not null value.
    
    @sample samples.misc.Preconditions.failCheckWithLazyMessage

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun <T : Any> checkNotNull(value: T?): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt#L106)

### 2. Common

```kotlin
@kotlin.internal.InlineOnly
@IgnorableReturnValue
public inline fun <T : Any> checkNotNull(value: T?, lazyMessage: () -> Any): T
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt#L121)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
fun stateLength(state: String?): Int {
    checkNotNull(state)
    return state.length
}

fun main() {
    println(stateLength("ready"))
    println(checkNotNull("initialized") { "state is not initialized" })

    try {
        stateLength(null)
    } catch (e: IllegalStateException) {
        println("${e::class.simpleName}: ${e.message}")
    }

    try {
        checkNotNull(null as String?) { "state is not initialized" }
    } catch (e: IllegalStateException) {
        println("${e::class.simpleName}: ${e.message}")
    }
}
```

```text title="输出"
5
initialized
IllegalStateException: Required value was null.
IllegalStateException: state is not initialized
```

## 版本与来源

本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。
