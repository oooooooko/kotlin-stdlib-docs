# AbstractCoroutineContextKey

`kotlin.coroutines` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

此多态键 API 在 2.4 中已弃用。新代码建议按基础键获取元素后显式转换类型。

??? note "查看英文原文"

    Base class for `CoroutineContext.Key` associated with polymorphic `CoroutineContext.Element` implementation.
    Polymorphic element implementation implies delegating its `get``Element.get` and `minusKey``Element.minusKey`
    to `getPolymorphicElement` and `minusPolymorphicKey` respectively.
    
    Polymorphic elements can be extracted from the coroutine context using both element key and its supertype key.
    Example of polymorphic elements:
    ```
    open class BaseElement : CoroutineContext.Element {
        companion object Key : CoroutineContext.Key<BaseElement>
        override val key: CoroutineContext.Key<*> get() = Key
        // It is important to use getPolymorphicKey and minusPolymorphicKey
        override fun <E : CoroutineContext.Element> get(key: CoroutineContext.Key<E>): E? = getPolymorphicElement(key)
        override fun minusKey(key: CoroutineContext.Key<*>): CoroutineContext = minusPolymorphicKey(key)
    }
    
    class DerivedElement : BaseElement() {
        companion object Key : AbstractCoroutineContextKey<BaseElement, DerivedElement>(BaseElement, { it as? DerivedElement })
    }
    // Now it is possible to query both `BaseElement` and `DerivedElement`
    someContext`BaseElement` // Returns BaseElement?, non-null both for BaseElement and DerivedElement instances
    someContext`DerivedElement` // Returns DerivedElement?, non-null only for DerivedElement instance
    ```
    @param B base class of a polymorphic element
    @param baseKey an instance of base key
    @param E element type associated with the current key
    @param safeCast a function that can safely cast abstract `CoroutineContext.Element` to the concrete `E` type
                    and return the element if it is a subtype of `E` or `null` otherwise.

## 声明与重载

### 1. Common

```kotlin
@SinceKotlin("1.3")
@ExperimentalStdlibApi
@Deprecated(
    "Polymorphic coroutine context keys are error-prone, difficult to implement correctly, and can encourage " +
            "depending on implementation details. Prefer retrieving the element by its base key and casting " +
            "it explicitly when needed or introducing a dedicated extension property."
)
@DeprecatedSinceKotlin(warningSince = "2.4")
public abstract class AbstractCoroutineContextKey<B : Element, E : B>(
    baseKey: Key<B>,
    private val safeCast: (element: Element) -> E?
) : Key<E>
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/coroutines/CoroutineContextImpl.kt#L19)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
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

```text title="输出"
true
true
```

## 版本与来源

本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。
