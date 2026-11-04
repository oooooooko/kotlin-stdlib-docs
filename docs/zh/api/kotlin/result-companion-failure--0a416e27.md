# Result.Companion.failure

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回一个将给定 `Throwable` `exception` 封装为失败的实例。

??? note "查看英文原文"

    Returns an instance that encapsulates the given `Throwable` `exception` as failure.

## 声明与重载

### 1. Common

```kotlin
@Suppress("INAPPLICABLE_JVM_NAME")
        @InlineOnly
        @JvmName("failure")
        public inline fun <T> failure(exception: Throwable): Result<T>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Result.kt#L95)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*

class CustomException(message: String) : Exception(message) {
        override fun toString(): String = "CustomException: $message"
    }

fun error(message: String): Nothing = throw CustomException(message)

private fun <T> checkSuccess(ok: Result<T>, v: T, topLevel: Boolean = false) {
        println(ok.isSuccess)
        println(ok.isFailure)
        println(ok.getOrThrow())
        println(ok.getOrElse { throw it })
        println(ok.getOrNull())
        println(ok.getOrElse { null })
        println(ok.getOrDefault("DEF"))
        println(ok.getOrElse { "EX:$it" })
        println(ok.fold({ "V:$it" }, { "EX:$it" }))
        println(ok.exceptionOrNull())
        println(ok.fold(onSuccess = { null }, onFailure = { it }))
        println(ok.toString())
        println(ok)
        if (topLevel) {
            checkSuccess(ok.map { 42 }, 42)
            checkSuccess(ok.mapCatching { 42 }, 42)
            checkFailure(ok.mapCatching { error("FAIL") }, "FAIL")
            checkSuccess(ok.recover { 42 }, "OK")
            checkSuccess(ok.recoverCatching { 42 }, "OK")
            checkSuccess(ok.recoverCatching { error("FAIL") }, "OK")
        }
        var sCnt = 0
        var fCnt = 0
        println(ok.onSuccess { sCnt++ })
        println(ok.onFailure { fCnt++ })
        println(sCnt)
        println(fCnt)
    }

private fun <T> checkFailure(fail: Result<T>, msg: String, topLevel: Boolean = false) {
        println(fail.isSuccess)
        println(fail.isFailure)
        assertFails { fail.getOrThrow() }
        assertFails { fail.getOrElse { throw it } }
        println(fail.getOrNull())
        println(fail.getOrElse { null })
        println(fail.getOrDefault("DEF"))
        println(fail.getOrElse { "EX:$it" })
        println(fail.fold({ "V:$it" }, { "EX:$it" }))
        println(fail.exceptionOrNull()!!.message)
        println(fail.fold(onSuccess = { null }, onFailure = { it })!!.message)
        println(fail.toString())
        println(fail)
        if (topLevel) {
            checkFailure(fail.map { 42 }, msg)
            checkFailure(fail.mapCatching { 42 }, msg)
            checkFailure(fail.mapCatching { error("FAIL") }, msg)
            checkSuccess(fail.recover { 42 }, 42)
            checkSuccess(fail.recoverCatching { 42 }, 42)
            checkFailure(fail.recoverCatching { error("FAIL") }, "FAIL")
        }
        var sCnt = 0
        var fCnt = 0
        println(fail.onSuccess { sCnt++ })
        println(fail.onFailure { fCnt++ })
        println(sCnt)
        println(fCnt)
    }

fun main() {

        val fail = Result.failure<Unit>(CustomException("F"))
        checkFailure(fail, "F", true)
    
}
```

```text title="输出"
false
true
null
null
DEF
EX:CustomException: F
EX:CustomException: F
F
F
Failure(CustomException: F)
Failure(CustomException: F)
false
true
null
null
DEF
EX:CustomException: F
EX:CustomException: F
F
F
Failure(CustomException: F)
Failure(CustomException: F)
Failure(CustomException: F)
Failure(CustomException: F)
0
1
false
true
null
null
DEF
EX:CustomException: F
EX:CustomException: F
F
F
Failure(CustomException: F)
Failure(CustomException: F)
Failure(CustomException: F)
Failure(CustomException: F)
0
1
false
true
null
null
DEF
EX:CustomException: F
EX:CustomException: F
F
F
Failure(CustomException: F)
Failure(CustomException: F)
Failure(CustomException: F)
Failure(CustomException: F)
0
1
true
false
42
42
42
42
42
42
V:42
null
null
Success(42)
Success(42)
Success(42)
Success(42)
1
0
true
false
42
42
42
42
42
42
V:42
null
null
Success(42)
Success(42)
Success(42)
Success(42)
1
0
false
true
null
null
DEF
EX:CustomException: FAIL
EX:CustomException: FAIL
FAIL
FAIL
Failure(CustomException: FAIL)
Failure(CustomException: FAIL)
Failure(CustomException: FAIL)
Failure(CustomException: FAIL)
0
1
Failure(CustomException: F)
Failure(CustomException: F)
0
1
```

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/coroutines/ResultTest.kt#L36)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
