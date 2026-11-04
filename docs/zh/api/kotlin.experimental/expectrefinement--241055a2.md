# ExpectRefinement

`kotlin.experimental` · **2.4.21** · Common

本文含经 Kotlin / stdlib 2.4.21 在 **JVM** 上编译运行的代表性示例。

## 用途与说明

这是实验性的 expect 声明细化示例：common → shared → JVM。shared 重复原成员并新增成员，最终由 actual 类实现；它属于 Common 多平台声明机制。

??? note "查看英文原文"

    The marked `expect` declaration refines `expect` declaration from the closest transitive *dependsOn* [source set](https://kotlinlang.org/docs/multiplatform-discover-project.html#source-sets).
    The marked declaration is called a *refinement*.
    The annotation can be put only on top-level `expect` declarations.
    
    A pair of an `expect` declaration and *refinement* declaration must obey the same rules
    as a pair of regular `expect` and `actual` declarations.
    Except, the `expect` *refinement* declaration must not have a body.
    The rules are checked by the compiler.
    
    Example:
    ```
    // SOURCE SET: common
    expect class PlatformSpecific {
        fun availableOnAllPlatforms()
    }
    
    // SOURCE SET: native (dependsOn: common)
    @ExpectRefinement
    expect class PlatformSpecific { // `PlatformSpecific` in native source set refines `PlatformSpecific` in common source set
        fun availableOnAllPlatforms() // The declarations from the original expect declaration must be repeated
        fun availableOnlyOnNativePlatforms() // Add a new member
    }
    
    // SOURCE SET: linux (dependsOn: native)
    actual class PlatformSpecific {
        actual fun availableOnAllPlatforms() {}
        actual fun availableOnlyOnNativePlatforms() {}
    }
    ```
    
    An *refinement* declaration can be further refined by other *refinements*,
    forming a chain of `expect` *refinement* declarations.
    The chain must always end with an `actual` declaration.
    
    It's possible to have multiple *dependsOn* dependencies.
    *dependsOn* relation forms a graph, it's not a tree.
    Given that, a *refinement* must refine one and only one `expect` declaration.
    The same applies to `actual` declarations.
    An `actual` declaration must actualize one and only one `expect` declaration.
    
    ## Stability guarantees
    
    The feature is experimental.
    **No stability guarantees are provided.**

## 声明与重载

### 1. Common

```kotlin
@Target(AnnotationTarget.CLASS)
@Retention(AnnotationRetention.SOURCE)
@Suppress("NEWER_VERSION_IN_SINCE_KOTLIN")
@SinceKotlin("2.2")
@ExperimentalMultiplatform
public annotation class ExpectRefinement
```

[Common 源码](https://github.com/JetBrains/kotlin/blob/v2.4.21/libraries/stdlib/src/kotlin/experimental/ExpectRefinement.kt#L8)

## 用法示例与输出

### 示例 1 · JVM

```kotlin title="示例 1" linenums="1"
@file:Suppress("DEPRECATION", "DEPRECATION_ERROR")
@file:OptIn(kotlin.ExperimentalStdlibApi::class, kotlin.ExperimentalUnsignedTypes::class, kotlin.time.ExperimentalTime::class, kotlin.contracts.ExperimentalContracts::class, kotlin.contracts.ExperimentalExtendedContracts::class, kotlin.experimental.ExperimentalTypeInference::class, kotlin.ExperimentalMultiplatform::class, kotlin.ExperimentalVersionOverloading::class, kotlin.coroutines.ExperimentalStdlibCoroutineSupportApi::class)


actual class Device {
    actual fun name(): String = "device"
    actual fun feature(): String = "refined"
}
fun main() { val device = Device(); println(device.name()); println(device.feature()) }
```

```text title="输出"
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

编译选项：`-Xmulti-platform` `-XXLanguage:+ExpectRefinement` `-Xfragments=common,shared,jvm` `-Xfragment-refines=shared:common` `-Xfragment-refines=jvm:shared` `-Xfragment-sources=common:{common.kt}` `-Xfragment-sources=shared:{shared.kt}` `-Xfragment-sources=jvm:{main}`

## 版本与来源

本页用途说明和示例已单独整理。声明取自官方源码固定标签 `v2.4.21`，示例在 JVM 上使用 Kotlin / stdlib 2.4.21 校验。
