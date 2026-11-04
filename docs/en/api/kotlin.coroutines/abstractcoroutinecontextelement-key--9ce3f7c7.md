# AbstractCoroutineContextElement.key

`kotlin.coroutines` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Declarations and overloads

### 1. Common

```kotlin
public override val key: Key<*>
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/CoroutineContextImpl.kt#L17)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.io.path.ExperimentalPathApi::class, kotlin.uuid.ExperimentalUuidApi::class, kotlin.concurrent.atomics.ExperimentalAtomicApi::class, kotlin.io.encoding.ExperimentalEncodingApi::class)

import kotlin.coroutines.*
import kotlin.test.*

private val CoroutineContext.size get() = fold(0) { acc, _ -> acc + 1 }

abstract class Base : AbstractCoroutineContextElement(Key) {
        companion object Key : CoroutineContext.Key<Base>

        override fun <E : CoroutineContext.Element> get(key: CoroutineContext.Key<E>): E? =
            @Suppress("DEPRECATION") getPolymorphicElement(key)

        override fun minusKey(key: CoroutineContext.Key<*>): CoroutineContext =
            @Suppress("DEPRECATION") minusPolymorphicKey(key)
    }

class DerivedWithoutKey : Base() {
        // No custom key
    }

open class DerivedWithKey : Base() {
        @Suppress("DEPRECATION")
        companion object Key : AbstractCoroutineContextKey<Base, DerivedWithKey>(Base, { it as? DerivedWithKey })
    }

class SubDerivedWithKey : DerivedWithKey() {
        @Suppress("DEPRECATION")
        companion object Key : AbstractCoroutineContextKey<Base, SubDerivedWithKey>(Base, { it as? SubDerivedWithKey })
    }

class SubDerivedWithKeyAndDifferentBase : DerivedWithKey() {
        // Note how different base class is used
        @Suppress("DEPRECATION")
        companion object Key :
            AbstractCoroutineContextKey<DerivedWithKey, SubDerivedWithKeyAndDifferentBase>(
                DerivedWithKey,
                { it as? SubDerivedWithKeyAndDifferentBase })
    }

object IrrelevantElement : AbstractCoroutineContextElement(Key) {
        object Key : CoroutineContext.Key<IrrelevantElement>
    }

private fun testDerivedWithoutKey(context: CoroutineContext, element: CoroutineContext.Element) {
        val ctx = context + element
        println(ctx.size)
        println(element === ctx[Base]!!)
        println(ctx[DerivedWithKey])
        println(ctx.minusKey(Base))
        println(ctx === ctx.minusKey(DerivedWithKey))
    }

private fun testDerivedWithKey(context: CoroutineContext, element: CoroutineContext.Element) {
        val ctx = context + element
        println(ctx.size)
        println(element === ctx[Base]!!)
        println(element === ctx[DerivedWithKey]!!)
        println(ctx.minusKey(Base))
        println(ctx.minusKey(DerivedWithKey))
    }

private fun testSubDerivedWithKey(context: CoroutineContext, element: CoroutineContext.Element) {
        val ctx = context + element
        println(ctx.size)
        println(element === ctx[Base]!!)
        println(element === ctx[DerivedWithKey]!!)
        println(element === ctx[SubDerivedWithKey]!!)
        println(ctx[SubDerivedWithKeyAndDifferentBase])
        println(ctx.minusKey(Base))
        println(ctx.minusKey(DerivedWithKey))
        println(ctx.minusKey(SubDerivedWithKey))
        println(ctx === ctx.minusKey(SubDerivedWithKeyAndDifferentBase))
    }

private fun testSubDerivedWithKeyAndDifferentBase(context: CoroutineContext, element: CoroutineContext.Element) {
        val ctx = context + element
        println(ctx.size)
        println(element === ctx[Base]!!)
        println(element === ctx[DerivedWithKey]!!)
        println(element === ctx[SubDerivedWithKeyAndDifferentBase]!!)
        println(ctx[SubDerivedWithKey])
        println(ctx.minusKey(Base))
        println(ctx.minusKey(DerivedWithKey))
        println(ctx.minusKey(SubDerivedWithKeyAndDifferentBase))
        println(ctx === ctx.minusKey(SubDerivedWithKey))
    }

private inline fun <reified T : CoroutineContext.Element> testSubDerivedOverrides(context: CoroutineContext, key: CoroutineContext.Key<T>) {
        println(context.size)
        println({ context[Base] is DerivedWithKey })
        println({ context[DerivedWithKey] is DerivedWithKey })
        println({ context[DerivedWithKey] is T })
        println({ context[key] is T })
        println(context.minusKey(Base))
        println(context.minusKey(DerivedWithKey))
    }

fun main() {

        val derivedWithoutKey = DerivedWithoutKey()
        println(Base.Key === derivedWithoutKey.key)
        testDerivedWithoutKey(EmptyCoroutineContext, derivedWithoutKey) // Single element
        testDerivedWithoutKey(IrrelevantElement, derivedWithoutKey) // Combined context
    
}
```

```text title="Output"
true
1
true
null
EmptyCoroutineContext
true
2
true
null
IrrelevantElement@27c170f0
true
```

The output above was captured from a real execution. Random values, times, temporary paths, and object identities can vary between runs and environments.

This edge-case sample also uses assertions from `kotlin-test:2.4.21`.

This example requires `kotlin-reflect:2.4.21`.

[Sample source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/coroutines/AbstractCoroutineContextElementTest.kt#L52)

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
