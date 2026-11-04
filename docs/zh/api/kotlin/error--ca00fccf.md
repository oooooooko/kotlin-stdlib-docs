# error

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

立即抛出带指定消息的 `IllegalStateException`，不会正常返回。返回类型是 `Nothing`，因此可以放在 `when` 分支、Elvis 表达式等需要某个返回类型的位置。异常会结束当前执行路径，而不是返回错误字符串。

??? note "查看英文原文"

    Throws an `IllegalStateException` with the given `message`.
    
    @sample samples.misc.Preconditions.failWithError

## 声明与重载

### 1. Common

```kotlin
@kotlin.internal.InlineOnly
public inline fun error(message: Any): Nothing
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Preconditions.kt#L143)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
fun statusText(code: Int): String = when (code) {
    200 -> "OK"
    else -> error("Unexpected status: $code")
}

fun main() {
    println(statusText(200))

    try {
        println(statusText(500))
    } catch (e: IllegalStateException) {
        println("${e::class.simpleName}: ${e.message}")
    }
}
```

```text title="输出"
OK
IllegalStateException: Unexpected status: 500
```

## 版本与来源

本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。
