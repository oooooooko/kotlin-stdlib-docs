# Result.Companion.failure

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns an instance that encapsulates the given `Throwable` `exception` as failure.

## Declarations and overloads

### 1. Common

```kotlin
@Suppress("INAPPLICABLE_JVM_NAME")
        @InlineOnly
        @JvmName("failure")
        public inline fun <T> failure(exception: Throwable): Result<T>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/util/Result.kt#L95)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
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

```text title="Output"
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

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/coroutines/ResultTest.kt#L36)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
