# SubclassOptInRequired

`kotlin` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

说明可分为分类和接口,并规定此类声明的执行和延期要求明确选择适用。

适用时,任何将目标宣布分类的企图都将触发选择加入,并附带相应的级别和信息。

亚类选择进入标记的预期用途包括但不仅限于以下API: 稳定使用,但由于进一步的演变而难以执行。 稳定使用,但因内部或技术原因关闭了第三期执行。 稳定使用,但微妙或脆弱执行。 稳定使用,但合同今后可能因外部执行而以反向不兼容的方式被削弱。

与正常的`RequiresOptIn`相反,选择加入分分类要求有三种方式: - 以标记注解注告声明,使其传播。 - 以`OptIn`注解声明,以便以非传播方式选择加入所提供的保证。 - 以同样的标记等级注注注`SubclassOptInRequired`,使之进一步推广,仅用于分分类。

使用这种注释仅限于开放和抽象的分类,以及非`fun`接口。 `CLASS` 注释目标允许的任何其他用途都会产生编译错误。

@property标记标记码指定标记注解,要求明确选择输入。 @see 要求OptIn详细描述选入语义和传播规则。

??? note "查看英文原文"

    Annotation that marks open for subclassing classes and interfaces, and makes implementation
    and extension of such declarations as requiring an explicit opt-in.
    
    When applied, any attempt to subclass the target declaration will trigger an opt-in
    with the corresponding level and message.
    
    The intended uses of subclass opt-in markers include, but are not limited to the following API:
    - Stable to use, but unstable to implement due to its further evolution.
    - Stable to use, but closed for 3rd-part implementations due to internal or technical reasons.
    - Stable to use, but delicate or fragile to implement.
    - Stable to use, but with a contract that may be weakened in the future in a backwards-incompatible
      manner for external implementations.
    
    Contrary to regular `RequiresOptIn`, there are three ways to opt-in into the subclassing requirement:
    - Annotate declaration with the marker annotation, making it propagating.
    - Annotate declaration with `OptIn` in order to opt in into the provided guarantees in a non-propagating manner.
    - Annotate declaration with `SubclassOptInRequired` with the same marker class, making it further propagating only for subclassing.
    
    Uses of this annotation are limited to open and abstract classes, and non-`fun` interfaces.
    Any other uses allowed by `CLASS` annotation target yield a compilation error.
    
    @property markerClass specifies marker annotation that require explicit opt-in.
    @see RequiresOptIn for a detailed description of opt-in semantics and propagation rules.

## 声明与重载

### 1. Common

```kotlin
@Target(CLASS)
@Retention(BINARY)
@MustBeDocumented
@SinceKotlin("2.1")
@WasExperimental(ExperimentalSubclassOptIn::class)
public annotation class SubclassOptInRequired(
    vararg val markerClass: KClass<out Annotation>,
)
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotations/OptIn.kt#L153)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


@RequiresOptIn annotation class ExtensionApi
@SubclassOptInRequired(ExtensionApi::class)
open class Service { fun value(): Int = 42 }
@OptIn(ExtensionApi::class)
class CustomService : Service()
fun main() { println(Service().value()); println(CustomService().value()) }
```

```text title="输出"
42
42
```

## 版本与来源

声明和 KDoc 取自 Kotlin 官方源码的固定标签 `v2.4.21`。中文 KDoc 为自动翻译初稿，尚未经逐条人工审校；有歧义时请展开英文原文。示例的 JVM 验证结果不能视为对 JS、Native 或 Wasm 专有行为的验证。
