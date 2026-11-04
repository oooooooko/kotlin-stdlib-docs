# CoroutineContext.minusKey

`kotlin.coroutines` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

返回含有此上下文元素的上下文,但没有包含指定 `key` 的元素。

??? note "查看英文原文"

    Returns a context containing elements from this context, but without an element with
    the specified `key`.

## 声明与重载

### 1. Common

```kotlin
public fun minusKey(key: Key<*>): CoroutineContext
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/CoroutineContext.kt#L45)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.test.*
import kotlin.coroutines.*

data class CtxA(val i: Int) : AbstractCoroutineContextElement(CtxA) {
        companion object Key : CoroutineContext.Key<CtxA>
    }

data class CtxB(val i: Int) : AbstractCoroutineContextElement(CtxB) {
        companion object Key : CoroutineContext.Key<CtxB>
    }

data class CtxC(val i: Int) : AbstractCoroutineContextElement(CtxC) {
        companion object Key : CoroutineContext.Key<CtxC>
    }

object Disp1 : AbstractCoroutineContextElement(ContinuationInterceptor), ContinuationInterceptor {
        override fun <T> interceptContinuation(continuation: Continuation<T>): Continuation<T> = continuation
        override fun toString(): String = "Disp1"
    }

object Disp2 : AbstractCoroutineContextElement(ContinuationInterceptor), ContinuationInterceptor {
        override fun <T> interceptContinuation(continuation: Continuation<T>): Continuation<T> = continuation
        override fun toString(): String = "Disp2"
    }

private fun assertContents(ctx: CoroutineContext, vararg elements: CoroutineContext.Element) {
        val set = ctx.fold(setOf<CoroutineContext>()) { a, b -> a + b }
        println(set.toList())
        for (elem in elements)
            println(ctx[elem.key] == elem)
    }

private fun checkContentsAndRemoves(context: CoroutineContext, vararg es: CoroutineContext.Element) {
        checkContents(context, *es)
        for (e in es) {
            checkContents(context.minusKey(e.key), *(es.toSet() - e).toTypedArray())
        }
    }

private fun checkContents(context: CoroutineContext, vararg es: CoroutineContext.Element) {
        val size = context.fold(0) { c, _ -> c + 1 }
        println(size)
        for (e in es) {
            val key = e.key
            println(e === context[key])
        }
        val set = mutableSetOf<CoroutineContext.Element>()
        context.fold(set) { s, e -> s.apply { add(e) } }
        println(es.toSet())
        when (es.size) {
            0 -> println(context === EmptyCoroutineContext)
            1 -> println(context === es[0])
        }
    }

class DataElement(val data: Int) : AbstractCoroutineContextElement(Key) {
        companion object Key : CoroutineContext.Key<DataElement>
    }

class OtherElement(val data: Int) : AbstractCoroutineContextElement(Key) {
        companion object Key : CoroutineContext.Key<DataElement>
    }

data class WrapperKey(val key: String) : CoroutineContext.Key<WrapperElement>

class WrapperElement(key: String) : CoroutineContext.Element {
        override val key = WrapperKey(key)
    }

class CustomContinuationInterceptor : ContinuationInterceptor {
        override val key: CoroutineContext.Key<*>
            get() = ContinuationInterceptor

        override fun <T> interceptContinuation(continuation: Continuation<T>): Continuation<T> =
            continuation
    }

fun main() {

        val we1 = WrapperElement("1")
        val we2 = WrapperElement("2")
        checkContents(we1, we1)
        checkContents(we2, we2)
        val we1we2 = we1 + we2
        checkContents(we1we2, we1, we2)
        checkContents(we1we2.minusKey(WrapperKey("1")), we2)
        checkContents(we1we2.minusKey(WrapperKey("2")), we1)
    
}
```

```text title="输出"
1
true
[WrapperElement@45ee12a7]
true
1
true
[WrapperElement@6ff3c5b5]
true
2
true
true
[WrapperElement@45ee12a7, WrapperElement@6ff3c5b5]
1
true
[WrapperElement@6ff3c5b5]
true
1
true
[WrapperElement@45ee12a7]
true
```

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/coroutines/CoroutineContextTest.kt#L184)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
