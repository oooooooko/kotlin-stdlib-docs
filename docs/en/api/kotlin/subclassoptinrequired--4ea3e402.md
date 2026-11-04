# SubclassOptInRequired

`kotlin` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

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

## Declarations and overloads

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

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/annotations/OptIn.kt#L153)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


@RequiresOptIn annotation class ExtensionApi
@SubclassOptInRequired(ExtensionApi::class)
open class Service { fun value(): Int = 42 }
@OptIn(ExtensionApi::class)
class CustomService : Service()
fun main() { println(Service().value()); println(CustomService().value()) }
```

```text title="Output"
42
42
```

## Version and sources

Declarations and KDoc are taken from the pinned official Kotlin `v2.4.21` source tag. Chinese KDoc is a machine-translated draft, not individually human-reviewed. JVM example validation does not establish JS-, Native-, or Wasm-specific behavior.
