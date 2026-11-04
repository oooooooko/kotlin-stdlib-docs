# AbstractCoroutineContextKey.constructor

`kotlin.coroutines` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

Polymorphic context keys are deprecated since 2.4. Retrieve by the base key and cast explicitly in new code.

## Declarations and overloads

### 1. Common

```kotlin
(
    baseKey: Key<B>,
    private val safeCast: (element: Element) -> E?
)
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/CoroutineContextImpl.kt#L56)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


import kotlin.coroutines.*
open class BaseElement : CoroutineContext.Element {
    companion object Key : CoroutineContext.Key<BaseElement>
    override val key: CoroutineContext.Key<*> get() = Key
    override fun <E : CoroutineContext.Element> get(key: CoroutineContext.Key<E>): E? = getPolymorphicElement(key)
    override fun minusKey(key: CoroutineContext.Key<*>): CoroutineContext = minusPolymorphicKey(key)
}
class DerivedElement : BaseElement() {
    companion object Key : AbstractCoroutineContextKey<BaseElement, DerivedElement>(BaseElement, { it as? DerivedElement })
}
fun main() {
    val context: CoroutineContext = DerivedElement()
    println(context[BaseElement] != null)
    println(context[DerivedElement] != null)
}
```

```text title="Output"
true
true
```

## Version and sources

This page's explanation and examples have been separately prepared. Declarations are pinned to `v2.4.21`; examples were verified on the JVM with Kotlin / stdlib 2.4.21.
