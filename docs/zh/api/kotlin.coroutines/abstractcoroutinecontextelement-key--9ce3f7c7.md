# AbstractCoroutineContextElement.key

`kotlin.coroutines` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 声明与重载

### 1. Common

```kotlin
public override val key: Key<*>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/CoroutineContextImpl.kt#L17)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
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

```text title="输出"
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

本次实际运行的输出如上；随机数、时间、临时路径或对象标识等内容可能随运行和环境变化。

此边界示例还使用 `kotlin-test:2.4.21` 的断言工具。

此示例需要 `kotlin-reflect:2.4.21`。

[示例来源](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/test/coroutines/AbstractCoroutineContextElementTest.kt#L52)

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
