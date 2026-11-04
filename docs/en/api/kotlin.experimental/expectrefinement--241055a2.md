# ExpectRefinement

`kotlin.experimental` · **2.4.21** · Common

Representative examples on this page were compiled and executed on **JVM** with Kotlin / stdlib 2.4.21.

## Description

This experimental expect-refinement example follows common → shared → JVM. The intermediate expect repeats existing members and adds a member, with a final actual implementation.

## Declarations and overloads

### 1. Common

```kotlin
@Target(AnnotationTarget.CLASS)
@Retention(AnnotationRetention.SOURCE)
@Suppress("NEWER_VERSION_IN_SINCE_KOTLIN")
@SinceKotlin("2.2")
@ExperimentalMultiplatform
public annotation class ExpectRefinement
```

[Common source](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/experimental/ExpectRefinement.kt#L8)

## Usage examples and output

### Example 1 · JVM

```kotlin title="Example 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


actual class Device {
    actual fun name(): String = "device"
    actual fun feature(): String = "refined"
}
fun main() { val device = Device(); println(device.name()); println(device.feature()) }
```

```text title="Output"
device
refined
```

```kotlin title="common.kt"
expect class Device { fun name(): String }
```

```kotlin title="shared.kt"
@file:OptIn(kotlin.ExperimentalMultiplatform::class)
import kotlin.experimental.ExpectRefinement
@ExpectRefinement
expect class Device { fun name(): String; fun feature(): String }
```

Compiler options: `-Xmulti-platform` `-XXLanguage:+ExpectRefinement` `-Xfragments=common,shared,jvm` `-Xfragment-refines=shared:common` `-Xfragment-refines=jvm:shared` `-Xfragment-sources=common:{common.kt}` `-Xfragment-sources=shared:{shared.kt}` `-Xfragment-sources=jvm:{main}`

## Version and sources

This page's explanation and examples have been separately prepared. Declarations are pinned to `v2.4.21`; examples were verified on the JVM with Kotlin / stdlib 2.4.21.
