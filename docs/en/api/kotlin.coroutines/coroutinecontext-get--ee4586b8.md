# CoroutineContext.get

`kotlin.coroutines` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Returns the element with the given `key` from this context or `null`.

## Declarations and overloads

### 1. Common

```kotlin
public operator fun <E : Element> get(key: Key<E>): E?
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/CoroutineContext.kt#L15)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
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

        val ctx1 = CtxA(1) + CtxB(2)
        val ctx2 = CtxB(3) + CtxC(4)
        val ctx = ctx1 + ctx2
        assertContents(ctx, CtxA(1), CtxB(3), CtxC(4))
        println(ctx.toString())
        println(ctx[CtxA])
        println(ctx[CtxB])
        println(ctx[CtxC])
    
}
```

```text title="Output"
[CtxA(i=1), CtxB(i=3), CtxC(i=4)]
true
true
true
[CtxA(i=1), CtxB(i=3), CtxC(i=4)]
CtxA(i=1)
CtxB(i=3)
CtxC(i=4)
```

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/coroutines/CoroutineContextTest.kt#L113)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
